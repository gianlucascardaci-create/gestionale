from datetime import date
import calendar
import streamlit as st

st.set_page_config(page_title="Noleggi Confermati", page_icon="📅", layout="wide")
MESI = {1:"Gennaio",2:"Febbraio",3:"Marzo",4:"Aprile",5:"Maggio",6:"Giugno",7:"Luglio",8:"Agosto",9:"Settembre",10:"Ottobre",11:"Novembre",12:"Dicembre"}

if "eventi" not in st.session_state:
    st.session_state.eventi = [
        {"id":1,"data":date(2026,6,5),"tipo":"noleggio","stato":"confermato","titolo":"Noleggio Ergo","inizio":"09:00","fine":"18:00","location":"Villa Aurora","referente":"Marco Bianchi","telefono":"+39 333 1234567","bolla":"Bolla_05062026.pdf","ddt":"DDT_05062026.pdf","vario":"Foto_carico.jpg","note":"Consegna ingresso principale."},
        {"id":2,"data":date(2026,6,5),"tipo":"noleggio","stato":"non confermato","titolo":"Secondo noleggio","inizio":"19:00","fine":"23:00","location":"Villa Aurora","referente":"Paolo Neri","telefono":"+39 333 2223344","bolla":"Bolla_2.pdf","ddt":"DDT_2.pdf","vario":"Planimetria.pdf","note":"Da confermare."},
        {"id":3,"data":date(2026,6,12),"tipo":"noleggio","stato":"non confermato","titolo":"Noleggio in attesa","inizio":"14:00","fine":"12:00 del 13/06","location":"Tenuta Verde","referente":"Laura Rossi","telefono":"+39 347 7654321","bolla":"Bolla_in_attesa.pdf","ddt":"DDT_in_attesa.pdf","vario":"Planimetria.pdf","note":"In attesa della conferma."},
        {"id":4,"data":date(2026,6,18),"tipo":"catering","stato":"catering","titolo":"Evento Catering Scardaci","inizio":"18:30","fine":"01:00 del 19/06","location":"Palazzo Blu","referente":"Elena Verdi","telefono":"+39 320 5558899","note":"Evento Catering collegato."},
        {"id":5,"data":date(2026,6,24),"tipo":"noleggio","stato":"confermato","titolo":"Noleggio Tavoli e Sedie","inizio":"08:00","fine":"20:00","location":"Castello San Marco","referente":"Andrea Neri","telefono":"+39 328 9876543","bolla":"Bolla_24062026.pdf","ddt":"DDT_24062026.pdf","vario":"Lista_materiale.pdf","note":"Ritiro il giorno successivo."},
    ]
if "prossimo_id" not in st.session_state: st.session_state.prossimo_id = 10

st.markdown("""
<style>
.main-title{color:#0056b3;font-size:2.3rem;font-weight:800}.subtitle{color:#667085;margin-bottom:16px}.leg{display:flex;gap:18px;flex-wrap:wrap;margin:12px 0 18px}.leg span{font-weight:600}.dot{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:6px}.blue{background:#0056b3}.orange{background:#f2b84b}.teal{background:#4b9f9a}.daybox{border:1px solid #d9e2ec;border-radius:10px;padding:7px;background:#fff;min-height:140px}.dayhead{font-weight:800;color:#344054;text-align:center;margin-bottom:6px}.eventline{border-radius:7px;padding:6px;color:white;font-size:.76rem;font-weight:700;margin:5px 0;line-height:1.15}.eventline.orange{color:#3d2b00}.newday{margin-top:5px}.card{border:1px solid #d9e2ec;border-radius:12px;padding:18px;background:#fff}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📅 Noleggi Confermati</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Calendario operativo di noleggi ed eventi</div>', unsafe_allow_html=True)

r1, r2, r3 = st.columns([2,2,1])
with r1: ruolo = st.selectbox("Visualizza come", ["Amministratore","Magazzino2","Magazzino1"])
with r2: mese = st.selectbox("Mese", list(MESI), format_func=lambda x: MESI[x], index=5)
with r3: anno = st.number_input("Anno", 2025, 2035, 2026)

st.markdown('<div class="leg"><span><i class="dot blue"></i>Confermato</span><span><i class="dot orange"></i>Non confermato</span><span><i class="dot teal"></i>Evento Catering</span></div>', unsafe_allow_html=True)
st.markdown(f"### {MESI[mese]} {anno}")

for col, label in zip(st.columns(7), ["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]):
    with col: st.markdown(f"**{label}**", unsafe_allow_html=True)

for settimana in calendar.Calendar(firstweekday=0).monthdatescalendar(int(anno), mese):
    cols = st.columns(7)
    for col, giorno in zip(cols, settimana):
        with col:
            if giorno.month != mese:
                st.write("")
                continue
            eventi_giorno = [e for e in st.session_state.eventi if e["data"] == giorno]
            # Questa è l’area vuota del giorno: non appartiene a nessun evento.
            # Premendola si apre sempre la creazione di un nuovo evento per quella data.
            st.markdown(f'<div class="daybox"><div class="dayhead">{giorno.strftime("%d")}</div></div>', unsafe_allow_html=True)
            if st.button(f"📅 {giorno.day} · Crea evento", key=f"nuovo_{giorno}", use_container_width=True):
                st.session_state.modale = "crea"
                st.session_state.giorno_creazione = giorno
                st.session_state.evento_aperto = None
                st.rerun()
            for evento in eventi_giorno:
                classe = "blue" if evento["stato"] == "confermato" else "orange" if evento["stato"] == "non confermato" else "teal"
                etichetta = ("🍽️ " if evento["tipo"] == "catering" else "🚚 ") + evento["titolo"]
                # Ogni evento è un pulsante distinto, anche quando la data è la stessa.
                if st.button(etichetta, key=f"evento_{evento['id']}", use_container_width=True):
                    st.session_state.modale = "modifica"
                    st.session_state.evento_aperto = evento["id"]
                    st.session_state.rerun_nonce = st.session_state.get("rerun_nonce", 0) + 1
                    st.rerun()
                st.markdown(f'<div class="eventline {classe}">{evento["inizio"]} · {evento["stato"].title()}</div>', unsafe_allow_html=True)

st.divider()

# Form unico, nello stile delle altre creazioni dell'app.
if st.session_state.get("modale") == "crea":
    giorno = st.session_state.giorno_creazione
    st.markdown(f"### Nuovo evento del {giorno.strftime('%d/%m/%Y')}")
    with st.form("form_crea_evento_calendario"):
        tipo = st.selectbox("Tipo evento", ["Noleggio", "Evento Catering"])
        titolo = st.text_input("Nome evento")
        c1, c2 = st.columns(2)
        with c1:
            data_inizio = st.date_input("Data inizio", giorno)
            ora_inizio = st.time_input("Ora inizio")
            location = st.text_input("Location")
            referente = st.text_input("Persona di riferimento")
            telefono = st.text_input("Numero di telefono referente")
        with c2:
            data_fine = st.date_input("Data fine", giorno)
            ora_fine = st.time_input("Ora fine")
            stato = st.selectbox("Stato", ["Confermato", "Non confermato"])
            note = st.text_area("Note", height=100)
        st.markdown("#### Allegati")
        a,b,c = st.columns(3)
        with a: bolla = st.file_uploader("Bolla", type=["pdf","jpg","jpeg","png"])
        with b: ddt = st.file_uploader("DDT", type=["pdf","jpg","jpeg","png"])
        with c: vario = st.file_uploader("Vario", type=["pdf","jpg","jpeg","png"])
        save = st.form_submit_button("Salva evento", type="primary")
    if save:
        if not titolo.strip() or not location.strip() or not referente.strip() or not telefono.strip():
            st.error("Compila nome, location, referente e telefono.")
        else:
            nuovo = {"id":st.session_state.prossimo_id,"data":data_inizio,"tipo":"noleggio" if tipo == "Noleggio" else "catering","stato":"confermato" if stato == "Confermato" else "non confermato","titolo":titolo,"inizio":ora_inizio.strftime('%H:%M'),"fine":f"{ora_fine.strftime('%H:%M')} del {data_fine.strftime('%d/%m')}","location":location,"referente":referente,"telefono":telefono,"bolla":bolla.name if bolla else "Nessun file","ddt":ddt.name if ddt else "Nessun file","vario":vario.name if vario else "Nessun file","note":note or "Nessuna nota"}
            st.session_state.eventi.append(nuovo)
            st.session_state.prossimo_id += 1
            st.session_state.modale = None
            st.success("Evento creato nella demo.")
            st.rerun()

elif st.session_state.get("modale") == "modifica":
    evento = next((e for e in st.session_state.eventi if e["id"] == st.session_state.evento_aperto), None)
    if evento:
        modificabile = ruolo in {"Amministratore", "Magazzino2"}
        st.markdown(f"### {'Modifica' if modificabile else 'Visualizza'} evento")
        with st.form("form_dettaglio_evento"):
            titolo = st.text_input("Nome evento", evento["titolo"], disabled=not modificabile)
            c1,c2 = st.columns(2)
            with c1:
                giorno = st.date_input("Data", evento["data"], disabled=not modificabile)
                inizio = st.text_input("Ora inizio", evento["inizio"], disabled=not modificabile)
                location = st.text_input("Location", evento["location"], disabled=not modificabile)
                referente = st.text_input("Persona di riferimento", evento["referente"], disabled=not modificabile)
                telefono = st.text_input("Numero di telefono", evento["telefono"], disabled=not modificabile)
            with c2:
                fine = st.text_input("Ora fine", evento["fine"], disabled=not modificabile)
                stato = st.selectbox("Stato", ["Confermato","Non confermato"], index=0 if evento["stato"] == "confermato" else 1, disabled=not modificabile)
                note = st.text_area("Note", evento["note"], disabled=not modificabile)
            if evento["tipo"] == "noleggio":
                st.markdown("#### Allegati")
                st.write(f"Bolla: `{evento.get('bolla','Nessun file')}`")
                st.write(f"DDT: `{evento.get('ddt','Nessun file')}`")
                st.write(f"Vario: `{evento.get('vario','Nessun file')}`")
            submit = st.form_submit_button("Salva modifiche", type="primary", disabled=not modificabile)
        if submit:
            evento.update({"data":giorno,"titolo":titolo,"inizio":inizio,"fine":fine,"location":location,"referente":referente,"telefono":telefono,"note":note,"stato":"confermato" if stato == "Confermato" else "non confermato"})
            st.success("Modifiche salvate nella demo.")
            st.rerun()

st.caption("Anteprima indipendente: i dati sono temporanei e Supabase non viene utilizzato.")
