from datetime import date, datetime
import calendar
import base64
from io import BytesIO
import json
import os
import socket
import uuid
import difflib
import re
import unicodedata
import qrcode
import streamlit as str_lit
from supabase import create_client, Client
import requests
from urllib.parse import quote

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
# CONFIGURAZIONE SUPABASE
# ==============================================================================
try:
    SUPABASE_URL = str_lit.secrets["SUPABASE_URL"]
    SUPABASE_KEY = str_lit.secrets["SUPABASE_KEY"]
except Exception:
    str_lit.error("Configurare SUPABASE_URL e SUPABASE_KEY nei Secrets di Streamlit.")
    str_lit.stop()
BUCKET_IMMAGINI = "immagini_prodotti"

@str_lit.cache_resource
def init_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

if not SUPABASE_URL or not SUPABASE_KEY:
    str_lit.error("⚠️ Sostituisci SUPABASE_URL e SUPABASE_KEY con le tue credenziali reali.")
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

    ::-webkit-scrollbar-thumb,
    div[data-testid="stVerticalBlockBorderWrapper"]::-webkit-scrollbar-thumb,
    div[data-testid="stScrollable"]::-webkit-scrollbar-thumb,
    div[aria-label="Scrollable container"]::-webkit-scrollbar-thumb {
        background-color: #0056b3 !important;
        background: #0056b3 !important;
        border-radius: 6px !important;
        border: 2px solid #f3f4f6 !important;
        min-height: 40px !important;
        visibility: visible !important;
        opacity: 1 !important;
        display: block !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stScrollable"],
    div[aria-label="Scrollable container"] {
        scrollbar-width: auto !important;
        scrollbar-color: #0056b3 #f3f4f6 !important;
        overflow-y: scroll !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]::-webkit-scrollbar,
    div[data-testid="stScrollable"]::-webkit-scrollbar,
    div[aria-label="Scrollable container"]::-webkit-scrollbar,
    div[data-testid="stVerticalBlockBorderWrapper"][style*="550px"]::-webkit-scrollbar {
        width: 16px !important;
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }

    /* Catalogo Lista Attrezzature: contenitore alto 550px */
    div[data-testid="stVerticalBlockBorderWrapper"][style*="550px"],
    div[data-testid="stVerticalBlockBorderWrapper"][style*="height: 550"] {
        overflow-y: scroll !important;
        scrollbar-width: auto !important;
        scrollbar-color: #0056b3 #f3f4f6 !important;
        scrollbar-gutter: stable !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"][style*="550px"]::-webkit-scrollbar-thumb,
    div[data-testid="stVerticalBlockBorderWrapper"][style*="height: 550"]::-webkit-scrollbar-thumb {
        background: #0056b3 !important;
        background-color: #0056b3 !important;
        border-radius: 8px !important;
        border: 2px solid #f3f4f6 !important;
        opacity: 1 !important;
        visibility: visible !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"][style*="550px"]::-webkit-scrollbar-track,
    div[data-testid="stVerticalBlockBorderWrapper"][style*="height: 550"]::-webkit-scrollbar-track {
        background: #f3f4f6 !important;
        visibility: visible !important;
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

    /* Tag delle categorie selezionate nel multiselect: regola globale */
    [data-baseweb="tag"],
    div[data-baseweb="tag"],
    span[data-baseweb="tag"] {
        background: #0056b3 !important;
        background-color: #0056b3 !important;
        color: #ffffff !important;
        border: 1px solid #004494 !important;
        border-radius: 7px !important;
        font-weight: 700 !important;
        box-shadow: none !important;
    }
    [data-baseweb="tag"] *,
    [data-baseweb="tag"] span,
    [data-baseweb="tag"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
        stroke: #ffffff !important;
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


def categorie_prodotto(valore):
  """Restituisce sempre una lista, compatibile con dati vecchi e multipli."""
  if isinstance(valore, list):
    return [str(x).strip() for x in valore if str(x).strip()]
  if not valore:
    return []
  return [parte.strip() for parte in str(valore).split(",") if parte.strip()]


def testo_categorie(valore):
  categorie = categorie_prodotto(valore)
  return ", ".join(categorie) if categorie else "N/D"


def normalizza_testo_ricerca(valore):
  testo = unicodedata.normalize("NFD", str(valore or "").lower())
  testo = "".join(car for car in testo if unicodedata.category(car) != "Mn")
  return " ".join(testo.split())


def varianti_parola_italiana(parola):
  parola = normalizza_testo_ricerca(parola)
  varianti = {parola}
  if len(parola) >= 4:
    if parola.endswith("i"):
      varianti.update({parola[:-1] + "o", parola[:-1] + "e", parola[:-1] + "a"})
    elif parola.endswith("e"):
      varianti.update({parola[:-1] + "a", parola[:-1] + "o", parola[:-1] + "i"})
    elif parola.endswith("a"):
      varianti.update({parola[:-1] + "e", parola[:-1] + "i"})
    elif parola.endswith("o"):
      varianti.add(parola[:-1] + "i")
  return varianti


def parole_simili(parola_query, parola_testo):
  if parola_query == parola_testo:
    return True
  if len(parola_query) < 4 or len(parola_testo) < 4:
    return False
  # Accetta una lettera finale mancante o aggiunta: JASMIN/JASMINE.
  if abs(len(parola_query) - len(parola_testo)) <= 2:
    if parola_query.startswith(parola_testo) or parola_testo.startswith(parola_query):
      return True
    if parola_query[:4] == parola_testo[:4]:
      return True
  return difflib.SequenceMatcher(None, parola_query, parola_testo).ratio() >= 0.78


def ricerca_intelligente(query, campi):
  query_norm = normalizza_testo_ricerca(query)
  if not query_norm:
    return True
  testo_norm = normalizza_testo_ricerca(" ".join(str(c or "") for c in campi))
  if query_norm in testo_norm:
    return True
  parole_testo = re.findall(r"[a-z0-9]+", testo_norm)
  parole_query = query_norm.split()
  for parola_query in parole_query:
    varianti = varianti_parola_italiana(parola_query)
    if not any(
        any(parole_simili(variante, parola_testo) for parola_testo in parole_testo)
        for variante in varianti
    ):
      return False
  return True


COLORI_CATEGORIE = {
    "TAVOLI": "#0056b3",
    "SEDIE": "#2f6fb0",
    "PIATTI E SOTTOPIATTI": "#4b9f9a",
    "BICCHIERI": "#6b8fc4",
    "CUCINA": "#6f7fbf",
    "ARREDO": "#567d8e",
    "TOVAGLIATO": "#2d8bb8",
    "ARGENTERIA": "#4b5563",
    "POSATERIA": "#3d6b8f",
    "VASSOI": "#3d9b9b",
    "LUCI E CANDELABRI": "#7893b0",
}

LISTA_RUOLI_DISPONIBILI = [
    "Amministratore",
    "Wedding",
    "Cucina",
    "Sala",
    "Magazzino",
    "Magazzino2",
]


@str_lit.cache_data(ttl=600, show_spinner=False)
def carica_dati_esterni():
  try:
    # Vengono richiesti solo i campi necessari; gli allegati restano nel DB
    # ma non vengono caricati nella pagina del magazzino.
    res_prod = supabase.table("prodotti_noleggio").select(
        "id,codice,nome,categoria,quantita,posizione,costo_noleggio,note,foto_path"
    ).order("nome").execute()
    prodotti = res_prod.data or []

    # Gli eventi vengono caricati solo entrando nella sezione Catering o Liste.
    eventi = []

    res_usr = supabase.table("utenti_autorizzati").select(
        "id,username,password,ruolo,nome,email"
    ).execute()
    utenti = {}
    for u in (res_usr.data or []):
      username = u.get("username")
      if username:
        utenti[username] = {
            "id": u.get("id"),
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
    return {"prodotti_noleggio": [], "eventi_catering": [], "utenti_autorizzati": None}


@str_lit.cache_data(ttl=600, show_spinner=False)
def carica_eventi_solo_quando_servono():
  """Carica gli eventi solo quando viene aperta una sezione che li usa."""
  try:
    return supabase.table("eventi_catering").select("*").order("data").execute().data or []
  except Exception as e:
    str_lit.error(f"Errore di caricamento eventi da Supabase: {e}")
    return []


def salva_dati_esterni():
  try:
    # Gli aggiornamenti usano l'id del database. Non vengono eseguite
    # SELECT aggiuntive per ogni prodotto.
    for p in str_lit.session_state.prodotti_noleggio:
      payload = {k: p.get(k) for k in (
          "codice", "nome", "categoria", "quantita", "posizione",
          "costo_noleggio", "note", "foto_path")}
      payload = {k: v for k, v in payload.items() if v is not None}
      if p.get("id"):
        res = supabase.table("prodotti_noleggio").update(payload).eq("id", p["id"]).execute()
      else:
        res = supabase.table("prodotti_noleggio").insert(payload).execute()
        if res.data:
          p["id"] = res.data[0].get("id")
      if not res.data and p.get("id"):
        raise RuntimeError(f"Prodotto non salvato: {p.get('nome', '')}")

    for ev in str_lit.session_state.eventi_catering:
      payload = {k: ev.get(k) for k in (
          "nome_evento", "data", "data_display", "location", "ospiti",
          "bambini", "staff", "note_tutti", "allegati_tutti", "note_sala",
          "allegati_sala", "note_cucina", "allegati_cucina",
          "note_magazzino", "allegati_magazzino")}
      payload = {k: v for k, v in payload.items() if v is not None}
      if ev.get("id"):
        res = supabase.table("eventi_catering").update(payload).eq("id", ev["id"]).execute()
      else:
        res = supabase.table("eventi_catering").insert(payload).execute()
        if res.data:
          ev["id"] = res.data[0].get("id")
      if not res.data and ev.get("id"):
        raise RuntimeError(f"Evento non salvato: {ev.get('nome_evento', '')}")

    for usr_k, usr_v in str_lit.session_state.utenti_autorizzati.items():
      payload = {"username": usr_k, "password": usr_v.get("password"),
                 "ruolo": usr_v.get("ruolo"), "nome": usr_v.get("nome"),
                 "email": usr_v.get("email")}
      existing = supabase.table("utenti_autorizzati").select("id").eq("username", usr_k).execute()
      if existing.data:
        res = supabase.table("utenti_autorizzati").update(payload).eq("username", usr_k).execute()
      else:
        res = supabase.table("utenti_autorizzati").insert(payload).execute()
      if not res.data and not existing.data:
        raise RuntimeError(f"Utente non salvato: {usr_k}")

    carica_dati_esterni.clear()
  except Exception as e:
    str_lit.error(f"Errore durante il salvataggio su Supabase: {e}")


def salva_evento_singolo(ev):
  """Salva soltanto un evento, evitando il lento salvataggio globale."""
  try:
    payload = {k: ev.get(k) for k in (
        "nome_evento", "data", "data_display", "location", "ospiti",
        "bambini", "staff", "note_tutti", "allegati_tutti", "note_sala",
        "allegati_sala", "note_cucina", "allegati_cucina",
        "note_magazzino", "allegati_magazzino")}
    payload = {k: v for k, v in payload.items() if v is not None}
    if ev.get("id"):
      res = supabase.table("eventi_catering").update(payload).eq("id", ev["id"]).execute()
    else:
      res = supabase.table("eventi_catering").insert(payload).execute()
      if res.data:
        ev["id"] = res.data[0].get("id")
    if not res.data:
      raise RuntimeError("Evento non salvato")
    # Non invalidiamo il caricamento completo dei prodotti: dopo un salvataggio
    # evento la pagina deve restare rapida e i dati sono già aggiornati in sessione.
    carica_eventi_solo_quando_servono.clear()
    return True
  except Exception as e:
    str_lit.error(f"Errore durante il salvataggio dell’evento: {e}")
    return False


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


def get_app_url():
  """Restituisce l’URL completo dell’app, usato nei QR code."""
  try:
    url = str_lit.context.url
    if url:
      return url.split("?")[0].rstrip("/")
  except Exception:
    pass
  return str_lit.secrets.get("APP_URL", "").rstrip("/")


BASE_URL = get_app_url()


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
      from PIL import Image, ImageOps

      # Ridimensiona e comprime la foto per risparmiare spazio e velocizzare
      # il caricamento. L'originale non viene mai salvato nel database.
      immagine = Image.open(uploaded_file)
      immagine = ImageOps.exif_transpose(immagine).convert("RGB")
      immagine.thumbnail((2400, 2400), Image.Resampling.LANCZOS)

      buffer = BytesIO()
      immagine.save(buffer, format="JPEG", quality=90, optimize=True, progressive=True)
      file_bytes = buffer.getvalue()
      nome_file_unico = f"{uuid.uuid4()}.jpg"

      supabase.storage.from_(BUCKET_IMMAGINI).upload(
          path=nome_file_unico,
          file=file_bytes,
          file_options={"content-type": "image/jpeg", "upsert": "false"},
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
if "eventi_caricati" not in str_lit.session_state:
  str_lit.session_state.eventi_caricati = False

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

# Demo temporanea Noleggi Confermati: non legge e non scrive su Supabase.
if "noleggi_demo" not in str_lit.session_state:
  str_lit.session_state.noleggi_demo = [
    {"id": 1, "titolo": "Noleggio Villa Aurora", "inizio": datetime(2026, 6, 5, 9, 0), "fine": datetime(2026, 6, 6, 18, 0), "stato": "confermato", "location": "Villa Aurora", "referente": "Marco Bianchi", "telefono": "+39 333 1234567", "note": "Consegna ingresso principale.", "bolla": "Bolla_05062026.pdf", "ddt": "DDT_05062026.pdf", "vario": "Foto_carico.jpg"},
    {"id": 2, "titolo": "Secondo noleggio", "inizio": datetime(2026, 6, 5, 19, 0), "fine": datetime(2026, 6, 5, 23, 0), "stato": "non confermato", "location": "Villa Aurora", "referente": "Paolo Neri", "telefono": "+39 333 2223344", "note": "Da confermare.", "bolla": "Bolla_2.pdf", "ddt": "DDT_2.pdf", "vario": "Planimetria.pdf"},
    {"id": 3, "titolo": "Noleggio Tavoli e Sedie", "inizio": datetime(2026, 6, 24, 8, 0), "fine": datetime(2026, 6, 25, 20, 0), "stato": "confermato", "location": "Castello San Marco", "referente": "Andrea Neri", "telefono": "+39 328 9876543", "note": "Ritiro il giorno successivo.", "bolla": "Bolla_24062026.pdf", "ddt": "DDT_24062026.pdf", "vario": "Lista_materiale.pdf"},
  ]
if "noleggio_demo_mese" not in str_lit.session_state:
  str_lit.session_state.noleggio_demo_mese = 6
if "noleggio_demo_anno" not in str_lit.session_state:
  str_lit.session_state.noleggio_demo_anno = 2026

@str_lit.dialog("Nuovo Noleggio Confermato", width="large")
def modale_crea_noleggio_demo(data_selezionata):
  str_lit.write(f"Data selezionata: **{data_selezionata.strftime('%d/%m/%Y')}**")
  with str_lit.form("form_crea_noleggio_demo"):
    titolo = str_lit.text_input("Nome del noleggio")
    col_a, col_b = str_lit.columns(2)
    with col_a:
      data_inizio = str_lit.date_input("Data inizio", data_selezionata)
      ora_inizio = str_lit.time_input("Ora inizio")
      location = str_lit.text_input("Location")
      referente = str_lit.text_input("Persona di riferimento")
      telefono = str_lit.text_input("Numero di telefono")
    with col_b:
      data_fine = str_lit.date_input("Data fine", data_selezionata)
      ora_fine = str_lit.time_input("Ora fine")
      stato = str_lit.selectbox("Stato", ["Confermato", "Non confermato"])
      note = str_lit.text_area("Note varie")
    a1, a2, a3 = str_lit.columns(3)
    with a1:
      bolla = str_lit.file_uploader("Bolla con prezzo", type=["pdf", "jpg", "jpeg", "png"])
    with a2:
      ddt = str_lit.file_uploader("DDT", type=["pdf", "jpg", "jpeg", "png"])
    with a3:
      vario = str_lit.file_uploader("Vario", type=["pdf", "jpg", "jpeg", "png"])
    salva = str_lit.form_submit_button("Salva noleggio", type="primary", use_container_width=True)
  if salva:
    if not titolo.strip() or not location.strip() or not referente.strip() or not telefono.strip():
      str_lit.error("Compila nome, location, referente e numero di telefono.")
    else:
      nuovo_id = max([x.get("id", 0) for x in str_lit.session_state.noleggi_demo] + [0]) + 1
      str_lit.session_state.noleggi_demo.append({
          "id": nuovo_id, "titolo": titolo, "inizio": datetime.combine(data_inizio, ora_inizio),
          "fine": datetime.combine(data_fine, ora_fine), "stato": "confermato" if stato == "Confermato" else "non confermato",
          "location": location, "referente": referente, "telefono": telefono, "note": note,
          "bolla": bolla.name if bolla else "Nessun file", "ddt": ddt.name if ddt else "Nessun file", "vario": vario.name if vario else "Nessun file"})
      str_lit.session_state.noleggio_demo_crea_data = None
      str_lit.success("Noleggio creato nella demo temporanea.")
      str_lit.rerun()


@str_lit.dialog("Dettaglio Noleggio Confermato", width="large")
def modale_modifica_noleggio_demo(noleggio_id):
  noleggio = next((x for x in str_lit.session_state.noleggi_demo if x.get("id") == noleggio_id), None)
  if not noleggio:
    str_lit.error("Noleggio non trovato.")
    return
  utente_corrente = str_lit.session_state.get("utente_loggato") or {}
  ruolo_corrente = utente_corrente.get("ruolo", "")
  puo_modificare = ruolo_corrente in {"Amministratore", "Magazzino2"}
  if not puo_modificare:
    str_lit.info("Modalità sola visualizzazione.")
  with str_lit.form(f"form_modifica_noleggio_demo_{noleggio_id}"):
    titolo = str_lit.text_input("Nome del noleggio", noleggio["titolo"], disabled=not puo_modificare)
    col_a, col_b = str_lit.columns(2)
    with col_a:
      data_inizio = str_lit.date_input("Data inizio", noleggio["inizio"].date(), disabled=not puo_modificare)
      ora_inizio = str_lit.time_input("Ora inizio", noleggio["inizio"].time(), disabled=not puo_modificare)
      location = str_lit.text_input("Location", noleggio["location"], disabled=not puo_modificare)
      referente = str_lit.text_input("Persona di riferimento", noleggio["referente"], disabled=not puo_modificare)
      telefono = str_lit.text_input("Numero di telefono", noleggio["telefono"], disabled=not puo_modificare)
    with col_b:
      data_fine = str_lit.date_input("Data fine", noleggio["fine"].date(), disabled=not puo_modificare)
      ora_fine = str_lit.time_input("Ora fine", noleggio["fine"].time(), disabled=not puo_modificare)
      stato = str_lit.selectbox("Stato", ["Confermato", "Non confermato"], index=0 if noleggio["stato"] == "confermato" else 1, disabled=not puo_modificare)
      note = str_lit.text_area("Note varie", noleggio["note"], disabled=not puo_modificare)
    str_lit.markdown("#### Allegati")
    if ruolo_corrente in {"Amministratore", "Magazzino2"}:
      str_lit.write(f"Bolla con prezzo: `{noleggio['bolla']}`")
    if ruolo_corrente in {"Amministratore", "Magazzino2", "Magazzino"}:
      str_lit.write(f"DDT: `{noleggio['ddt']}`")
      str_lit.write(f"Vario: `{noleggio['vario']}`")
    salva = str_lit.form_submit_button("Salva modifiche", type="primary", use_container_width=True, disabled=not puo_modificare)
  if salva:
    noleggio.update({"titolo": titolo, "inizio": datetime.combine(data_inizio, ora_inizio), "fine": datetime.combine(data_fine, ora_fine), "location": location, "referente": referente, "telefono": telefono, "note": note, "stato": "confermato" if stato == "Confermato" else "non confermato"})
    str_lit.session_state.noleggio_demo_modifica = None
    str_lit.success("Modifiche salvate nella demo temporanea.")
    str_lit.rerun()


def mostra_noleggi_demo():
  str_lit.subheader("📅 Noleggi Confermati")
  str_lit.caption("Anteprima completa con dati dimostrativi. Supabase non viene utilizzato in questa fase.")
  col_mese, col_anno = str_lit.columns([2, 1])
  with col_mese:
    mese = str_lit.selectbox("Mese calendario", list(range(1, 13)), index=str_lit.session_state.noleggio_demo_mese - 1, format_func=lambda m: ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"][m - 1], key="noleggio_mese_select")
  with col_anno:
    anno = str_lit.selectbox("Anno calendario", list(range(2025, 2036)), index=list(range(2025, 2036)).index(str_lit.session_state.noleggio_demo_anno), key="noleggio_anno_select")
  str_lit.markdown("""
  <style>
  .noleggi-layout-title {font-size:1rem; font-weight:800; color:#344054; margin:8px 0 10px;}
  .noleggi-week {display:grid; grid-template-columns:repeat(7,1fr); gap:6px; margin-bottom:6px;}
  .noleggi-weekday {text-align:center; color:#667085; font-size:.72rem; font-weight:800; letter-spacing:.04em; padding:6px 0;}
  .noleggi-month-note {color:#667085; font-size:.82rem; margin:0 0 12px;}
  .noleggi-legend {display:flex; gap:16px; color:#667085; font-size:.78rem; margin:0 0 12px;}
  .noleggi-dot {display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:5px;}
  .noleggi-side-panel {background:#f8fafc; border:1px solid #d9e2ec; border-radius:12px; padding:18px; min-height:500px;}
  .noleggi-side-title {font-size:1.2rem; font-weight:800; color:#1d2939; margin-bottom:3px;}
  .noleggi-side-subtitle {font-size:.82rem; color:#667085; margin-bottom:16px;}
  .noleggi-day-muted {height:70px; background:#f8fafc; border:1px solid #eef2f6; border-radius:8px;}
  .noleggi-dots {display:flex; justify-content:center; gap:4px; min-height:12px; padding:4px 0 2px;}
  .noleggi-event-dot {display:inline-block; width:8px; height:8px; border-radius:50%;}
  </style>
  """, unsafe_allow_html=True)

  if "noleggio_demo_giorno_selezionato" not in str_lit.session_state:
    str_lit.session_state.noleggio_demo_giorno_selezionato = date(int(anno), int(mese), 1)
  giorno_selezionato = str_lit.session_state.noleggio_demo_giorno_selezionato
  if giorno_selezionato.year != int(anno) or giorno_selezionato.month != int(mese):
    giorno_selezionato = date(int(anno), int(mese), 1)
    str_lit.session_state.noleggio_demo_giorno_selezionato = giorno_selezionato

  calendario_col, pannello_col = str_lit.columns([1.55, 1], gap="large")
  with calendario_col:
    str_lit.markdown("<div class='noleggi-layout-title'>Calendario mensile</div>", unsafe_allow_html=True)
    str_lit.markdown(f"<div class='noleggi-month-note'>Seleziona un giorno per vedere i noleggi nel pannello laterale.</div>", unsafe_allow_html=True)
    str_lit.markdown("<div class='noleggi-legend'><span><i class='noleggi-dot' style='background:#0056b3'></i>Confermato</span><span><i class='noleggi-dot' style='background:#e7a928'></i>Non confermato</span></div>", unsafe_allow_html=True)
    intestazioni = str_lit.columns(7, gap="small")
    for col, nome_giorno in zip(intestazioni, ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]):
      with col:
        str_lit.markdown(f"<div class='noleggi-weekday'>{nome_giorno}</div>", unsafe_allow_html=True)
    for settimana in calendar.Calendar(firstweekday=0).monthdatescalendar(int(anno), int(mese)):
      colonne = str_lit.columns(7, gap="small")
      for colonna, giorno in zip(colonne, settimana):
        with colonna:
          if giorno.month != int(mese):
            str_lit.markdown("<div class='noleggi-day-muted'></div>", unsafe_allow_html=True)
            continue
          eventi_giorno = [n for n in str_lit.session_state.noleggi_demo if n["inizio"].date() <= giorno <= n["fine"].date()]
          selezionato = giorno == giorno_selezionato
          simboli_eventi = []
          for noleggio in eventi_giorno[:5]:
            simboli_eventi.append("🔵" if noleggio["stato"] == "confermato" else "🟠")
          riga_eventi = " ".join(simboli_eventi) if simboli_eventi else "·"
          etichetta = f"{'● ' if selezionato else ''}{giorno.day}\n{riga_eventi}"
          if len(eventi_giorno) > 5:
            etichetta += f"  +{len(eventi_giorno)-5}"
          if str_lit.button(etichetta, key=f"demo_giorno_{giorno}", use_container_width=True):
            str_lit.session_state.noleggio_demo_giorno_selezionato = giorno
            str_lit.session_state.noleggio_demo_crea_data = None
            str_lit.session_state.noleggio_demo_modifica = None
            str_lit.rerun()

  with pannello_col:
    eventi_selezionati = [n for n in str_lit.session_state.noleggi_demo if n["inizio"].date() <= giorno_selezionato <= n["fine"].date()]
    with str_lit.container(border=True):
      str_lit.markdown(f"<div class='noleggi-side-title'>{giorno_selezionato.strftime('%A %d %B %Y').capitalize()}</div>", unsafe_allow_html=True)
      str_lit.markdown("<div class='noleggi-side-subtitle'>Noleggi presenti nella giornata selezionata</div>", unsafe_allow_html=True)
      if str_lit.button("＋ Crea nuovo noleggio", type="primary", use_container_width=True, key="demo_crea_noleggio_laterale"):
        str_lit.session_state.noleggio_demo_crea_data = giorno_selezionato
        str_lit.session_state.noleggio_demo_modifica = None
        str_lit.rerun()
      str_lit.markdown("---")
      if not eventi_selezionati:
        str_lit.info("Nessun noleggio in questa giornata. Puoi crearne uno con il pulsante sopra.")
      else:
        for noleggio in eventi_selezionati:
          colore = "🔵" if noleggio["stato"] == "confermato" else "🟠"
          orario = f"{noleggio['inizio'].strftime('%H:%M')} – {noleggio['fine'].strftime('%H:%M')}"
          if noleggio["inizio"].date() != giorno_selezionato:
            orario = f"In corso · fino alle {noleggio['fine'].strftime('%H:%M')}"
          if str_lit.button(f"{colore} {noleggio['titolo']}\n{orario}", key=f"demo_pannello_noleggio_{noleggio['id']}", use_container_width=True):
            str_lit.session_state.noleggio_demo_modifica = noleggio["id"]
            str_lit.session_state.noleggio_demo_crea_data = None
            str_lit.rerun()
          str_lit.caption(f"{noleggio['location']} · {noleggio['referente']}")

  if str_lit.session_state.get("noleggio_demo_crea_data"):
    modale_crea_noleggio_demo(str_lit.session_state.noleggio_demo_crea_data)
  if str_lit.session_state.get("noleggio_demo_modifica"):
    modale_modifica_noleggio_demo(str_lit.session_state.noleggio_demo_modifica)


query_params = str_lit.query_params
codice_scansionato = query_params.get("codice")

if codice_scansionato and str_lit.session_state.area_selezionata is None:
  str_lit.session_state.area_selezionata = "opzione_1"

# Scheda pubblica QR in sola lettura.
# Viene eseguita prima del login e non mostra mai il prezzo di noleggio.
if codice_scansionato:
  try:
    prodotto_qr = (
        supabase.table("prodotti_noleggio")
        .select("id,codice,nome,categoria,quantita,posizione,note,foto_path")
        .eq("codice", codice_scansionato)
        .limit(1)
        .execute()
        .data
    )
    prodotto_qr = prodotto_qr[0] if prodotto_qr else None
  except Exception as e:
    prodotto_qr = None
    str_lit.error(f"Impossibile leggere il prodotto: {e}")

  if prodotto_qr:
    str_lit.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)
    str_lit.markdown(
        "<h1 style='text-align:center; color:#0056b3;'>Scheda Prodotto</h1>",
        unsafe_allow_html=True,
    )
    str_lit.markdown(
        "<p style='text-align:center; color:#555;'>Consultazione pubblica in sola lettura</p>",
        unsafe_allow_html=True,
    )
    col_qr_img, col_qr_info = str_lit.columns([1.15, 2])
    with col_qr_img:
      if prodotto_qr.get("foto_path"):
        str_lit.image(prodotto_qr.get("foto_path"), use_container_width=True)
      else:
        str_lit.info("Nessuna foto disponibile")
    with col_qr_info:
      str_lit.subheader(prodotto_qr.get("nome") or "Prodotto")
      str_lit.markdown(f"**Codice:** {prodotto_qr.get('codice') or '-'}")
      str_lit.markdown(f"**Categorie:** {testo_categorie(prodotto_qr.get('categoria'))}")
      str_lit.markdown(f"**Quantità:** {prodotto_qr.get('quantita') or 0}")
      str_lit.markdown(f"**Posizione:** {prodotto_qr.get('posizione') or '-'}")
      str_lit.markdown(f"**Note:** {prodotto_qr.get('note') or 'Nessuna nota.'}")
    str_lit.caption("Questa scheda non consente modifiche e non mostra il prezzo di noleggio.")
    str_lit.stop()
  else:
    str_lit.error("Prodotto non trovato. Verifica che il QR sia aggiornato.")
    str_lit.stop()


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

  if MODO == "modifica" and p_edit.get("codice"):
    qr_modifica = genera_qrcode_img(
        f"{BASE_URL}/?codice={quote(str(p_edit.get('codice', '')))}"
    )
    col_qr_mod1, col_qr_mod2 = str_lit.columns([1, 2])
    with col_qr_mod1:
      str_lit.image(qr_modifica, width=145)
    with col_qr_mod2:
      str_lit.markdown("**QR code del prodotto**")
      str_lit.caption("Puoi scaricarlo e stamparlo per applicarlo fisicamente al prodotto.")
      str_lit.download_button(
          "⬇️ Scarica QR code",
          data=qr_modifica,
          file_name=f"QR_{p_edit.get('codice')}.png",
          mime="image/png",
          key=f"download_qr_modifica_{p_edit.get('id', p_edit.get('codice'))}",
      )

  with str_lit.form("form_prodotto_dialog"):
    col_form1, col_form2 = str_lit.columns(2)
    with col_form1:
      f_nome = str_lit.text_input("🏷️ Nome Prodotto", value=p_edit.get("nome", ""))
      f_codice = str_lit.text_input("🆔 Codice Identificativo", value=p_edit.get("codice", ""))

      cat_correnti = categorie_prodotto(p_edit.get("categoria", "TAVOLI"))
      cat_default = [cat for cat in cat_correnti if cat in CATEGORIE_PRODOTTI]
      if not cat_default:
        cat_default = [CATEGORIE_PRODOTTI[0]]
      str_lit.markdown("**📂 Categorie (puoi sceglierne più di una)**")
      f_categorie = []
      cat_key_suffix = str(p_edit.get("id") or p_edit.get("codice") or "nuovo")
      for cat_start in range(0, len(CATEGORIE_PRODOTTI), 3):
        cat_cols = str_lit.columns(3)
        for cat_pos, cat_nome in enumerate(CATEGORIE_PRODOTTI[cat_start:cat_start + 3]):
          with cat_cols[cat_pos]:
            selezionata = str_lit.checkbox(
                cat_nome,
                value=(cat_nome in cat_default),
                key=f"cat_check_{cat_key_suffix}_{cat_nome}",
            )
            if selezionata:
              f_categorie.append(cat_nome)

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
          "id": p_edit.get("id"),
          "codice": f_codice.strip(),
          "nome": f_nome,
          "categoria": ", ".join(f_categorie) if f_categorie else CATEGORIE_PRODOTTI[0],
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
        salva_evento_singolo(nuovo_ev)
        str_lit.toast("✅ Evento creato con successo!")
        str_lit.rerun()


@str_lit.dialog("✏️ Modifica Evento", width="large")
def modale_modifica_evento(idx_ev):
  if idx_ev >= len(str_lit.session_state.eventi_catering):
    str_lit.warning("Evento non trovato.")
    return

  ev_mod = str_lit.session_state.eventi_catering[idx_ev]

  if str_lit.session_state.get(f"eliminazione_evento_in_attesa_{idx_ev}", False):
    str_lit.warning("Conferma eliminazione: questa operazione è definitiva e non può essere annullata.")
    col_conf1, col_conf2 = str_lit.columns(2)
    with col_conf1:
      if str_lit.button("Conferma eliminazione", key=f"conferma_evento_{idx_ev}", type="primary", use_container_width=True):
        try:
          if ev_mod.get("id"):
            supabase.table("eventi_catering").delete().eq("id", ev_mod.get("id")).execute()
          else:
            supabase.table("eventi_catering").delete().eq("nome_evento", ev_mod.get("nome_evento")).eq("data", ev_mod.get("data")).execute()
        except:
          pass
        str_lit.session_state.eventi_catering.pop(idx_ev)
        str_lit.session_state[f"eliminazione_evento_in_attesa_{idx_ev}"] = False
        str_lit.toast("🗑️ Evento eliminato con successo!")
        str_lit.rerun()
    with col_conf2:
      if str_lit.button("Annulla", key=f"annulla_evento_{idx_ev}", use_container_width=True):
        str_lit.session_state[f"eliminazione_evento_in_attesa_{idx_ev}"] = False
        str_lit.rerun()
    str_lit.stop()

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
      salva_evento_singolo(ev_mod)
      str_lit.toast("✅ Modifiche salvate con successo!")
      str_lit.rerun()

    if btn_elim_ev:
      # Il submit del form provoca già il rerun: non forziamo un secondo
      # rerun, altrimenti la finestra di dialogo si chiude prima della conferma.
      str_lit.session_state[f"eliminazione_evento_in_attesa_{idx_ev}"] = True


if str_lit.session_state.utente_loggato is None:
  str_lit.markdown("<br><br>", unsafe_allow_html=True)
  html_loghi_login = """
  <div style="display:flex; justify-content:center; align-items:center;
              gap:90px; margin-bottom:40px; min-height:220px;">
    <div style="width:260px; height:220px; display:flex;
                align-items:center; justify-content:center; overflow:visible;">
  """
  if logo_noleggio_b64:
    html_loghi_login += f'<img src="data:image/png;base64,{logo_noleggio_b64}" style="width:310px; height:245px; object-fit:contain; display:block;">'
  html_loghi_login += """
    </div>
    <div style="width:260px; height:220px; display:flex;
                align-items:center; justify-content:center; overflow:visible;">
  """
  if logo_catering_b64:
    # Il logo Catering contiene più spazio vuoto nel file originale: lo
    # ingrandiamo otticamente senza deformarlo, per bilanciare i due marchi.
    html_loghi_login += f'<img src="data:image/png;base64,{logo_catering_b64}" style="width:360px; height:285px; object-fit:contain; display:block; transform:scale(1.30);">'
  html_loghi_login += """
    </div>
  </div>
  """

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

  # Magazzino2 ha gli stessi permessi del Magazzino, ma non può aprire Catering.
  if is_magazzino2 and str_lit.session_state.area_selezionata == "opzione_2":
    str_lit.session_state.area_selezionata = None

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
          "<h1 style='text-align: center; margin: 0; color: #0056b3 !important; font-size: 2.55rem; font-weight: 700; letter-spacing: -0.02em;'>Gestionale Ergo &amp; Scardaci</h1>",
          unsafe_allow_html=True,
      )

    str_lit.markdown(
        "<p style='text-align: center; color: #0056b3 !important; font-size: 1.1rem;"
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
                ' style="height: 150px; width: 100%; object-fit: contain; transform: scale(1.10);"></div>',
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
      # Nuova voce aggiunta senza modificare le card esistenti.
      c_noleggi, _, _, _ = str_lit.columns(4)
      with c_noleggi:
        with str_lit.container(border=True):
          str_lit.markdown("<div style='height: 100px; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin-bottom: 15px;'>📅</div>", unsafe_allow_html=True)
          str_lit.markdown("### Noleggi Confermati")
          str_lit.markdown("<div class='card-desc'>Calendario dei noleggi e degli eventi.</div>", unsafe_allow_html=True)
          if str_lit.button("Apri Noleggi", use_container_width=True, type="primary", key="btn_h_noleggi_admin"):
            str_lit.session_state.area_selezionata = "opzione_noleggi"
            str_lit.rerun()
      
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
        if is_wedding or is_cucina or is_sala or is_magazzino:
          with str_lit.container(border=True):
            if logo_catering_b64:
              str_lit.markdown(
                  f'<div style="height: 100px; display: flex; align-items:'
                  ' center; justify-content: center; margin-bottom:'
                  f' 15px; overflow:visible;"><img src="data:image/png;base64,{logo_catering_b64}"'
                  ' style="height: 150px; width: 100%; object-fit: contain;'
                  ' transform: scale(1.10);"></div>',
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
        if is_magazzino or is_magazzino2:
          with str_lit.container(border=True):
            str_lit.markdown("<div style='height: 100px; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin-bottom: 15px;'>📅</div>", unsafe_allow_html=True)
            str_lit.markdown("### Noleggi Confermati")
            str_lit.markdown("<div class='card-desc'>Calendario dei noleggi e degli eventi.</div>", unsafe_allow_html=True)
            if str_lit.button("Apri Noleggi", use_container_width=True, type="primary", key="btn_h_noleggi_magazzino"):
              str_lit.session_state.area_selezionata = "opzione_noleggi"
              str_lit.rerun()

  else:
    if str_lit.button("⬅️ Torna alla Home"):
      str_lit.session_state.area_selezionata = None
      str_lit.session_state.modale_prodotto = None
      str_lit.query_params.clear()
      str_lit.rerun()
      str_lit.stop()

    if str_lit.session_state.area_selezionata == "opzione_noleggi":
      mostra_noleggi_demo()

    elif str_lit.session_state.area_selezionata == "opzione_1":
      
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

      testo_ricerca = ricerca_query.strip()
      prodotti_filtrati = []
      for idx, p in enumerate(str_lit.session_state.prodotti_noleggio):
        match_cat = (categoria_filtro_mag == "Tutte le categorie") or (categoria_filtro_mag in categorie_prodotto(p.get("categoria")))
        match_text = ricerca_intelligente(
            testo_ricerca,
            [p.get("nome", ""), p.get("codice", ""), testo_categorie(p.get("categoria"))],
        )
        if match_cat and match_text:
          prodotti_filtrati.append((idx, p))

      page_size = 50
      total_pages = max(1, (len(prodotti_filtrati) + page_size - 1) // page_size)
      page_num = str_lit.number_input(
          f"Pagina catalogo (1-{total_pages})", min_value=1,
          max_value=total_pages, value=1, step=1,
          key="pagina_catalogo_magazzino")
      start_page = (int(page_num) - 1) * page_size
      prodotti_da_mostrare = prodotti_filtrati[start_page:start_page + page_size]

      str_lit.markdown("""
      <style>
      .prodotto-griglia-titolo {font-size:1.08rem; font-weight:700; line-height:1.15; color:#1f2937; min-height:2.35em;}
      .prodotto-griglia-riga {font-size:0.88rem; line-height:1.35; color:#374151; margin:4px 0;}
      .prodotto-griglia-quantita {font-size:1.18rem; font-weight:800; color:#0056b3; background:#eaf3ff; border-radius:8px; padding:5px 8px; margin:6px 0; text-align:center;}
      .prodotto-griglia-nota {font-size:0.82rem; line-height:1.3; color:#6b7280; min-height:2.4em;}
      </style>
      """, unsafe_allow_html=True)

      # Griglia compatta: sette schede per riga su desktop.
      for riga_start in range(0, len(prodotti_da_mostrare), 7):
        blocco_prodotti = prodotti_da_mostrare[riga_start:riga_start + 7]
        colonne_griglia = str_lit.columns(7, gap="small")
        for posizione_colonna, (idx, p) in enumerate(blocco_prodotti):
          with colonne_griglia[posizione_colonna]:
            with str_lit.container(border=True):
              str_lit.markdown(
                  html_thumb(p.get("foto_path"), size=108),
                  unsafe_allow_html=True,
              )
              str_lit.markdown(
                  f"<div class='prodotto-griglia-titolo'>{p.get('nome', 'Senza Nome')}</div>",
                  unsafe_allow_html=True,
              )
              str_lit.markdown(
                  f"<div class='prodotto-griglia-riga'><b>Codice:</b> {p.get('codice', '-')}</div>"
                  f"<div class='prodotto-griglia-riga'><b>Categorie:</b> {testo_categorie(p.get('categoria'))}</div>"
                  f"<div class='prodotto-griglia-riga'><b>Posizione:</b> {p.get('posizione', '-')}</div>",
                  unsafe_allow_html=True,
              )
              str_lit.markdown(
                  f"<div class='prodotto-griglia-quantita'>📦 Quantità: {p.get('quantita', 0)}</div>",
                  unsafe_allow_html=True,
              )
              if not is_magazzino and p.get("costo_noleggio") is not None:
                str_lit.markdown(
                    f"<div class='prodotto-griglia-riga'><b>Prezzo:</b> {p.get('costo_noleggio', 0)}€</div>",
                    unsafe_allow_html=True,
                )
              if p.get("note"):
                str_lit.markdown(
                    f"<div class='prodotto-griglia-nota'>📝 {p.get('note')}</div>",
                    unsafe_allow_html=True,
                )
              else:
                str_lit.markdown("<div class='prodotto-griglia-nota'></div>", unsafe_allow_html=True)

              if is_admin:
                col_mod, col_dup, col_del = str_lit.columns(3)
                with col_mod:
                  if str_lit.button("✏️", key=f"edit_{idx}", help="Modifica", use_container_width=True):
                    str_lit.session_state.modale_prodotto = "modifica"
                    str_lit.session_state.prodotto_in_modifica = p
                    str_lit.session_state.indice_modifica = idx
                    modale_gestione_prodotto()
                with col_dup:
                  if str_lit.button("📄", key=f"dup_{idx}", help="Duplica", use_container_width=True):
                    nuovo_p = p.copy()
                    nuovo_p["codice"] = p.get("codice", "") + "-COPIA"
                    nuovo_p.pop("id", None)
                    str_lit.session_state.prodotti_noleggio.append(nuovo_p)
                    salva_dati_esterni()
                    str_lit.rerun()
                with col_del:
                  with str_lit.popover("🗑️", help="Elimina"):
                    str_lit.warning("Eliminazione definitiva")
                    if str_lit.button(
                        "Conferma", key=f"conferma_elimina_prodotto_{idx}",
                        type="primary", use_container_width=True,
                    ):
                      try:
                        if p.get("id"):
                          supabase.table("prodotti_noleggio").delete().eq("id", p.get("id")).execute()
                        else:
                          supabase.table("prodotti_noleggio").delete().eq("codice", p.get("codice")).execute()
                      except:
                        pass
                      str_lit.session_state.prodotti_noleggio.pop(idx)
                      salva_dati_esterni()
                      str_lit.rerun()


    elif str_lit.session_state.area_selezionata == "opzione_2":
      if not str_lit.session_state.eventi_caricati:
        str_lit.session_state.eventi_catering = carica_eventi_solo_quando_servono()
        str_lit.session_state.eventi_caricati = True
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

              def mostra_sezione_note(titolo, testo, allegati, funzione_colore, prefisso):
                str_lit.markdown(f"**{titolo}:**")
                getattr(str_lit, funzione_colore)(testo or "Nessuna nota.")
                if allegati:
                  str_lit.markdown(f"📎 **Allegati {titolo.replace('Note per ', '')}:**")
                  for att in allegati:
                    str_lit.download_button(
                        f"📥 Scarica allegato: {att['nome_file']}",
                        data=base64.b64decode(att["dati_b64"]),
                        file_name=att["nome_file"],
                        key=f"dl_{prefisso}_{idx_ev}_{att['nome_file']}",
                    )

              mostra_sezione_note(
                  "Note per tutti", ev.get("note_tutti"),
                  ev.get("allegati_tutti") or [], "info", "tutti"
              )

              if is_admin or is_wedding:
                mostra_sezione_note(
                    "Note per la sala", ev.get("note_sala"),
                    ev.get("allegati_sala") or [], "warning", "sala_all"
                )
                mostra_sezione_note(
                    "Note per la cucina", ev.get("note_cucina"),
                    ev.get("allegati_cucina") or [], "success", "cucina_all"
                )
                mostra_sezione_note(
                    "Note per il magazzino", ev.get("note_magazzino"),
                    ev.get("allegati_magazzino") or [], "error", "mag_all"
                )
              elif is_cucina:
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
                  try:
                    supabase.table("utenti_autorizzati").delete().eq("username", usr_k).execute()
                  except:
                    pass
                  del str_lit.session_state.utenti_autorizzati[usr_k]
                  salva_dati_esterni()
                  str_lit.toast(f"🗑️ Utente '{usr_k}' eliminato.")
                  str_lit.rerun()
              else:
                str_lit.caption("Admin principale protetto")

    elif str_lit.session_state.area_selezionata == "opzione_4":
      if not str_lit.session_state.eventi_caricati:
        str_lit.session_state.eventi_catering = carica_eventi_solo_quando_servono()
        str_lit.session_state.eventi_caricati = True
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
          t_ricerca = ricerca_cat.strip()

          mostra_prodotti = (
              (t_ricerca != "")
              or (cat_selezionata_filtro != "Tutte le categorie")
          )

          if not mostra_prodotti:
            str_lit.info("💡 Seleziona una categoria dal menu a tendina o digita un termine di ricerca per visualizzare i prodotti del catalogo.")
          else:
            prodotti_filtrati_cat = []
            for p_idx, p_item in enumerate(prod_disp):
              cat_item = p_item.get("categoria", "")
              categorie_item = categorie_prodotto(cat_item)
              nome_item = p_item.get("nome", "")
              codice_item = p_item.get("codice", "")

              match_cat = (cat_selezionata_filtro == "Tutte le categorie") or (cat_selezionata_filtro in categorie_item)
              match_text = ricerca_intelligente(
                  t_ricerca,
                  [nome_item, codice_item, testo_categorie(p_item.get("categoria"))],
              )

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
                        f" (`{testo_categorie(p_item.get('categoria'))}`)"
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

                    # Il PDF resta esclusivamente nell’elenco allegati.
                    # Il testo delle Note per tutti non viene modificato.
                    salva_evento_singolo(ev_target)
                    str_lit.toast(f"✅ Lista attrezzature inoltrata all'evento '{ev_target.get('nome_evento')}'!")
                    str_lit.session_state.lista_attrezzature_corrente = []
                    str_lit.rerun()

                with col_s2:
                  if str_lit.button("🧹 Svuota Lista", use_container_width=True):
                    str_lit.session_state.lista_attrezzature_corrente = []
                    str_lit.rerun()
