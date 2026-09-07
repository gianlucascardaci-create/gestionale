from datetime import date, timedelta
import calendar
import streamlit as st

st.set_page_config(page_title="Anteprima Noleggi", page_icon="📅", layout="wide")

# Demo completamente autonoma: nessun collegamento a Supabase e nessun dato reale.
RUOLI = ["Amministratore", "Magazzino2", "Magazzino1"]
MESI = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile", 5: "Maggio", 6: "Giugno",
    7: "Luglio", 8: "Agosto", 9: "Settembre", 10: "Ottobre", 11: "Novembre", 12: "Dicembre",
}

DEMO_NOLEGGI = {
    date(2026, 6, 5): {
        "tipo": "noleggio", "stato": "confermato", "titolo": "Noleggio Ergo",
        "inizio": "09:00", "fine": "18:00", "location": "Villa Aurora",
        "referente": "Marco Bianchi", "bolla": "Bolla_05062026.pdf",
        "ddt": "DDT_05062026.pdf", "vario": "Foto_carico_05062026.jpg",
        "note": "Consegna ingresso principale.",
    },
    date(2026, 6, 12): {
        "tipo": "noleggio", "stato": "non confermato", "titolo": "Noleggio in attesa",
        "inizio": "14:00", "fine": "12:00 del 13/06", "location": "Tenuta Verde",
        "referente": "Laura Rossi", "bolla": "Bolla_in_attesa.pdf",
        "ddt": "DDT_in_attesa.pdf", "vario": "Planimetria.pdf",
        "note": "In attesa della conferma definitiva.",
    },
    date(2026, 6, 18): {
        "tipo": "catering", "stato": "catering", "titolo": "Evento Catering Scardaci",
        "inizio": "18:30", "fine": "01:00 del 19/06", "location": "Palazzo Blu",
        "referente": "Elena Verdi", "note": "Evento con note per tutti e reparti.",
    },
    date(2026, 6, 24): {
        "tipo": "noleggio", "stato": "confermato", "titolo": "Noleggio Tavoli e Sedie",
        "inizio": "08:00", "fine": "20:00", "location": "Castello San Marco",
        "referente": "Andrea Neri", "bolla": "Bolla_24062026.pdf",
        "ddt": "DDT_24062026.pdf", "vario": "Lista_materiale.pdf",
        "note": "Ritiro il giorno successivo.",
    },
}

st.markdown("""
<style>
.main-title { color:#0056b3; font-size:2.25rem; font-weight:800; margin-bottom:0; }
.subtitle { color:#5b6b7a; font-size:1.05rem; margin-bottom:18px; }
.legend { display:flex; gap:18px; flex-wrap:wrap; margin:12px 0 20px; }
.legend-item { display:flex; align-items:center; gap:7px; font-weight:600; color:#344054; }
.dot { width:15px; height:15px; border-radius:50%; display:inline-block; }
.calendar-day { min-height:92px; border:1px solid #d9e2ec; border-radius:10px; padding:8px; margin-bottom:8px; background:#fff; }
.calendar-day.empty { background:#f8fafc; border-color:#eef2f6; }
.calendar-day.today { border:2px solid #0056b3; }
.day-number { font-weight:800; color:#344054; margin-bottom:6px; }
.event-pill { border-radius:7px; padding:5px 6px; color:#fff; font-size:.74rem; font-weight:700; line-height:1.15; }
.confirmed { background:#0056b3; }
.pending { background:#f2b84b; color:#3d2b00; }
.catering { background:#4b9f9a; }
.card { border:1px solid #d9e2ec; border-radius:12px; padding:16px; background:#fff; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📅 Noleggi Confermati</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Anteprima grafica — dati dimostrativi, nessuna modifica all’app reale</div>', unsafe_allow_html=True)

col_role, col_month, col_year = st.columns([2, 2, 1])
with col_role:
    ruolo = st.selectbox("Ruolo di anteprima", RUOLI)
with col_month:
    mese = st.selectbox("Mese", list(MESI), format_func=lambda x: MESI[x], index=5)
with col_year:
    anno = st.number_input("Anno", min_value=2025, max_value=2035, value=2026, step=1)

puo_creare = ruolo in {"Amministratore", "Magazzino2"}
st.info("In questa anteprima possono creare noleggi soltanto Amministratore e Magazzino2. Magazzino1 può consultare il calendario.")

st.markdown("""
<div class="legend">
  <div class="legend-item"><span class="dot" style="background:#0056b3"></span>Noleggio confermato</div>
  <div class="legend-item"><span class="dot" style="background:#f2b84b"></span>Noleggio non confermato</div>
  <div class="legend-item"><span class="dot" style="background:#4b9f9a"></span>Evento Catering</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"### {MESI[mese]} {anno}")
header = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]
head_cols = st.columns(7)
for col, label in zip(head_cols, header):
    col.markdown(f"**{label}**")

cal = calendar.Calendar(firstweekday=0)
for settimana in cal.monthdatescalendar(int(anno), mese):
    cols = st.columns(7)
    for col, giorno in zip(cols, settimana):
        with col:
            if giorno.month != mese:
                st.markdown('<div class="calendar-day empty"></div>', unsafe_allow_html=True)
                continue
            evento = DEMO_NOLEGGI.get(giorno)
            oggi = " today" if giorno == date.today() else ""
            html = f'<div class="calendar-day{oggi}"><div class="day-number">{giorno.day}</div>'
            if evento:
                classe = "confirmed" if evento["stato"] == "confermato" else "pending" if evento["stato"] == "non confermato" else "catering"
                html += f'<div class="event-pill {classe}">{evento["titolo"]}</div>'
            else:
                html += '<div style="color:#98a2b3;font-size:.75rem">Nessun evento</div>'
            html += '</div>'
            st.markdown(html, unsafe_allow_html=True)

st.divider()
st.markdown("### Dettaglio giorno")
giorni_con_evento = sorted([g for g in DEMO_NOLEGGI if g.month == mese and g.year == int(anno)])
scelta = st.selectbox("Seleziona un giorno colorato per vedere la scheda", giorni_con_evento, format_func=lambda g: g.strftime("%d/%m/%Y"))
evento = DEMO_NOLEGGI[scelta]

if evento["tipo"] == "catering":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🍽️ Evento Catering")
    st.write(f"**{evento['titolo']}**")
    st.write(f"📍 Location: {evento['location']}")
    st.write(f"🕒 Orario: {evento['inizio']} – {evento['fine']}")
    st.write(f"👤 Referente: {evento['referente']}")
    st.write(f"📝 {evento['note']}")
    st.caption("Nella versione reale questo pulsante aprirà la cartella Catering già esistente.")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚚 Scheda Noleggio")
    st.write(f"**{evento['titolo']}**")
    st.write(f"📅 Giorno: {scelta.strftime('%d/%m/%Y')}")
    st.write(f"🕒 Inizio: {evento['inizio']} | Fine: {evento['fine']}")
    st.write(f"📍 Location: {evento['location']}")
    st.write(f"👤 Persona di riferimento: {evento['referente']}")
    st.write(f"📝 Note varie: {evento['note']}")
    st.markdown("#### Allegati e visibilità")
    if ruolo in {"Amministratore", "Magazzino2"}:
        st.success(f"Bolla — visibile a {ruolo}: {evento['bolla']}")
    if ruolo in {"Amministratore", "Magazzino2", "Magazzino1"}:
        st.info(f"DDT — visibile a {ruolo}: {evento['ddt']}")
        st.info(f"Vario — visibile a {ruolo}: {evento['vario']}")
    if puo_creare:
        st.markdown("#### Anteprima comando")
        st.button("➕ Crea nuovo noleggio (solo anteprima)", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("Questa è soltanto un’anteprima grafica. Non legge e non salva dati in Supabase.")
