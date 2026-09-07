from datetime import date
import calendar
import streamlit as st

st.set_page_config(page_title="Noleggi Confermati", page_icon="📅", layout="wide")

MESI = {1:"Gennaio",2:"Febbraio",3:"Marzo",4:"Aprile",5:"Maggio",6:"Giugno",7:"Luglio",8:"Agosto",9:"Settembre",10:"Ottobre",11:"Novembre",12:"Dicembre"}

if "eventi" not in st.session_state:
    st.session_state.eventi = {
        date(2026,6,5): {"tipo":"noleggio","stato":"confermato","titolo":"Noleggio Ergo","inizio":"09:00","fine":"18:00","location":"Villa Aurora","referente":"Marco Bianchi","telefono":"+39 333 1234567","bolla":"Bolla_05062026.pdf","ddt":"DDT_05062026.pdf","vario":"Foto_carico_05062026.jpg","note":"Consegna ingresso principale."},
        date(2026,6,12): {"tipo":"noleggio","stato":"non confermato","titolo":"Noleggio in attesa","inizio":"14:00","fine":"12:00 del 13/06","location":"Tenuta Verde","referente":"Laura Rossi","telefono":"+39 347 7654321","bolla":"Bolla_in_attesa.pdf","ddt":"DDT_in_attesa.pdf","vario":"Planimetria.pdf","note":"In attesa della conferma definitiva."},
        date(2026,6,18): {"tipo":"catering","stato":"catering","titolo":"Evento Catering Scardaci","inizio":"18:30","fine":"01:00 del 19/06","location":"Palazzo Blu","referente":"Elena Verdi","telefono":"+39 320 5558899","note":"Evento con note per tutti e reparti."},
        date(2026,6,24): {"tipo":"noleggio","stato":"confermato","titolo":"Noleggio Tavoli e Sedie","inizio":"08:00","fine":"20:00","location":"Castello San Marco","referente":"Andrea Neri","telefono":"+39 328 9876543","bolla":"Bolla_24062026.pdf","ddt":"DDT_24062026.pdf","vario":"Lista_materiale.pdf","note":"Ritiro il giorno successivo."},
    }

st.markdown("""
<style>
.main-title{color:#0056b3;font-size:2.35rem;font-weight:800;margin-bottom:0}.subtitle{color:#5b6b7a;font-size:1.05rem;margin-bottom:18px}.legend{display:flex;gap:18px;flex-wrap:wrap;margin:12px 0 20px}.legend-item{display:flex;align-items:center;gap:7px;font-weight:600;color:#344054}.dot{width:15px;height:15px;border-radius:50%;display:inline-block}.day-label{text-align:center;color:#475467;font-weight:700;margin-bottom:5px}.day-event{border-radius:7px;padding:5px 6px;color:#fff;font-size:.72rem;font-weight:700;line-height:1.15;margin-top:4px;min-height:31px}.confirmed{background:#0056b3}.pending{background:#f2b84b;color:#3d2b00}.catering{background:#4b9f9a}.card{border:1px solid #d9e2ec;border-radius:12px;padding:18px;background:#fff}.small-note{color:#667085;font-size:.9rem}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📅 Noleggi Confermati</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Calendario operativo di noleggi ed eventi</div>', unsafe_allow_html=True)

c1, c2 = st.columns([2,1])
with c1:
    mese = st.selectbox("Mese", list(MESI), format_func=lambda x: MESI[x], index=5)
with c2:
    anno = st.number_input("Anno", min_value=2025, max_value=2035, value=2026, step=1)

st.markdown("""
<div class="legend"><div class="legend-item"><span class="dot" style="background:#0056b3"></span>Confermato</div><div class="legend-item"><span class="dot" style="background:#f2b84b"></span>Non confermato</div><div class="legend-item"><span class="dot" style="background:#4b9f9a"></span>Evento Catering</div></div>
""", unsafe_allow_html=True)
st.markdown(f"### {MESI[mese]} {anno}")

head = st.columns(7)
for col, label in zip(head, ["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]):
    with col: st.markdown(f'<div class="day-label">{label}</div>', unsafe_allow_html=True)

for settimana in calendar.Calendar(firstweekday=0).monthdatescalendar(int(anno), mese):
    cols = st.columns(7)
    for col, giorno in zip(cols, settimana):
        with col:
            if giorno.month != mese:
                st.write("")
                continue
            evento = st.session_state.eventi.get(giorno)
            testo = str(giorno.day) + ("  •  " + ("Catering" if evento["tipo"] == "catering" else "Noleggio") if evento else "")
            if st.button(testo, key=f"giorno_{giorno.isoformat()}", use_container_width=True):
                st.session_state.giorno_selezionato = giorno
                st.session_state.mostra_creazione = False
                st.rerun()
            if evento:
                classe = "confirmed" if evento["stato"] == "confermato" else "pending" if evento["stato"] == "non confermato" else "catering"
                st.markdown(f'<div class="day-event {classe}">{evento["titolo"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="small-note">giorno libero</div>', unsafe_allow_html=True)

st.divider()
giorno = st.session_state.get("giorno_selezionato")
if giorno is None or giorno.month != mese or giorno.year != int(anno):
    giorno = next(iter(sorted([g for g in st.session_state.eventi if g.month == mese and g.year == int(anno)])), date(int(anno), mese, 1))
    st.session_state.giorno_selezionato = giorno

evento = st.session_state.eventi.get(giorno)
st.markdown(f"### Giorno selezionato: {giorno.strftime('%d/%m/%Y')}")

if evento:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if evento["tipo"] == "catering":
        st.subheader("🍽️ Evento Catering")
    else:
        st.subheader("🚚 Dettagli noleggio")
    st.write(f"**{evento['titolo']}**")
    st.write(f"📅 Giorno: {giorno.strftime('%d/%m/%Y')}")
    st.write(f"🕒 Inizio: {evento['inizio']}  |  Fine: {evento['fine']}")
    st.write(f"📍 Location: {evento['location']}")
    st.write(f"👤 Persona di riferimento: {evento['referente']}")
    st.write(f"☎️ Numero di telefono: {evento['telefono']}")
    st.write(f"📝 Note: {evento['note']}")
    if evento["tipo"] == "noleggio":
        st.markdown("#### Allegati")
        st.write(f"📄 Bolla: `{evento['bolla']}`")
        st.write(f"📄 DDT: `{evento['ddt']}`")
        st.write(f"📎 Vario: `{evento['vario']}`")
    else:
        st.caption("Nella versione definitiva questo giorno aprirà la scheda Catering già presente nel gestionale.")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Questo giorno è libero. Premi il pulsante qui sotto per creare un nuovo noleggio per questa data.")
    if st.button(f"➕ Crea noleggio del {giorno.strftime('%d/%m/%Y')}", type="primary"):
        st.session_state.mostra_creazione = True

if st.session_state.get("mostra_creazione", False) and evento is None:
    st.markdown("### Nuovo noleggio")
    with st.form("form_nuovo_noleggio"):
        titolo = st.text_input("Nome del noleggio", placeholder="Es. Noleggio tavoli e sedie")
        a, b = st.columns(2)
        with a:
            data_inizio = st.date_input("Data inizio", value=giorno)
            ora_inizio = st.time_input("Ora inizio")
            location = st.text_input("Location")
            referente = st.text_input("Persona di riferimento")
            telefono = st.text_input("Numero di telefono referente")
        with b:
            data_fine = st.date_input("Data fine", value=giorno)
            ora_fine = st.time_input("Ora fine")
            stato = st.selectbox("Stato", ["Confermato", "Non confermato"])
            note = st.text_area("Note varie", height=100)
        st.markdown("#### Allegati")
        x, y, z = st.columns(3)
        with x: bolla = st.file_uploader("Bolla", type=["pdf","jpg","jpeg","png"])
        with y: ddt = st.file_uploader("DDT", type=["pdf","jpg","jpeg","png"])
        with z: vario = st.file_uploader("Vario", type=["pdf","jpg","jpeg","png"])
        salva = st.form_submit_button("Salva anteprima", type="primary")
    if salva:
        if not titolo.strip() or not location.strip() or not referente.strip() or not telefono.strip():
            st.error("Compila nome, location, referente e numero di telefono.")
        else:
            st.session_state.eventi[data_inizio] = {"tipo":"noleggio","stato":"confermato" if stato == "Confermato" else "non confermato","titolo":titolo,"inizio":ora_inizio.strftime('%H:%M'),"fine":f"{ora_fine.strftime('%H:%M')} del {data_fine.strftime('%d/%m')}","location":location,"referente":referente,"telefono":telefono,"bolla":bolla.name if bolla else "Nessun file caricato","ddt":ddt.name if ddt else "Nessun file caricato","vario":vario.name if vario else "Nessun file caricato","note":note or "Nessuna nota"}
            st.session_state.giorno_selezionato = data_inizio
            st.session_state.mostra_creazione = False
            st.success("Noleggio creato nella demo. Il calendario verrà aggiornato.")
            st.rerun()

st.caption("Anteprima indipendente: i dati sono temporanei e non vengono salvati in Supabase.")
