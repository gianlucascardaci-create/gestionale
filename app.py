from datetime import date
import calendar
import streamlit as st

st.set_page_config(page_title="Noleggi Confermati", page_icon="📅", layout="wide")
MESI={1:"Gennaio",2:"Febbraio",3:"Marzo",4:"Aprile",5:"Maggio",6:"Giugno",7:"Luglio",8:"Agosto",9:"Settembre",10:"Ottobre",11:"Novembre",12:"Dicembre"}

if "eventi" not in st.session_state:
    st.session_state.eventi=[
      {"id":1,"data":date(2026,6,5),"tipo":"noleggio","stato":"confermato","titolo":"Noleggio Ergo","inizio":"09:00","fine":"18:00","location":"Villa Aurora","referente":"Marco Bianchi","telefono":"+39 333 1234567","bolla":"Bolla_05062026.pdf","ddt":"DDT_05062026.pdf","vario":"Foto_carico.jpg","note":"Consegna ingresso principale."},
      {"id":2,"data":date(2026,6,5),"tipo":"noleggio","stato":"non confermato","titolo":"Secondo noleggio","inizio":"19:00","fine":"23:00","location":"Villa Aurora","referente":"Paolo Neri","telefono":"+39 333 2223344","bolla":"Bolla_2.pdf","ddt":"DDT_2.pdf","vario":"Planimetria.pdf","note":"Da confermare."},
      {"id":3,"data":date(2026,6,12),"tipo":"noleggio","stato":"non confermato","titolo":"Noleggio in attesa","inizio":"14:00","fine":"12:00 del 13/06","location":"Tenuta Verde","referente":"Laura Rossi","telefono":"+39 347 7654321","bolla":"Bolla_in_attesa.pdf","ddt":"DDT_in_attesa.pdf","vario":"Planimetria.pdf","note":"In attesa della conferma."},
      {"id":4,"data":date(2026,6,18),"tipo":"catering","stato":"catering","titolo":"Evento Catering Scardaci","inizio":"18:30","fine":"01:00 del 19/06","location":"Palazzo Blu","referente":"Elena Verdi","telefono":"+39 320 5558899","note":"Evento Catering collegato."},
      {"id":5,"data":date(2026,6,24),"tipo":"noleggio","stato":"confermato","titolo":"Noleggio Tavoli e Sedie","inizio":"08:00","fine":"20:00","location":"Castello San Marco","referente":"Andrea Neri","telefono":"+39 328 9876543","bolla":"Bolla_24062026.pdf","ddt":"DDT_24062026.pdf","vario":"Lista_materiale.pdf","note":"Ritiro il giorno successivo."},
    ]
if "next_id" not in st.session_state: st.session_state.next_id=10

st.markdown("""
<style>
.title{color:#0056b3;font-size:2.25rem;font-weight:800}.sub{color:#667085;margin-bottom:18px}.legend{display:flex;gap:20px;margin:12px 0 22px;flex-wrap:wrap}.legend span{font-weight:600;color:#344054}.dot{display:inline-block;width:13px;height:13px;border-radius:50%;margin-right:6px}.b{background:#0056b3}.o{background:#f2b84b}.t{background:#4b9f9a}.calendar{border:1px solid #d9e2ec;border-radius:14px;padding:12px;background:#fbfcfe}.cell{min-height:92px;border:1px solid #e5eaf0;border-radius:9px;background:white;padding:8px}.muted{background:#f7f9fb}.num{font-weight:800;color:#344054;text-align:center;margin-bottom:9px}.mark{height:9px;border-radius:8px;margin:4px 2px}.panel{border:1px solid #d9e2ec;border-radius:14px;padding:20px;background:white}.event-button{margin-top:6px}
</style>
""",unsafe_allow_html=True)

st.markdown('<div class="title">📅 Noleggi Confermati</div>',unsafe_allow_html=True)
st.markdown('<div class="sub">Calendario operativo di noleggi ed eventi</div>',unsafe_allow_html=True)

c1,c2,c3=st.columns([2,2,1])
with c1: ruolo=st.selectbox("Visualizza come",["Amministratore","Magazzino2","Magazzino1"])
with c2: mese=st.selectbox("Mese",list(MESI),format_func=lambda x:MESI[x],index=5)
with c3: anno=st.number_input("Anno",2025,2035,2026)

st.markdown('<div class="legend"><span><i class="dot b"></i>Confermato</span><span><i class="dot o"></i>Non confermato</span><span><i class="dot t"></i>Catering</span></div>',unsafe_allow_html=True)
st.markdown(f"### {MESI[mese]} {anno}")

for col,label in zip(st.columns(7),["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]):
    with col: st.markdown(f"**{label}**")

# Nel calendario compaiono solo il numero e indicatori, senza testi degli eventi.
for settimana in calendar.Calendar(firstweekday=0).monthdatescalendar(int(anno),int(mese)):
    cols=st.columns(7)
    for col,giorno in zip(cols,settimana):
        with col:
            if giorno.month!=int(mese):
                st.markdown('<div class="cell muted"></div>',unsafe_allow_html=True); continue
            eventi=[e for e in st.session_state.eventi if e["data"]==giorno]
            st.markdown('<div class="cell">',unsafe_allow_html=True)
            st.markdown(f'<div class="num">{giorno.day}</div>',unsafe_allow_html=True)
            for e in eventi:
                classe="b" if e["stato"]=="confermato" else "o" if e["stato"]=="non confermato" else "t"
                st.markdown(f'<div class="mark {classe}" title="{e["titolo"]}"></div>',unsafe_allow_html=True)
            if not eventi: st.markdown('<div style="height:9px"></div>',unsafe_allow_html=True)
            st.markdown('</div>',unsafe_allow_html=True)
            # Un solo click sul numero/giorno: seleziona la data e apre il pannello ordinato sotto.
            if st.button(f"{giorno.day}",key=f"day_{giorno}",use_container_width=True):
                st.session_state.selected_day=giorno
                st.session_state.open_event=None
                st.rerun()

st.divider()
selected=st.session_state.get("selected_day",date(int(anno),int(mese),1))
if selected.month!=int(mese) or selected.year!=int(anno): selected=date(int(anno),int(mese),1)
st.session_state.selected_day=selected
events=[e for e in st.session_state.eventi if e["data"]==selected]

st.markdown(f"### {selected.strftime('%d/%m/%Y')}")
if not events:
    st.info("Giornata libera. Premi il pulsante per creare un nuovo evento in questa data.")
    if st.button("＋ Crea nuovo evento",type="primary"):
        st.session_state.open_event="create"
else:
    st.markdown(f"**{len(events)} evento/i in questa giornata**")
    for e in events:
        icon="🍽️" if e["tipo"]=="catering" else "🚚"
        colore="🔵" if e["stato"]=="confermato" else "🟠" if e["stato"]=="non confermato" else "🟢"
        if st.button(f"{colore}  {icon}  {e['titolo']}  ·  {e['inizio']}–{e['fine']}",key=f"open_{e['id']}",use_container_width=True):
            st.session_state.open_event=e["id"]
            st.rerun()
    if st.button("＋ Crea un altro evento in questa giornata"):
        st.session_state.open_event="create"

open_event=st.session_state.get("open_event")
if open_event=="create":
    st.markdown('<div class="panel">',unsafe_allow_html=True)
    st.subheader("Nuovo evento")
    with st.form("create_form"):
        tipo=st.selectbox("Tipo evento",["Noleggio","Evento Catering"]); titolo=st.text_input("Nome evento")
        a,b=st.columns(2)
        with a:
            data_i=st.date_input("Data inizio",selected); ora_i=st.time_input("Ora inizio"); location=st.text_input("Location"); referente=st.text_input("Persona di riferimento"); telefono=st.text_input("Numero di telefono")
        with b:
            data_f=st.date_input("Data fine",selected); ora_f=st.time_input("Ora fine"); stato=st.selectbox("Stato",["Confermato","Non confermato"]); note=st.text_area("Note")
        x,y,z=st.columns(3)
        with x: bolla=st.file_uploader("Bolla",type=["pdf","jpg","jpeg","png"])
        with y: ddt=st.file_uploader("DDT",type=["pdf","jpg","jpeg","png"])
        with z: vario=st.file_uploader("Vario",type=["pdf","jpg","jpeg","png"])
        save=st.form_submit_button("Salva evento",type="primary")
    if save:
        if not titolo.strip() or not location.strip() or not referente.strip() or not telefono.strip(): st.error("Compila nome, location, referente e telefono.")
        else:
            st.session_state.eventi.append({"id":st.session_state.next_id,"data":data_i,"tipo":"noleggio" if tipo=="Noleggio" else "catering","stato":"confermato" if stato=="Confermato" else "non confermato","titolo":titolo,"inizio":ora_i.strftime('%H:%M'),"fine":f"{ora_f.strftime('%H:%M')} del {data_f.strftime('%d/%m')}","location":location,"referente":referente,"telefono":telefono,"bolla":bolla.name if bolla else "Nessun file","ddt":ddt.name if ddt else "Nessun file","vario":vario.name if vario else "Nessun file","note":note or "Nessuna nota"}); st.session_state.next_id+=1; st.session_state.open_event=None; st.success("Evento creato nella demo."); st.rerun()
    st.markdown('</div>',unsafe_allow_html=True)
elif isinstance(open_event,int):
    e=next((x for x in st.session_state.eventi if x["id"]==open_event),None)
    if e:
        edit=ruolo in {"Amministratore","Magazzino2"}
        st.markdown('<div class="panel">',unsafe_allow_html=True); st.subheader("Modifica evento" if edit else "Dettagli evento")
        with st.form(f"detail_{e['id']}"):
            titolo=st.text_input("Nome evento",e["titolo"],disabled=not edit); a,b=st.columns(2)
            with a: giorno=st.date_input("Data",e["data"],disabled=not edit); inizio=st.text_input("Ora inizio",e["inizio"],disabled=not edit); location=st.text_input("Location",e["location"],disabled=not edit); referente=st.text_input("Referente",e["referente"],disabled=not edit); telefono=st.text_input("Telefono",e["telefono"],disabled=not edit)
            with b: fine=st.text_input("Ora fine",e["fine"],disabled=not edit); stato=st.selectbox("Stato",["Confermato","Non confermato"],index=0 if e["stato"]=="confermato" else 1,disabled=not edit); note=st.text_area("Note",e["note"],disabled=not edit)
            if e["tipo"]=="noleggio": st.markdown(f"Bolla: `{e.get('bolla','Nessun file')}`  \nDDT: `{e.get('ddt','Nessun file')}`  \nVario: `{e.get('vario','Nessun file')}`")
            save=st.form_submit_button("Salva modifiche",type="primary",disabled=not edit)
        if save: e.update({"data":giorno,"titolo":titolo,"inizio":inizio,"fine":fine,"location":location,"referente":referente,"telefono":telefono,"note":note,"stato":"confermato" if stato=="Confermato" else "non confermato"}); st.success("Modifiche salvate nella demo."); st.rerun()
        st.markdown('</div>',unsafe_allow_html=True)

st.caption("Anteprima indipendente: dati temporanei, nessun collegamento a Supabase.")
