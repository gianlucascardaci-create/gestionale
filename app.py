from datetime import date, datetime, time, timedelta
import calendar
import streamlit as st

st.set_page_config(page_title="Gestionale Ergo & Scardaci", page_icon="📦", layout="wide")

BLUE = "#0056b3"
USERS = {
    "admin": ("admin", "Amministratore"), "magazzino2": ("magazzino2", "Magazzino2"),
    "magazzino1": ("magazzino1", "Magazzino1"), "wedding": ("wedding", "Wedding"),
    "cucina": ("cucina", "Cucina"), "sala": ("sala", "Sala"),
}

if "prodotti" not in st.session_state:
    st.session_state.prodotti = [
        {"codice":"P001","nome":"Sedia Chiavarina","categoria":"Sedie","quantita":180,"posizione":"Scaffale A1"},
        {"codice":"P002","nome":"Piatto Jasmine","categoria":"Piatti","quantita":420,"posizione":"Scaffale B2"},
        {"codice":"P003","nome":"Bicchiere Acqua","categoria":"Bicchieri","quantita":600,"posizione":"Scaffale C1"},
    ]
if "catering" not in st.session_state:
    st.session_state.catering = [
        {"id":1,"nome":"Matrimonio Rossi","data":"2026-06-18","location":"Palazzo Blu","ospiti":150,"note":"Allestimento sala principale."},
        {"id":2,"nome":"Evento Aziendale Verdi","data":"2026-06-24","location":"Villa Aurora","ospiti":90,"note":"Servizio cena e buffet."},
    ]
if "noleggi" not in st.session_state:
    st.session_state.noleggi = [
        {"id":1,"titolo":"Noleggio Ergo","inizio":datetime(2026,6,5,9),"fine":datetime(2026,6,6,18),"stato":"confermato","location":"Villa Aurora","referente":"Marco Bianchi","telefono":"+39 333 1234567","note":"Consegna ingresso principale.","bolla":"Bolla_05062026.pdf","ddt":"DDT_05062026.pdf","vario":"Foto_carico.jpg"},
        {"id":2,"titolo":"Secondo noleggio","inizio":datetime(2026,6,5,19),"fine":datetime(2026,6,5,23),"stato":"non confermato","location":"Villa Aurora","referente":"Paolo Neri","telefono":"+39 333 2223344","note":"Da confermare.","bolla":"Bolla_2.pdf","ddt":"DDT_2.pdf","vario":"Planimetria.pdf"},
        {"id":3,"titolo":"Noleggio Tavoli e Sedie","inizio":datetime(2026,6,24,8),"fine":datetime(2026,6,25,20),"stato":"confermato","location":"Castello San Marco","referente":"Andrea Neri","telefono":"+39 328 9876543","note":"Ritiro il giorno successivo.","bolla":"Bolla_24062026.pdf","ddt":"DDT_24062026.pdf","vario":"Lista_materiale.pdf"},
    ]

st.markdown(f"""
<style>
:root{{--blue:{BLUE};}}
.main-title{{color:{BLUE};font-size:2.25rem;font-weight:800;margin-bottom:0}}
.subtitle{{color:#667085;margin-bottom:18px}}
button[kind="primary"]{{background-color:{BLUE}!important;border-color:{BLUE}!important}}
.stButton>button{{border-radius:8px;border-color:#d0d5dd}}
.stButton>button:hover{{border-color:{BLUE};color:{BLUE}}}
.card{{border:1px solid #d9e2ec;border-radius:12px;padding:18px;background:white;min-height:115px}}
.kpi{{font-size:1.8rem;font-weight:800;color:{BLUE}}}
.cell{{border:1px solid #d9e2ec;border-radius:8px;background:#fff;padding:6px;min-height:135px}}
.cell-muted{{background:#f7f9fb}}
.day-number{{font-weight:800;color:#344054;margin-bottom:5px}}
.event-bar{{border-radius:5px;padding:4px 5px;margin:3px 0;color:white;font-size:.71rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.confirmed{{background:{BLUE}}}.pending{{background:#f2b84b;color:#3d2b00}}.catering-bar{{background:#4b9f9a}}
.panel{{border:1px solid #d9e2ec;border-radius:12px;padding:20px;background:#fff}}
</style>
""", unsafe_allow_html=True)


def logout():
    st.session_state.logged = False
    st.session_state.page = "Dashboard"


def open_create_rental(selected_day):
    st.session_state.rental_dialog_day = selected_day
    st.session_state.rental_dialog_mode = "create"


def open_edit_rental(rental_id):
    st.session_state.rental_dialog_id = rental_id
    st.session_state.rental_dialog_mode = "edit"


@st.dialog("Nuovo noleggio", width="large")
def rental_create_dialog(selected_day):
    st.write(f"Data selezionata: **{selected_day.strftime('%d/%m/%Y')}**")
    with st.form("rental_create_form"):
        titolo = st.text_input("Nome noleggio")
        a,b = st.columns(2)
        with a:
            data_i = st.date_input("Data inizio", selected_day); ora_i = st.time_input("Ora inizio", time(9,0))
            location = st.text_input("Location"); referente = st.text_input("Persona di riferimento"); telefono = st.text_input("Numero di telefono")
        with b:
            data_f = st.date_input("Data fine", selected_day); ora_f = st.time_input("Ora fine", time(18,0))
            stato = st.selectbox("Stato", ["Confermato", "Non confermato"]); note = st.text_area("Note varie")
        x,y,z = st.columns(3)
        with x: bolla = st.file_uploader("Bolla", type=["pdf","jpg","jpeg","png"])
        with y: ddt = st.file_uploader("DDT", type=["pdf","jpg","jpeg","png"])
        with z: vario = st.file_uploader("Vario", type=["pdf","jpg","jpeg","png"])
        save = st.form_submit_button("Salva noleggio", type="primary")
    if save:
        if not titolo or not location or not referente or not telefono:
            st.error("Compila nome, location, referente e numero di telefono.")
        else:
            next_id = max([x["id"] for x in st.session_state.noleggi] + [0]) + 1
            st.session_state.noleggi.append({"id":next_id,"titolo":titolo,"inizio":datetime.combine(data_i,ora_i),"fine":datetime.combine(data_f,ora_f),"stato":"confermato" if stato == "Confermato" else "non confermato","location":location,"referente":referente,"telefono":telefono,"note":note,"bolla":bolla.name if bolla else "Nessun file","ddt":ddt.name if ddt else "Nessun file","vario":vario.name if vario else "Nessun file"})
            st.session_state.rental_dialog_mode = None
            st.success("Noleggio creato nella demo.")
            st.rerun()


@st.dialog("Dettaglio noleggio", width="large")
def rental_detail_dialog(rental_id, can_edit):
    rental = next(x for x in st.session_state.noleggi if x["id"] == rental_id)
    st.caption("Modifica evento" if can_edit else "Visualizzazione evento")
    with st.form(f"rental_detail_{rental_id}"):
        titolo = st.text_input("Nome noleggio", rental["titolo"], disabled=not can_edit)
        a,b = st.columns(2)
        with a:
            data_i = st.date_input("Data inizio", rental["inizio"].date(), disabled=not can_edit)
            ora_i = st.time_input("Ora inizio", rental["inizio"].time(), disabled=not can_edit)
            location = st.text_input("Location", rental["location"], disabled=not can_edit)
            referente = st.text_input("Referente", rental["referente"], disabled=not can_edit)
            telefono = st.text_input("Telefono", rental["telefono"], disabled=not can_edit)
        with b:
            data_f = st.date_input("Data fine", rental["fine"].date(), disabled=not can_edit)
            ora_f = st.time_input("Ora fine", rental["fine"].time(), disabled=not can_edit)
            stato_options = ["Confermato","Non confermato"]
            stato = st.selectbox("Stato", stato_options, index=0 if rental["stato"] == "confermato" else 1, disabled=not can_edit)
            note = st.text_area("Note", rental["note"], disabled=not can_edit)
        st.markdown(f"**Bolla:** `{rental['bolla']}`  \n**DDT:** `{rental['ddt']}`  \n**Vario:** `{rental['vario']}`")
        save = st.form_submit_button("Salva modifiche", type="primary", disabled=not can_edit)
    if save:
        rental.update({"titolo":titolo,"inizio":datetime.combine(data_i,ora_i),"fine":datetime.combine(data_f,ora_f),"location":location,"referente":referente,"telefono":telefono,"note":note,"stato":"confermato" if stato == "Confermato" else "non confermato"})
        st.session_state.rental_dialog_mode = None
        st.success("Modifiche salvate.")
        st.rerun()


@st.dialog("Nuovo prodotto", width="large")
def product_dialog():
    with st.form("product_form"):
        a,b = st.columns(2)
        with a: codice = st.text_input("Codice"); nome = st.text_input("Nome prodotto"); categoria = st.text_input("Categoria")
        with b: quantita = st.number_input("Quantità", min_value=0, step=1); posizione = st.text_input("Posizione"); foto = st.file_uploader("Foto", type=["jpg","jpeg","png"])
        save = st.form_submit_button("Salva prodotto", type="primary")
    if save:
        if not nome: st.error("Inserisci il nome del prodotto.")
        else:
            st.session_state.prodotti.append({"codice":codice,"nome":nome,"categoria":categoria,"quantita":quantita,"posizione":posizione})
            st.session_state.product_dialog = False; st.success("Prodotto creato nella demo."); st.rerun()


@st.dialog("Nuovo evento Catering", width="large")
def catering_dialog():
    with st.form("catering_form"):
        nome = st.text_input("Nome evento"); data_evento = st.date_input("Data", date(2026,6,18)); location = st.text_input("Location"); ospiti = st.number_input("Ospiti", min_value=0, step=1); note = st.text_area("Note")
        save = st.form_submit_button("Salva evento", type="primary")
    if save:
        st.session_state.catering.append({"id":max([x["id"] for x in st.session_state.catering]+[0])+1,"nome":nome or "Nuovo evento","data":data_evento.isoformat(),"location":location,"ospiti":ospiti,"note":note})
        st.session_state.catering_dialog = False; st.success("Evento Catering creato nella demo."); st.rerun()


if not st.session_state.get("logged", False):
    st.markdown('<div class="main-title">Gestionale Ergo & Scardaci</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Accesso alla gestione aziendale</div>', unsafe_allow_html=True)
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Accedi", type="primary", use_container_width=True)
    if login:
        if username in USERS and USERS[username][0] == password:
            st.session_state.logged = True; st.session_state.username = username; st.session_state.ruolo = USERS[username][1]; st.session_state.page = "Dashboard"; st.rerun()
        else: st.error("Credenziali non valide.")
    st.caption("Demo: admin/admin · magazzino2/magazzino2 · magazzino1/magazzino1")
    st.stop()

ruolo = st.session_state.ruolo
st.sidebar.markdown("### Gestionale Ergo & Scardaci")
st.sidebar.write(f"Utente: **{ruolo}**")
if st.sidebar.button("Dashboard", use_container_width=True): st.session_state.page = "Dashboard"
if st.sidebar.button("Magazzino", use_container_width=True): st.session_state.page = "Magazzino"
if st.sidebar.button("Catering ed Eventi", use_container_width=True): st.session_state.page = "Catering"
if ruolo in {"Amministratore","Magazzino1","Magazzino2"}:
    if st.sidebar.button("Noleggi Confermati", use_container_width=True): st.session_state.page = "Noleggi"
if st.sidebar.button("Esci", use_container_width=True): logout(); st.rerun()

page = st.session_state.get("page", "Dashboard")
if page == "Dashboard":
    st.markdown('<div class="main-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Panoramica del gestionale</div>', unsafe_allow_html=True)
    a,b,c,d = st.columns(4)
    for col, label, value in [(a,"Prodotti",len(st.session_state.prodotti)),(b,"Eventi Catering",len(st.session_state.catering)),(c,"Noleggi",len(st.session_state.noleggi)),(d,"Ruolo",ruolo)]:
        with col:
            st.markdown(f'<div class="card"><div>{label}</div><div class="kpi">{value}</div></div>',unsafe_allow_html=True)
    st.divider(); st.info("Questa è una demo grafica autonoma: i dati sono temporanei e Supabase non viene utilizzato.")

elif page == "Magazzino":
    st.markdown('<div class="main-title">Magazzino</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Prodotti e attrezzature</div>', unsafe_allow_html=True)
    if ruolo in {"Amministratore","Magazzino2"} and st.button("＋ Nuovo prodotto", type="primary"): st.session_state.product_dialog = True
    ricerca = st.text_input("Cerca prodotto")
    prodotti = [p for p in st.session_state.prodotti if not ricerca or ricerca.lower() in p["nome"].lower() or ricerca.lower() in p["categoria"].lower()]
    for start in range(0,len(prodotti),4):
        cols = st.columns(4)
        for col,p in zip(cols,prodotti[start:start+4]):
            with col: st.markdown(f'<div class="card"><b>{p["nome"]}</b><br><small>{p["codice"]} · {p["categoria"]}</small><br><br>Quantità: <b>{p["quantita"]}</b><br>Posizione: {p["posizione"]}</div>',unsafe_allow_html=True)
    if st.session_state.get("product_dialog"): product_dialog()

elif page == "Catering":
    st.markdown('<div class="main-title">Catering ed Eventi</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Eventi, ospiti e note operative</div>', unsafe_allow_html=True)
    if ruolo in {"Amministratore","Wedding"} and st.button("＋ Nuovo evento Catering", type="primary"): st.session_state.catering_dialog = True
    for e in st.session_state.catering:
        with st.container(border=True):
            st.subheader(e["nome"]); st.write(f"📅 {e['data']}  ·  📍 {e['location']}  ·  👥 {e['ospiti']} ospiti"); st.write(e["note"])
    if st.session_state.get("catering_dialog"): catering_dialog()

elif page == "Noleggi":
    st.markdown('<div class="main-title">Noleggi Confermati</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Calendario mensile dei noleggi e degli eventi Catering</div>', unsafe_allow_html=True)
    anno, mese = 2026, 6
    st.markdown("**Legenda:** 🔵 Confermato &nbsp;&nbsp; 🟠 Non confermato &nbsp;&nbsp; 🟢 Catering")
    for col,label in zip(st.columns(7),["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]):
        with col: st.markdown(f"**{label}**")
    catering_by_day = {date.fromisoformat(e["data"]):e for e in st.session_state.catering}
    for week in calendar.Calendar(firstweekday=0).monthdatescalendar(anno,mese):
        cols = st.columns(7)
        for col,day in zip(cols,week):
            with col:
                if day.month != mese:
                    st.markdown('<div class="cell cell-muted"></div>',unsafe_allow_html=True); continue
                rentals = [r for r in st.session_state.noleggi if r["inizio"].date() <= day <= r["fine"].date()]
                catering = catering_by_day.get(day)
                with st.container(border=True):
                    if st.button(str(day.day), key=f"day_{day}", use_container_width=True):
                        if not rentals and not catering: open_create_rental(day)
                    for r in rentals:
                        cls = "confirmed" if r["stato"] == "confermato" else "pending"
                        label = r["titolo"] if day != r["inizio"].date() else f"{r['inizio'].strftime('%H:%M')} {r['titolo']}"
                        if st.button(f"{label}", key=f"rental_{r['id']}_{day}", use_container_width=True): open_edit_rental(r["id"])
                    if catering and not rentals:
                        st.markdown(f'<div class="event-bar catering-bar">🍽️ {catering["nome"]}</div>',unsafe_allow_html=True)
                    elif catering:
                        st.markdown(f'<div class="event-bar catering-bar">🍽️ {catering["nome"]}</div>',unsafe_allow_html=True)
    if st.session_state.get("rental_dialog_mode") == "create": rental_create_dialog(date.fromisoformat(st.session_state.rental_dialog_day.isoformat()))
    if st.session_state.get("rental_dialog_mode") == "edit": rental_detail_dialog(st.session_state.rental_dialog_id, ruolo in {"Amministratore","Magazzino2"})
