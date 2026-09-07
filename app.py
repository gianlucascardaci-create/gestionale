from datetime import date
import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="Noleggi Confermati", page_icon="📅", layout="wide")

if "eventi" not in st.session_state:
    st.session_state.eventi = [
        {"id":"n1","data":"2026-06-05","tipo":"noleggio","stato":"confermato","titolo":"Noleggio Ergo","inizio":"09:00","fine":"18:00","location":"Villa Aurora","referente":"Marco Bianchi","telefono":"+39 333 1234567","bolla":"Bolla_05062026.pdf","ddt":"DDT_05062026.pdf","vario":"Foto_carico.jpg","note":"Consegna ingresso principale."},
        {"id":"n2","data":"2026-06-05","tipo":"noleggio","stato":"non confermato","titolo":"Secondo noleggio","inizio":"19:00","fine":"23:00","location":"Villa Aurora","referente":"Paolo Neri","telefono":"+39 333 2223344","bolla":"Bolla_2.pdf","ddt":"DDT_2.pdf","vario":"Planimetria.pdf","note":"Da confermare."},
        {"id":"n3","data":"2026-06-12","tipo":"noleggio","stato":"non confermato","titolo":"Noleggio in attesa","inizio":"14:00","fine":"12:00 del 13/06","location":"Tenuta Verde","referente":"Laura Rossi","telefono":"+39 347 7654321","bolla":"Bolla_in_attesa.pdf","ddt":"DDT_in_attesa.pdf","vario":"Planimetria.pdf","note":"In attesa della conferma."},
        {"id":"c1","data":"2026-06-18","tipo":"catering","stato":"catering","titolo":"Evento Catering Scardaci","inizio":"18:30","fine":"01:00 del 19/06","location":"Palazzo Blu","referente":"Elena Verdi","telefono":"+39 320 5558899","bolla":"","ddt":"","vario":"","note":"Evento Catering collegato."},
        {"id":"n4","data":"2026-06-24","tipo":"noleggio","stato":"confermato","titolo":"Noleggio Tavoli e Sedie","inizio":"08:00","fine":"20:00","location":"Castello San Marco","referente":"Andrea Neri","telefono":"+39 328 9876543","bolla":"Bolla_24062026.pdf","ddt":"DDT_24062026.pdf","vario":"Lista_materiale.pdf","note":"Ritiro il giorno successivo."},
    ]
if "next_id" not in st.session_state: st.session_state.next_id = 10
if "open_event" not in st.session_state: st.session_state.open_event = None
if "create_date" not in st.session_state: st.session_state.create_date = None

st.markdown("""
<style>
.title{color:#0056b3;font-size:2.25rem;font-weight:800;margin-bottom:0}.sub{color:#667085;margin-bottom:16px}.panel{border:1px solid #d9e2ec;border-radius:14px;padding:20px;background:#fff;margin-top:18px}.fc{font-family:inherit}.fc .fc-toolbar-title{color:#0056b3;font-size:1.35rem}.fc .fc-button-primary{background:#0056b3;border-color:#0056b3}.fc .fc-daygrid-day-number{color:#344054;font-weight:700}.fc .fc-daygrid-day.fc-day-today{background:#eef6ff}.fc .fc-event{border:0;border-radius:5px;padding:3px 5px;font-size:.78rem;font-weight:600}.fc .fc-daygrid-event-dot{display:none}.fc .fc-more-link{color:#0056b3;font-weight:700}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📅 Noleggi Confermati</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Calendario mensile di noleggi ed eventi</div>', unsafe_allow_html=True)

c1, c2 = st.columns([2, 1])
with c1: ruolo = st.selectbox("Visualizza come", ["Amministratore", "Magazzino2", "Magazzino1"])
with c2: st.caption("Clicca sul giorno vuoto per creare. Clicca sul nome di un evento per aprirlo.")

st.markdown("**Legenda:** 🔵 Confermato &nbsp;&nbsp; 🟠 Non confermato &nbsp;&nbsp; 🟢 Catering")

# Ogni record diventa una riga evento nel calendario classico.
eventi_calendar = []
for e in st.session_state.eventi:
    if e["stato"] == "confermato": colore = "#0056b3"
    elif e["stato"] == "non confermato": colore = "#f2b84b"
    else: colore = "#4b9f9a"
    eventi_calendar.append({
        "id": e["id"],
        "title": f"{e['inizio']}  {e['titolo']}",
        "start": e["data"],
        "allDay": True,
        "color": colore,
        "textColor": "#ffffff" if e["stato"] != "non confermato" else "#3d2b00",
    })

calendar_state = calendar(
    events=eventi_calendar,
    options={
        "initialView": "dayGridMonth",
        "initialDate": "2026-06-01",
        "locale": "it",
        "firstDay": 1,
        "height": 650,
        "dayMaxEvents": 5,
        "fixedWeekCount": False,
        "displayEventTime": False,
        "eventDisplay": "block",
        "headerToolbar": {"left": "prev,next today", "center": "title", "right": ""},
    },
    callbacks=["dateClick", "eventClick"],
    key="noleggi_calendar",
)

# Clic sulla data vuota: apre la creazione. Clic sul singolo evento: apre la scheda.
if isinstance(calendar_state, dict):
    click_event = calendar_state.get("eventClick") or {}
    event_data = click_event.get("event", {}) if isinstance(click_event, dict) else {}
    if event_data.get("id"):
        st.session_state.open_event = event_data["id"]
        st.session_state.create_date = None
        st.rerun()
    click_date = calendar_state.get("dateClick") or {}
    if click_date.get("date") and not event_data.get("id"):
        st.session_state.create_date = click_date["date"][:10]
        st.session_state.open_event = None
        st.rerun()

if st.session_state.create_date:
    selected = st.session_state.create_date
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader(f"Nuovo evento — {selected}")
    with st.form("form_crea_noleggio"):
        tipo = st.selectbox("Tipo evento", ["Noleggio", "Evento Catering"])
        titolo = st.text_input("Nome evento")
        a, b = st.columns(2)
        with a:
            data_i = st.date_input("Data inizio", date.fromisoformat(selected))
            ora_i = st.time_input("Ora inizio")
            location = st.text_input("Location")
            referente = st.text_input("Persona di riferimento")
            telefono = st.text_input("Numero di telefono")
        with b:
            data_f = st.date_input("Data fine", date.fromisoformat(selected))
            ora_f = st.time_input("Ora fine")
            stato = st.selectbox("Stato", ["Confermato", "Non confermato"])
            note = st.text_area("Note", height=100)
        x, y, z = st.columns(3)
        with x: bolla = st.file_uploader("Bolla", type=["pdf", "jpg", "jpeg", "png"])
        with y: ddt = st.file_uploader("DDT", type=["pdf", "jpg", "jpeg", "png"])
        with z: vario = st.file_uploader("Vario", type=["pdf", "jpg", "jpeg", "png"])
        save = st.form_submit_button("Salva evento", type="primary")
    if save:
        if not titolo.strip() or not location.strip() or not referente.strip() or not telefono.strip():
            st.error("Compila nome, location, referente e telefono.")
        else:
            st.session_state.eventi.append({"id":f"n{st.session_state.next_id}","data":data_i.isoformat(),"tipo":"noleggio" if tipo == "Noleggio" else "catering","stato":"confermato" if stato == "Confermato" else "non confermato","titolo":titolo,"inizio":ora_i.strftime("%H:%M"),"fine":f"{ora_f.strftime('%H:%M')} del {data_f.strftime('%d/%m')}","location":location,"referente":referente,"telefono":telefono,"bolla":bolla.name if bolla else "Nessun file","ddt":ddt.name if ddt else "Nessun file","vario":vario.name if vario else "Nessun file","note":note or "Nessuna nota"})
            st.session_state.next_id += 1
            st.session_state.create_date = None
            st.success("Evento creato nella demo.")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.open_event:
    e = next((x for x in st.session_state.eventi if x["id"] == st.session_state.open_event), None)
    if e:
        modificabile = ruolo in {"Amministratore", "Magazzino2"}
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Modifica evento" if modificabile else "Dettagli evento")
        with st.form(f"form_dettaglio_{e['id']}"):
            titolo = st.text_input("Nome evento", e["titolo"], disabled=not modificabile)
            a, b = st.columns(2)
            with a:
                giorno = st.date_input("Data", date.fromisoformat(e["data"]), disabled=not modificabile)
                inizio = st.text_input("Ora inizio", e["inizio"], disabled=not modificabile)
                location = st.text_input("Location", e["location"], disabled=not modificabile)
                referente = st.text_input("Referente", e["referente"], disabled=not modificabile)
                telefono = st.text_input("Telefono", e["telefono"], disabled=not modificabile)
            with b:
                fine = st.text_input("Ora fine", e["fine"], disabled=not modificabile)
                stato = st.selectbox("Stato", ["Confermato", "Non confermato"], index=0 if e["stato"] == "confermato" else 1, disabled=not modificabile)
                note = st.text_area("Note", e["note"], disabled=not modificabile)
            if e["tipo"] == "noleggio":
                st.markdown(f"**Bolla:** `{e.get('bolla','Nessun file')}`  \n**DDT:** `{e.get('ddt','Nessun file')}`  \n**Vario:** `{e.get('vario','Nessun file')}`")
            save = st.form_submit_button("Salva modifiche", type="primary", disabled=not modificabile)
        if save:
            e.update({"data": giorno.isoformat(), "titolo": titolo, "inizio": inizio, "fine": fine, "location": location, "referente": referente, "telefono": telefono, "note": note, "stato": "confermato" if stato == "Confermato" else "non confermato"})
            st.success("Modifiche salvate nella demo.")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

st.caption("Anteprima indipendente: dati temporanei, nessun collegamento a Supabase.")
