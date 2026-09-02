from datetime import date, datetime
import base64
from io import BytesIO
import json
import os
import socket
import uuid
import qrcode
import streamlit as str_lit
from supabase import create_client, Client
import requests

try:
  from reportlab.lib import colors
  from reportlab.lib.pagesizes import letter
  from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
  from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, Image as ReportLabImage
  REPORTLAB_DISPONIBILE = True
except ImportError:
  REPORTLAB_DISPONIBILE = False

str_lit.set_page_config(
    page_title="Gestionale Ergo & Scardaci", page_icon="📦", layout="wide"
)

# ==============================================================================
# CONFIGURAZIONE SUPABASE (Legge in automatico dai Secrets di Streamlit Cloud)
# ==============================================================================
SUPABASE_URL = str_lit.secrets.get("SUPABASE_URL", "IL_TUO_SUPABASE_URL")
SUPABASE_KEY = str_lit.secrets.get("SUPABASE_KEY", "IL_TUO_SUPABASE_ANON_KEY")
BUCKET_IMMAGINI = "immagini_prodotti"

@str_lit.cache_resource
def init_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

if SUPABASE_URL == "IL_TUO_SUPABASE_URL" or SUPABASE_KEY == "IL_TUO_SUPABASE_ANON_KEY":
    str_lit.error("⚠️ Configura SUPABASE_URL e SUPABASE_KEY nei Secrets di Streamlit Cloud o nel codice.")
    str_lit.stop()

supabase = init_supabase()

str_lit.markdown(
    """
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"],
    div[data-testid="stVerticalBlockBorderWrapper"],
    div[aria-label="Scrollable container"],
    div[data-testid="stScrollable"] {
        scrollbar-width: thin !important;
        scrollbar-color: #0056b3 #f3f4f6 !important;
        overflow-y: scroll !important;
    }

    ::-webkit-scrollbar {
        width: 12px !important;
        height: 12px !important;
        display: block !important;
        visibility: visible !important;
    }

    ::-webkit-scrollbar-track {
        background: #f3f4f6 !important;
        border-radius: 6px !important;
        display: block !important;
    }

    ::-webkit-scrollbar-thumb {
        background-color: #0056b3 !important;
        border-radius: 6px !important;
        border: 2px solid #f3f4f6 !important;
        min-height: 40px !important;
        visibility: visible !important;
        opacity: 1 !important;
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: #004494 !important;
    }

    button[kind="primary"], 
    div.stButton > button[kind="primary"], 
    [data-testid="baseButton-primary"],
    div.stFormSubmitButton > button {
        background-color: #0056b3 !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: bold !important;
    }
    button[kind="primary"]:hover, 
    div.stButton > button[kind="primary"]:hover, 
    [data-testid="baseButton-primary"]:hover,
    div.stFormSubmitButton > button:hover {
        background-color: #004494 !important;
        color: white !important;
    }
    
    div.stButton > button:not([kind="primary"]), .stButton > button:not([kind="primary"]) {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #d1d5db !important;
        border-radius: 6px !important;
        font-weight: 500 !important;
    }
    div.stButton > button:not([kind="primary"]):hover, .stButton > button:not([kind="primary"]):hover {
        background-color: #f3f4f6 !important;
        color: #111111 !important;
        border-color: #9ca3af !important;
    }

    div.stTextInput div[data-baseweb="input"],
    div.stTextInput div[data-baseweb="input"]:hover,
    div.stTextInput div[data-baseweb="input"]:focus,
    div.stTextInput div[data-baseweb="input"]:focus-within,
    div.stTextInput div[data-baseweb="input"][aria-invalid="true"] {
        border-color: #0056b3 !important;
        box-shadow: 0 0 0 1px #0056b3 !important;
    }

    .card-desc {
        height: 45px;
        color: #555;
        font-size: 1rem;
        margin-bottom: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

CATEGORIE_PRODOTTI = [
    "TAVOLI",
    "SEDIE",
    "PIATTI E SOTTOPIATTI",
    "BICCHIERI",
    "CUCINA",
    "ARREDO",
    "TOVAGLIATO",
    "ARGENTERIA",
    "POSATERIA",
    "VASSOI",
    "LUCI E CANDELABRI",
]

COLORI_CATEGORIE = {
    "TAVOLI": "#0056b3",
    "SEDIE": "#d97706",
    "PIATTI E SOTTOPIATTI": "#059669",
    "BICCHIERI": "#dc2626",
    "CUCINA": "#7c3aed",
    "ARREDO": "#db2777",
    "TOVAGLIATO": "#0284c7",
    "ARGENTERIA": "#4b5563",
    "POSATERIA": "#ca8a04",
    "VASSOI": "#0d9488",
    "LUCI E CANDELABRI": "#ea580c",
}

LISTA_RUOLI_DISPONIBILI = [
    "Amministratore",
    "Wedding",
    "Cucina",
    "Sala",
    "Magazzino",
    "Magazzino2",
]


def carica_dati_esterni():
  try:
    res_prod = supabase.table("prodotti_noleggio").select("*").execute()
    prodotti = res_prod.data if res_prod.data else []

    res_ev = supabase.table("eventi_catering").select("*").execute()
    eventi = res_ev.data if res_ev.data else []

    res_usr = supabase.table("utenti_autorizzati").select("*").execute()
    utenti = {}
    if res_usr.data:
      for u in res_usr.data:
        username = u.get("username")
        utenti[username] = {
            "password": u.get("password"),
            "ruolo": u.get("ruolo"),
            "nome": u.get("nome"),
            "email": u.get("email"),
        }

    return {
        "prodotti_noleggio": prodotti,
        "eventi_catering": eventi,
        "utenti_autorizzati": utenti if utenti else None,
    }
  except Exception as e:
    str_lit.error(f"Errore di caricamento dati da Supabase: {e}")
    return None


def salva_dati_esterni():
  try:
    supabase.table("prodotti_noleggio").delete().neq("id", -1).execute()
    for p in str_lit.session_state.prodotti_noleggio:
      p_to_save = {k: v for k, v in p.items() if k != "id"}
      supabase.table("prodotti_noleggio").insert(p_to_save).execute()

    supabase.table("eventi_catering").delete().neq("id", -1).execute()
    for ev in str_lit.session_state.eventi_catering:
      ev_to_save = {k: v for k, v in ev.items() if k != "id"}
      supabase.table("eventi_catering").insert(ev_to_save).execute()

    supabase.table("utenti_autorizzati").delete().neq("id", -1).execute()
    for usr_k, usr_v in str_lit.session_state.utenti_autorizzati.items():
      u_data = {
          "username": usr_k,
          "password": usr_v.get("password"),
          "ruolo": usr_v.get("ruolo"),
          "nome": usr_v.get("nome"),
          "email": usr_v.get("email"),
      }
      supabase.table("utenti_autorizzati").insert(u_data).execute()
  except Exception as e:
    str_lit.error(f"Errore durante il salvataggio su Supabase: {e}")


dati_salvati = carica_dati_esterni()


def get_local_ip():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
  except:
    return "localhost"


LOCAL_IP = get_local_ip()
BASE_URL = f"http://{LOCAL_IP}:8501"


def get_base64_image(nome_base):
  for ext in [".png", ".jpg", ".jpeg"]:
    if os.path.exists(nome_base + ext):
      with open(nome_base + ext, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
  return None


def html_thumb(path, size=110):
  if path:
    if path.startswith("http://") or path.startswith("https://"):
      return (
          f"<div style='width:{size}px; height:{size}px; background:#f8f9fa;"
          f" border-radius:8px; overflow:hidden; display:flex; align-items:center;"
          f" justify-content:center; margin: 0 auto;'><img"
          f" src='{path}' style='width:100%; height:100%;"
          " object-fit:cover;'></div>"
      )
    elif os.path.exists(path):
      try:
        with open(path, "rb") as f:
          b64 = base64.b64encode(f.read()).decode("utf-8")
        return (
            f"<div style='width:{size}px; height:{size}px; background:#f8f9fa;"
            f" border-radius:8px; overflow:hidden; display:flex;"
            f" align-items:center; justify-content:center; margin: 0 auto;'><img"
            f" src='data:image/jpeg;base64,{b64}' style='width:100%;"
            " height:100%; object-fit:cover;'></div>"
        )
      except:
        pass
  return (
      f"<div style='width:{size}px; height:{size}px; background:#f8f9fa;"
      f" border-radius:8px; display:flex; align-items:center;"
      f" justify-content:center; color:#888; font-size:0.8rem; margin: 0"
      " auto;'>No Foto</div>"
  )


def salva_immagine_su_disco(uploaded_file):
  if uploaded_file is not None:
    try:
      ext = os.path.splitext(uploaded_file.name)[1]
      nome_file_unico = f"{uuid.uuid4()}{ext}"
      file_bytes = uploaded_file.getvalue()
      supabase.storage.from_(BUCKET_IMMAGINI).upload(
          file_path=nome_file_unico,
          file=file_bytes,
          file_options={"content-type": uploaded_file.type},
      )
      public_url = supabase.storage.from_(BUCKET_IMMAGINI).get_public_url(nome_file_unico)
      return public_url
    except Exception as e:
      str_lit.error(f"Errore caricamento immagine su Supabase Storage: {e}")
      return None
  return None


@str_lit.cache_data
def genera_qrcode_img(testo):
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=6,
      border=2,
  )
  qr.add_data(testo)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  buffer = BytesIO()
  img.save(buffer, format="PNG")
  return buffer.getvalue()


def parse_data_evento(d_str):
  if not d_str:
    return datetime(2026, 1, 1)
  for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
    try:
      return datetime.strptime(d_str.strip(), fmt)
    except ValueError:
      continue
  return datetime(2026, 1, 1)


def genera_testo_lista_attrezzature(nome_evento, lista_prodotti):
  testo = f"LISTA ATTREZZATURE PER EVENTO: {nome_evento}\n"
  testo += "=" * 55 + "\n\n"

  prodotti_per_cat = {}
  for item in lista_prodotti:
    cat = item.get("categoria", "ALTRO")
    if cat not in prodotti_per_cat:
      prodotti_per_cat[cat] = []
    prodotti_per_cat[cat].append(item)

  for cat, items in prodotti_per_cat.items():
    testo += f"--- {cat} ---\n"
    for item in items:
      testo += f"• {item.get('nome')} (ID: {item.get('codice', '-')}) | Q.tà: {item.get('quantita_selezionata', 1)}\n"
    testo += "\n"
  return testo.encode("utf-8")


def genera_pdf_lista_attrezzature(nome_evento, lista_prodotti):
  buffer = BytesIO()
  doc = SimpleDocTemplate(
      buffer,
      pagesize=letter,
      rightMargin=30,
      leftMargin=30,
      topMargin=30,
      bottomMargin=30,
  )
  story = []
  styles = getSampleStyleSheet()

  title_style = ParagraphStyle(
      "TitleStyle",
      parent=styles["Heading1"],
      fontSize=15,
      spaceAfter=15,
      textColor=colors.HexColor("#0056b3"),
  )
  story.append(
      Paragraph(
          f"<b>Lista Attrezzature per Evento:</b> {nome_evento}", title_style
      )
  )

  cat_style = ParagraphStyle(
      "CatStyle",
      parent=styles["Heading2"],
      fontSize=11,
      spaceAfter=6,
      spaceBefore=10,
      textColor=colors.HexColor("#333333"),
  )

  prodotti_per_cat = {}
  for item in lista_prodotti:
    cat = item.get("categoria", "ALTRO")
    if cat not in prodotti_per_cat:
      prodotti_per_cat[cat] = []
    prodotti_per_cat[cat].append(item)

  for cat, items in prodotti_per_cat.items():
    story.append(Paragraph(f"<b>Reparto / Categoria: {cat}</b>", cat_style))

    table_data = [["Foto", "Prodotto", "Codice", "Q.tà"]]
    for item in items:
      img_obj = ""
      foto_p = item.get("foto_path")
      if foto_p:
        if foto_p.startswith("http://") or foto_p.startswith("https://"):
          try:
            resp = requests.get(foto_p, timeout=3)
            if resp.status_code == 200:
              img_obj = ReportLabImage(BytesIO(resp.content), width=35, height=35)
          except:
            img_obj = "-"
        elif os.path.exists(foto_p):
          try:
            img_obj = ReportLabImage(foto_p, width=35, height=35)
          except:
            img_obj = "-"

      table_data.append([
          img_obj,
          str(item.get("nome", "")),
          str(item.get("codice", "")),
          str(item.get("quantita_selezionata", item.get("quantita", 1))),
      ])

    t = Table(table_data, colWidths=[50, 312, 130, 60])
    t.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0056b3")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (1, 0), (-1, -1), "LEFT"),
            ("ALIGN", (3, 0), (3, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("TOPPADDING", (0, 0), (-1, 0), 8),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f9fafb")),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d1d5db")),
            ("FONTSIZE", (0, 1), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
            ("TOPPADDING", (0, 1), (-1, -1), 6),
        ])
    )
    story.append(t)
    story.append(Spacer(1, 10))

  doc.build(story)
  return buffer.getvalue()


if "utenti_autorizzati" not in str_lit.session_state:
  if dati_salvati and dati_salvati.get("utenti_autorizzati"):
    str_lit.session_state.utenti_autorizzati = dati_salvati["utenti_autorizzati"]
  else:
    str_lit.session_state.utenti_autorizzati = {
        "admin": {
            "password": "123",
            "ruolo": "Amministratore",
            "nome": "Gianluca (Admin)",
            "email": "admin@gestionale.it",
        },
        "wedding": {
            "password": "wedding123",
            "ruolo": "Wedding",
            "nome": "Cristina (Wedding Planner)",
            "email": "wedding@gestionale.it",
        },
        "cucina": {
            "password": "cucina123",
            "ruolo": "Cucina",
            "nome": "Chef Cucina",
            "email": "cucina@gestionale.it",
        },
        "sala": {
            "password": "sala123",
            "ruolo": "Sala",
            "nome": "Responsabile Sala",
            "email": "sala@gestionale.it",
        },
        "magazzino": {
            "password": "mag123",
            "ruolo": "Magazzino",
            "nome": "Addetto Magazzino",
            "email": "magazzino@gestionale.it",
        },
        "magazzino2": {
            "password": "mag2123",
            "ruolo": "Magazzino2",
            "nome": "Assistente Magazzino",
            "email": "magazzino2@gestionale.it",
        },
    }

if "prodotti_noleggio" not in str_lit.session_state:
  if dati_salvati and "prodotti_noleggio" in dati_salvati:
    str_lit.session_state.prodotti_noleggio = dati_salvati["prodotti_noleggio"]
  else:
    str_lit.session_state.prodotti_noleggio = []

if "eventi_catering" not in str_lit.session_state:
  if dati_salvati and "eventi_catering" in dati_salvati:
    str_lit.session_state.eventi_catering = dati_salvati["eventi_catering"]
  else:
    str_lit.session_state.eventi_catering = []

if "lista_attrezzature_corrente" not in str_lit.session_state:
  str_lit.session_state.lista_attrezzature_corrente = []

if "utente_loggato" not in str_lit.session_state:
  str_lit.session_state.utente_loggato = None
if "area_selezionata" not in str_lit.session_state:
  str_lit.session_state.area_selezionata = None
if "modale_prodotto" not in str_lit.session_state:
  str_lit.session_state.modale_prodotto = None
if "prodotto_in_modifica" not in str_lit.session_state:
  str_lit.session_state.prodotto_in_modifica = None
if "indice_modifica" not in str_lit.session_state:
  str_lit.session_state.indice_modifica = None

query_params = str_lit.query_params
codice_scansionato = query_params.get("codice")

if codice_scansionato and str_lit.session_state.area_selezionata is None:
  str_lit.session_state.area_selezionata = "opzione_1"

logo_noleggio_b64 = get_base64_image("logo_noleggio")
logo_catering_b64 = get_base64_image("logo_catering")
logo_principale_b64 = get_base64_image("logo")


@str_lit.dialog("📦 Gestione Prodotto Magazzino", width="large")
def modale_gestione_prodotto():
  MODO = str_lit.session_state.get("modale_prodotto", "nuovo")
  p_edit = (
      str_lit.session_state.get("prodotto_in_modifica", {})
      if MODO == "modifica"
      else {}
  )

  testo_titolo_prodotto = (
      "✏️ Modifica Prodotto"
      if MODO == "modifica"
      else "🆕 Aggiungi Nuovo Prodotto"
  )
  str_lit.markdown(f"#### {testo_titolo_prodotto}")

  with str_lit.form("form_prodotto_dialog"):
    col_form1, col_form2 = str_lit.columns(2)
    with col_form1:
      f_nome = str_lit.text_input("🏷️ Nome Prodotto", value=p_edit.get("nome", ""))
      f_codice = str_lit.text_input("🆔 Codice Identificativo", value=p_edit.get("codice", ""))

      cat_corrente = p_edit.get("categoria", "TAVOLI")
      cat_index = (
          CATEGORIE_PRODOTTI.index(cat_corrente)
          if cat_corrente in CATEGORIE_PRODOTTI
          else 0
      )
      f_categoria = str_lit.selectbox("📂 Categoria", CATEGORIE_PRODOTTI, index=cat_index)

    with col_form2:
      f_qta = str_lit.number_input(
          "📦 Quantità",
          value=int(p_edit.get("quantita", 1)),
          min_value=0,
      )
      f_pos = str_lit.text_input("📍 Posizione in magazzino", value=p_edit.get("posizione", ""))
      f_prezzo = str_lit.number_input(
          "💶 Prezzo di noleggio (€)",
          value=float(p_edit.get("costo_noleggio", 0.0)),
          min_value=0.0,
      )

    f_note = str_lit.text_area("📝 Note (opzionale)", value=p_edit.get("note", ""))
    f_foto = str_lit.file_uploader(
        "📸 Carica Foto Prodotto (opzionale)", type=["png", "jpg", "jpeg"]
    )

    if str_lit.form_submit_button("💾 Salva Prodotto", type="primary", use_container_width=True):
      percorso_foto_finale = (
          salva_immagine_su_disco(f_foto)
          if f_foto
          else p_edit.get("foto_path", None)
      )

      nuovo_item = {
          "codice": f_codice,
          "nome": f_nome,
          "categoria": f_categoria,
          "quantita": f_qta,
          "posizione": f_pos,
          "costo_noleggio": f_prezzo,
          "note": f_note,
          "foto_path": percorso_foto_finale,
      }

      if MODO == "modifica":
        idx = str_lit.session_state.indice_modifica
        if idx is not None and 0 <= idx < len(str_lit.session_state.prodotti_noleggio):
          str_lit.session_state.prodotti_noleggio[idx] = nuovo_item
      else:
        str_lit.session_state.prodotti_noleggio.append(nuovo_item)

      salva_dati_esterni()
      str_lit.toast(f"✅ Prodotto '{f_nome}' salvato con successo!")
      str_lit.session_state.modale_prodotto = None
      str_lit.session_state.prodotto_in_modifica = None
      str_lit.rerun()


@str_lit.dialog("🆕 Crea Nuovo Evento", width="large")
def modale_crea_evento():
  with str_lit.form("form_nuovo_evento_dialog"):
    str_lit.markdown("#### 📋 Dati Principali dell'Evento")
    col_n1, col_n2, col_n3 = str_lit.columns(3)
    with col_n1:
      n_nome = str_lit.text_input("🏷️ Nome Evento / Cliente *")
    with col_n2:
      n_data = str_lit.text_input(
          "📅 Data Evento (es. 25/12/2026)",
          value=date.today().strftime("%d/%m/%Y"),
      )
    with col_n3:
      n_loc = str_lit.text_input("📍 Location")

    col_p1, col_p2, col_p3 = str_lit.columns(3)
    with col_p1:
      n_ospiti = str_lit.number_input("👥 Numero Ospiti", min_value=0, value=0)
    with col_p2:
      n_bambini = str_lit.number_input("👶 Numero Bambini", min_value=0, value=0)
    with col_p3:
      n_staff = str_lit.number_input("👔 Numero Staff", min_value=0, value=0)

    str_lit.markdown("---")
    str_lit.markdown("#### 📝 Note e Allegati per Reparto")

    def comp_sezione_creazione(titolo_rep, chiave_pref):
      str_lit.markdown(f"**{titolo_rep}**")
      t_val = str_lit.text_area(
          f"Testo note - {titolo_rep}",
          key=f"dialog_crea_{chiave_pref}_t",
          label_visibility="collapsed",
          placeholder=f"Inserisci note per {titolo_rep.lower()}...",
      )
      f_val = str_lit.file_uploader(
          f"Aggiungi allegati ({titolo_rep})",
          accept_multiple_files=True,
          type=["png", "jpg", "jpeg", "pdf"],
          key=f"dialog_crea_{chiave_pref}_f",
      )
      str_lit.markdown("")
      return t_val, f_val

    t_tutti, f_tutti = comp_sezione_creazione("Note per tutti", "tutti")
    t_sala, f_sala = comp_sezione_creazione("Note per la sala", "sala")
    t_cucina, f_cucina = comp_sezione_creazione("Note per la cucina", "cucina")
    t_mag, f_mag = comp_sezione_creazione("Note per il magazzino", "magazzino")

    if str_lit.form_submit_button(
        "💾 Salva e Registra Evento", type="primary", use_container_width=True
    ):
      if not n_nome.strip():
        str_lit.error("Il campo 'Nome Evento / Cliente' è obbligatorio.")
      else:

        def process_files(files):
          res = []
          if files:
            for f in files:
              res.append({
                  "nome_file": f.name,
                  "dati_b64": base64.b64encode(f.getvalue()).decode("utf-8"),
              })
          return res

        dt_parsed = parse_data_evento(n_data)
        nuovo_ev = {
            "nome_evento": n_nome,
            "data": dt_parsed.strftime("%Y-%m-%d"),
            "data_display": n_data.strip(),
            "location": n_loc,
            "ospiti": n_ospiti,
            "bambini": n_bambini,
            "staff": n_staff,
            "note_tutti": t_tutti,
            "allegati_tutti": process_files(f_tutti),
            "note_sala": t_sala,
            "allegati_sala": process_files(f_sala),
            "note_cucina": t_cucina,
            "allegati_cucina": process_files(f_cucina),
            "note_magazzino": t_mag,
            "allegati_magazzino": process_files(f_mag),
        }
        str_lit.session_state.eventi_catering.append(nuovo_ev)
        salva_dati_esterni()
        str_lit.toast("✅ Evento creato con successo!")
        str_lit.rerun()


@str_lit.dialog("✏️ Modifica Evento", width="large")
def modale_modifica_evento(idx_ev):
  if idx_ev >= len(str_lit.session_state.eventi_catering):
    str_lit.warning("Evento non trovato.")
    return

  ev_mod = str_lit.session_state.eventi_catering[idx_ev]

  with str_lit.form(f"form_mod_ev_dialog_{idx_ev}"):
    m_nome = str_lit.text_input(
        "Nome Evento / Cliente", value=ev_mod.get("nome_evento", "")
    )

    col_m1, col_m2 = str_lit.columns(2)
    with col_m1:
      m_data = str_lit.text_input(
          "Data Evento",
          value=ev_mod.get(
              "data_display",
              ev_mod.get("data", date.today().strftime("%d/%m/%Y")),
          ),
      )
    with col_m2:
      m_loc = str_lit.text_input("Location", value=ev_mod.get("location", ""))

    col_mp1, col_mp2, col_mp3 = str_lit.columns(3)
    with col_mp1:
      m_osp = str_lit.number_input(
          "Ospiti", min_value=0, value=int(ev_mod.get("ospiti", 0))
      )
    with col_mp2:
      m_bam = str_lit.number_input(
          "Bambini", min_value=0, value=int(ev_mod.get("bambini", 0))
      )
    with col_mp3:
      m_stf = str_lit.number_input(
          "Staff", min_value=0, value=int(ev_mod.get("staff", 0))
      )

    str_lit.markdown("---")
    str_lit.markdown("#### 📝 Modifica Note e Gestione Allegati per Reparto")

    def comp_sezione_modifica(titolo_rep, chiave_testo, chiave_all):
      str_lit.markdown(f"**{titolo_rep}**")
      t_curr = ev_mod.get(chiave_testo, "")
      a_curr = ev_mod.get(chiave_all, [])

      t_mod = str_lit.text_area(
          f"Testo - {titolo_rep}",
          value=t_curr,
          key=f"dialog_t_{chiave_testo}_{idx_ev}",
          label_visibility="collapsed",
      )

      if a_curr:
        str_lit.markdown("📁 *Allegati esistenti (deseleziona per rimuovere):*")
        for a_idx, all_item in enumerate(a_curr):
          str_lit.checkbox(
              f"Mantieni: {all_item['nome_file']}",
              value=True,
              key=f"dialog_mantieni_{chiave_testo}_{idx_ev}_{a_idx}",
          )

      f_aggiunta = str_lit.file_uploader(
          f"Aggiungi nuovi allegati - {titolo_rep}",
          accept_multiple_files=True,
          type=["png", "jpg", "jpeg", "pdf"],
          key=f"dialog_up_{chiave_testo}_{idx_ev}",
      )
      str_lit.markdown("")
      return t_mod, f_aggiunta, a_curr

    mt_tutti, mf_tutti, curr_tutti = comp_sezione_modifica(
        "Note per tutti", "note_tutti", "allegati_tutti"
    )
    mt_sala, mf_sala, curr_sala = comp_sezione_modifica(
        "Note per la sala", "note_sala", "allegati_sala"
    )
    mt_cucina, mf_cucina, curr_cucina = comp_sezione_modifica(
        "Note per la cucina", "note_cucina", "allegati_cucina"
    )
    mt_mag, mf_mag, curr_mag = comp_sezione_modifica(
        "Note per il magazzino", "note_magazzino", "allegati_magazzino"
    )

    col_btn_mod1, col_btn_mod2 = str_lit.columns(2)
    with col_btn_mod1:
      btn_salva_ev = str_lit.form_submit_button(
          "💾 Salva Modifiche", type="primary", use_container_width=True
      )
    with col_btn_mod2:
      btn_elim_ev = str_lit.form_submit_button(
          "🗑️ Elimina Evento", use_container_width=True
      )

    if btn_salva_ev:

      def filtra_e_unisci_allegati(existing_list, nuovi_files, chiave_testo):
        risultati = []
        if existing_list:
          for a_idx, item in enumerate(existing_list):
            if str_lit.session_state.get(
                f"dialog_mantieni_{chiave_testo}_{idx_ev}_{a_idx}", True
            ):
              risultati.append(item)
        if nuovi_files:
          for f in nuovi_files:
            risultati.append({
                "nome_file": f.name,
                "dati_b64": base64.b64encode(f.getvalue()).decode("utf-8"),
            })
        return risultati

      dt_parsed = parse_data_evento(m_data)
      ev_mod.update({
          "nome_evento": m_nome,
          "data": dt_parsed.strftime("%Y-%m-%d"),
          "data_display": m_data.strip(),
          "location": m_loc,
          "ospiti": m_osp,
          "bambini": m_bam,
          "staff": m_stf,
          "note_tutti": mt_tutti,
          "allegati_tutti": filtra_e_unisci_allegati(
              curr_tutti, mf_tutti, "note_tutti"
          ),
          "note_sala": mt_sala,
          "allegati_sala": filtra_e_unisci_allegati(
              curr_sala, mf_sala, "note_sala"
          ),
          "note_cucina": mt_cucina,
          "allegati_cucina": filtra_e_unisci_allegati(
              curr_cucina, mf_cucina, "note_cucina"
          ),
          "note_magazzino": mt_mag,
          "allegati_magazzino": filtra_e_unisci_allegati(
              curr_mag, mf_mag, "note_magazzino"
          ),
      })
      salva_dati_esterni()
      str_lit.toast("✅ Modifiche salvate con successo!")
      str_lit.rerun()

    if btn_elim_ev:
      str_lit.session_state.eventi_catering.pop(idx_ev)
      salva_dati_esterni()
      str_lit.toast("🗑️ Evento eliminato con successo!")
      str_lit.rerun()


if str_lit.session_state.utente_loggato is None:
  str_lit.markdown("<br><br>", unsafe_allow_html=True)
  html_loghi_login = '<div style="display: flex; justify-content: center; align-items: center; gap: 100px; margin-bottom: 40px;">'
  if logo_noleggio_b64:
    html_loghi_login += f'<img src="data:image/png;base64,{logo_noleggio_b64}" style="max-height: 200px; object-fit: contain;">'
  if logo_catering_b64:
    html_loghi_login += f'<img src="data:image/png;base64,{logo_catering_b64}" style="max-height: 200px; object-fit: contain;">'
  html_loghi_login += "</div>"

  str_lit.markdown(html_loghi_login, unsafe_allow_html=True)
  str_lit.markdown(
      "<h2 style='text-align: center; margin-bottom: 30px;'>🔐 Accesso"
      " Gestionale Unificato</h2>",
      unsafe_allow_html=True,
  )

  col_f1, col_form, col_f2 = str_lit.columns([1, 1.5, 1])
  with col_form:
    with str_lit.form("form_login"):
      username_inserito = str_lit.text_input("Username o indirizzo email")
      password_inserita = str_lit.text_input("Password", type="password")
      if str_lit.form_submit_button(
          "Accesso", use_container_width=True, type="primary"
      ):
        trovato = None
        for usr, dati in str_lit.session_state.utenti_autorizzati.items():
          if usr == username_inserito or dati.get("email") == username_inserito:
            if dati["password"] == password_inserita:
              trovato = dati.copy()
              trovato["username_chiave"] = usr
        if trovato:
          str_lit.session_state.utente_loggato = trovato
          str_lit.session_state.area_selezionata = None
          str_lit.toast(f"✅ Benvenuto, {trovato['nome']}!")
          str_lit.rerun()
        else:
          str_lit.error("Credenziali non corrette.")
else:
  utente = str_lit.session_state.utente_loggato
  ruolo_utente = utente.get("ruolo", "")

  is_admin = ruolo_utente == "Amministratore"
  is_wedding = ruolo_utente == "Wedding"
  is_cucina = ruolo_utente == "Cucina"
  is_sala = ruolo_utente == "Sala"
  is_magazzino = ruolo_utente == "Magazzino"
  is_magazzino2 = ruolo_utente == "Magazzino2"

  puoi_gestire_eventi = is_admin or is_wedding

  col_top1, col_top2 = str_lit.columns([8, 1])
  with col_top2:
    if str_lit.button("Esci", key="btn_esci_app", use_container_width=True):
      str_lit.session_state.utente_loggato = None
      str_lit.session_state.area_selezionata = None
      str_lit.rerun()

  if str_lit.session_state.area_selezionata is None:
    if logo_principale_b64:
      str_lit.markdown(
          f'<div style="text-align: center; margin-bottom: 10px;"><img'
          f' src="data:image/png;base64,{logo_principale_b64}"'
          ' style="max-height: 120px;"></div>',
          unsafe_allow_html=True,
      )
    else:
      str_lit.markdown(
          "<h1 style='text-align: center; margin-bottom: 0;'>🌟 Gestionale"
          " Ergo & Scardaci</h1>",
          unsafe_allow_html=True,
      )

    str_lit.markdown(
        "<p style='text-align: center; color: #666; font-size: 1.1rem;"
        " margin-top: 5px; margin-bottom: 40px;'>Piattaforma Unificata: Catering"
        " & Noleggio Attrezzature per Eventi</p>",
        unsafe_allow_html=True,
    )

    if is_admin:
      c1, c2, c3, c4 = str_lit.columns(4)
      with c1:
        with str_lit.container(border=True):
          if logo_noleggio_b64:
            str_lit.markdown(
                f'<div style="height: 100px; display: flex; align-items: center;'
                ' justify-content: center; margin-bottom: 15px;"><img'
                f' src="data:image/png;base64,{logo_noleggio_b64}"'
                ' style="max-height: 100%; max-width: 100%; object-fit:'
                ' contain;"></div>',
                unsafe_allow_html=True,
            )
          else:
            str_lit.markdown(
                "<div style='height: 100px; display: flex; align-items: center;"
                " justify-content: center; font-size: 3rem; margin-bottom:"
                " 15px;'>📦</div>",
                unsafe_allow_html=True,
            )
          str_lit.markdown("### Magazzino & Noleggio")
          str_lit.markdown(
              "<div class='card-desc'>Gestione scorte e codici QR.</div>",
              unsafe_allow_html=True,
          )
          if str_lit.button(
              "Apri Magazzino",
              use_container_width=True,
              type="primary",
              key="btn_h_mag",
          ):
            str_lit.session_state.area_selezionata = "opzione_1"
            str_lit.rerun()
            str_lit.stop()

      with c2:
        with str_lit.container(border=True):
          if logo_catering_b64:
            str_lit.markdown(
                f'<div style="height: 100px; display: flex; align-items: center;'
                ' justify-content: center; margin-bottom: 15px;"><img'
                f' src="data:image/png;base64,{logo_catering_b64}"'
                ' style="max-height: 100%; max-width: 100%; object-fit:'
                ' contain;"></div>',
                unsafe_allow_html=True,
            )
          else:
            str_lit.markdown(
                "<div style='height: 100px; display: flex; align-items: center;"
                " justify-content: center; font-size: 3rem; margin-bottom:"
                " 15px;'>🍽️</div>",
                unsafe_allow_html=True,
            )
          str_lit.markdown("### Catering ed Eventi")
          str_lit.markdown(
              "<div class='card-desc'>Pianificazione eventi e reparti.</div>",
              unsafe_allow_html=True,
          )
          if str_lit.button(
              "Apri Catering",
              use_container_width=True,
              type="primary",
              key="btn_h_cat",
          ):
            str_lit.session_state.area_selezionata = "opzione_2"
            str_lit.rerun()
            str_lit.stop()

      with c3:
        with str_lit.container(border=True):
          str_lit.markdown(
              "<div style='height: 100px; display: flex; align-items: center;"
              " justify-content: center; font-size: 3rem; margin-bottom:"
              " 15px;'>📋</div>",
              unsafe_allow_html=True,
          )
          str_lit.markdown("### Lista Attrezzature")
          str_lit.markdown(
              "<div class='card-desc'>Crea e invia liste per eventi.</div>",
              unsafe_allow_html=True,
          )
          if str_lit.button(
              "Apri Liste",
              use_container_width=True,
              type="primary",
              key="btn_h_liste",
          ):
            str_lit.session_state.area_selezionata = "opzione_4"
            str_lit.rerun()
            str_lit.stop()

      with c4:
        with str_lit.container(border=True):
          str_lit.markdown(
              "<div style='height: 100px; display: flex; align-items: center;"
              " justify-content: center; font-size: 3rem; margin-bottom:"
              " 15px;'>👥</div>",
              unsafe_allow_html=True,
          )
          str_lit.markdown("### Sistema Ruoli")
          str_lit.markdown(
              "<div class='card-desc'>Configurazione utenti autorizzati.</div>",
              unsafe_allow_html=True,
          )
          if str_lit.button(
              "Apri Ruoli",
              use_container_width=True,
              type="primary",
              key="btn_h_ruoli",
          ):
            str_lit.session_state.area_selezionata = "opzione_3"
            str_lit.rerun()
            str_lit.stop()
    else:
      c1, c2, c3 = str_lit.columns(3)
      with c1:
        if is_magazzino or is_magazzino2:
          with str_lit.container(border=True):
            if logo_noleggio_b64:
              str_lit.markdown(
                  f'<div style="height: 100px; display: flex; align-items:'
                  ' center; justify-content: center; margin-bottom:'
                  f' 15px;"><img src="data:image/png;base64,{logo_noleggio_b64}"'
                  ' style="max-height: 100%; max-width: 100%; object-fit:'
                  ' contain;"></div>',
                  unsafe_allow_html=True,
              )
            else:
              str_lit.markdown(
                  "<div style='height: 100px; display: flex; align-items:"
                  " center; justify-content: center; font-size: 3rem;"
                  " margin-bottom: 15px;'>📦</div>",
                  unsafe_allow_html=True,
              )
            str_lit.markdown("### Magazzino & Noleggio")
            str_lit.markdown(
                "<div class='card-desc'>Gestione scorte e codici QR.</div>",
                unsafe_allow_html=True,
            )
            if str_lit.button(
                "Apri Magazzino", use_container_width=True, type="primary"
            ):
              str_lit.session_state.area_selezionata = "opzione_1"
              str_lit.rerun()
              str_lit.stop()

      with c2:
        if is_wedding or is_cucina or is_sala or is_magazzino or is_magazzino2:
          with str_lit.container(border=True):
            if logo_catering_b64:
              str_lit.markdown(
                  f'<div style="height: 100px; display: flex; align-items:'
                  ' center; justify-content: center; margin-bottom:'
                  f' 15px;"><img src="data:image/png;base64,{logo_catering_b64}"'
                  ' style="max-height: 100%; max-width: 100%; object-fit:'
                  ' contain;"></div>',
                  unsafe_allow_html=True,
              )
            else:
              str_lit.markdown(
                  "<div style='height: 100px; display: flex; align-items:"
                  " center; justify-content: center; font-size: 3rem;"
                  " margin-bottom: 15px;'>🍽️</div>",
                  unsafe_allow_html=True,
              )
            str_lit.markdown("### Catering ed Eventi")
            str_lit.markdown(
                "<div class='card-desc'>Pianificazione eventi e reparti.</div>",
                unsafe_allow_html=True,
            )
            if str_lit.button(
                "Apri Catering", use_container_width=True, type="primary"
            ):
              str_lit.session_state.area_selezionata = "opzione_2"
              str_lit.rerun()
              str_lit.stop()
      with c3:
        pass

  else:
    if str_lit.button("⬅️ Torna alla Home"):
      str_lit.session_state.area_selezionata = None
      str_lit.session_state.modale_prodotto = None
      str_lit.query_params.clear()
      str_lit.rerun()
      str_lit.stop()

    if str_lit.session_state.area_selezionata == "opzione_1":
      
      str_lit.subheader("📦 Magazzino & Noleggio Attrezzature")

      col_btn_nuovo, col_cat_filtro, col_search = str_lit.columns([1, 1.5, 2.5])
      with col_btn_nuovo:
        if is_admin:
          str_lit.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
          if str_lit.button(
              "➕ Nuovo Prodotto", use_container_width=True, type="primary"
          ):
            str_lit.session_state.modale_prodotto = "nuovo"
            str_lit.session_state.prodotto_in_modifica = {}
            modale_gestione_prodotto()

      with col_cat_filtro:
        cat_opzioni_mag = ["Tutte le categorie"] + CATEGORIE_PRODOTTI
        categoria_filtro_mag = str_lit.selectbox(
            "Filtra per Categoria", cat_opzioni_mag, key="filtro_cat_magazzino"
        )

      with col_search:
        default_search = codice_scansionato if codice_scansionato else ""
        ricerca_query = str_lit.text_input(
            "Cerca",
            value=default_search,
            placeholder="Cerca per nome, codice...",
        )

      testo_ricerca = ricerca_query.strip().lower()
      prodotti_filtrati = []
      for idx, p in enumerate(str_lit.session_state.prodotti_noleggio):
        match_cat = (categoria_filtro_mag == "Tutte le categorie") or (p.get("categoria") == categoria_filtro_mag)
        match_text = (
            not testo_ricerca
            or testo_ricerca in p.get("nome", "").lower()
            or testo_ricerca in p.get("codice", "").lower()
            or testo_ricerca in p.get("categoria", "").lower()
        )
        if match_cat and match_text:
          prodotti_filtrati.append((idx, p))

      for idx, p in prodotti_filtrati:
        with str_lit.container(border=True):
          if is_admin:
            col_img, col_info, col_qr, col_azioni = str_lit.columns(
                [1.2, 3.8, 1, 1.5]
            )
          else:
            col_img, col_info, col_qr = str_lit.columns([1.2, 4.8, 1])

          with col_img:
            str_lit.markdown(
                html_thumb(p.get("foto_path"), size=110),
                unsafe_allow_html=True,
            )

          with col_info:
            str_lit.markdown(
                f"<div style='font-size: 1.25rem; font-weight: bold;"
                f" margin-bottom: 4px;'>{p.get('nome', 'Senza Nome')} &nbsp;<span"
                " style='font-size: 0.9rem; color: #555; font-weight: normal;'>ID:"
                f" `{p.get('codice', '-')}`</span></div>",
                unsafe_allow_html=True,
            )
            str_lit.markdown(
                f"<div style='font-size: 1.05rem; margin-bottom:"
                f" 4px;'><b>📂 Categoria:</b> {p.get('categoria', 'N/D')}</div>",
                unsafe_allow_html=True,
            )

            testo_prezzo = "" if is_magazzino else f" &nbsp;|&nbsp; <b>💶 Prezzo:</b> {p.get('costo_noleggio', 0)}€"

            str_lit.markdown(
                f"<div style='font-size: 1.05rem; margin-bottom: 4px;'>"
                f"<b>📍 Posizione in magazzino:</b> {p.get('posizione', '-')}"
                f" &nbsp;|&nbsp; <b>📦 Q.tà:</b> {p.get('quantita', 0)}"
                f"{testo_prezzo}</div>",
                unsafe_allow_html=True,
            )
            if p.get("note"):
              str_lit.markdown(
                  f"<div style='font-size: 0.95rem; color: #666;'>📝"
                  f" <i>Note: {p['note']}</i></div>",
                  unsafe_allow_html=True,
              )

          with col_qr:
            str_lit.markdown(
                "<div style='display: flex; flex-direction: column;"
                " align-items: center; justify-content: center; height:"
                " 100%;'>",
                unsafe_allow_html=True,
            )
            qr_bytes = genera_qrcode_img(
                f"{BASE_URL}/?codice={p.get('codice', '')}"
            )
            str_lit.image(qr_bytes, width=95)
            str_lit.markdown("</div>", unsafe_allow_html=True)

          if is_admin:
            with col_azioni:
              str_lit.markdown(
                  "<div style='display: flex; flex-direction: column;"
                  " justify-content: center; height: 100%; gap: 6px;'>",
                  unsafe_allow_html=True,
              )
              if str_lit.button(
                  "✏️ Modifica", key=f"edit_{idx}", use_container_width=True
              ):
                str_lit.session_state.modale_prodotto = "modifica"
                str_lit.session_state.prodotto_in_modifica = p
                str_lit.session_state.indice_modifica = idx
                modale_gestione_prodotto()
              if str_lit.button(
                  "📄 Duplica", key=f"dup_{idx}", use_container_width=True
              ):
                nuovo_p = p.copy()
                nuovo_p["codice"] = p.get("codice", "") + "-COPIA"
                str_lit.session_state.prodotti_noleggio.append(nuovo_p)
                salva_dati_esterni()
                str_lit.rerun()
              if str_lit.button(
                  "🗑️ Elimina", key=f"del_{idx}", use_container_width=True
              ):
                str_lit.session_state.prodotti_noleggio.pop(idx)
                salva_dati_esterni()
                str_lit.rerun()
              str_lit.markdown("</div>", unsafe_allow_html=True)

    elif str_lit.session_state.area_selezionata == "opzione_2":
      str_lit.subheader("🍽️ Gestione Eventi & Catering")

      if puoi_gestire_eventi:
        if str_lit.button(
            "➕ Crea Nuovo Evento", type="primary", use_container_width=True
        ):
          modale_crea_evento()

      str_lit.markdown("---")
      str_lit.subheader("📜 Cronologia Eventi")

      if not str_lit.session_state.eventi_catering:
        str_lit.info(
            "Nessun evento registrato nella cronologia. Crea il primo evento"
            " sopra."
        )
      else:

        def sort_key_evento(item):
          idx, ev = item
          d_str = ev.get("data", "")
          return parse_data_evento(d_str)

        eventi_ordinati = sorted(
            list(enumerate(str_lit.session_state.eventi_catering)),
            key=sort_key_evento,
        )

        for idx_ev, ev in eventi_ordinati:
          data_disp = ev.get(
              "data_display", ev.get("data", "Data non specificata")
          )
          with str_lit.container(border=True):
            col_info_ev_c1, col_info_ev_c2 = str_lit.columns([4, 1])
            with col_info_ev_c1:
              str_lit.markdown(
                  f"### 📅 {data_disp} — 🏷️"
                  f" {ev.get('nome_evento', 'Evento')}"
              )
              str_lit.markdown(
                  f"📍 **Location:** {ev.get('location', 'N/D')} | 👥"
                  f" **Ospiti:** {ev.get('ospiti', 0)} | 👶 **Bambini:**"
                  f" {ev.get('bambini', 0)} | 👔 **Staff:**"
                  f" {ev.get('staff', 0)}"
              )
            with col_info_ev_c2:
              if puoi_gestire_eventi:
                if str_lit.button(
                    "✏️ Modifica",
                    key=f"btn_mod_dialog_{idx_ev}",
                    use_container_width=True,
                    type="primary",
                ):
                  modale_modifica_evento(idx_ev)

            with str_lit.expander("📖 Visualizza dettagli e note per reparto"):
              str_lit.markdown(
                  f"📊 **Dati Importanti Evento:** 👥 Ospiti:"
                  f" **{ev.get('ospiti', 0)}** | 👶 Bambini:"
                  f" **{ev.get('bambini', 0)}** | 👔 Staff:"
                  f" **{ev.get('staff', 0)}**"
              )
              str_lit.markdown("---")

              if is_cucina:
                str_lit.markdown("**Note per tutti:**")
                str_lit.info(ev.get("note_tutti") or "Nessuna nota.")
                str_lit.markdown("**Note per la cucina:**")
                str_lit.success(ev.get("note_cucina") or "Nessuna nota.")
                if ev.get("allegati_cucina"):
                  for att in ev.get("allegati_cucina"):
                    str_lit.download_button(
                        f"📥 Scarica allegato: {att['nome_file']}",
                        data=base64.b64decode(att["dati_b64"]),
                        file_name=att["nome_file"],
                        key=f"dl_cucina_c_{idx_ev}_{att['nome_file']}",
                    )
              elif is_sala:
                str_lit.markdown("**Note per tutti:**")
                str_lit.info(ev.get("note_tutti") or "Nessuna nota.")
                str_lit.markdown("**Note per la sala:**")
                str_lit.success(ev.get("note_sala") or "Nessuna nota.")
                if ev.get("allegati_sala"):
                  for att in ev.get("allegati_sala"):
                    str_lit.download_button(
                        f"📥 Scarica allegato: {att['nome_file']}",
                        data=base64.b64decode(att["dati_b64"]),
                        file_name=att["nome_file"],
                        key=f"dl_sala_s_{idx_ev}_{att['nome_file']}",
                    )
              elif is_magazzino or is_magazzino2:
                str_lit.markdown("**Note per tutti:**")
                str_lit.info(ev.get("note_tutti") or "Nessuna nota.")
                str_lit.markdown("**Note per il magazzino:**")
                str_lit.success(ev.get("note_magazzino") or "Nessuna nota.")
                if ev.get("allegati_magazzino"):
                  for att in ev.get("allegati_magazzino"):
                    str_lit.download_button(
                        f"📥 Scarica allegato: {att['nome_file']}",
                        data=base64.b64decode(att["dati_b64"]),
                        file_name=att["nome_file"],
                        key=f"dl_mag_{idx_ev}_{att['nome_file']}",
                    )
              else:
                str_lit.markdown("**Note per tutti:**")
                str_lit.info(ev.get("note_tutti") or "Nessuna nota.")
                str_lit.markdown("**Note per la sala:**")
                str_lit.write(ev.get("note_sala") or "Nessuna nota.")
                str_lit.markdown("**Note per la cucina:**")
                str_lit.write(ev.get("note_cucina") or "Nessuna nota.")
                str_lit.markdown("**Note per il magazzino:**")
                str_lit.write(ev.get("note_magazzino") or "Nessuna nota.")
                if ev.get("allegati_tutti"):
                  str_lit.markdown("📎 **Allegati Note per Tutti:**")
                  for att in ev.get("allegati_tutti"):
                    str_lit.download_button(
                        f"📥 Scarica allegato: {att['nome_file']}",
                        data=base64.b64decode(att["dati_b64"]),
                        file_name=att["nome_file"],
                        key=f"dl_tutti_gen_{idx_ev}_{att['nome_file']}",
                    )

    elif str_lit.session_state.area_selezionata == "opzione_3":
      if is_admin:
        str_lit.subheader("👥 Ruoli: Gestione Utenti e Credenziali")
        str_lit.write(
            "Crea e gestisci le credenziali e i permessi di accesso per il"
            " personale autorizzato."
        )

        str_lit.markdown("#### ➕ Aggiungi Nuovo Utente")
        with str_lit.form("form_nuovo_utente"):
          col_u1, col_u2 = str_lit.columns(2)
          with col_u1:
            ins_user_key = str_lit.text_input("Username di accesso (es. cucina2)")
            ins_pass = str_lit.text_input("Password", type="password")
            ins_nome = str_lit.text_input("Nome e Cognome / Reparto")
          with col_u2:
            ins_email = str_lit.text_input("Indirizzo Email")
            ins_ruolo = str_lit.selectbox(
                "Ruolo / Permessi", LISTA_RUOLI_DISPONIBILI
            )

          if str_lit.form_submit_button(
              "💾 Salva Nuovo Utente", type="primary", use_container_width=True
          ):
            if not ins_user_key.strip() or not ins_pass.strip():
              str_lit.error("Username e Password sono campi obbligatori.")
            elif (
                ins_user_key.strip()
                in str_lit.session_state.utenti_autorizzati
            ):
              str_lit.error("Questo username esiste già. Scegline un altro.")
            else:
              str_lit.session_state.utenti_autorizzati[ins_user_key.strip()] = {
                  "password": ins_pass.strip(),
                  "ruolo": ins_ruolo,
                  "nome": ins_nome.strip() or ins_user_key.strip(),
                  "email": ins_email.strip(),
              }
              salva_dati_esterni()
              str_lit.toast(f"✅ Utente '{ins_user_key}' creato con successo!")
              str_lit.rerun()

        str_lit.markdown("---")
        str_lit.markdown("#### 📋 Utenti Attualmente Registrati")

        for usr_k, usr_v in list(
            str_lit.session_state.utenti_autorizzati.items()
        ):
          with str_lit.container(border=True):
            col_info_u, col_del_u = str_lit.columns([4, 1])
            with col_info_u:
              str_lit.markdown(f"**👤 Utente / Username:** `{usr_k}`")
              str_lit.markdown(
                  f"🏷️ **Nome:** {usr_v.get('nome', '-')} | 🛡️ **Ruolo:**"
                  f" `{usr_v.get('ruolo', '-')}` | ✉️ **Email:**"
                  f" {usr_v.get('email', '-')}"
              )
              str_lit.markdown(f"🔑 **Password:** `{usr_v.get('password', '-')}`")
            with col_del_u:
              if usr_k != "admin":
                if str_lit.button(
                    "🗑️ Elimina", key=f"del_usr_{usr_k}", use_container_width=True
                ):
                  del str_lit.session_state.utenti_autorizzati[usr_k]
                  salva_dati_esterni()
                  str_lit.toast(f"🗑️ Utente '{usr_k}' eliminato.")
                  str_lit.rerun()
              else:
                str_lit.caption("Admin principale protetto")

    elif str_lit.session_state.area_selezionata == "opzione_4":
      if not is_admin:
        str_lit.error("Accesso non autorizzato.")
      else:
        str_lit.subheader("📋 Lista Attrezzature per Eventi")
        str_lit.write(
            "Seleziona i prodotti dal catalogo, controllali suddivisi per"
            " categoria e inoltrali come allegato nella sezione 'Note per"
            " tutti' dell'evento desiderato."
        )

        col_cat, col_spacer, col_lista = str_lit.columns([5, 0.5, 5])

        with col_cat:
          with str_lit.container(border=True):
            str_lit.markdown("#### 🔍 Catalogo Prodotti")
            
            cat_opzioni = ["Tutte le categorie"] + CATEGORIE_PRODOTTI
            cat_selezionata_filtro = str_lit.selectbox(
                "📂 Seleziona Categoria", cat_opzioni, key="filtro_cat_catalogo"
            )
            ricerca_cat = str_lit.text_input(
                "Cerca per nome o codice", key="search_cat_lista", placeholder="Digita per cercare un prodotto..."
            )

          prod_disp = str_lit.session_state.prodotti_noleggio
          t_ricerca = ricerca_cat.strip().lower()

          mostra_prodotti = (t_ricerca != "") or (cat_selezionata_filtro != "Tutte le categorie")

          if not mostra_prodotti:
            str_lit.info("💡 Seleziona una categoria dal menu a tendina o digita un termine di ricerca per visualizzare i prodotti del catalogo.")
          else:
            prodotti_filtrati_cat = []
            for p_idx, p_item in enumerate(prod_disp):
              cat_item = p_item.get("categoria", "")
              nome_item = p_item.get("nome", "").lower()
              codice_item = p_item.get("codice", "").lower()

              match_cat = (cat_selezionata_filtro == "Tutte le categorie") or (cat_item == cat_selezionata_filtro)
              match_text = (t_ricerca == "") or (t_ricerca in nome_item) or (t_ricerca in codice_item)

              if match_cat and match_text:
                prodotti_filtrati_cat.append((p_idx, p_item))

            with str_lit.container(height=550, border=True):
              for p_idx, p_item in prodotti_filtrati_cat:
                with str_lit.container(border=True):
                  c_img_cat, c_info_cat = str_lit.columns([1, 3])
                  with c_img_cat:
                    str_lit.markdown(
                        html_thumb(p_item.get("foto_path"), size=55),
                        unsafe_allow_html=True,
                    )
                  with c_info_cat:
                    str_lit.markdown(
                        f"**{p_item.get('nome')}**"
                        f" (`{p_item.get('categoria')}`)"
                    )
                    str_caption = (
                        f"Disp: {p_item.get('quantita', 0)} | Pos:"
                        f" {p_item.get('posizione', '-')}"
                    )
                    str_lit.caption(str_caption)

                  q_ins = str_lit.number_input(
                      "Quantità",
                      min_value=1,
                      max_value=max(1, int(p_item.get("quantita", 1))),
                      value=1,
                      key=f"q_add_{p_idx}_{p_item.get('codice', '')}",
                  )

                  gia_in_lista = any(
                      item_L.get("codice") == p_item.get("codice")
                      and item_L.get("nome") == p_item.get("nome")
                      for item_L in str_lit.session_state.lista_attrezzature_corrente
                  )

                  if gia_in_lista:
                    str_lit.button(
                        "✅ Già in Lista",
                        key=f"btn_add_lista_{p_idx}_{p_item.get('codice', '')}",
                        use_container_width=True,
                        disabled=True,
                    )
                  else:
                    if str_lit.button(
                        "➕ Aggiungi alla Lista",
                        key=f"btn_add_lista_{p_idx}_{p_item.get('codice', '')}",
                        use_container_width=True,
                    ):
                      trovato_in_lista = False
                      for item_L in str_lit.session_state.lista_attrezzature_corrente:
                        if (
                            item_L.get("codice") == p_item.get("codice")
                            and item_L.get("nome") == p_item.get("nome")
                        ):
                          item_L["quantita_selezionata"] += q_ins
                          trovato_in_lista = True
                          break
                      if not trovato_in_lista:
                        nuovo_elem = p_item.copy()
                        nuovo_elem["quantita_selezionata"] = q_ins
                        str_lit.session_state.lista_attrezzature_corrente.append(
                            nuovo_elem
                        )
                      str_lit.toast(
                          f"Aggiunto {p_item.get('nome')} (Q.tà: {q_ins})"
                      )
                      str_lit.rerun()

        with col_lista:
          with str_lit.container(height=720, border=True):
            str_lit.markdown("#### 🛒 Lista Attrezzature Selezionata")

            if not str_lit.session_state.lista_attrezzature_corrente:
              str_lit.info(
                  "La lista è attualmente vuota. Aggiungi i prodotti dal"
                  " catalogo a sinistra."
              )
            else:
              str_lit.markdown("##### 📂 Divisione per Categoria")

              prodotti_per_cat = {}
              for item in str_lit.session_state.lista_attrezzature_corrente:
                cat = item.get("categoria", "ALTRO")
                if cat not in prodotti_per_cat:
                  prodotti_per_cat[cat] = []
                prodotti_per_cat[cat].append(item)

              for cat_nome, lista_cat in prodotti_per_cat.items():
                colore_cat = COLORI_CATEGORIE.get(cat_nome, "#4b5563")
                
                str_lit.markdown(
                    f"<div style='background-color: {colore_cat}; color: white; padding: 8px 12px; "
                    f"border-radius: 6px; font-weight: bold; margin-top: 12px; margin-bottom: 8px; "
                    f"display: flex; justify-content: space-between; align-items: center;'>"
                    f"<span>📂 {cat_nome}</span>"
                    f"<span style='background-color: rgba(255,255,255,0.25); padding: 2px 8px; "
                    f"border-radius: 12px; font-size: 0.8rem;'>{len(lista_cat)} articoli</span>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

                with str_lit.expander("Visualizza articoli", expanded=True):
                  for idx_l, item_l in enumerate(lista_cat):
                    c_code = item_l.get('codice', idx_l)
                    col_l1, col_l2, col_l3 = str_lit.columns([3, 1, 1])
                    with col_l1:
                      str_lit.markdown(
                          f"**{item_l.get('nome')}**"
                          f" (`ID: {item_l.get('codice', '-')}`)"
                      )
                      str_caption = f"Pos: {item_l.get('posizione', '-')}"
                      str_lit.caption(str_caption)
                    with col_l2:
                      nuova_q = str_lit.number_input(
                          "Q.tà",
                          min_value=1,
                          value=int(item_l.get("quantita_selezionata", 1)),
                          key=f"mod_q_{cat_nome}_{c_code}_{idx_l}",
                      )
                      item_l["quantita_selezionata"] = nuova_q
                    with col_l3:
                      str_lit.markdown("<br>", unsafe_allow_html=True)
                      if str_lit.button(
                          "🗑️ Rimuovi",
                          key=f"rem_{cat_nome}_{c_code}_{idx_l}",
                          use_container_width=True,
                      ):
                        str_lit.session_state.lista_attrezzature_corrente.remove(
                            item_l
                        )
                        str_lit.rerun()

              str_lit.markdown("---")
              str_lit.markdown("#### 📤 Inoltra Lista a un Evento")

              if not str_lit.session_state.eventi_catering:
                str_lit.warning(
                    "Nessun evento disponibile. Crea prima un evento nella"
                    " sezione Catering."
                )
              else:
                eventi_scelta = {
                    f"{ev.get('nome_evento')} ({ev.get('data_display', ev.get('data'))})": e_idx
                    for e_idx, ev in enumerate(
                        str_lit.session_state.eventi_catering
                    )
                }
                evento_selezionato_str = str_lit.selectbox(
                    "Seleziona Evento di destinazione",
                    list(eventi_scelta.keys()),
                )

                col_s1, col_s2 = str_lit.columns(2)
                with col_s1:
                  if str_lit.button(
                      "💾 Salva e Inoltra",
                      type="primary",
                      use_container_width=True,
                  ):
                    idx_ev_scelto = eventi_scelta[evento_selezionato_str]
                    ev_target = str_lit.session_state.eventi_catering[
                        idx_ev_scelto
                    ]

                    nome_file_allegato = f"Lista_Attrezzature_{ev_target.get('nome_evento', 'evento').replace(' ', '_')}"

                    if REPORTLAB_DISPONIBILE:
                      try:
                        file_bytes = genera_pdf_lista_attrezzature(
                            ev_target.get("nome_evento"),
                            str_lit.session_state.lista_attrezzature_corrente,
                        )
                        nome_file_allegato += ".pdf"
                      except Exception:
                        file_bytes = genera_testo_lista_attrezzature(
                            ev_target.get("nome_evento"),
                            str_lit.session_state.lista_attrezzature_corrente,
                        )
                        nome_file_allegato += ".txt"
                    else:
                      file_bytes = genera_testo_lista_attrezzature(
                          ev_target.get("nome_evento"),
                          str_lit.session_state.lista_attrezzature_corrente,
                      )
                      nome_file_allegato += ".txt"

                    if "allegati_tutti" not in ev_target:
                      ev_target["allegati_tutti"] = []

                    ev_target["allegati_tutti"].append({
                        "nome_file": nome_file_allegato,
                        "dati_b64": base64.b64encode(file_bytes).decode("utf-8"),
                    })

                    nota_esistente = ev_target.get("note_tutti", "")
                    testo_aggiunta = (
                        f"\n[LISTA ATTREZZATURE INOLTRATA]: Aggiunta nuova lista attrezzature ({nome_file_allegato}) con "
                        f"{len(str_lit.session_state.lista_attrezzature_corrente)} articoli."
                    )
                    ev_target["note_tutti"] = (
                        nota_esistente + testo_aggiunta
                    ).strip()

                    salva_dati_esterni()
                    str_lit.toast(f"✅ Lista attrezzature inoltrata all'evento '{ev_target.get('nome_evento')}'!")
                    str_lit.session_state.lista_attrezzature_corrente = []
                    str_lit.rerun()

                with col_s2:
                  if str_lit.button("🧹 Svuota Lista", use_container_width=True):
                    str_lit.session_state.lista_attrezzature_corrente = []
                    str_lit.rerun()
