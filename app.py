<!doctype html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ergo & Scardaci</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#152238;--muted:#6b778c;--line:#e5e9f0;--paper:#f7f8fb;--blue:#083278;--blue-soft:#eaf1fb;--sage:#3e765e;--sage-soft:#e9f3ee;--gold:#a66d24;--gold-soft:#fff4df;--violet:#6a5a9a;--violet-soft:#f0edfa}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',-apple-system,sans-serif;background:var(--paper);color:var(--ink);-webkit-font-smoothing:antialiased}
button{font:inherit;cursor:pointer;border:0;background:none}
input,select,textarea{font:inherit}
h1,h2,h3{font-family:Georgia,serif}
.login{min-height:100vh;display:grid;place-items:center;background:radial-gradient(circle at 80% 20%,#dbe6f6cc,transparent 45%),radial-gradient(circle at 10% 90%,#f0edfab3,transparent 40%),var(--paper);padding:20px}
.login-box{background:#fff;border:1px solid var(--line);border-radius:24px;padding:34px 30px;width:100%;max-width:420px;box-shadow:0 18px 55px rgba(21,34,56,0.08)}
.logos{display:flex;justify-content:center;gap:14px;margin-bottom:16px}
.logos img{height:60px;max-width:120px;object-fit:contain}
.login h1{font-size:1.5rem;text-align:center;color:var(--blue);margin-bottom:6px}
.login .sub{text-align:center;color:var(--muted);font-size:.82rem;margin-bottom:24px}
.field{display:block;font-size:.72rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin:12px 0 6px}
.inp{width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.9rem;outline:none;background:#fafbfd}
.inp:focus{border-color:var(--blue);background:#fff}
.btn-login{width:100%;padding:13px;background:var(--blue);color:#fff;border-radius:11px;font-weight:700;margin-top:20px}
.hint{text-align:center;color:var(--muted);font-size:.72rem;margin-top:14px;line-height:1.7}
.hint code{background:var(--blue-soft);color:var(--blue);padding:2px 7px;border-radius:5px;font-weight:700}
.err{background:#fee2e2;color:#b91c1c;padding:11px;border-radius:10px;font-size:.8rem;margin-bottom:12px}
.app{min-height:100vh;display:flex;background:var(--paper)}
.sidebar{width:220px;background:#fff;border-right:1px solid var(--line);padding:22px 16px;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;overflow-y:auto}
.brand{display:flex;flex-direction:column;align-items:center;padding:6px 10px 22px;gap:6px}
.brand-logos{display:flex;gap:8px;align-items:center;justify-content:center}
.brand-logos img{height:32px;max-width:60px;object-fit:contain}
.brand strong{color:var(--blue);font-family:Georgia,serif;font-size:1rem;text-align:center}
.brand span{color:#8a94a6;text-transform:uppercase;letter-spacing:.14em;font-size:.55rem}
.nav-label{color:#8b96a9;text-transform:uppercase;letter-spacing:.15em;font-size:.64rem;font-weight:800;padding:0 12px 10px}
.nav{display:grid;gap:5px}
.nav button{color:#68758a;text-align:left;border-radius:11px;padding:10px 12px;font-size:.82rem;font-weight:600;display:flex;gap:12px;align-items:center;width:100%;transition:all .18s}
.nav button:hover{color:var(--ink);background:#f5f7fb}
.nav button.on{background:var(--blue);color:#fff}
.side-bottom{margin-top:auto;display:grid;gap:12px;padding-top:20px}
.role-card{background:#f4f7fc;color:var(--blue);border-radius:13px;padding:13px;font-size:1.05rem;display:flex;gap:10px}
.role-card strong{display:block;font-size:.75rem}
.role-card span{display:block;color:#8190a5;margin-top:3px;font-size:.67rem}
.btn-out{width:100%;height:40px;border:1px solid var(--line);background:#fff;border-radius:10px;font-weight:700;font-size:.78rem;color:var(--ink);transition:all .18s}
.btn-out:hover{background:#f5f7fb}
.main{flex:1;min-width:0}
.topbar{height:68px;background:#f7f8fbc2;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;padding:0 28px;position:sticky;top:0;z-index:5}
.crumb{color:#a0a9b8;display:flex;gap:10px;font-size:.78rem}
.crumb strong{color:var(--ink)}
.user{display:flex;gap:8px;align-items:center;color:#69768b;font-size:.78rem;font-weight:700}
.avatar{width:32px;height:32px;background:#dbe8f8;color:var(--blue);border-radius:50%;display:grid;place-items:center;font-weight:800;font-size:.7rem}
.page{padding:36px 28px;max-width:1300px;margin:0 auto}
.eyebrow{color:#8b96a9;text-transform:uppercase;letter-spacing:.15em;font-size:.64rem;font-weight:800}
h1.title{font-size:clamp(1.8rem,3vw,2.6rem);margin-top:8px;line-height:1.08}
.lede{color:var(--muted);margin-top:12px;font-size:.9rem;line-height:1.6;max-width:620px}
.footer{color:#a0a9b8;padding:15px 28px 22px;font-size:.61rem;display:flex;justify-content:space-between}
.footer span:first-child{color:var(--blue);font-weight:800}
.mobile-btn{display:none;width:35px;height:35px;background:#fff;border:1px solid var(--line);border-radius:10px;color:var(--blue);font-size:1.1rem}
.cd-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:20px}
.cd-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:0 8px 27px rgba(21,34,56,0.035);position:relative;overflow:hidden}
.cd-card:after{content:"";position:absolute;bottom:-40px;right:-40px;width:120px;height:120px;border-radius:50%;opacity:.06;background:currentColor}
.cd-card.event{color:var(--sage)}
.cd-card.rental{color:var(--blue)}
.cd-head{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:16px;position:relative;z-index:1}
.cd-label{font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.14em}
.cd-tag{padding:4px 9px;border-radius:100px;font-size:.6rem;font-weight:800}
.event .cd-tag{background:var(--sage-soft);color:var(--sage)}
.rental .cd-tag{background:var(--blue-soft);color:var(--blue)}
.cd-title{font-family:Georgia,serif;font-size:1.25rem;color:var(--ink);margin-bottom:6px}
.cd-when{font-size:.75rem;color:var(--muted);margin-bottom:18px}
.cd-timer{display:flex;gap:8px}
.cd-unit{flex:1;background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:10px 6px;text-align:center}
.event .cd-unit{border-color:#c8e0d2;background:#f3f9f5}
.rental .cd-unit{border-color:#c4d9f2;background:#f0f6fe}
.cd-unit .n{display:block;font-family:Georgia,serif;font-size:1.6rem;font-weight:800;line-height:1;letter-spacing:-.04em}
.event .cd-unit .n{color:var(--sage)}
.rental .cd-unit .n{color:var(--blue)}
.cd-unit .u{display:block;font-size:.58rem;color:var(--muted);margin-top:5px;text-transform:uppercase;letter-spacing:.08em;font-weight:700}
.cd-wait{font-size:.8rem;color:var(--muted);padding:14px 0;font-style:italic;text-align:center}
.cd-empty{padding:24px 0;text-align:center;color:var(--muted);font-size:.82rem}
.cd-empty .emo{font-size:2rem;display:block;margin-bottom:8px;opacity:.4}
.feed{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:0 8px 27px rgba(21,34,56,0.035)}
.feed-head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-bottom:12px;flex-wrap:wrap}
.feed-head h2{font-size:1.3rem;margin-top:5px}
.feed-actions{display:flex;gap:6px;flex-wrap:wrap}
.btn-mini{padding:7px 11px;border-radius:9px;font-size:.68rem;font-weight:700;border:1px solid var(--line);background:#fff;color:var(--muted);transition:all .18s}
.btn-mini:hover{background:#f5f7fb;color:var(--ink)}
.btn-mini.active{background:var(--blue);color:#fff;border-color:var(--blue)}
.feed-item{display:flex;gap:12px;align-items:flex-start;padding:14px 12px;border-radius:10px;cursor:pointer;transition:background .15s;position:relative}
.feed-item:hover{background:#f8fafc}
.feed-item.unread{background:#f0f6ff}
.feed-item.unread:hover{background:#e6efff}
.feed-item.unread::before{content:"";position:absolute;left:4px;top:50%;transform:translateY(-50%);width:6px;height:6px;background:#2563eb;border-radius:50%}
.feed-ico{width:36px;height:36px;border-radius:10px;display:grid;place-items:center;font-size:1rem;flex-shrink:0}
.feed-ico.sage{background:var(--sage-soft);color:var(--sage)}
.feed-ico.blue{background:var(--blue-soft);color:var(--blue)}
.feed-ico.gold{background:var(--gold-soft);color:var(--gold)}
.feed-ico.violet{background:var(--violet-soft);color:var(--violet)}
.feed-txt{flex:1;min-width:0}
.feed-txt strong{font-size:.85rem;display:block;line-height:1.35;font-weight:700}
.feed-txt span{font-size:.72rem;color:var(--muted);display:block;margin-top:3px}
.feed-time{font-size:.68rem;color:#a0a9b8;white-space:nowrap;flex-shrink:0}
.feed-empty{text-align:center;padding:40px 20px;color:var(--muted);font-size:.85rem}
.feed-empty .emo{font-size:2rem;display:block;margin-bottom:10px;opacity:.4}
.admin-only{display:inline-block;font-size:.55rem;background:#fef3c7;color:#92400e;padding:2px 6px;border-radius:5px;margin-left:6px;font-weight:800;vertical-align:middle}
.drawer-bg{position:fixed;inset:0;background:rgba(21,34,56,0.35);opacity:0;pointer-events:none;transition:opacity .25s;z-index:40}
.drawer-bg.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;right:0;bottom:0;width:min(460px,92vw);background:#fff;box-shadow:-20px 0 60px rgba(21,34,56,0.15);transform:translateX(100%);transition:transform .28s cubic-bezier(.16,1,.3,1);z-index:41;display:flex;flex-direction:column}
.drawer.open{transform:translateX(0)}
.drawer-head{padding:24px 24px 16px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.drawer-head h2{font-size:1.35rem;line-height:1.15}
.drawer-close{width:36px;height:36px;border-radius:10px;border:1px solid var(--line);background:#fff;color:var(--muted);display:grid;place-items:center;font-size:1.1rem;flex-shrink:0}
.drawer-close:hover{color:var(--ink);background:#f5f7fb}
.drawer-body{padding:22px 24px;overflow-y:auto;flex:1}
.drawer-body h4{font-size:.68rem;text-transform:uppercase;letter-spacing:.14em;color:#8b96a9;font-weight:800;margin:18px 0 8px}
.drawer-body h4:first-child{margin-top:0}
.drawer-body p{font-size:.85rem;color:#4b5563;line-height:1.55}
.note-box{background:#f3f8ff;border:1px solid #d7e7fa;border-radius:12px;padding:14px 16px;font-size:.85rem;color:#344054;line-height:1.6;white-space:pre-wrap}
.note-box.sala{background:#f0fdf4;border-color:#bbf7d0}
.note-box.cucina{background:#fff7ed;border-color:#fed7aa}
.note-box.magazzino{background:#f5f3ff;border-color:#ddd6fe}
.note-box.tutti{background:#eef2ff;border-color:#c7d2fe}
.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0}
.meta-grid div{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.meta-grid small{display:block;font-size:.6rem;text-transform:uppercase;letter-spacing:.1em;color:#8b96a9;font-weight:800}
.meta-grid strong{display:block;font-size:.78rem;margin-top:5px}
.drawer-foot{padding:16px 24px;border-top:1px solid var(--line);display:flex;gap:10px;background:#fafbfd}
.btn-primary{flex:1;padding:12px;background:var(--blue);color:#fff;border-radius:10px;font-weight:700;font-size:.82rem;transition:all .18s;border:0;cursor:pointer}
.btn-primary:hover{background:#0b438d}
.btn-ghost{padding:12px 16px;border:1px solid var(--line);background:#fff;border-radius:10px;font-weight:700;font-size:.82rem;color:var(--ink);cursor:pointer;transition:all .18s}
.btn-ghost:hover{background:#f5f7fb}
.campo{margin-bottom:14px}
.campo label{display:block;font-size:.7rem;font-weight:800;color:#6b778c;text-transform:uppercase;letter-spacing:.08em;margin-bottom:7px}
.campo input,.campo select,.campo textarea{width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;outline:none;background:#fff;transition:all .18s;font-family:inherit;color:var(--ink);box-sizing:border-box}
.campo input:focus,.campo select:focus,.campo textarea:focus{border-color:var(--blue);box-shadow:0 0 0 4px rgba(8,50,120,0.08)}
.campo textarea{min-height:70px;resize:vertical;line-height:1.5}
.campo input[readonly]{background:#f8fafc;color:#94a3b8;cursor:not-allowed}
.campo input[type="file"]{padding:11px 12px;border:2px dashed #c4cbd6;border-radius:11px;background:#fafbfd;cursor:pointer;font-size:.78rem}
.campo input[type="file"]:hover{border-color:var(--blue);background:#f0f6ff}
.campo input[type="file"]::file-selector-button{background:var(--blue);color:#fff;border:0;padding:8px 14px;border-radius:8px;font-weight:700;font-size:.72rem;margin-right:12px;cursor:pointer}
.campo-2{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px}
.campo-2 .campo{margin-bottom:0}
.campo-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:14px}
.campo-3 .campo{margin-bottom:0}
.divisore-modale{display:flex;align-items:center;gap:10px;margin:18px 0 14px;color:#94a3b8;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.14em}
.divisore-modale:before,.divisore-modale:after{content:"";flex:1;height:1px;background:var(--line)}
.cat-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.cat-item{display:flex;align-items:center;gap:9px;padding:11px 12px;background:#fafbfd;border:1.5px solid var(--line);border-radius:10px;cursor:pointer;font-size:.74rem;font-weight:600;color:var(--ink);transition:all .15s;user-select:none;line-height:1.3}
.cat-item:hover{background:#f4f7fc;border-color:#c4d1e5}
.cat-item input{margin:0;accent-color:var(--blue);cursor:pointer;width:16px;height:16px;flex-shrink:0}
.cat-item.on{background:#eaf1fb;border-color:var(--blue);color:var(--blue);box-shadow:0 0 0 3px rgba(8,50,120,0.05)}
.foto-preview-box{display:flex;align-items:center;gap:12px;padding:12px;background:#f0fdf4;border:1.5px solid #bbf7d0;border-radius:12px;margin-top:10px}
.foto-preview-box img{width:54px;height:54px;border-radius:10px;object-fit:cover;border:2px solid #fff;box-shadow:0 2px 8px rgba(22,101,52,0.15)}
.foto-preview-box .info strong{display:block;font-size:.78rem;color:#166534;font-weight:800}
.foto-preview-box .info span{display:block;font-size:.7rem;color:#4d7c5a;margin-top:3px}
.allegato-riga{display:flex;align-items:center;gap:10px;background:#fafbfd;border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:6px;transition:all .15s}
.allegato-riga:hover{background:#f5f8ff;border-color:#c4d9f2}
.allegato-info{flex:1;display:flex;align-items:center;gap:10px;min-width:0}
.allegato-icona{width:36px;height:36px;border-radius:9px;background:#eaf1fb;color:#083278;display:grid;place-items:center;font-size:1.1rem;flex-shrink:0}
.allegato-info strong{font-size:.78rem;display:block;color:var(--ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.allegato-info small{font-size:.65rem;color:var(--muted);display:block;margin-top:2px}
.allegato-azioni{display:flex;gap:5px;flex-shrink:0}
.allegato-btn{padding:8px 11px;border-radius:8px;font-size:.7rem;font-weight:700;border:1.5px solid var(--line);background:#fff;color:var(--ink);cursor:pointer;transition:all .15s;display:inline-flex;align-items:center;gap:4px;min-height:34px}
.allegato-btn:hover{background:#f5f7fb;border-color:#c4d1e5}
.allegato-btn.anteprima{background:var(--blue);color:#fff;border-color:var(--blue)}
.allegato-btn.anteprima:hover{background:#0b438d}
.lista-layout{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px}
.lista-pannello{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:0 4px 16px rgba(21,34,56,0.04);display:flex;flex-direction:column;max-height:75vh}
.lista-titolo{font-family:Georgia,serif;font-size:1.15rem;color:var(--ink);font-weight:700;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.lista-titolo .count{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:800;background:var(--blue-soft);color:var(--blue);padding:3px 9px;border-radius:100px;letter-spacing:.04em}
.lista-search{margin-bottom:10px;display:flex;gap:8px;flex-wrap:wrap}
.lista-search input{flex:1;min-width:140px;padding:10px 12px;border:1.5px solid var(--line);border-radius:10px;font-size:.85rem;outline:none;background:#fafbfd}
.lista-search input:focus{border-color:var(--blue);background:#fff;box-shadow:0 0 0 3px rgba(8,50,120,0.08)}
.lista-search select{padding:10px 12px;border:1.5px solid var(--line);border-radius:10px;font-size:.85rem;outline:none;background:#fafbfd;cursor:pointer;min-width:150px}
.lista-prodotti{flex:1;overflow-y:auto;display:grid;gap:8px;padding-right:4px}
.lista-prodotto{background:#fafbfd;border:1px solid var(--line);border-radius:11px;padding:11px 12px;display:flex;align-items:center;gap:10px;transition:all .15s}
.lista-prodotto:hover{border-color:#c4d9f2;background:#fff}
.lista-prodotto .info{flex:1;min-width:0}
.lista-prodotto .info strong{font-size:.82rem;display:block;line-height:1.3;color:var(--ink)}
.lista-prodotto .info small{font-size:.68rem;color:var(--muted);display:block;margin-top:3px}
.lista-prodotto .info small b{color:var(--blue);font-weight:700}
.lista-prodotto .qta-box{display:flex;align-items:center;gap:6px}
.lista-prodotto input[type=number]{width:60px;padding:8px 6px;border:1.5px solid var(--line);border-radius:8px;font-size:.8rem;text-align:center;outline:none;font-weight:700}
.lista-prodotto .aggiungi{padding:8px 12px;background:var(--blue);color:#fff;border-radius:8px;font-size:.72rem;font-weight:700;cursor:pointer;transition:all .15s;white-space:nowrap;border:0}
.lista-prodotto .aggiungi:hover{background:#0b438d}
.lista-prodotto .aggiungi:disabled{background:#cbd5e1;cursor:not-allowed}
.lista-carrello{flex:1;overflow-y:auto;padding-right:4px}
.cat-header{background:var(--blue);color:#fff;padding:8px 12px;border-radius:9px;font-weight:800;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;margin:10px 0 6px;display:flex;justify-content:space-between;align-items:center}
.cat-header:first-child{margin-top:0}
.cat-header .badge{background:rgba(255,255,255,0.25);padding:2px 8px;border-radius:100px;font-size:.62rem}
.carrello-item{display:flex;align-items:center;gap:10px;background:#fafbfd;border:1px solid var(--line);border-radius:9px;padding:9px 11px;margin-bottom:6px}
.carrello-item .info{flex:1;min-width:0}
.carrello-item .info strong{font-size:.78rem;display:block;line-height:1.3;color:var(--ink)}
.carrello-item .info small{font-size:.65rem;color:var(--muted);display:block;margin-top:2px}
.carrello-item input[type=number]{width:52px;padding:7px 4px;border:1.5px solid var(--line);border-radius:7px;font-size:.78rem;text-align:center;outline:none;font-weight:700}
.carrello-item .rimuovi{background:#fef2f2;color:#b91c1c;border:1px solid #fecaca;width:30px;height:30px;border-radius:7px;font-size:.85rem;cursor:pointer;display:grid;place-items:center;transition:all .15s;flex-shrink:0}
.carrello-item .rimuovi:hover{background:#fee2e2}
.carrello-vuoto{text-align:center;padding:40px 20px;color:var(--muted);font-size:.82rem}
.carrello-vuoto .emo{font-size:2.2rem;display:block;margin-bottom:10px;opacity:.35}
.carrello-azioni{border-top:1px solid var(--line);padding-top:12px;margin-top:12px;display:flex;gap:8px}
.carrello-azioni button{flex:1;padding:11px;border-radius:10px;font-weight:700;font-size:.78rem;cursor:pointer;transition:all .15s;border:0}
.carrello-azioni .btn-invia{background:var(--blue);color:#fff;box-shadow:0 4px 10px rgba(8,50,120,0.2)}
.carrello-azioni .btn-invia:hover{background:#0b438d}
.carrello-azioni .btn-invia:disabled{background:#cbd5e1;cursor:not-allowed;box-shadow:none}
.carrello-azioni .btn-svuota{background:#fff;color:#b91c1c;border:1.5px solid #fecaca}
.carrello-azioni .btn-svuota:hover{background:#fef2f2}
.ruolo-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:0 4px 16px rgba(21,34,56,0.04);transition:all .2s;display:flex;flex-direction:column;gap:12px}
.ruolo-card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(21,34,56,0.08);border-color:#c4d9f2}
.ruolo-head{display:flex;align-items:center;gap:12px}
.ruolo-avatar{width:46px;height:46px;border-radius:50%;display:grid;place-items:center;font-weight:800;font-size:.85rem;flex-shrink:0;letter-spacing:.03em}
.ruolo-nome{font-size:.92rem;font-weight:700;color:var(--ink);line-height:1.2;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ruolo-username{font-size:.72rem;color:#94a3b8;margin-top:3px;letter-spacing:.02em}
.ruolo-badge{padding:4px 10px;border-radius:100px;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;white-space:nowrap;flex-shrink:0}
.ruolo-info{background:#fafbfd;border:1px solid var(--line);border-radius:10px;padding:10px 12px;display:grid;gap:8px}
.ruolo-riga{display:flex;justify-content:space-between;align-items:center;gap:10px;font-size:.75rem}
.ruolo-riga span{color:#94a3b8;font-weight:600}
.ruolo-riga strong{color:var(--ink);font-weight:700;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:60%}
.ruolo-azioni{display:flex;gap:8px;margin-top:auto;padding-top:10px;border-top:1px solid #f0f3f8;align-items:center}
.ruolo-btn{flex:1;padding:9px 12px;border-radius:9px;font-size:.75rem;font-weight:700;border:1.5px solid var(--line);background:#fff;color:var(--ink);cursor:pointer;transition:all .15s;display:inline-flex;align-items:center;justify-content:center;gap:5px;min-height:38px}
.ruolo-btn:hover{background:#f5f7fb;border-color:#c4d1e5}
.ruolo-btn.pericolo{color:#b91c1c;border-color:#fecaca;background:#fef2f2;flex:0 0 44px;width:44px;padding:0;min-height:38px;font-size:1rem}
.ruolo-btn.pericolo:hover{background:#fee2e2;border-color:#fca5a5}
.ruolo-protetto{flex:0 0 auto;padding:8px 12px;background:#fef3c7;color:#92400e;border-radius:9px;font-size:.7rem;font-weight:800;letter-spacing:.02em;display:inline-flex;align-items:center;gap:5px}
  /* === FIX CALENDARIO MIGLIORATO === */
.cal-toolbar{display:flex;justify-content:space-between;align-items:center;gap:14px;margin-bottom:16px;flex-wrap:wrap}
.cal-nav{display:flex;align-items:center;gap:8px}
.cal-nav button{width:38px;height:38px;border-radius:10px;border:1.5px solid var(--line);background:#fff;color:var(--blue);font-weight:800;font-size:1.1rem;display:grid;place-items:center;transition:all .18s}
.cal-nav .mese select{font-family:'DM Sans',sans-serif;font-size:1rem;font-weight:800;color:#fff;background:var(--blue);border:0;border-radius:10px;padding:8px 34px 8px 14px;cursor:pointer;outline:none;transition:all .18s;box-shadow:0 4px 12px rgba(8,50,120,0.22);appearance:none;-webkit-appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 12px center;background-size:12px;letter-spacing:.04em}
.cal-nav .mese select:hover{background:#0b438d;box-shadow:0 6px 16px rgba(8,50,120,0.32);transform:translateY(-1px)}
.cal-nav .mese select:focus{background:#0b438d;box-shadow:0 0 0 4px rgba(8,50,120,0.2)}
.cal-nav .mese select option{background:#fff;color:var(--ink);font-weight:700;padding:8px}
.cal-nav .mese select:hover{background-color:#f4f7fc;border-color:var(--blue);box-shadow:0 4px 10px rgba(8,50,120,0.12)}
.cal-nav .mese select:focus{border-color:var(--blue);box-shadow:0 0 0 4px rgba(8,50,120,0.12)}
.cal-nav .mese select:hover{background:#eaf1fb;border-color:#c4d9f2}
.cal-nav .mese select:focus{border-color:var(--blue);background:#fff}
.cal-nav .mese{font-family:'DM Sans',sans-serif;font-size:.95rem;color:var(--ink);font-weight:800;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.06em}
.cal-azioni{display:flex;gap:8px}
.btn-crea{padding:11px 18px;border-radius:11px;font-size:.8rem;font-weight:700;display:inline-flex;align-items:center;gap:6px;transition:all .18s;border:0;cursor:pointer;white-space:nowrap}
.btn-crea.evento{background:#3e765e;color:#fff;box-shadow:0 6px 14px rgba(62,118,94,0.2)}
.btn-crea.evento:hover{background:#2f5c49;transform:translateY(-1px)}
.btn-crea.noleggio{background:var(--blue);color:#fff;box-shadow:0 6px 14px rgba(8,50,120,0.2)}
.btn-crea.noleggio:hover{background:#0b438d;transform:translateY(-1px)}
.cal-filtro{display:inline-flex;gap:6px;background:#f4f7fc;padding:6px;border-radius:12px;margin-bottom:16px;border:1px solid var(--line)}
.cal-filtro button{padding:8px 18px;border-radius:9px;font-size:.78rem;font-weight:700;background:transparent;color:var(--muted);border:0;cursor:pointer;transition:all .18s;white-space:nowrap}
.cal-filtro button:hover{background:rgba(255,255,255,0.8);color:var(--ink)}
.cal-filtro button.active{background:var(--blue);color:#fff;box-shadow:0 3px 8px rgba(8,50,120,0.25)}
.cal-legenda{display:flex;gap:16px;margin-bottom:14px;flex-wrap:wrap;font-size:.72rem;color:var(--muted);font-weight:700}
.cal-legenda span{display:inline-flex;align-items:center;gap:6px}
.cal-legenda i{width:12px;height:12px;border-radius:4px;display:inline-block}
.cal-griglia{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:8px;min-width:620px}
.cal-int{text-align:center;font-size:.68rem;font-weight:800;color:#9aa4b3;text-transform:uppercase;letter-spacing:.12em;padding:4px 0 8px}
.cal-giorno{min-height:100px;border:1px solid var(--line);border-radius:12px;padding:8px;background:#fff;transition:all .15s;cursor:pointer;position:relative}
.cal-giorno:hover{border-color:#93c5fd;background:#f8fbff;transform:translateY(-1px)}
.cal-giorno.vuoto{background:#f8fafc;border-color:#eef1f5;cursor:default}
.cal-giorno.vuoto:hover{transform:none}
.cal-giorno.oggi{border-color:var(--blue);box-shadow:0 0 0 2px rgba(8,50,120,0.15)}
.cal-giorno.oggi .num{color:var(--blue);background:var(--blue);color:#fff}
.cal-giorno .num{font-family:Georgia,serif;font-size:.95rem;font-weight:800;color:#243b53;line-height:1;display:inline-grid;place-items:center;width:26px;height:26px;border-radius:8px;margin-bottom:6px}
.cal-chip{display:block;font-size:.6rem;font-weight:700;padding:4px 6px;border-radius:6px;margin-bottom:4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;line-height:1.25;cursor:pointer;transition:all .12s}
.cal-chip:hover{transform:translateX(2px);box-shadow:0 2px 6px rgba(0,0,0,0.08)}
.cal-chip.evento{background:#bbf7d0;color:#166534}
.cal-chip.noleggio{background:#bfdbfe;color:#1e3a8a}
.cal-chip.noleggio.pending{background:#fed7aa;color:#9a3412}
.cal-chip.piu{background:#f1f5f9;color:#64748b;text-align:center;font-weight:800}
.cal-pannello{margin-top:18px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:0 8px 27px rgba(21,34,56,0.04);display:none}
.cal-pannello.on{display:block;animation:slideDown .25s ease-out}
@keyframes slideDown{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}
.cal-pannello h3{font-size:1.15rem;margin-bottom:14px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.cal-pannello h3 .badge{font-size:.62rem;background:var(--blue-soft);color:var(--blue);padding:4px 10px;border-radius:100px;font-weight:800}
.cal-lista{display:grid;gap:8px}
.cal-riga{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:#fafbfd;cursor:pointer;transition:all .15s}
.cal-riga:hover{background:#fff;border-color:#93c5fd;transform:translateX(3px);box-shadow:0 3px 10px rgba(8,50,120,0.06)}
.cal-riga .ico{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;font-size:1.1rem;flex-shrink:0}
.cal-riga.evento .ico{background:var(--sage-soft);color:var(--sage)}
.cal-riga.noleggio .ico{background:var(--blue-soft);color:var(--blue)}
.cal-riga .txt{flex:1;min-width:0}
.cal-riga .txt strong{font-size:.88rem;display:block;line-height:1.3}
.cal-riga .txt span{font-size:.72rem;color:var(--muted);display:block;margin-top:3px}
.cal-riga .ora{font-family:Georgia,serif;font-size:.9rem;font-weight:700;color:var(--blue);flex-shrink:0}

/* === FIX INVENTARIO MIGLIORATO === */
.inv-toolbar{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:22px;flex-wrap:wrap;background:#fff;padding:16px;border-radius:14px;border:1px solid var(--line);box-shadow:0 4px 16px rgba(21,34,56,0.04)}
.inv-filtri{display:flex;gap:10px;flex:1;flex-wrap:wrap;align-items:center}
.inv-search{position:relative;flex:1;min-width:220px;max-width:440px}
.inv-search input{width:100%;padding:12px 16px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;outline:none;background:#fafbfd;transition:all .18s}
.inv-search input:focus{border-color:var(--blue);background:#fff;box-shadow:0 0 0 4px rgba(8,50,120,0.08)}
.inv-select{padding:12px 16px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;outline:none;background:#fafbfd;min-width:200px;color:var(--ink);cursor:pointer;transition:all .18s;font-weight:600}
.inv-select:hover{border-color:#c4d1e5}
.inv-select:focus{border-color:var(--blue);background:#fff}
.inv-add{padding:12px 22px;background:var(--blue);color:#fff;border-radius:11px;font-weight:700;font-size:.85rem;box-shadow:0 6px 16px rgba(8,50,120,0.22);white-space:nowrap;transition:all .18s;display:inline-flex;align-items:center;gap:6px;border:0;cursor:pointer}
.inv-add:hover{background:#0b438d;transform:translateY(-2px);box-shadow:0 10px 22px rgba(8,50,120,0.28)}
.inv-griglia{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px}
.inv-card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;transition:all .22s cubic-bezier(.16,1,.3,1);box-shadow:0 4px 16px rgba(21,34,56,0.04);display:flex;flex-direction:column;height:100%}
.inv-card:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(21,34,56,0.10);border-color:#c4d9f2}
.inv-foto{width:100%;height:180px;background:linear-gradient(135deg,#eef4fa 0%,#f8fafc 100%);display:grid;place-items:center;overflow:hidden;position:relative;color:#9ab1c9;font-size:2.6rem}
.inv-foto img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s}
.inv-card:hover .inv-foto img{transform:scale(1.05)}
.inv-foto.no-foto::before{content:"📦";font-size:2.6rem;opacity:.35}
.inv-badge-cat{position:absolute;top:12px;left:12px;background:rgba(255,255,255,0.97);color:var(--blue);padding:5px 11px;border-radius:100px;font-size:.6rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;box-shadow:0 3px 10px rgba(21,34,56,0.10);z-index:2;max-width:80%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.inv-body{padding:16px;display:flex;flex-direction:column;flex:1;gap:8px}
.inv-nome{font-size:.98rem;font-weight:700;line-height:1.3;color:var(--ink);min-height:2.6em;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin:0}
.inv-codice{font-size:.68rem;color:#98a2b3;letter-spacing:.06em;font-weight:700;margin:0;text-transform:uppercase}
.inv-qta{background:linear-gradient(135deg,#eaf3ff 0%,#dce9fa 100%);color:var(--blue);border-radius:10px;padding:10px;text-align:center;font-weight:800;font-size:1.02rem;font-family:Georgia,serif;letter-spacing:.02em;margin:0;border:1px solid #cfe0f5}
.inv-info{font-size:.72rem;color:var(--muted);line-height:1.5;margin:0;display:flex;align-items:center;gap:5px}
.inv-info b{color:var(--ink);font-weight:700}
.inv-prezzo{color:var(--sage);font-weight:800;font-size:.88rem;margin:2px 0 0;font-family:Georgia,serif;letter-spacing:.02em}
.inv-azioni{display:flex;gap:6px;margin-top:auto;padding-top:12px;border-top:1px solid #f0f3f8;align-items:center}
.inv-btn{flex:1;min-width:0;padding:10px 8px;border-radius:9px;font-size:.74rem;font-weight:700;border:1.5px solid var(--line);background:#fff;color:var(--ink);transition:all .18s;display:inline-flex;align-items:center;justify-content:center;gap:5px;white-space:nowrap;min-height:40px;overflow:hidden;box-sizing:border-box;line-height:1;cursor:pointer}
.inv-btn:hover{background:#f5f7fb;border-color:#c4d1e5;transform:translateY(-1px)}
.inv-btn.primario{background:var(--blue);color:#fff;border-color:var(--blue);box-shadow:0 3px 8px rgba(8,50,120,0.15)}
.inv-btn.primario:hover{background:#0b438d;border-color:#0b438d}
.inv-btn.pericolo{color:#b91c1c;border-color:#fecaca;background:#fef2f2;flex:0 0 44px;width:44px;min-width:44px;max-width:44px;padding:0;font-size:1.05rem;overflow:visible}
.inv-btn.pericolo:hover{background:#fee2e2;border-color:#fca5a5}
.inv-btn[data-azione="modifica"]{flex:0 0 44px;width:44px;min-width:44px;max-width:44px;padding:0;font-size:1.05rem}
.inv-vuoto{grid-column:1/-1;text-align:center;padding:70px 20px;color:var(--muted);font-size:.9rem;background:#fff;border:2px dashed var(--line);border-radius:16px}
.inv-vuoto .emo{font-size:3rem;display:block;margin-bottom:14px;opacity:.35}
.qr-page{min-height:100vh;background:linear-gradient(135deg,#f3f7fc 0%,#eef4fb 100%);padding:20px;display:flex;align-items:center;justify-content:center}
.qr-card{background:#fff;border-radius:22px;width:100%;max-width:900px;padding:28px;box-shadow:0 20px 60px rgba(21,34,56,0.12);display:grid;grid-template-columns:minmax(220px,280px) minmax(0,1fr);gap:28px;align-items:start}
.qr-foto{width:100%;aspect-ratio:1;background:linear-gradient(145deg,#eef4fa,#f8fafc);border-radius:16px;overflow:hidden;display:grid;place-items:center;color:#9ab1c9;font-size:4rem}
.qr-foto img{width:100%;height:100%;object-fit:cover;display:block}
.qr-info{min-width:0}
.qr-kicker{font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.14em;color:#8b96a9;margin-bottom:6px}
.qr-nome{font-family:Georgia,serif;font-size:1.5rem;color:var(--blue);line-height:1.15;margin-bottom:6px}
.qr-codice{font-size:.78rem;color:#98a2b3;letter-spacing:.06em;margin-bottom:16px}
.qr-qta{background:linear-gradient(135deg,#083278,#0b438d);color:#fff;border-radius:14px;padding:14px 18px;margin-bottom:14px}
.qr-qta small{display:block;font-size:.62rem;text-transform:uppercase;letter-spacing:.12em;opacity:.82;font-weight:700}
.qr-qta strong{display:block;font-family:Georgia,serif;font-size:2rem;font-weight:800;line-height:1;margin-top:4px}
.qr-note{background:#f3f8ff;border:1px solid #d7e7fa;border-radius:12px;padding:14px;font-size:.82rem;line-height:1.6;color:#526783;margin-bottom:12px;white-space:pre-wrap}
.qr-tech-grid{display:grid;grid-template-columns:1fr;gap:8px;margin-top:10px}
.qr-tech-item{background:#f3f8ff;border:1px solid #d7e7fa;border-radius:10px;padding:10px 12px}
.qr-tech-item span{display:block;font-size:.6rem;text-transform:uppercase;letter-spacing:.1em;color:#7890ac;font-weight:800}
.qr-tech-item b{display:block;font-size:.85rem;color:#344054;margin-top:4px;font-weight:700}
.qr-errore{text-align:center;padding:60px 20px;background:#fff;border-radius:22px;max-width:500px;box-shadow:0 20px 60px rgba(21,34,56,0.12)}
.qr-errore .emo{font-size:4rem;margin-bottom:16px;opacity:.4}
.qr-errore h1{font-family:Georgia,serif;color:var(--blue);font-size:1.6rem;margin-bottom:10px}
.qr-errore p{color:var(--muted);font-size:.88rem;line-height:1.6}
@media(max-width:900px){
 .cd-grid{grid-template-columns:1fr}
 .lista-layout{grid-template-columns:1fr}
 .qr-card{grid-template-columns:1fr;gap:20px}
 .campo-3{grid-template-columns:1fr 1fr}
}
@media(max-width:760px){
 .sidebar{position:fixed;left:0;top:0;transform:translateX(-100%);transition:transform .25s;z-index:30}
 .sidebar.open{transform:translateX(0)}
 .mobile-btn{display:grid;place-items:center}
 .page{padding:24px 16px}
 .topbar{padding:0 16px}
 .user span:last-child{display:none}
 .inv-griglia{grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}
 .inv-foto{height:130px}
 .inv-toolbar{flex-direction:column;align-items:stretch;padding:12px}
 .inv-search{max-width:none}
 .inv-filtri{width:100%}
 .inv-nome{font-size:.85rem}
 .cat-grid{grid-template-columns:1fr}
 .campo-2,.campo-3{grid-template-columns:1fr}
 .drawer{width:100%}
 .cal-toolbar{flex-direction:column;align-items:stretch;gap:10px}
 .cal-azioni{width:100%}
 .btn-crea{flex:1;justify-content:center}
}
@media(max-width:520px){
 .inv-griglia{grid-template-columns:1fr 1fr}
 .cal-filtro{width:100%;justify-content:center;flex-wrap:wrap}
}
  /* === RESPONSIVE — schermi grandi (Mac/PC 1800px+) === */
@media (min-width:1800px){
 body{font-size:16.5px}
 .page{padding:48px 50px 40px;max-width:1600px;margin:0 auto}
 .sidebar{width:270px;padding:26px 18px}
 h1.title{font-size:3rem}
 .lede{font-size:.98rem}
 .cd-grid{gap:20px;margin-bottom:26px}
 .cd-card{padding:28px}
 .cd-title{font-size:1.4rem}
 .cd-unit .n{font-size:1.9rem}
 .feed{padding:28px}
 .feed-item{padding:17px 14px}
 .feed-ico{width:42px;height:42px;font-size:1.1rem}
 .inv-toolbar{padding:18px;gap:14px}
 .inv-griglia{grid-template-columns:repeat(auto-fill,minmax(275px,1fr));gap:20px}
 .inv-foto{height:200px}
 .inv-body{padding:19px}
 .inv-nome{font-size:1.08rem}
 .inv-qta{font-size:1.12rem;padding:12px}
 .inv-btn{font-size:.8rem;min-height:44px}
 .inv-btn.pericolo,.inv-btn[data-azione="modifica"]{flex:0 0 50px;width:50px;min-width:50px;max-width:50px}
 .lista-pannello{padding:24px}
 .lista-titolo{font-size:1.3rem}
 .drawer{width:min(580px,50vw)}
 .drawer-head{padding:28px 28px 20px}
 .drawer-body{padding:24px 28px}
 .meta-grid div{padding:13px 15px}
 .note-box{padding:17px 19px;font-size:.93rem}
 .ruolo-card{padding:20px}
 .ruolo-avatar{width:54px;height:54px}
 .ruolo-nome{font-size:1rem}
}

/* === RESPONSIVE — tablet grande / laptop (1025-1799px) === */
@media (min-width:1025px) and (max-width:1799px){
 body{font-size:15.5px}
 .page{padding:36px 32px;max-width:1350px}
 .inv-griglia{grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}
 .inv-foto{height:170px}
}

/* === RESPONSIVE — tablet piccolo (768-1024px) === */
@media (min-width:768px) and (max-width:1024px){
 body{font-size:15px}
 .page{padding:28px 24px}
 h1.title{font-size:2.1rem}
 .sidebar{width:230px}
 .cd-grid{grid-template-columns:1fr 1fr;gap:16px}
 .inv-griglia{grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:14px}
 .inv-foto{height:145px}
 .lista-layout{grid-template-columns:1fr 1fr}
 .drawer{width:min(540px,100%)}
}

/* === RESPONSIVE — tablet verticale (481-767px) === */
@media (min-width:481px) and (max-width:767px){
 body{font-size:14.5px}
 .page{padding:24px 18px 30px}
 h1.title{font-size:1.85rem}
 .sidebar{width:270px}
 .cd-grid{grid-template-columns:1fr;gap:14px}
 .inv-griglia{grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}
 .inv-foto{height:130px}
 .inv-nome{font-size:.85rem}
 .lista-layout{grid-template-columns:1fr}
 .campo-2,.campo-3{grid-template-columns:1fr 1fr}
 .drawer{width:min(500px,100%)}
}

/* === RESPONSIVE — telefono (< 480px) === */
@media (max-width:480px){
 body{font-size:14px}
 .page{padding:20px 14px 30px}
 h1.title{font-size:1.6rem}
 .lede{font-size:.82rem}
 .sidebar{width:260px}
 .topbar{padding:0 14px;height:56px}
 .cd-grid{grid-template-columns:1fr;gap:12px}
 .cd-card{padding:16px}
 .cd-title{font-size:1.05rem}
 .cd-timer{gap:5px}
 .cd-unit{padding:8px 4px}
 .cd-unit .n{font-size:1.2rem}
 .feed{padding:16px}
 .feed-item{padding:11px 10px;gap:9px}
 .feed-ico{width:30px;height:30px;font-size:.85rem}
 .feed-txt strong{font-size:.78rem}
 .feed-txt span{font-size:.66rem}
 .inv-griglia{grid-template-columns:1fr 1fr;gap:10px}
 .inv-foto{height:110px}
 .inv-nome{font-size:.78rem}
 .inv-qta{font-size:.78rem;padding:7px 8px}
 .inv-btn{font-size:.65rem;min-height:34px;padding:7px 6px}
 .inv-btn.pericolo,.inv-btn[data-azione="modifica"]{flex:0 0 34px;width:34px;min-width:34px;max-width:34px;font-size:.85rem}
 .inv-toolbar{padding:10px;gap:8px;flex-direction:column;align-items:stretch}
 .inv-search{max-width:none}
 .inv-select{min-width:100%}
 .lista-layout{grid-template-columns:1fr;gap:12px}
 .lista-pannello{padding:12px;max-height:none}
 .lista-titolo{font-size:1rem}
 .cal-toolbar{flex-direction:column;gap:10px;align-items:stretch}
 .cal-nav{justify-content:center}
 .cal-azioni{flex-direction:column}
 .btn-crea{width:100%;justify-content:center;padding:10px;font-size:.75rem}
 .cal-filtro{width:100%;justify-content:center;flex-wrap:wrap}
 .cal-filtro button{padding:6px 12px;font-size:.7rem}
 .cal-griglia{min-width:600px;gap:4px}
 .cal-giorno{min-height:78px;padding:5px}
 .cal-giorno .num{font-size:.85rem;width:22px;height:22px}
 .cal-chip{font-size:.5rem;padding:2px 4px}
 .campo input,.campo select,.campo textarea{font-size:.82rem;padding:10px 12px}
 .campo-2,.campo-3{grid-template-columns:1fr}
 .cat-grid{grid-template-columns:1fr}
 .drawer{width:100%}
 .drawer-head{padding:18px 18px 14px}
 .drawer-head h2{font-size:1.15rem}
 .drawer-body{padding:18px}
 .drawer-foot{padding:14px 18px;flex-wrap:wrap}
 .drawer-foot button{flex:1}
 .meta-grid{grid-template-columns:1fr}
 .ruolo-card{padding:13px}
 .ruolo-nome{font-size:.85rem}
 .footer{flex-direction:column;gap:8px;text-align:center;font-size:.6rem;padding:14px 14px 20px}
 .allegato-azioni{flex-direction:column;gap:4px}
 .allegato-btn{padding:6px 8px;font-size:.6rem;min-height:28px}
 .allegato-icona{width:30px;height:30px;font-size:.9rem}
}
  /* === LOGIN — grafica nuova === */
.login-box{padding:52px 46px 44px;border-radius:28px;max-width:520px;position:relative;overflow:hidden}
.login-box::before{content:"";position:absolute;top:0;left:0;right:0;height:6px;background:linear-gradient(90deg,#083278 0%,#0b438d 50%,#a66d24 100%)}
.login-box h1{font-size:2rem;text-align:center;color:#083278;font-family:Georgia,serif;font-weight:700;margin-bottom:8px;line-height:1.1;letter-spacing:-.02em}
.login-box h1 span{color:#a66d24;font-style:italic;font-weight:400;margin:0 4px;font-size:1.15em}
.login-box .sub{text-align:center;color:#6b778c;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:38px}
.login-box .field{display:block;font-size:.72rem;font-weight:800;color:#6b778c;text-transform:uppercase;letter-spacing:.1em;margin:22px 0 10px}
.login-box .inp{padding:16px 18px;font-size:1rem;border-radius:14px;border:1.5px solid #e5e9f0;background:#fafbfd;transition:all .22s;outline:none;width:100%;color:#152238}
.login-box .inp:hover{border-color:#c4d1e5;background:#fff}
.login-box .inp:focus{border-color:#083278;background:#fff;box-shadow:0 0 0 4px rgba(8,50,120,0.08)}
.login-box .btn-login{padding:17px;font-size:.95rem;border-radius:14px;background:linear-gradient(135deg,#083278 0%,#0b438d 100%);box-shadow:0 8px 24px rgba(8,50,120,0.28);margin-top:32px;font-weight:800;letter-spacing:.03em;border:0;color:#fff;width:100%;cursor:pointer;transition:all .22s}
.login-box .btn-login:hover{background:linear-gradient(135deg,#0b438d 0%,#0f4fa3 100%);transform:translateY(-2px);box-shadow:0 12px 30px rgba(8,50,120,0.38)}
.login-box .logos img{height:78px;max-width:160px;object-fit:contain}
.login-box .logos{gap:22px;margin-bottom:26px}

/* Login sul telefono */
@media (max-width:520px){
 .login-box{padding:38px 26px 32px;border-radius:22px;max-width:100%}
 .login-box::before{height:5px}
 .login-box .logos{gap:14px;margin-bottom:20px}
 .login-box .logos img{height:60px;max-width:120px}
 .login-box h1{font-size:1.55rem}
 .login-box .sub{font-size:.68rem;letter-spacing:.12em;margin-bottom:28px}
 .login-box .inp{padding:14px 16px;font-size:.92rem;border-radius:12px}
 .login-box .btn-login{padding:15px;font-size:.88rem;margin-top:26px;border-radius:12px}
}

/* Login su schermo grande */
@media (min-width:1800px){
 .login-box{max-width:620px;padding:64px 56px 54px;border-radius:32px}
 .login-box::before{height:8px}
 .login-box .logos{gap:28px;margin-bottom:32px}
 .login-box .logos img{height:95px;max-width:190px}
 .login-box h1{font-size:2.5rem;margin-bottom:12px}
 .login-box .sub{font-size:.88rem;margin-bottom:46px}
 .login-box .inp{padding:19px 22px;font-size:1.1rem;border-radius:16px}
 .login-box .btn-login{padding:20px;font-size:1.05rem;margin-top:38px;border-radius:16px}
}
</style>
</head>
<body>
<div id="root"></div>
<div class="drawer-bg" id="d-bg"></div>
<aside class="drawer" id="d-panel">
  <div class="drawer-head">
    <div><p class="eyebrow" id="d-eyebrow">Notifica</p><h2 id="d-titolo">—</h2></div>
    <button class="drawer-close" id="d-close">✕</button>
  </div>
  <div class="drawer-body" id="d-body"></div>
  <div class="drawer-foot" id="d-foot"></div>
</aside>
<script>
/* ============================================================
   UTENTI E RUOLI
   ============================================================ */
const UTENTI={
 admin:{password:'123',ruolo:'Amministratore',nome:'Gianluca',iniziali:'GS'},
 wedding:{password:'wedding123',ruolo:'Wedding',nome:'Cristina',iniziali:'CR'},
 cucina:{password:'cucina123',ruolo:'Cucina',nome:'Chef',iniziali:'CH'},
 sala:{password:'sala123',ruolo:'Sala',nome:'Sala',iniziali:'SL'},
 magazzino:{password:'mag123',ruolo:'Magazzino',nome:'Magazzino',iniziali:'MG'},
 magazzino2:{password:'mag2123',ruolo:'Magazzino2',nome:'Mag.2',iniziali:'M2'}
};

const CATEGORIE_INV=['TAVOLI','SEDIE','CALTAGIRONE','COMPLEMENTI VARI','PIATTI E SOTTOPIATTI','BICCHIERI','CUCINA','ARREDO','TOVAGLIATO','ARGENTERIA','POSATERIA','VASSOI','LUCI E CANDELABRI'];

const EVENTI=[];
const NOLEGGI=[];
const PRODOTTI=[];
const NOTIFICHE=[];

/* ============================================================
   PERMESSI
   ============================================================ */
function notifichePerUtente(utente){
 const mappa={
  'Amministratore':['tutti','sala','cucina','magazzino','admin'],
  'Wedding':['tutti','sala','cucina','magazzino'],
  'Cucina':['tutti','cucina'],
  'Sala':['tutti','sala'],
  'Magazzino':['tutti','magazzino'],
  'Magazzino2':['tutti','magazzino']
 };
 const rep=mappa[utente.ruolo]||['tutti'];
 return NOTIFICHE.filter(n=>rep.includes(n.reparto));
}

function puoVedere(r,c){
 const m={'Amministratore':['evento','noleggio'],'Wedding':['evento'],'Cucina':['evento'],'Sala':['evento'],'Magazzino':['evento','noleggio'],'Magazzino2':['noleggio']};
 return (m[r]||[]).includes(c);
}
function puoCreare(r,c){
 const m={'Amministratore':['evento','noleggio'],'Wedding':['evento'],'Cucina':[],'Sala':[],'Magazzino':[],'Magazzino2':['noleggio']};
 return (m[r]||[]).includes(c);
}

/* ============================================================
   LETTO / NON LETTO
   ============================================================ */
function chiaveLetto(u){return 'ergo_lette_'+u}
function getLette(u){try{return JSON.parse(localStorage.getItem(chiaveLetto(u)))||[]}catch(e){return[]}}
function setLette(u,arr){localStorage.setItem(chiaveLetto(u),JSON.stringify(arr))}
function isLetta(u,id){return getLette(u).includes(id)}
function segnaLetta(u,id){const l=getLette(u);if(!l.includes(id)){l.push(id);setLette(u,l)}}
function segnaTutteLette(u,ids){const l=getLette(u);ids.forEach(i=>{if(!l.includes(i))l.push(i)});setLette(u,l)}

function tempoFa(iso){
 const diff=(Date.now()-new Date(iso).getTime())/1000;
 if(diff<60)return 'ora';
 if(diff<3600)return Math.floor(diff/60)+' min fa';
 if(diff<86400)return Math.floor(diff/3600)+' ore fa';
 if(diff<172800)return 'ieri';
 return Math.floor(diff/86400)+' giorni fa';
}

/* ============================================================
   STATO GLOBALE
   ============================================================ */
let user=null,view='dashboard',timer=null,filtroFeed='tutte';
let calFiltro='tutti';
let listaAttrezzature=[];
let invRicerca='',invCategoria='Tutte';
const R=document.getElementById('root');

/* ============================================================
   NAV
   ============================================================ */
const NAV=[
 {id:'dashboard',label:'Panoramica',icon:'◈',r:['Amministratore','Wedding','Cucina','Sala','Magazzino','Magazzino2']},
 {id:'calendario',label:'Calendario',icon:'▦',r:['Amministratore','Wedding','Cucina','Sala','Magazzino','Magazzino2']},
 {id:'inventario',label:'Inventario',icon:'◆',r:['Amministratore','Magazzino','Magazzino2']},
 {id:'liste',label:'Lista Attrezzature',icon:'✦',r:['Amministratore']},
 {id:'ruoli',label:'Ruoli',icon:'👥',r:['Amministratore']}
];

/* ============================================================
   UTILITÀ TESTO
   ============================================================ */
function escapeAttr(t){return String(t||'').replace(/"/g,'&quot;').replace(/</g,'&lt;')}

function normalizzaTesto(t){
 return String(t||'').toLowerCase()
  .normalize('NFD').replace(/[\u0300-\u036f]/g,'')
  .replace(/[^a-z0-9 ]/g,' ')
  .split(/\s+/).filter(Boolean).join(' ').trim();
}

function variantiParola(p){
 const varianti=new Set([p]);
 if(p.length>=4){
  if(p.endsWith('i')){varianti.add(p.slice(0,-1)+'o');varianti.add(p.slice(0,-1)+'e');varianti.add(p.slice(0,-1)+'a')}
  else if(p.endsWith('e')){varianti.add(p.slice(0,-1)+'a');varianti.add(p.slice(0,-1)+'o');varianti.add(p.slice(0,-1)+'i')}
  else if(p.endsWith('a')){varianti.add(p.slice(0,-1)+'e');varianti.add(p.slice(0,-1)+'i')}
  else if(p.endsWith('o')){varianti.add(p.slice(0,-1)+'i')}
 }
 if(p.length>=5){varianti.add(p.slice(0,-1));varianti.add(p.slice(0,-2))}
 return Array.from(varianti);
}

function paroleSimili(a,b){
 if(a===b)return true;
 if(a.length<3||b.length<3)return false;
 if(Math.abs(a.length-b.length)<=2){
  if(a.startsWith(b)||b.startsWith(a))return true;
  if(a.slice(0,3)===b.slice(0,3))return true;
 }
 let match=0;const min=Math.min(a.length,b.length);
 for(let i=0;i<min;i++){if(a[i]===b[i])match++}
 return match/min>=0.7;
}

function ricercaIntelligente(query,campi){
 const q=normalizzaTesto(query);
 if(!q)return true;
 const testo=normalizzaTesto(campi.filter(Boolean).join(' '));
 if(testo.includes(q))return true;
 const paroleTesto=testo.split(/\s+/);
 const paroleQuery=q.split(/\s+/);
 for(const pq of paroleQuery){
  const varianti=variantiParola(pq);
  const trovata=varianti.some(v=>paroleTesto.some(pt=>paroleSimili(v,pt)));
  if(!trovata)return false;
 }
 return true;
}

function formattaDataIt(iso){
 const d=new Date(iso);
 return d.toLocaleDateString('it-IT',{day:'2-digit',month:'2-digit',year:'numeric'})+' · '+d.toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
}

function iconaAllegato(mime){
 if(!mime)return '📎';
 if(mime.startsWith('image/'))return '🖼️';
 if(mime==='application/pdf'||mime.includes('pdf'))return '📄';
 return '📎';
}
/* ============================================================
   LOGIN
   ============================================================ */
function login(){
 if(timer){clearInterval(timer);timer=null}
 R.innerHTML=`<div class="login"><div class="login-box">
  <div class="logos">
   <img src="logo-ergo.png" alt="Ergo" onerror="this.style.display='none'">
   <img src="logo-scardaci.png" alt="Scardaci" onerror="this.style.display='none'">
  </div>
  <h1>Ergo <span style="color:#a66d24;font-style:italic">&</span> Scardaci</h1>
<p style="text-align:center;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:#8b96a9;font-weight:700;margin-bottom:24px">Gestionale Eventi</p>
  <p class="sub">Catering &amp; Noleggio Attrezzature</p>
  <div id="e"></div>
  <label class="field">Username</label>
  <input class="inp" id="u" value="" placeholder="Inserisci username" autocapitalize="off" autocomplete="username">
  <label class="field">Password</label>
  <input class="inp" id="p" type="password" value="" placeholder="Inserisci password" autocomplete="current-password">
  <button class="btn-login" id="go">Accedi al gestionale</button>
  
 </div></div>`;
 document.getElementById('go').onclick=doLogin;
 document.getElementById('p').addEventListener('keydown',e=>{if(e.key==='Enter')doLogin()});
}

function doLogin(){
 const u=document.getElementById('u').value.trim(),p=document.getElementById('p').value,f=UTENTI[u];
 if(f&&f.password===p){user={username:u,...f};view='dashboard';filtroFeed='tutte';app()}
 else{document.getElementById('e').innerHTML='<div class="err">Credenziali non corrette.</div>'}
}

/* ============================================================
   APP SHELL
   ============================================================ */
function app(){
 if(timer){clearInterval(timer);timer=null}
 const voci=NAV.filter(v=>v.r.includes(user.ruolo));
 const titolo=(voci.find(v=>v.id===view)||{}).label||'Panoramica';
 R.innerHTML=`<div class="app">
  <aside class="sidebar" id="sb">
   <div class="brand">
    <div class="brand-logos">
     <img src="logo-ergo.png" alt="E" onerror="this.style.display='none'">
     <img src="logo-scardaci.png" alt="S" onerror="this.style.display='none'">
    </div>
    <strong>Ergo &amp; Scardaci</strong>
    <span>Gestionale</span>
   </div>
   <div class="nav-label">Workspace</div>
   <nav class="nav" id="nav"></nav>
   <div class="side-bottom">
    <div class="role-card"><span>👑</span><div><strong>${user.ruolo}</strong><span>${user.username}</span></div></div>
    <button class="btn-out" id="out">Esci dal gestionale</button>
   </div>
  </aside>
  <main class="main">
   <header class="topbar">
    <button class="mobile-btn" id="mm">☰</button>
    <div class="crumb"><span>Gestionale</span><span>/</span><strong>${titolo}</strong></div>
    <div style="display:flex;gap:12px;align-items:center">
     <div class="user"><span class="avatar">${user.iniziali}</span><span>${user.nome}</span></div>
    </div>
   </header>
   <div id="pc"></div>
   <footer class="footer"><span>Ergo &amp; Scardaci</span><span>Prototipo · anteprima</span></footer>
  </main>
 </div>`;
 const nav=document.getElementById('nav');
 voci.forEach(v=>{
  const b=document.createElement('button');
  b.className=v.id===view?'on':'';
  b.innerHTML=`<span style="width:22px;text-align:center">${v.icon}</span><span>${v.label}</span>`;
  b.onclick=()=>{view=v.id;app()};
  nav.appendChild(b);
 });
 document.getElementById('mm').onclick=()=>document.getElementById('sb').classList.toggle('open');
 document.getElementById('out').onclick=()=>{user=null;login()};
 const pc=document.getElementById('pc');
 if(view==='dashboard')dash(pc);
 else if(view==='inventario')inv(pc);
 else if(view==='calendario')cal(pc);
 else if(view==='ruoli')ruoli(pc);
 else if(view==='liste')lista(pc);
 else pc.innerHTML=`<div class="page"><p class="eyebrow">Sezione</p><h1 class="title">${titolo}</h1><p class="lede">In costruzione…</p></div>`;
}
/* ============================================================
   DASHBOARD
   ============================================================ */
function dash(el){
 const visibili=notifichePerUtente(user);
 const nuove=visibili.filter(n=>!isLetta(user.username,n.id));
 const daMostrare=filtroFeed==='nuove'?nuove:visibili;

 let prossimoEv=null;
 const oggi=new Date();oggi.setHours(0,0,0,0);
 EVENTI.forEach(e=>{
  const d=new Date(e.inizio);
  if(d>=oggi&&(!prossimoEv||new Date(e.inizio)<new Date(prossimoEv.inizio)))prossimoEv=e;
 });
 let prossimoNl=null;
 NOLEGGI.forEach(n=>{
  const d=new Date(n.inizio);
  if(d>=oggi&&(!prossimoNl||new Date(n.inizio)<new Date(prossimoNl.inizio)))prossimoNl=n;
 });

 const oggi_str=oggi.toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});

 const cardEv=prossimoEv
  ?`<div class="cd-card event">
    <div class="cd-head"><div class="cd-label">📅 Prossimo evento</div><span class="cd-tag">${prossimoEv.stato||'confermato'}</span></div>
    <div class="cd-title">${prossimoEv.titolo}</div>
    <div class="cd-when">${prossimoEv.location||'—'} · ${prossimoEv.ospiti||0} ospiti</div>
    <div id="cd-e" data-target="${prossimoEv.inizio}"></div>
   </div>`
  :`<div class="cd-card event" style="opacity:.7">
    <div class="cd-head"><div class="cd-label">📅 Prossimo evento</div></div>
    <div class="cd-empty"><span class="emo">📅</span>Nessun evento programmato</div>
   </div>`;

 const cardNl=prossimoNl
  ?`<div class="cd-card rental">
    <div class="cd-head"><div class="cd-label">🚚 Prossimo noleggio</div><span class="cd-tag">${prossimoNl.stato||'confermato'}</span></div>
    <div class="cd-title">${prossimoNl.titolo}</div>
    <div class="cd-when">${prossimoNl.location||'—'}</div>
    <div id="cd-n" data-target="${prossimoNl.inizio}"></div>
   </div>`
  :`<div class="cd-card rental" style="opacity:.7">
    <div class="cd-head"><div class="cd-label">🚚 Prossimo noleggio</div></div>
    <div class="cd-empty"><span class="emo">🚚</span>Nessun noleggio programmato</div>
   </div>`;

 el.innerHTML=`<div class="page">
  <div style="margin-bottom:28px">
   <p class="eyebrow">${oggi_str.charAt(0).toUpperCase()+oggi_str.slice(1)}</p>
   <h1 class="title">Bentornato, ${user.nome}.</h1>
   <p class="lede">Ecco cosa bolle in pentola per i prossimi giorni.</p>
  </div>
  <div class="cd-grid">${cardEv}${cardNl}</div>
  <div class="feed">
   <div class="feed-head">
    <div><p class="eyebrow">Novità recenti</p><h2>Ultimi aggiornamenti ${nuove.length>0?`<span style="color:#2563eb;font-size:.8rem;font-weight:700">(${nuove.length} nuove)</span>`:''}</h2></div>
    <div class="feed-actions">
     <button class="btn-mini ${filtroFeed==='tutte'?'active':''}" id="f-tutte">Tutte</button>
     <button class="btn-mini ${filtroFeed==='nuove'?'active':''}" id="f-nuove">Solo nuove</button>
     ${nuove.length>0?`<button class="btn-mini" id="segna-tutte">✓ Segna tutte</button>`:''}
    </div>
   </div>
   ${daMostrare.length===0
     ?`<div class="feed-empty"><span class="emo">✨</span>${filtroFeed==='nuove'?'Nessuna notifica nuova.':'Nessuna novità per ora.'}</div>`
     :daMostrare.map(notifRow).join('')}
  </div>
 </div>`;
 document.getElementById('f-tutte').onclick=()=>{filtroFeed='tutte';dash(el)};
 document.getElementById('f-nuove').onclick=()=>{filtroFeed='nuove';dash(el)};
 const st=document.getElementById('segna-tutte');
 if(st)st.onclick=()=>{segnaTutteLette(user.username,visibili.map(n=>n.id));dash(el)};
 document.querySelectorAll('.feed-item').forEach(elm=>{elm.onclick=()=>apriDrawerNotif(elm.dataset.notif)});
 avviaCD();
}

function notifRow(n){
 const ico={evento:'📅',noleggio:'🚚',nota:'📝',allegato:'📎',accesso:'👤'};
 const cls={evento:'sage',noleggio:'blue',nota:'violet',allegato:'gold',accesso:'gold'};
 const letto=isLetta(user.username,n.id);
 return `<div class="feed-item ${letto?'':'unread'}" data-notif="${n.id}">
  <div class="feed-ico ${cls[n.tipo]||'blue'}">${ico[n.tipo]||'•'}</div>
  <div class="feed-txt"><strong>${n.titolo}${n.reparto==='admin'?' <span class="admin-only">🔒 ADMIN</span>':''}</strong><span>${n.sottotitolo}</span></div>
  <div class="feed-time">${tempoFa(n.quando)}</div>
 </div>`;
}

function avviaCD(){
 if(timer)clearInterval(timer);
 const tick=()=>{
  const be=document.getElementById('cd-e'),bn=document.getElementById('cd-n');
  if(!be&&!bn){clearInterval(timer);timer=null;return}
  if(be)be.innerHTML=renderCD(be.dataset.target);
  if(bn)bn.innerHTML=renderCD(bn.dataset.target);
 };
 tick();
 if(document.getElementById('cd-e')||document.getElementById('cd-n'))timer=setInterval(tick,1000);
}

function renderCD(iso){
 const diff=new Date(iso)-new Date();
 if(diff<=0)return `<div class="cd-wait">🟢 In corso oppure già iniziato</div>`;
 const s=Math.floor(diff/1000),g=Math.floor(s/86400),h=Math.floor((s%86400)/3600),m=Math.floor((s%3600)/60),sec=s%60;
 const p=n=>String(n).padStart(2,'0');
 return `<div class="cd-timer">
  <div class="cd-unit"><span class="n">${p(g)}</span><span class="u">giorni</span></div>
  <div class="cd-unit"><span class="n">${p(h)}</span><span class="u">ore</span></div>
  <div class="cd-unit"><span class="n">${p(m)}</span><span class="u">min</span></div>
  <div class="cd-unit"><span class="n">${p(sec)}</span><span class="u">sec</span></div>
 </div>`;
}
/* ============================================================
   DRAWER NOTIFICHE
   ============================================================ */
function apriDrawerNotif(id){
 const n=NOTIFICHE.find(x=>x.id===id);if(!n)return;
 segnaLetta(user.username,n.id);
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent=labelTipo(n.tipo);
 document.getElementById('d-titolo').textContent=n.titolo;
 document.getElementById('d-body').innerHTML=renderDetNotif(n);
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 setTimeout(()=>{if(view==='dashboard'){const pc=document.getElementById('pc');if(pc)dash(pc)}},200);
}

function chiudiDrawer(){
 document.getElementById('d-panel').classList.remove('open');
 document.getElementById('d-bg').classList.remove('open');
}

function labelTipo(t){
 return {evento:'Evento',noleggio:'Noleggio',nota:'Nota',allegato:'Allegato',accesso:'Accesso'}[t]||'Notifica';
}

function renderDetNotif(n){
 const d=n.dettagli||{};let h='';
 if(d.evento){h+=`<h4>Evento</h4><div class="note-box tutti"><strong style="font-family:Georgia,serif;font-size:1rem">${d.evento}</strong>${d.location?`<br><span style="color:#667085;font-size:.8rem">📍 ${d.location}</span>`:''}</div>`}
 if(d.noleggio){h+=`<h4>Noleggio</h4><div class="note-box"><strong style="font-family:Georgia,serif;font-size:1rem">${d.noleggio}</strong></div>`}
 if(d.testoNota){
  const cls=n.reparto==='cucina'?'cucina':n.reparto==='sala'?'sala':n.reparto==='magazzino'?'magazzino':'tutti';
  h+=`<h4>Testo della nota</h4><div class="note-box ${cls}">${d.testoNota}</div>`;
 }
 if(d.utente){h+=`<h4>Utente</h4><div class="note-box tutti"><strong>${d.utente}</strong><br><span style="color:#667085;font-size:.8rem">Ruolo: ${d.ruolo}</span></div>`}
 h+=`<h4>Info</h4><div class="meta-grid"><div><small>Da</small><strong>${n.da||'—'}</strong></div><div><small>Quando</small><strong>${tempoFa(n.quando)}</strong></div></div>`;
 return h;
}
/* ============================================================
   CALENDARIO
   ============================================================ */
const MESI=['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre','Ottobre','Novembre','Dicembre'];
const GIORNI=['Lun','Mar','Mer','Gio','Ven','Sab','Dom'];
let calMese=new Date().getMonth(),calAnno=new Date().getFullYear();

function cal(el){
 const anno=calAnno,mese=calMese;
 const oggi=new Date();oggi.setHours(0,0,0,0);
 const primo=new Date(anno,mese,1);
 const inizioSett=(primo.getDay()+6)%7;
 const ggMese=new Date(anno,mese+1,0).getDate();
 const celle=[];
 for(let i=0;i<inizioSett;i++)celle.push(null);
 for(let d=1;d<=ggMese;d++)celle.push(new Date(anno,mese,d));
 while(celle.length%7!==0)celle.push(null);
 const filtroAttivo=calFiltro||'tutti';
 const mostraEventi=filtroAttivo==='tutti'||filtroAttivo==='catering';
 const mostraNoleggi=filtroAttivo==='tutti'||filtroAttivo==='noleggi';
 const vedE=puoVedere(user.ruolo,'evento')&&mostraEventi;
 const vedN=puoVedere(user.ruolo,'noleggio')&&mostraNoleggi;
 const creaE=puoCreare(user.ruolo,'evento');
 const creaN=puoCreare(user.ruolo,'noleggio');
 let bottoni='';
 if(creaE)bottoni+=`<button class="btn-crea evento" id="btn-nuovo-evento">＋ Crea Evento</button>`;
 if(creaN)bottoni+=`<button class="btn-crea noleggio" id="btn-nuovo-noleggio">＋ Crea Noleggio</button>`;
 let legenda='';
 if(vedE)legenda+=`<span><i style="background:#bbf7d0"></i>Evento</span>`;
 if(vedN)legenda+=`<span><i style="background:#bfdbfe"></i>Noleggio</span><span><i style="background:#fed7aa"></i>Da confermare</span>`;
 const puoFiltrare=puoVedere(user.ruolo,'evento')&&puoVedere(user.ruolo,'noleggio');
 const filtroHtml=puoFiltrare?`<div class="cal-filtro"><button class="${filtroAttivo==='tutti'?'active':''}" data-filtro="tutti">Tutti</button><button class="${filtroAttivo==='catering'?'active':''}" data-filtro="catering">🍽️ Catering</button><button class="${filtroAttivo==='noleggi'?'active':''}" data-filtro="noleggi">🚚 Noleggi</button></div>`:'';
 el.innerHTML=`<div class="page">
  <div style="margin-bottom:22px"><p class="eyebrow">Pianificazione</p><h1 class="title">Calendario</h1><p class="lede">${filtroAttivo==='catering'?'Solo eventi catering.':filtroAttivo==='noleggi'?'Solo noleggi.':'Eventi e noleggi in un\'unica vista mensile.'}</p></div>
  <div class="cal-toolbar">
   <div class="cal-nav">
    <button id="cal-prev">‹</button>
    <span class="mese">${MESI[mese]} <select id="cal-anno-sel" style="font-family:Georgia,serif;font-size:1.05rem;font-weight:700;color:var(--blue);background:#f4f7fc;border:1px solid var(--line);border-radius:8px;padding:4px 8px;cursor:pointer;outline:none;margin-left:4px">${[2025,2026,2027,2028,2029,2030,2031,2032].map(a=>`<option value="${a}" ${a===anno?'selected':''}>${a}</option>`).join('')}</select></span>
    <button id="cal-next">›</button>
    <button id="cal-oggi" style="width:auto;padding:0 12px;font-size:.72rem;font-weight:700">Oggi</button>
   </div>
   <div class="cal-azioni">${bottoni}</div>
  </div>
  ${filtroHtml}
  <div class="cal-legenda">${legenda}</div>
  <div style="overflow-x:auto"><div class="cal-griglia">
   ${GIORNI.map(g=>`<div class="cal-int">${g}</div>`).join('')}
   ${celle.map((d,i)=>{
     if(!d)return `<div class="cal-giorno vuoto"></div>`;
     const eventiG=vedE?EVENTI.filter(e=>stessaData(e.inizio,d)):[];
     const nolG=vedN?NOLEGGI.filter(n=>inRange(d,n)):[];
     const isOggi=d.getTime()===oggi.getTime();
     let cls='cal-giorno';
     if(eventiG.length&&nolG.length)cls+=' ha-entrambi';
     else if(eventiG.length)cls+=' ha-eventi';
     else if(nolG.length)cls+=' ha-noleggi';
     if(isOggi)cls+=' oggi';
     let chips='';
     eventiG.slice(0,2).forEach(e=>{chips+=`<span class="cal-chip evento" data-id="${e.id}" data-tipo="evento">${e.titolo}</span>`});
     nolG.slice(0,2).forEach(n=>{const pend=n.stato!=='confermato';chips+=`<span class="cal-chip noleggio ${pend?'pending':''}" data-id="${n.id}" data-tipo="noleggio">${n.titolo}</span>`});
     const tot=eventiG.length+nolG.length;
     if(tot>2)chips+=`<span class="cal-chip piu">+${tot-2}</span>`;
     return `<div class="${cls}" data-giorno="${d.toISOString()}"><span class="num">${d.getDate()}</span>${chips}</div>`;
   }).join('')}
  </div></div>
  <div class="cal-pannello" id="cal-pannello"></div>
 </div>`;
 document.getElementById('cal-prev').onclick=()=>{calMese--;if(calMese<0){calMese=11;calAnno--}cal(el)};
 document.getElementById('cal-next').onclick=()=>{calMese++;if(calMese>11){calMese=0;calAnno++}cal(el)};
 document.getElementById('cal-oggi').onclick=()=>{const n=new Date();calMese=n.getMonth();calAnno=n.getFullYear();cal(el)};
 document.getElementById('cal-anno-sel').onchange=e=>{calAnno=parseInt(e.target.value);cal(el)};
 const be=document.getElementById('btn-nuovo-evento'),bn=document.getElementById('btn-nuovo-noleggio');
 if(be)be.onclick=()=>apriModaleEvento();
 if(bn)bn.onclick=()=>apriModaleNoleggio();
 el.querySelectorAll('.cal-filtro button').forEach(b=>{b.onclick=()=>{calFiltro=b.dataset.filtro;cal(el)}});
 document.querySelectorAll('.cal-chip[data-id]').forEach(c=>{
  c.onclick=e=>{e.stopPropagation();const id=c.dataset.id,tipo=c.dataset.tipo;
   if(tipo==='evento'){const ev=EVENTI.find(x=>x.id===id);if(ev)apriDrawerEnt('evento',ev)}
   else{const nl=NOLEGGI.find(x=>x.id===id);if(nl)apriDrawerEnt('noleggio',nl)}
  };
 });
 document.querySelectorAll('.cal-giorno[data-giorno]').forEach(g=>{
  g.onclick=()=>{const dt=new Date(g.dataset.giorno);mostraPann(dt);document.querySelectorAll('.cal-giorno').forEach(x=>x.style.outline='');g.style.outline='2px solid var(--blue)'};
 });
}
function stessaData(iso,d){
 const x=new Date(iso);
 return x.getFullYear()===d.getFullYear()&&x.getMonth()===d.getMonth()&&x.getDate()===d.getDate();
}

function inRange(d,n){
 const i=new Date(n.inizio),f=new Date(n.fine);
 i.setHours(0,0,0,0);f.setHours(23,59,59,999);
 return d>=i&&d<=f;
}

function mostraPann(d){
 const p=document.getElementById('cal-pannello');if(!p)return;
 const filtroAttivo=calFiltro||'tutti';
 const vedE=puoVedere(user.ruolo,'evento')&&(filtroAttivo==='tutti'||filtroAttivo==='catering');
 const vedN=puoVedere(user.ruolo,'noleggio')&&(filtroAttivo==='tutti'||filtroAttivo==='noleggi');
 const eventiG=vedE?EVENTI.filter(e=>stessaData(e.inizio,d)):[];
 const nolG=vedN?NOLEGGI.filter(n=>inRange(d,n)):[];
 const dataStr=d.toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long'});
 p.classList.add('on');
 if(eventiG.length===0&&nolG.length===0){
  p.innerHTML=`<h3>${dataStr.charAt(0).toUpperCase()+dataStr.slice(1)} <span class="badge">Nessun evento</span></h3><p style="color:var(--muted);font-size:.82rem">Non ci sono eventi o noleggi in questa data.</p>`;
  return;
 }
 let righe='';
 eventiG.forEach(e=>{
  const ora=new Date(e.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  righe+=`<div class="cal-riga evento" data-id="${e.id}" data-tipo="evento"><div class="ico">📅</div><div class="txt"><strong>${e.titolo}</strong><span>${e.location||'—'} · ${e.ospiti||0} ospiti</span></div><div class="ora">${ora}</div></div>`;
 });
 nolG.forEach(n=>{
  const ora=new Date(n.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  righe+=`<div class="cal-riga noleggio" data-id="${n.id}" data-tipo="noleggio"><div class="ico">🚚</div><div class="txt"><strong>${n.titolo}</strong><span>${n.location||'—'}</span></div><div class="ora">${ora}</div></div>`;
 });
 p.innerHTML=`<h3>${dataStr.charAt(0).toUpperCase()+dataStr.slice(1)} <span class="badge">${eventiG.length+nolG.length} appuntament${eventiG.length+nolG.length===1?'o':'i'}</span></h3><div class="cal-lista">${righe}</div>`;
 p.querySelectorAll('.cal-riga').forEach(r=>{
  r.onclick=()=>{const id=r.dataset.id,tipo=r.dataset.tipo;
   if(tipo==='evento'){const ev=EVENTI.find(x=>x.id===id);if(ev)apriDrawerEnt('evento',ev)}
   else{const nl=NOLEGGI.find(x=>x.id===id);if(nl)apriDrawerEnt('noleggio',nl)}
  };
 });
 p.scrollIntoView({behavior:'smooth',block:'nearest'});
}
/* ============================================================
   LEGGI ALLEGATI (base64)
   ============================================================ */
async function leggiAllegati(inputId,folder){
 const inp=document.getElementById(inputId);
 if(!inp||!inp.files||inp.files.length===0)return [];
 const files=Array.from(inp.files);
 const risultati=[];
 for(const f of files){
  try{
   if(window.ergoSupabaseUpload){
    const uploaded=await window.ergoSupabaseUpload(f,folder||'allegati_noleggi');
    if(uploaded){
     risultati.push({nome:f.name,nome_file:f.name,mime:f.type||'application/octet-stream',size:f.size,url:uploaded.url,path:uploaded.path,bucket:uploaded.bucket,caricato_il:new Date().toISOString()});
     continue;
    }
   }
   const data=await new Promise((resolve,reject)=>{const r=new FileReader();r.onload=e=>resolve(e.target.result);r.onerror=reject;r.readAsDataURL(f)});
   risultati.push({nome:f.name,nome_file:f.name,mime:f.type||'application/octet-stream',size:f.size,data:data,caricato_il:new Date().toISOString()});
  }catch(e){console.warn('Allegato non caricato',f.name,e)}
 }
 return risultati;
}

/* ============================================================
   CREA EVENTO
   ============================================================ */
function apriModaleEvento(){
 const oggi=new Date().toISOString().slice(0,10);
 const isAdmin=user.ruolo==='Amministratore';
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Nuovo evento';
 document.getElementById('d-titolo').textContent='📅 Crea Evento Catering';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Nome evento / Cliente <span style="color:#dc2626">*</span></label><input id="ev-nome" placeholder="Es. Matrimonio Bianchi"></div>
  <div class="campo-2"><div class="campo"><label>Data</label><input id="ev-data" type="date" value="${oggi}"></div><div class="campo"><label>Orario</label><input id="ev-ora" type="time" value="18:30"></div></div>
  <div class="campo"><label>Location</label><input id="ev-loc" placeholder="Es. Villa San Giorgio"></div>
  <input id="ev-osp" type="number" min="0" placeholder="0" onfocus="if(this.value==='0')this.value=''">
  <div class="divisore-modale">📝 Note per tutti</div><div class="campo"><textarea id="ev-n-tutti" style="background:#eef2ff;border-color:#c7d2fe"></textarea><input type="file" id="ev-f-tutti" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">🍽️ Note per la sala</div><div class="campo"><textarea id="ev-n-sala" style="background:#f0fdf4;border-color:#bbf7d0"></textarea><input type="file" id="ev-f-sala" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">👨‍🍳 Note per la cucina</div><div class="campo"><textarea id="ev-n-cucina" style="background:#fff7ed;border-color:#fed7aa"></textarea><input type="file" id="ev-f-cucina" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">📦 Note per il magazzino</div><div class="campo"><textarea id="ev-n-mag" style="background:#f5f3ff;border-color:#ddd6fe"></textarea><input type="file" id="ev-f-mag" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  ${isAdmin?`<div class="divisore-modale">🔒 Cartella privata Admin</div><div class="campo"><textarea id="ev-n-priv" style="background:#fdf4ff;border-color:#f5d0fe"></textarea><input type="file" id="ev-f-priv" multiple accept="image/*,.pdf" style="margin-top:8px"></div>`:''}
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="ev-salva" style="background:#3e765e">💾 Crea Evento</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('ev-salva').onclick=async()=>{
  const btn=document.getElementById('ev-salva');btn.disabled=true;btn.textContent='⏳ Salvataggio...';
  const nome=document.getElementById('ev-nome').value.trim();
  if(!nome){alert('Il nome è obbligatorio.');btn.disabled=false;btn.textContent='💾 Crea Evento';return}
  const data=document.getElementById('ev-data').value;
  const ora=document.getElementById('ev-ora').value||'18:30';
  const ev={
   id:'e-'+Date.now(),titolo:nome,inizio:data+'T'+ora+':00',fine:data+'T23:59:00',
   location:document.getElementById('ev-loc').value.trim()||'—',
   ospiti:parseInt(document.getElementById('ev-osp').value)||0,
   bambini:parseInt(document.getElementById('ev-bam').value)||0,
   staff:parseInt(document.getElementById('ev-stf').value)||0,
   stato:'confermato',
   noteTutti:document.getElementById('ev-n-tutti').value,
   noteSala:document.getElementById('ev-n-sala').value,
   noteCucina:document.getElementById('ev-n-cucina').value,
   noteMagazzino:document.getElementById('ev-n-mag').value,
   notePrivata:document.getElementById('ev-n-priv')?document.getElementById('ev-n-priv').value:'',
   allegatiTutti:await leggiAllegati('ev-f-tutti'),
   allegatiSala:await leggiAllegati('ev-f-sala'),
   allegatiCucina:await leggiAllegati('ev-f-cucina'),
   allegatiMagazzino:await leggiAllegati('ev-f-mag'),
   allegatiPrivata:document.getElementById('ev-f-priv')?await leggiAllegati('ev-f-priv'):[],
   creatoDa:user.nome+' ('+user.ruolo+')',creatoIl:new Date().toISOString()
  };
  let salvati=[];try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
  salvati.push(ev);localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
  EVENTI.push(ev);generaNotifEvento(ev);
  chiudiDrawer();alert('✅ Evento creato!');
  const pc=document.getElementById('pc');if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}
/* ============================================================
   CREA NOLEGGIO
   ============================================================ */
function apriModaleNoleggio(){
 const oggi=new Date().toISOString().slice(0,10);
 const isAdmin=user.ruolo==='Amministratore';
 const isMag2=user.ruolo==='Magazzino2';
 const vediBolla=isAdmin||isMag2;
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Nuovo noleggio';
 document.getElementById('d-titolo').textContent='🚚 Crea Noleggio';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Titolo <span style="color:#dc2626">*</span></label><input id="nl-titolo" placeholder="Es. Noleggio tavoli Rossi"></div>
  <div class="campo-2"><div class="campo"><label>Data inizio</label><input id="nl-di" type="date" value="${oggi}"></div><div class="campo"><label>Ora inizio</label><input id="nl-oi" type="time" value="09:00"></div></div>
  <div class="campo-2"><div class="campo"><label>Data fine</label><input id="nl-df" type="date" value="${oggi}"></div><div class="campo"><label>Ora fine</label><input id="nl-of" type="time" value="18:00"></div></div>
  <div class="campo"><label>Location <span style="color:#dc2626">*</span></label><input id="nl-loc"></div>
  <div class="campo-2"><div class="campo"><label>Referente <span style="color:#dc2626">*</span></label><input id="nl-ref"></div><div class="campo"><label>Telefono <span style="color:#dc2626">*</span></label><input id="nl-tel" type="tel"></div></div>
  <div class="campo"><label>Stato</label><select id="nl-stato" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff"><option value="confermato">Confermato</option><option value="non confermato">Non confermato</option></select></div>
  <div class="campo"><label>Note</label><textarea id="nl-note"></textarea></div>
  ${vediBolla?`<div class="divisore-modale">💰 Bolla con prezzo</div><div class="campo"><input type="file" id="nl-f-bolla" multiple accept="image/*,.pdf"></div>`:''}
  <div class="divisore-modale">📄 DDT</div><div class="campo"><input type="file" id="nl-f-ddt" multiple accept="image/*,.pdf"></div>
  <div class="divisore-modale">📎 Vario</div><div class="campo"><input type="file" id="nl-f-vario" multiple accept="image/*,.pdf"></div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="nl-salva">💾 Crea Noleggio</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('nl-salva').onclick=async()=>{
  const btn=document.getElementById('nl-salva');btn.disabled=true;btn.textContent='⏳ Salvataggio...';
  const titolo=document.getElementById('nl-titolo').value.trim();
  const loc=document.getElementById('nl-loc').value.trim();
  const ref=document.getElementById('nl-ref').value.trim();
  const tel=document.getElementById('nl-tel').value.trim();
  if(!titolo||!loc||!ref||!tel){alert('Compila tutti i campi obbligatori.');btn.disabled=false;btn.textContent='💾 Crea Noleggio';return}
  const nl={
   id:'n-'+Date.now(),tipo:'noleggio',titolo,
   inizio:document.getElementById('nl-di').value+'T'+(document.getElementById('nl-oi').value||'09:00')+':00',
   fine:document.getElementById('nl-df').value+'T'+(document.getElementById('nl-of').value||'18:00')+':00',
   location:loc,referente:ref,telefono:tel,
   stato:document.getElementById('nl-stato').value,
   note:document.getElementById('nl-note').value,
   allegatiBolla:vediBolla?await leggiAllegati('nl-f-bolla'):[],
   allegatiDDT:await leggiAllegati('nl-f-ddt'),
   allegatiVario:await leggiAllegati('nl-f-vario'),
   creatoDa:user.nome+' ('+user.ruolo+')',creatoIl:new Date().toISOString()
  };
  let salvati=[];try{salvati=JSON.parse(localStorage.getItem('ergo_noleggi'))||[]}catch(e){}
  salvati.push(nl);localStorage.setItem('ergo_noleggi',JSON.stringify(salvati));
  NOLEGGI.push(nl);generaNotifNoleggio(nl);
  chiudiDrawer();alert('✅ Noleggio creato!');
  const pc=document.getElementById('pc');if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}
/* ============================================================
   NOTIFICHE AUTOMATICHE
   ============================================================ */
function generaNotifEvento(ev){
 const nuovi=[];
 nuovi.push({id:'nf-'+Date.now()+'-ev',tipo:'evento',reparto:'tutti',
  titolo:'Evento creato: '+ev.titolo,
  sottotitolo:ev.location+' · '+ev.ospiti+' ospiti',
  quando:new Date().toISOString(),da:ev.creatoDa,
  dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),location:ev.location,ospiti:ev.ospiti}});
 if(ev.noteTutti&&ev.noteTutti.trim()){
  nuovi.push({id:'nf-'+Date.now()+'-nt',tipo:'nota',reparto:'tutti',
   titolo:'Nuova nota per tutti',sottotitolo:'Da '+ev.creatoDa+' · '+ev.titolo,
   quando:new Date().toISOString(),da:ev.creatoDa,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteTutti}});
 }
 if(ev.noteSala&&ev.noteSala.trim()){
  nuovi.push({id:'nf-'+Date.now()+'-ns',tipo:'nota',reparto:'sala',
   titolo:'Nuova nota per la sala',sottotitolo:'Da '+ev.creatoDa+' · '+ev.titolo,
   quando:new Date().toISOString(),da:ev.creatoDa,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteSala}});
 }
 if(ev.noteCucina&&ev.noteCucina.trim()){
  nuovi.push({id:'nf-'+Date.now()+'-nc',tipo:'nota',reparto:'cucina',
   titolo:'Nuova nota per la cucina',sottotitolo:'Da '+ev.creatoDa+' · '+ev.titolo,
   quando:new Date().toISOString(),da:ev.creatoDa,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteCucina}});
 }
 if(ev.noteMagazzino&&ev.noteMagazzino.trim()){
  nuovi.push({id:'nf-'+Date.now()+'-nm',tipo:'nota',reparto:'magazzino',
   titolo:'Nuova nota per il magazzino',sottotitolo:'Da '+ev.creatoDa+' · '+ev.titolo,
   quando:new Date().toISOString(),da:ev.creatoDa,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteMagazzino}});
 }
 nuovi.forEach(n=>NOTIFICHE.unshift(n));
 let salvate=[];
 try{salvate=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
 nuovi.forEach(n=>salvate.unshift(n));
 localStorage.setItem('ergo_notifiche',JSON.stringify(salvate.slice(0,200)));
}

function generaNotifNoleggio(nl){
 const nuovo={id:'nf-'+Date.now()+'-nl',tipo:'noleggio',reparto:'magazzino',
  titolo:'Noleggio creato: '+nl.titolo,
  sottotitolo:nl.location+' · '+nl.stato,
  quando:new Date().toISOString(),da:nl.creatoDa,
  dettagli:{noleggio:nl.titolo,dal:formattaDataIt(nl.inizio),al:formattaDataIt(nl.fine),location:nl.location,referente:nl.referente,telefono:nl.telefono,note:nl.note||'—'}};
 NOTIFICHE.unshift(nuovo);
 let salvate=[];
 try{salvate=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
 salvate.unshift(nuovo);
 localStorage.setItem('ergo_notifiche',JSON.stringify(salvate.slice(0,200)));
}
/* ============================================================
   DRAWER EVENTO / NOLEGGIO
   ============================================================ */
function apriDrawerEnt(tipo,obj){
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 const isAdmin=user.ruolo==='Amministratore';
 const isWedding=user.ruolo==='Wedding';
 const isMag2=user.ruolo==='Magazzino2';
 const isMag1=user.ruolo==='Magazzino';
 document.getElementById('d-eyebrow').textContent=tipo==='evento'?'Evento Catering':'Noleggio';
 document.getElementById('d-titolo').textContent=obj.titolo;
 const dataI=new Date(obj.inizio).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
 const ora=new Date(obj.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 let h='';
 if(tipo==='evento'){
  h+=`<h4>Dettagli evento</h4><div class="meta-grid"><div><small>Data</small><strong>${dataI}</strong></div><div><small>Orario</small><strong>${ora}</strong></div><div><small>Location</small><strong>${obj.location||'—'}</strong></div><div><small>Ospiti</small><strong>${obj.ospiti||0}${obj.bambini?' · '+obj.bambini+' bimbi':''}${obj.staff?' · '+obj.staff+' staff':''}</strong></div></div>`;
  const vediSala=isAdmin||isWedding||user.ruolo==='Sala';
  const vediCucina=isAdmin||isWedding||user.ruolo==='Cucina';
  const vediMag=isAdmin||isWedding||isMag1||isMag2;
  if(obj.noteTutti)h+=`<h4>📝 Note per tutti</h4><div class="note-box tutti">${obj.noteTutti}</div>`;
  if(vediSala&&obj.noteSala)h+=`<h4>🍽️ Note per la sala</h4><div class="note-box sala">${obj.noteSala}</div>`;
  if(vediCucina&&obj.noteCucina)h+=`<h4>👨‍🍳 Note per la cucina</h4><div class="note-box cucina">${obj.noteCucina}</div>`;
  if(vediMag&&obj.noteMagazzino)h+=`<h4>📦 Note per il magazzino</h4><div class="note-box magazzino">${obj.noteMagazzino}</div>`;
  const tuttiAllegati=raccogliAllegatiEnt('evento',obj,vediSala,vediCucina,vediMag);
  if(tuttiAllegati.length>0){
   h+=`<h4>📎 Allegati (${tuttiAllegati.length})</h4>`;
   tuttiAllegati.forEach((a,i)=>{
    h+=`<div class="allegato-riga"><div class="allegato-info"><span class="allegato-icona">${iconaAllegato(a.mime)}</span><div><strong>${a.nome}</strong><small>${a.sezione}</small></div></div><div class="allegato-azioni"><button class="allegato-btn anteprima" data-allega-idx="${i}">👁️ Anteprima</button><button class="allegato-btn" data-allega-down="${i}">⬇️</button></div></div>`;
   });
  }
 }else{
  const dataF=new Date(obj.fine).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
  h+=`<h4>Dettagli noleggio</h4><div class="meta-grid"><div><small>Dal</small><strong>${dataI} · ${ora}</strong></div><div><small>Al</small><strong>${dataF}</strong></div><div><small>Location</small><strong>${obj.location||'—'}</strong></div><div><small>Stato</small><strong>${obj.stato}</strong></div><div><small>Referente</small><strong>${obj.referente||'—'}</strong></div><div><small>Telefono</small><strong>${obj.telefono||'—'}</strong></div></div>`;
  if(obj.note)h+=`<h4>📝 Note</h4><div class="note-box">${obj.note}</div>`;
  const vediBolla=isAdmin||isMag2;
  const vediDDT=isAdmin||isMag2||isMag1;
  const vediVario=isAdmin||isMag2||isMag1;
  const tuttiAllegati=raccogliAllegatiEnt('noleggio',obj,vediBolla,vediDDT,vediVario);
  if(tuttiAllegati.length>0){
   h+=`<h4>📎 Allegati (${tuttiAllegati.length})</h4>`;
   tuttiAllegati.forEach((a,i)=>{
    h+=`<div class="allegato-riga"><div class="allegato-info"><span class="allegato-icona">${iconaAllegato(a.mime)}</span><div><strong>${a.nome}</strong><small>${a.sezione}</small></div></div><div class="allegato-azioni"><button class="allegato-btn anteprima" data-allega-idx="${i}">👁️ Anteprima</button><button class="allegato-btn" data-allega-down="${i}">⬇️</button></div></div>`;
   });
  }
 }
 document.getElementById('d-body').innerHTML=h;
 const puoMod=puoModTipo(tipo);
 let footHtml=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 if(puoMod)footHtml+=`<button class="btn-primary" id="d-modifica">✏️ Modifica</button>`;
 if(puoMod)footHtml+=`<button class="btn-primary" id="d-elimina" style="background:#dc2626;flex:0 0 auto">🗑️</button>`;
 document.getElementById('d-foot').innerHTML=footHtml;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 const bm=document.getElementById('d-modifica');
 if(bm)bm.onclick=()=>{chiudiDrawer();if(tipo==='evento')alert('Modifica evento: in arrivo');else alert('Modifica noleggio: in arrivo')};
 const bel=document.getElementById('d-elimina');
 if(bel)bel.onclick=()=>{chiudiDrawer();confermaElimEnt(tipo,obj)};
 const allegati=raccogliAllegatiEnt(tipo,obj,true,true,true);
 document.querySelectorAll('[data-allega-idx]').forEach(b=>{
  b.onclick=()=>{const idx=parseInt(b.dataset.allegaIdx);if(allegati[idx])apriAnteprimaAllega(allegati[idx])};
 });
 document.querySelectorAll('[data-allega-down]').forEach(b=>{
  b.onclick=()=>{const idx=parseInt(b.dataset.allegaDown);if(allegati[idx])scaricaAllega(allegati[idx])};
 });
}
function puoModTipo(tipo){
 if(tipo==='evento')return user.ruolo==='Amministratore'||user.ruolo==='Wedding';
 return user.ruolo==='Amministratore'||user.ruolo==='Magazzino2';
}

function raccogliAllegatiEnt(tipo,ent,vediB,vediD,vediV){
 if(tipo==='evento'){
  const a=ent.allegatiTutti||[];
  const b=vediB?(ent.allegatiSala||[]):[];
  const c=vediD?(ent.allegatiCucina||[]):[];
  const e=vediV?(ent.allegatiMagazzino||[]):[];
  return [
   ...a.map(x=>({...x,sezione:'Note per tutti'})),
   ...b.map(x=>({...x,sezione:'Note per la sala'})),
   ...c.map(x=>({...x,sezione:'Note per la cucina'})),
   ...e.map(x=>({...x,sezione:'Note per il magazzino'}))
  ];
 }
 const a=vediB?(ent.allegatiBolla||[]):[];
 const b=vediD?(ent.allegatiDDT||[]):[];
 const c=vediV?(ent.allegatiVario||[]):[];
 return [
  ...a.map(x=>({...x,sezione:'Bolla con prezzo'})),
  ...b.map(x=>({...x,sezione:'DDT'})),
  ...c.map(x=>({...x,sezione:'Vario'}))
 ];
}

function apriAnteprimaAllega(allegato){
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Anteprima';
 document.getElementById('d-titolo').textContent=allegato.nome||'Allegato';
 const mime=allegato.mime||'';
 let contenuto='';
 if(mime.startsWith('image/')){
  contenuto=`<div style="background:#f3f5f8;border-radius:14px;padding:14px;text-align:center"><img src="${allegato.data||allegato.url}" style="max-width:100%;max-height:65vh;border-radius:10px"></div>`;
 }else if(mime.includes('pdf')){
  contenuto=`<div style="background:#f3f5f8;border-radius:14px;padding:14px"><iframe src="${allegato.data||allegato.url}" style="width:100%;height:60vh;border:0;border-radius:10px;background:#fff"></iframe></div>`;
 }else{
  contenuto=`<div class="note-box" style="text-align:center;padding:30px"><div style="font-size:2.5rem;margin-bottom:10px">📎</div><p>Anteprima non disponibile per questo tipo di file.</p></div>`;
 }
 document.getElementById('d-body').innerHTML=contenuto+`<div style="margin-top:14px;padding:12px;background:#f3f8ff;border:1px solid #d7e7fa;border-radius:10px;font-size:.78rem;color:#4b5563">📌 <b>${allegato.sezione}</b></div>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button><button class="btn-primary" id="d-scarica">⬇️ Scarica</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('d-scarica').onclick=()=>scaricaAllega(allegato);
}

function scaricaAllega(allegato){
 if(!allegato||!(allegato.data||allegato.url))return;
 const a=document.createElement('a');
 a.href=allegato.data||allegato.url;
 a.download=allegato.nome||'allegato';
 document.body.appendChild(a);
 a.click();
 document.body.removeChild(a);
}

function confermaElimEnt(tipo,obj){
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Conferma eliminazione';
 document.getElementById('d-titolo').textContent='🗑️ Elimina '+(tipo==='evento'?'evento':'noleggio');
 document.getElementById('d-body').innerHTML=`<div class="note-box" style="background:#fef2f2;border-color:#fecaca;color:#991b1b"><strong style="font-family:Georgia,serif;font-size:1.05rem">${obj.titolo}</strong><br><span style="font-size:.78rem;color:#b91c1c">Azione irreversibile</span></div><p style="color:#6b778c;font-size:.82rem;line-height:1.55;margin-top:14px">Richiede <b>due conferme</b>. Tocca il pulsante rosso per completare.</p>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="d-conf" style="background:#dc2626">🗑️ CONFERMA</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('d-conf').onclick=()=>{
  if(tipo==='evento'){
   const idx=EVENTI.findIndex(e=>e.id===obj.id);
   if(idx>=0)EVENTI.splice(idx,1);
   let salv=[];try{salv=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
   salv=salv.filter(e=>e.id!==obj.id);
   localStorage.setItem('ergo_eventi',JSON.stringify(salv));
  }else{
   const idx=NOLEGGI.findIndex(n=>n.id===obj.id);
   if(idx>=0)NOLEGGI.splice(idx,1);
   let salv=[];try{salv=JSON.parse(localStorage.getItem('ergo_noleggi'))||[]}catch(e){}
   salv=salv.filter(n=>n.id!==obj.id);
   localStorage.setItem('ergo_noleggi',JSON.stringify(salv));
  }
  chiudiDrawer();
  alert('✅ Eliminato.');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}
/* ============================================================
   INVENTARIO
   ============================================================ */
function tuttiProds(salvati){
 const base=PRODOTTI.slice();
 (salvati||[]).forEach(p=>{if(!base.find(x=>x.codice===p.codice))base.push(p)});
 return base;
}

function cardProd(p,isAdmin){
 const hasFoto=!!p.foto;
 return `<div class="inv-card">
  <div class="inv-foto">${hasFoto?`<img loading="lazy" src="${p.foto}">`:''}<span class="inv-badge-cat">${p.categoria||'—'}</span></div>
  <div class="inv-body">
   <div class="inv-nome">${p.nome||''}</div>
   <div class="inv-codice">Cod. ${p.codice||'—'}</div>
   <div class="inv-qta">📦 ${p.quantita||0}</div>
   <div class="inv-info">📍 <b>${p.posizione||'—'}</b></div>
   ${isAdmin?`<div class="inv-prezzo">€ ${(p.prezzo||0).toFixed(2)}</div>`:''}
   <div class="inv-azioni">
    <button class="inv-btn primario" data-azione="scheda" data-codice="${p.codice}">📋 Scheda</button>
    ${isAdmin?`<button class="inv-btn" data-azione="modifica" data-codice="${p.codice}">✏️</button>`:''}
    ${isAdmin?`<button class="inv-btn pericolo" data-azione="elimina" data-codice="${p.codice}">🗑️</button>`:''}
   </div>
  </div>
 </div>`;
}

function inv(el){
 let salvati=[];
 try{salvati=JSON.parse(localStorage.getItem('ergo_prodotti'))||[]}catch(e){}
 const tutti=tuttiProds(salvati);
 const filtrati=tutti.filter(p=>{
  const matchCat=invRicerca.trim()!==''||invCategoria==='Tutte'||(p.categoria||'').toUpperCase().includes(invCategoria.toUpperCase());
  const matchTxt=ricercaIntelligente(invRicerca,[p.nome,p.codice,p.categoria,p.posizione,p.note]);
  return matchCat&&matchTxt;
 });
 const isAdmin=user.ruolo==='Amministratore';
 el.innerHTML=`<div class="page">
  <div style="margin-bottom:20px"><p class="eyebrow">Catalogo</p><h1 class="title">Inventario</h1><p class="lede">${filtrati.length} prodott${filtrati.length===1?'o':'i'} trovat${filtrati.length===1?'o':'i'}${invRicerca?' per "'+invRicerca+'"':''}</p></div>
  <div class="inv-toolbar">
   <div class="inv-filtri">
    <div class="inv-search"><input id="inv-input-q" placeholder="Cerca nome, codice, categoria…" value="${invRicerca.replace(/"/g,'&quot;')}" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"></div>
    <select class="inv-select" id="inv-select-cat"><option value="Tutte">Tutte le categorie</option>${CATEGORIE_INV.map(c=>`<option value="${c}" ${invCategoria===c?'selected':''}>${c}</option>`).join('')}</select>
   </div>
   ${isAdmin?'<button class="inv-add" id="inv-btn-nuovo">＋ Nuovo prodotto</button>':''}
  </div>
  ${filtrati.length===0
   ?'<div class="inv-vuoto"><span class="emo">🔍</span>Nessun prodotto trovato'+(invRicerca?' per "'+invRicerca+'"':'')+'.</div>'
   :`<div class="inv-griglia" id="inv-griglia">${filtrati.map(p=>cardProd(p,isAdmin)).join('')}</div>`}
 </div>`;
 const inp=document.getElementById('inv-input-q');
 const griglia=document.getElementById('inv-griglia');
 const lede=el.querySelector('.lede');
 const riRender=()=>{
  const nf=tutti.filter(p=>{
   const matchCat=invRicerca.trim()!==''||invCategoria==='Tutte'||(p.categoria||'').toUpperCase().includes(invCategoria.toUpperCase());
   const matchTxt=ricercaIntelligente(invRicerca,[p.nome,p.codice,p.categoria,p.posizione,p.note]);
   return matchCat&&matchTxt;
  });
  if(lede)lede.textContent=nf.length+' prodott'+(nf.length===1?'o':'i')+' trovat'+(nf.length===1?'o':'i')+(invRicerca?' per "'+invRicerca+'"':'');
  if(griglia){
   griglia.innerHTML=nf.length===0
    ?'<div class="inv-vuoto" style="grid-column:1/-1"><span class="emo">🔍</span>Nessun prodotto trovato.</div>'
    :nf.map(p=>cardProd(p,isAdmin)).join('');
   agganciaBottoniCard(griglia,tutti);
  }
 };
 if(inp)inp.addEventListener('input',e=>{invRicerca=e.target.value;riRender()});
 const sc=document.getElementById('inv-select-cat');
 if(sc)sc.addEventListener('change',e=>{invCategoria=e.target.value;riRender()});
 const bn=document.getElementById('inv-btn-nuovo');
 if(bn)bn.onclick=()=>apriModaleProdotto();
 agganciaBottoniCard(el,tutti);
}

function agganciaBottoniCard(container,tutti){
 container.querySelectorAll('.inv-btn[data-azione]').forEach(b=>{
  b.onclick=()=>{
   const az=b.dataset.azione,prod=tutti.find(x=>x.codice===b.dataset.codice);
   if(!prod)return;
   if(az==='scheda')apriSchedaProd(prod);
   else if(az==='modifica')apriModaleProdotto(prod);
   else if(az==='elimina')confermaElim(prod);
  };
 });
}
/* ============================================================
   COMPRESSIONE FOTO (max 50-70 KB)
   ============================================================ */
function comprimiFoto(file){
 return new Promise((resolve,reject)=>{
  const reader=new FileReader();
  reader.onload=e=>{
   const img=new Image();
   img.onload=()=>{
    let maxLato=700;
    let w=img.width,h=img.height;
    if(w>maxLato||h>maxLato){
     if(w>h){h=Math.round(h*maxLato/w);w=maxLato}
     else{w=Math.round(w*maxLato/h);h=maxLato}
    }
    const canvas=document.createElement('canvas');
    canvas.width=w;canvas.height=h;
    const ctx=canvas.getContext('2d');
    ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);
    ctx.drawImage(img,0,0,w,h);
    const qualita=[0.65,0.55,0.48,0.42,0.35,0.28];
    let idx=0;
    let dataUrl=canvas.toDataURL('image/jpeg',qualita[idx]);
    while(dataUrl.length/1024>70&&idx<qualita.length-1){
     idx++;
     dataUrl=canvas.toDataURL('image/jpeg',qualita[idx]);
    }
    let fattore=0.85;
    while(dataUrl.length/1024>70&&fattore>0.3){
     w=Math.floor(w*fattore);h=Math.floor(h*fattore);
     canvas.width=w;canvas.height=h;
     ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);
     ctx.drawImage(img,0,0,w,h);
     dataUrl=canvas.toDataURL('image/jpeg',0.4);
     fattore-=0.1;
    }
    resolve({dataUrl,size:Math.round(dataUrl.length/1024),w,h});
   };
   img.onerror=reject;
   img.src=e.target.result;
  };
  reader.onerror=reject;
  reader.readAsDataURL(file);
 });
}
/* ============================================================
   MODALE NUOVO / MODIFICA PRODOTTO
   ============================================================ */
function apriModaleProdotto(prod){
 const modifica=!!prod;
 const p=prod||{codice:'',nome:'',categoria:'',quantita:0,posizione:'',prezzo:0,note:'',foto:'',scheda:{materiale:'',colore:'',dimensione:'',note:''}};
 const scheda=p.scheda||{materiale:'',colore:'',dimensione:'',note:''};
 const catsSel=(p.categoria||'').split(',').map(s=>s.trim()).filter(Boolean);
 const hasFoto=!!p.foto;
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent=modifica?'Modifica prodotto':'Nuovo prodotto';
 document.getElementById('d-titolo').textContent=modifica?p.nome:'Aggiungi al catalogo';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Nome prodotto <span style="color:#dc2626">*</span></label><input id="pr-nome" value="${(p.nome||'').replace(/"/g,'&quot;')}" placeholder="Es. Piatto Gourmet Jasmin"></div>
  <div class="campo"><label>Codice <span style="color:#dc2626">*</span></label><input id="pr-codice" value="${(p.codice||'').replace(/"/g,'&quot;')}" placeholder="Es. PGF-028" ${modifica?'readonly':''}></div>
  <div class="campo"><label>Categorie (seleziona almeno una) <span style="color:#dc2626">*</span></label>
   <div class="cat-grid">
    ${CATEGORIE_INV.map(c=>`<label class="cat-item ${catsSel.includes(c)?'on':''}"><input type="checkbox" class="pr-cat-check" value="${c}" ${catsSel.includes(c)?'checked':''}><span>${c}</span></label>`).join('')}
   </div>
  </div>
  <div class="campo-3">
   <div class="campo"><label>Quantità</label><input id="pr-qta" type="number" min="0" value="${p.quantita||0}"></div>
   <div class="campo"><label>Posizione</label><input id="pr-pos" value="${(p.posizione||'').replace(/"/g,'&quot;')}" placeholder="Es. A1"></div>
   <div class="campo"><label>Prezzo (€)</label><input id="pr-prezzo" type="number" min="0" step="0.01" value="${(p.prezzo||0).toFixed(2)}"></div>
  </div>
  <div class="campo"><label>Note (opzionale)</label><textarea id="pr-note" placeholder="Note visibili nella scheda prodotto...">${(p.note||'').replace(/</g,'&lt;')}</textarea></div>
  <div class="divisore-modale">📸 Foto prodotto</div>
  <div class="campo"><label style="text-transform:none;font-weight:600;color:#94a3b8;letter-spacing:0">Compressa automaticamente a max 70 KB</label><input type="file" id="pr-foto" accept="image/*"><div id="pr-foto-preview">${hasFoto?`<div class="foto-preview-box"><img loading="lazy" src="${p.foto}"><div class="info"><strong>✅ Foto attuale</strong><span>Già ottimizzata</span></div></div>`:''}</div></div>
  <div class="divisore-modale">📋 Scheda tecnica</div>
  <div class="campo-2"><div class="campo"><label>Materiale</label><input id="pr-mat" value="${(scheda.materiale||'').replace(/"/g,'&quot;')}"></div><div class="campo"><label>Colore</label><input id="pr-col" value="${(scheda.colore||'').replace(/"/g,'&quot;')}"></div></div>
  <div class="campo"><label>Dimensione</label><input id="pr-dim" value="${(scheda.dimensione||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo"><label>Note tecniche</label><textarea id="pr-nt">${(scheda.note||'').replace(/</g,'&lt;')}</textarea></div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="pr-salva">💾 ${modifica?'Salva':'Aggiungi'}</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.querySelectorAll('.pr-cat-check').forEach(cb=>{
  cb.addEventListener('change',()=>{cb.closest('label').classList.toggle('on',cb.checked)});
 });
 let nuovaFoto=p.foto||'';
 const fi=document.getElementById('pr-foto');
 fi.addEventListener('change',async e=>{
  const f=e.target.files[0];if(!f)return;
  const prev=document.getElementById('pr-foto-preview');
  prev.innerHTML='<div style="color:#6b778c;font-size:.75rem;padding:12px;background:#f3f8ff;border:1.5px solid #d7e7fa;border-radius:12px;margin-top:10px;text-align:center">🔄 Compressione...</div>';
  try{
   const r=await comprimiFoto(f);
   nuovaFoto=r.dataUrl;
   prev.innerHTML=`<div class="foto-preview-box"><img src="${r.dataUrl}"><div class="info"><strong>✅ Foto pronta</strong><span>${r.w}×${r.h}px · ${r.size} KB</span></div></div>`;
  }catch(err){
   prev.innerHTML='<div style="color:#b91c1c;font-size:.75rem;padding:12px;background:#fef2f2;border-radius:12px;margin-top:10px">❌ Errore</div>';
  }
 });
 document.getElementById('pr-salva').onclick=async()=>await salvaProdotto(modifica,p,nuovaFoto);
}
async function salvaProdotto(modifica,p,nuovaFoto){
 const nome=document.getElementById('pr-nome').value.trim();
 const codice=document.getElementById('pr-codice').value.trim();
 if(!nome||!codice){alert('Nome e Codice sono obbligatori.');return}
 const categorie=Array.from(document.querySelectorAll('.pr-cat-check:checked')).map(c=>c.value);
 if(categorie.length===0){alert('Seleziona almeno una categoria.');return}
 let foto=nuovaFoto||p.foto||'';
 let foto_path=p.foto_path||'';
 if(foto && foto.indexOf('data:')===0 && window.ergoSupabaseUpload && window.ergoDataUrlToFile){
  try{
   const file=window.ergoDataUrlToFile(foto,(codice||'prodotto')+'.jpg');
   const uploaded=await window.ergoSupabaseUpload(file,'immagini_prodotti');
   if(uploaded){foto=uploaded.url;foto_path=uploaded.path;}
  }catch(e){console.warn('Upload foto rinviato: uso temporaneamente la foto locale',e);}
 }
 const nuovo={
  id:p.id,
  codice,nome,categoria:categorie.join(', '),
  quantita:parseInt(document.getElementById('pr-qta').value)||0,
  posizione:document.getElementById('pr-pos').value.trim(),
  prezzo:parseFloat(document.getElementById('pr-prezzo').value)||0,
  note:document.getElementById('pr-note').value,
  foto,foto_path,
  scheda:{
   materiale:document.getElementById('pr-mat').value.trim(),
   colore:document.getElementById('pr-col').value.trim(),
   dimensione:document.getElementById('pr-dim').value.trim(),
   note:document.getElementById('pr-nt').value
  }
 };
 let salvati=[];
 try{salvati=JSON.parse(localStorage.getItem('ergo_prodotti'))||[]}catch(e){}
 if(modifica){
  const iB=PRODOTTI.findIndex(x=>x.codice===p.codice);
  if(iB>=0)PRODOTTI[iB]=nuovo;
  const iS=salvati.findIndex(x=>x.codice===p.codice);
  if(iS>=0)salvati[iS]=nuovo;else if(iB<0)salvati.push(nuovo);
 }else{
  if(PRODOTTI.find(x=>x.codice===codice)||salvati.find(x=>x.codice===codice)){
   alert('Esiste già un prodotto con questo codice.');return;
  }
  salvati.push(nuovo);
 }
 localStorage.setItem('ergo_prodotti',JSON.stringify(salvati));
 chiudiDrawer();
 alert('✅ Prodotto '+(modifica?'aggiornato':'creato')+'!');
 const pc=document.getElementById('pc');if(pc&&view==='inventario')inv(pc);
}

function apriSchedaProd(p){
 const scheda=p.scheda||{};
 const hasFoto=!!p.foto;
 const fotoHtml=hasFoto?`<img loading="lazy" src="${p.foto}" style="width:100%;height:100%;object-fit:cover">`:`<div style="font-size:4rem;opacity:.4">📦</div>`;
 let righe='';
 [['Materiale',scheda.materiale],['Colore',scheda.colore],['Dimensione',scheda.dimensione]].forEach(([k,v])=>{
  if(v&&v.trim())righe+=`<div style="display:flex;justify-content:space-between;gap:12px;padding:7px 0;border-bottom:1px dashed #c9dcf0;font-size:.8rem"><span style="color:#6b778c;font-weight:600">${k}</span><span style="color:#344054;font-weight:600;text-align:right">${v}</span></div>`;
 });
 const tech=righe?`<div style="background:#f3f8ff;border:1px solid #d7e7fa;border-radius:12px;padding:14px;margin-top:12px"><div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#083278;font-weight:800;margin-bottom:10px">Scheda tecnica</div>${righe}</div>`:'';
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Scheda prodotto';
 document.getElementById('d-titolo').textContent=p.nome;
 document.getElementById('d-body').innerHTML=`
  <div style="width:100%;aspect-ratio:1;background:linear-gradient(145deg,#eef4fa,#f8fafc);border-radius:14px;display:grid;place-items:center;overflow:hidden;color:#9ab1c9;margin-bottom:14px">${fotoHtml}</div>
  <div style="font-size:.75rem;color:#98a2b3;letter-spacing:.06em;margin-bottom:12px">COD. ${p.codice}</div>
  <div class="meta-grid"><div><small>Quantità</small><strong>📦 ${p.quantita||0}</strong></div><div><small>Categoria</small><strong>${p.categoria||'—'}</strong></div><div><small>Posizione</small><strong>📍 ${p.posizione||'—'}</strong></div>${user.ruolo==='Amministratore'?`<div><small>Prezzo</small><strong>€ ${(p.prezzo||0).toFixed(2)}</strong></div>`:''}</div>
  ${tech}
  <div style="background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center;margin-top:14px">
   <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#083278;font-weight:800;margin-bottom:10px">QR Code</div>
   <canvas id="qr-canvas" width="180" height="180" style="display:block;margin:0 auto;border-radius:8px;border:1px solid var(--line)"></canvas>
   <div style="margin-top:12px"><button class="inv-btn primario" id="qr-scarica" style="padding:9px 14px">⬇️ Scarica QR</button></div>
  </div>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 setTimeout(()=>{
  const c=document.getElementById('qr-canvas');
  if(c){
   const url=location.origin+location.pathname+'?codice='+encodeURIComponent(p.codice||'');
   const img=new Image();img.crossOrigin='anonymous';
   img.onload=()=>{const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,180,180);x.drawImage(img,0,0,180,180)};
   img.onerror=()=>{const x=c.getContext('2d');x.fillStyle='#f8fafc';x.fillRect(0,0,180,180);x.fillStyle='#98a2b3';x.font='12px sans-serif';x.textAlign='center';x.fillText('QR non disponibile',90,84);x.fillText('(richiede internet)',90,102)};
   img.src='https://api.qrserver.com/v1/create-qr-code/?size=180x180&data='+encodeURIComponent(url);
  }
  const bd=document.getElementById('qr-scarica');
  if(bd)bd.onclick=()=>{const c2=document.getElementById('qr-canvas');if(!c2)return;const a=document.createElement('a');a.download='QR_'+(p.codice||'prodotto')+'.png';a.href=c2.toDataURL('image/png');a.click()};
 },100);
}

function confermaElim(obj){
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Conferma eliminazione';
 document.getElementById('d-titolo').textContent='🗑️ Elimina prodotto';
 document.getElementById('d-body').innerHTML=`<div class="note-box" style="background:#fef2f2;border-color:#fecaca;color:#991b1b"><strong>${obj.nome}</strong><br><span style="font-size:.78rem;color:#b91c1c">Azione irreversibile</span></div><p style="color:#6b778c;font-size:.82rem;margin-top:14px">Richiede <b>due conferme</b>.</p>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="d-conf" style="background:#dc2626">🗑️ CONFERMA</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('d-conf').onclick=()=>{
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_prodotti'))||[]}catch(e){}
  const iB=PRODOTTI.findIndex(x=>x.codice===obj.codice);
  if(iB>=0)PRODOTTI.splice(iB,1);
  const iS=salvati.findIndex(x=>x.codice===obj.codice);
  if(iS>=0){salvati.splice(iS,1);localStorage.setItem('ergo_prodotti',JSON.stringify(salvati))}
  chiudiDrawer();
  const pc=document.getElementById('pc');if(pc&&view==='inventario')inv(pc);
 };
}
/* ============================================================
   COLORI CATEGORIE
   ============================================================ */
const COLORI_CATEGORIE={
 'TAVOLI':'#0056b3','SEDIE':'#2f6fb0','CALTAGIRONE':'#b45309',
 'COMPLEMENTI VARI':'#7c3aed','PIATTI E SOTTOPIATTI':'#0891b2',
 'BICCHIERI':'#0d9488','CUCINA':'#dc2626','ARREDO':'#6d28d9',
 'TOVAGLIATO':'#059669','ARGENTERIA':'#475569','POSATERIA':'#7c2d12',
 'VASSOI':'#0891b2','LUCI E CANDELABRI':'#d97706'
};

function coloreCategoria(cat){
 if(!cat)return '#4b5563';
 const c=cat.toUpperCase().trim();
 if(COLORI_CATEGORIE[c])return COLORI_CATEGORIE[c];
 let hash=0;
 for(let i=0;i<c.length;i++)hash=c.charCodeAt(i)+((hash<<5)-hash);
 const palette=['#0056b3','#0891b2','#7c3aed','#dc2626','#059669','#d97706','#b45309','#0d9488','#be185d','#4338ca'];
 return palette[Math.abs(hash)%palette.length];
}

/* ============================================================
   LISTA ATTREZZATURE
   ============================================================ */
let listaRicerca='',listaCategoria='Tutte';

function lista(el){
 const isAdmin=user.ruolo==='Amministratore';
 if(!isAdmin){
  el.innerHTML='<div class="page"><p class="eyebrow">Sezione</p><h1 class="title">Accesso negato</h1></div>';
  return;
 }
 let salvati=[];
 try{salvati=JSON.parse(localStorage.getItem('ergo_prodotti'))||[]}catch(e){}
 const tutti=tuttiProds(salvati);
 const filtrati=tutti.filter(p=>{
  const matchCat=listaCategoria==='Tutte'||(p.categoria||'').toUpperCase().includes(listaCategoria.toUpperCase());
  const matchTxt=ricercaIntelligente(listaRicerca,[p.nome,p.codice,p.categoria,p.posizione]);
  return matchCat&&matchTxt;
 });
 el.innerHTML=`<div class="page">
  <div style="margin-bottom:20px">
   <p class="eyebrow">Preparazione evento</p>
   <h1 class="title">Lista Attrezzature</h1>
   <p class="lede">Seleziona i prodotti dal catalogo e componi la lista da inviare all'evento.</p>
  </div>
  <div class="lista-layout">
   <div class="lista-pannello">
    <div class="lista-titolo">🔍 Catalogo prodotti</div>
    <div class="lista-search">
     <input id="lista-input-q" placeholder="Cerca per nome o codice…" value="${listaRicerca.replace(/"/g,'&quot;')}">
     <select id="lista-select-cat"><option value="Tutte">Tutte le categorie</option>${CATEGORIE_INV.map(c=>`<option value="${c}" ${listaCategoria===c?'selected':''}>${c}</option>`).join('')}</select>
    </div>
    <div class="lista-prodotti" id="lista-prodotti">
     ${filtrati.length===0
      ?'<div style="text-align:center;padding:30px;color:#94a3b8;font-size:.8rem">Nessun prodotto trovato</div>'
      :filtrati.map(p=>rigaProdottoLista(p)).join('')}
    </div>
   </div>
   <div class="lista-pannello">
    <div class="lista-titolo">🛒 Lista attrezzature <span class="count" id="lista-count">${listaAttrezzature.length} articoli</span></div>
    <div class="lista-carrello" id="lista-carrello">${renderCarrello()}</div>
    <div class="carrello-azioni">
     <button class="btn-invia" id="lista-invia" ${listaAttrezzature.length===0?'disabled':''}>📤 Invia a evento</button>
     <button class="btn-svuota" id="lista-svuota" ${listaAttrezzature.length===0?'disabled':''}>🧹 Svuota</button>
    </div>
   </div>
  </div>
 </div>`;
 const inp=document.getElementById('lista-input-q');
 inp.addEventListener('input',e=>{
  listaRicerca=e.target.value;
  const nf=tutti.filter(p=>{
   const matchCat=listaCategoria==='Tutte'||(p.categoria||'').toUpperCase().includes(listaCategoria.toUpperCase());
   const matchTxt=ricercaIntelligente(listaRicerca,[p.nome,p.codice,p.categoria,p.posizione]);
   return matchCat&&matchTxt;
  });
  const cont=document.getElementById('lista-prodotti');
  if(cont)cont.innerHTML=nf.length===0
   ?'<div style="text-align:center;padding:30px;color:#94a3b8;font-size:.8rem">Nessun prodotto trovato</div>'
   :nf.map(p=>rigaProdottoLista(p)).join('');
  agganciaAggiungi(tutti);
 });
 document.getElementById('lista-select-cat').addEventListener('change',e=>{
  listaCategoria=e.target.value;
  lista(el);
 });
 agganciaAggiungi(tutti);
 document.getElementById('lista-svuota').onclick=()=>{
  if(!confirm('Vuoi svuotare tutta la lista?'))return;
  listaAttrezzature=[];
  lista(el);
 };
 document.getElementById('lista-invia').onclick=()=>apriModaleInvioLista();
}
function rigaProdottoLista(p){
 const maxQta=p.quantita||0;
 const colore=coloreCategoria(p.categoria);
 return `<div class="lista-prodotto" style="border-left:4px solid ${colore}">
  <div class="info">
   <strong>${p.nome||''}</strong>
   <small><span style="background:${colore};color:#fff;padding:2px 7px;border-radius:6px;font-weight:800;font-size:.6rem;letter-spacing:.04em">${p.categoria||''}</span> · Disp: <b>${maxQta}</b></small>
  </div>
  <div class="qta-box">
   <input type="number" min="1" max="${maxQta}" value="1" id="qta-${p.codice}" ${maxQta<=0?'disabled':''}>
   <button class="aggiungi" data-codice="${p.codice}" ${maxQta<=0?'disabled':''}>➕ Aggiungi</button>
  </div>
 </div>`;
}

function agganciaAggiungi(tutti){
 document.querySelectorAll('.aggiungi[data-codice]').forEach(b=>{
  b.onclick=()=>{
   const codice=b.dataset.codice;
   const prod=tutti.find(x=>x.codice===codice);
   if(!prod)return;
   const inp=document.getElementById('qta-'+codice);
   const qta=parseInt(inp.value)||1;
   const disponibile=prod.quantita||0;
   if(qta<=0){alert('La quantità deve essere almeno 1.');return}
   if(qta>disponibile){alert('Quantità non disponibile.\n\nMassimo: '+disponibile+' pezzi.');inp.value=disponibile;return}
   const esistente=listaAttrezzature.find(x=>x.codice===codice);
   if(esistente){
    const nuovaQta=esistente.quantitaSelezionata+qta;
    if(nuovaQta>disponibile){
     alert('Hai già '+esistente.quantitaSelezionata+' pezzi in lista.\nPuoi aggiungerne al massimo '+(disponibile-esistente.quantitaSelezionata)+'.');
     return;
    }
    esistente.quantitaSelezionata=nuovaQta;
   }else{
    listaAttrezzature.push({...prod,quantitaSelezionata:qta});
   }
   lista(document.getElementById('pc'));
  };
 });
}

function renderCarrello(){
 if(listaAttrezzature.length===0){
  return '<div class="carrello-vuoto"><span class="emo">📋</span>La lista è vuota.<br>Aggiungi prodotti dal catalogo a sinistra.</div>';
 }
 const gruppi={};
 listaAttrezzature.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });
 let html='';
 Object.keys(gruppi).sort().forEach(cat=>{
  const items=gruppi[cat];
  const colore=coloreCategoria(cat);
  html+=`<div class="cat-header" style="background:${colore}">${cat}<span class="badge">${items.length}</span></div>`;
  items.forEach(item=>{
   html+=`<div class="carrello-item" style="border-left:4px solid ${colore}">
    <div class="info">
     <strong>${item.nome||''}</strong>
     <small>Cod. ${item.codice} · Max ${item.quantita}</small>
    </div>
    <input type="number" min="1" max="${item.quantita}" value="${item.quantitaSelezionata}" data-codice="${item.codice}" class="carrello-qta">
    <button class="rimuovi" data-codice="${item.codice}">🗑️</button>
   </div>`;
  });
 });
 return html;
}
document.addEventListener('input',e=>{
 if(e.target.classList&&e.target.classList.contains('carrello-qta')){
  const codice=e.target.dataset.codice;
  const item=listaAttrezzature.find(x=>x.codice===codice);
  if(!item)return;
  let v=parseInt(e.target.value)||1;
  if(v<1)v=1;
  if(v>item.quantita){v=item.quantita;e.target.value=v;alert('Massimo disponibile: '+item.quantita)}
  item.quantitaSelezionata=v;
  const c=document.getElementById('lista-count');
  if(c)c.textContent=listaAttrezzature.length+' articoli';
 }
});

document.addEventListener('click',e=>{
 if(e.target.classList&&e.target.classList.contains('rimuovi')){
  const codice=e.target.dataset.codice;
  listaAttrezzature=listaAttrezzature.filter(x=>x.codice!==codice);
  lista(document.getElementById('pc'));
 }
});

/* ============================================================
   INVIO LISTA A EVENTO
   ============================================================ */
function apriModaleInvioLista(){
 if(listaAttrezzature.length===0){alert('La lista è vuota.');return}
 const eventiDisponibili=EVENTI.slice().sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));
 if(eventiDisponibili.length===0){alert('Non ci sono eventi disponibili. Crea prima un evento.');return}
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Invia lista';
 document.getElementById('d-titolo').textContent='📤 Invia a evento';
 document.getElementById('d-body').innerHTML=`
  <p style="font-size:.85rem;color:#6b778c;margin-bottom:14px">Scegli l'evento a cui inviare questa lista attrezzature (<b>${listaAttrezzature.length} articoli</b>).</p>
  <div class="campo"><label>Evento di destinazione</label>
   <select id="invio-evento" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff">
    ${eventiDisponibili.map((e,i)=>{
     const d2=new Date(e.inizio).toLocaleDateString('it-IT',{day:'2-digit',month:'short',year:'numeric'});
     return `<option value="${e.id}" ${i===0?'selected':''}>${e.titolo} · ${d2}</option>`;
    }).join('')}
   </select>
  </div>
  <div style="background:#f0f6ff;border:1px solid #d7e7fa;border-radius:10px;padding:12px;font-size:.78rem;color:#4b5563;line-height:1.5;margin-top:8px">
   📎 La lista verrà salvata come allegato alla sezione <b>Note per tutti</b> dell'evento scelto.
  </div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="invio-conferma">📤 Invia</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('invio-conferma').onclick=eseguiInvioLista;
}

function eseguiInvioLista(){
 const idEv=document.getElementById('invio-evento').value;
 const ev=EVENTI.find(e=>e.id===idEv);
 if(!ev){alert('Evento non trovato.');return}
 const gruppi={};
 listaAttrezzature.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });
 let testo='LISTA ATTREZZATURE PER EVENTO: '+ev.titolo+'\n';
 testo+='Data: '+new Date(ev.inizio).toLocaleDateString('it-IT')+'\n';
 testo+='Location: '+(ev.location||'—')+'\n\n';
 Object.keys(gruppi).sort().forEach(cat=>{
  testo+='--- '+cat+' ---\n';
  gruppi[cat].forEach(i=>{
   testo+='• '+i.nome+' (ID: '+i.codice+') | Q.tà: '+i.quantitaSelezionata+'\n';
  });
  testo+='\n';
 });
 if(!ev.allegatiTutti)ev.allegatiTutti=[];
 ev.allegatiTutti.push({
  nome:'Lista_Attrezzature_'+ev.titolo.replace(/\s+/g,'_')+'.txt',
  mime:'text/plain',
  size:testo.length,
  data:'data:text/plain;base64,'+btoa(unescape(encodeURIComponent(testo)))
 });
 let salvati=[];
 try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
 const idx=salvati.findIndex(e=>e.id===ev.id);
 if(idx>=0)salvati[idx]=ev;
 localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
 const nuovo={
  id:'nf-'+Date.now()+'-lista',
  tipo:'allegato',reparto:'tutti',
  titolo:'Lista attrezzature inviata: '+ev.titolo,
  sottotitolo:listaAttrezzature.length+' articoli · da '+user.nome,
  quando:new Date().toISOString(),
  da:user.nome+' ('+user.ruolo+')',
  dettagli:{evento:ev.titolo,data:new Date(ev.inizio).toLocaleDateString('it-IT'),location:ev.location,allegato:'Lista attrezzature ('+listaAttrezzature.length+' articoli)'}
 };
 NOTIFICHE.unshift(nuovo);
 let salvateN=[];
 try{salvateN=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
 salvateN.unshift(nuovo);
 localStorage.setItem('ergo_notifiche',JSON.stringify(salvateN.slice(0,200)));
 chiudiDrawer();
 alert('✅ Lista inviata all\'evento "'+ev.titolo+'"!');
 listaAttrezzature=[];
 lista(document.getElementById('pc'));
}
/* ============================================================
   RUOLI
   ============================================================ */
function coloreRuolo(r){
 const m={
  'Amministratore':{bg:'#fef3c7',fg:'#92400e'},
  'Wedding':{bg:'#fce7f3',fg:'#9d174d'},
  'Cucina':{bg:'#ffedd5',fg:'#9a3412'},
  'Sala':{bg:'#d1fae5',fg:'#065f46'},
  'Magazzino':{bg:'#ede9fe',fg:'#5b21b6'},
  'Magazzino2':{bg:'#dbeafe',fg:'#1e40af'}
 };
 return m[r]||{bg:'#f1f5f9',fg:'#475569'};
}

function ruoli(el){
 if(user.ruolo!=='Amministratore'){
  el.innerHTML='<div class="page"><p class="eyebrow">Sezione</p><h1 class="title">Accesso negato</h1></div>';
  return;
 }
 const listaUtenti=Object.keys(UTENTI).map(k=>({username:k,...UTENTI[k]}));
 el.innerHTML=`<div class="page">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:24px;flex-wrap:wrap">
   <div><p class="eyebrow">Amministrazione</p><h1 class="title">Sistema Ruoli</h1><p class="lede">${listaUtenti.length} utenti autorizzati.</p></div>
   <button class="inv-add" id="ruoli-nuovo">＋ Nuovo utente</button>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px">
   ${listaUtenti.map(u=>{
    const isAdm=u.username==='admin';
    const col=coloreRuolo(u.ruolo);
    const ini=(u.nome||u.username).split(' ').map(x=>x[0]).slice(0,2).join('').toUpperCase();
    return `<div class="ruolo-card">
     <div class="ruolo-head">
      <div class="ruolo-avatar" style="background:${col.bg};color:${col.fg}">${ini}</div>
      <div style="flex:1;min-width:0">
       <div class="ruolo-nome">${u.nome||u.username}</div>
       <div class="ruolo-username">@${u.username}</div>
      </div>
      <span class="ruolo-badge" style="background:${col.bg};color:${col.fg}">${u.ruolo}</span>
     </div>
     <div class="ruolo-info">
      <div class="ruolo-riga"><span>📧 Email</span><strong>${u.email||'—'}</strong></div>
      <div class="ruolo-riga"><span>🔑 Password</span><strong>•••••••••</strong></div>
     </div>
     <div class="ruolo-azioni">
      <button class="ruolo-btn" data-azione="modifica" data-user="${u.username}">✏️ Modifica</button>
      ${isAdm?'<span class="ruolo-protetto">🔒 Protetto</span>':'<button class="ruolo-btn pericolo" data-azione="elimina" data-user="'+u.username+'">🗑️</button>'}
     </div>
    </div>`;
   }).join('')}
  </div>
 </div>`;
 document.getElementById('ruoli-nuovo').onclick=()=>modaleUtente(null);
 el.querySelectorAll('.ruolo-btn[data-azione]').forEach(b=>{
  b.onclick=()=>{
   const az=b.dataset.azione,usr=b.dataset.user;
   if(az==='modifica')modaleUtente(usr);
   else if(az==='elimina')eliminaUtente(usr);
  };
 });
}
function modaleUtente(username){
 const modifica=!!username;
 const u=modifica?UTENTI[username]:{password:'',ruolo:'Sala',nome:'',email:''};
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent=modifica?'Modifica utente':'Nuovo utente';
 document.getElementById('d-titolo').textContent=modifica?('👤 '+username):'👤 Aggiungi utente';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Username <span style="color:#dc2626">*</span></label><input id="usr-name" value="${modifica?username:''}" ${modifica?'readonly':''}></div>
  <div class="campo"><label>Nome / Reparto</label><input id="usr-nome" value="${(u.nome||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo"><label>Email</label><input id="usr-email" type="email" value="${(u.email||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo"><label>Ruolo <span style="color:#dc2626">*</span></label>
   <select id="usr-ruolo" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff">
    ${['Amministratore','Wedding','Cucina','Sala','Magazzino','Magazzino2'].map(r=>`<option value="${r}" ${u.ruolo===r?'selected':''}>${r}</option>`).join('')}
   </select>
  </div>
  <div class="divisore-modale">🔑 Password</div>
  <div class="campo"><label>${modifica?'Nuova password (lascia vuoto per non cambiare)':'Password *'}</label><input id="usr-pass" type="password" value=""></div>
  <div class="campo"><label>Conferma password</label><input id="usr-pass2" type="password" value=""></div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="usr-salva">💾 Salva</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('usr-salva').onclick=()=>{
  const username2=document.getElementById('usr-name').value.trim();
  const nome=document.getElementById('usr-nome').value.trim();
  const email=document.getElementById('usr-email').value.trim();
  const ruolo=document.getElementById('usr-ruolo').value;
  const p1=document.getElementById('usr-pass').value;
  const p2=document.getElementById('usr-pass2').value;
  if(!username2){alert('Username obbligatorio.');return}
  if(!modifica&&!p1){alert('Password obbligatoria.');return}
  if((p1||p2)&&p1!==p2){alert('Le password non coincidono.');return}
  if(!modifica&&UTENTI[username2]){alert('Username esistente.');return}
  if(modifica){
   const u2=UTENTI[username];
   u2.nome=nome||username;
   u2.email=email;
   u2.ruolo=ruolo;
   if(p1)u2.password=p1;
  }else{
   UTENTI[username2]={password:p1,ruolo,nome:nome||username2,email,iniziali:(nome||username2).split(' ').map(x=>x[0]).slice(0,2).join('').toUpperCase()};
  }
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_utenti'))||[]}catch(e){}
  const nuovo={username:modifica?username:username2,password:p1||(modifica?UTENTI[username].password:''),ruolo,nome:nome||username2,email};
  const idx=salvati.findIndex(x=>x.username===nuovo.username);
  if(idx>=0)salvati[idx]=nuovo;else salvati.push(nuovo);
  localStorage.setItem('ergo_utenti',JSON.stringify(salvati));
  chiudiDrawer();
  alert('✅ Utente '+(modifica?'aggiornato':'creato')+'!');
  ruoli(document.getElementById('pc'));
 };
}

function eliminaUtente(username){
 if(username==='admin'){alert('Admin non eliminabile.');return}
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Conferma';
 document.getElementById('d-titolo').textContent='🗑️ Elimina utente';
 document.getElementById('d-body').innerHTML=`<div class="note-box" style="background:#fef2f2;border-color:#fecaca;color:#991b1b"><strong>@${username}</strong><br><span style="font-size:.78rem;color:#b91c1c">Azione irreversibile</span></div><p style="color:#6b778c;font-size:.82rem;margin-top:14px">Richiede <b>due conferme</b>.</p>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="conf-del" style="background:#dc2626">🗑️ CONFERMA</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('conf-del').onclick=()=>{
  delete UTENTI[username];
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_utenti'))||[]}catch(e){}
  salvati=salvati.filter(x=>x.username!==username);
  localStorage.setItem('ergo_utenti',JSON.stringify(salvati));
  chiudiDrawer();
  alert('✅ Utente eliminato.');
  ruoli(document.getElementById('pc'));
 };
}
/* ============================================================
   CARICAMENTO DA LOCALSTORAGE
   ============================================================ */
function caricaDaLocalStorage(){
 try{
  const evLS=JSON.parse(localStorage.getItem('ergo_eventi'))||[];
  evLS.forEach(e=>{if(!EVENTI.find(x=>x.id===e.id))EVENTI.push(e)});
 }catch(e){}
 try{
  const nlLS=JSON.parse(localStorage.getItem('ergo_noleggi'))||[];
  nlLS.forEach(n=>{if(!NOLEGGI.find(x=>x.id===n.id))NOLEGGI.push(n)});
 }catch(e){}
 try{
  const nfLS=JSON.parse(localStorage.getItem('ergo_notifiche'))||[];
  nfLS.forEach(n=>{if(!NOTIFICHE.find(x=>x.id===n.id))NOTIFICHE.unshift(n)});
 }catch(e){}
 try{
  const usLS=JSON.parse(localStorage.getItem('ergo_utenti'))||[];
  usLS.forEach(u=>{
   if(!UTENTI[u.username]){
    UTENTI[u.username]={
     password:u.password,ruolo:u.ruolo,nome:u.nome,email:u.email,
     iniziali:(u.nome||u.username).split(' ').map(x=>x[0]).slice(0,2).join('').toUpperCase()
    };
   }
  });
 }catch(e){}
}

/* ============================================================
   QR PUBBLICO (accesso senza login)
   ============================================================ */
function apriQRPubblico(codice){
 let salvati=[];
 try{salvati=JSON.parse(localStorage.getItem('ergo_prodotti'))||[]}catch(e){}
 const tutti=tuttiProds(salvati);
 const prod=tutti.find(p=>p.codice===codice);
 R.innerHTML='';
 if(!prod){
  R.innerHTML='<div class="qr-page"><div class="qr-errore"><div class="emo">🔍</div><h1>Prodotto non trovato</h1><p>Il codice "<b>'+codice+'</b>" non corrisponde a nessun prodotto in catalogo.</p></div></div>';
  return;
 }
 const scheda=prod.scheda||{};
 const hasFoto=!!prod.foto;
 const fotoHtml=hasFoto?'<img src="'+prod.foto+'">':'<div style="font-size:4rem;opacity:.4">📦</div>';
 let techHtml='';
 [['Materiale',scheda.materiale],['Colore',scheda.colore],['Dimensione',scheda.dimensione]].forEach(([k,v])=>{
  if(v&&v.trim())techHtml+='<div class="qr-tech-item"><span>'+k+'</span><b>'+v+'</b></div>';
 });
 if(scheda.note&&scheda.note.trim())techHtml+='<div class="qr-tech-item"><span>Note tecniche</span><b>'+scheda.note+'</b></div>';
 R.innerHTML='<div class="qr-page"><div class="qr-card">'
  +'<div><div class="qr-foto">'+fotoHtml+'</div></div>'
  +'<div class="qr-info">'
  +'<div class="qr-kicker">Scheda prodotto</div>'
  +'<div class="qr-nome">'+(prod.nome||'')+'</div>'
  +'<div class="qr-codice">COD. '+(prod.codice||'')+'</div>'
  +'<div class="qr-qta"><small>Quantità disponibile</small><strong>'+(prod.quantita||0)+'</strong></div>'
  +(prod.note?'<div class="qr-note">📝 '+prod.note+'</div>':'')
  +(techHtml?'<div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#8b96a9;font-weight:800;margin:14px 0 6px">Scheda tecnica</div><div class="qr-tech-grid">'+techHtml+'</div>':'')
  +'<div style="margin-top:20px;padding-top:14px;border-top:1px solid var(--line);font-size:.68rem;color:#94a3b8;text-align:center">Ergo &amp; Scardaci · Gestionale</div>'
  +'</div></div></div>';
}

/* ============================================================
   AVVIO
   ============================================================ */
caricaDaLocalStorage();

const _qp=new URLSearchParams(location.search);
const _codiceQR=_qp.get('codice');
if(_codiceQR){apriQRPubblico(_codiceQR);}
else{login();}
  /* === FIX CAMPI OSPITI/BAMBINI/STAFF === */
function apriModaleEvento(){
 const oggi=new Date().toISOString().slice(0,10);
 const isAdmin=user.ruolo==='Amministratore';
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Nuovo evento';
 document.getElementById('d-titolo').textContent='📅 Crea Evento Catering';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Nome evento / Cliente <span style="color:#dc2626">*</span></label><input id="ev-nome" placeholder="Es. Matrimonio Bianchi"></div>
  <div class="campo-2">
   <div class="campo"><label>Data</label><input id="ev-data" type="date" value="${oggi}"></div>
   <div class="campo"><label>Orario</label><input id="ev-ora" type="time" value="18:30"></div>
  </div>
  <div class="campo"><label>Location</label><input id="ev-loc" placeholder="Es. Villa San Giorgio"></div>
  <div class="divisore-modale">👥 Persone</div>
  <div class="campo-3">
   <div class="campo"><label>Ospiti</label><input id="ev-osp" type="number" min="0" value="0" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
   <div class="campo"><label>Bambini</label><input id="ev-bam" type="number" min="0" value="0" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
   <div class="campo"><label>Staff</label><input id="ev-stf" type="number" min="0" value="0" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
  </div>
  <div class="divisore-modale">📝 Note per tutti</div>
  <div class="campo"><textarea id="ev-n-tutti" style="background:#eef2ff;border-color:#c7d2fe"></textarea><input type="file" id="ev-f-tutti" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">🍽️ Note per la sala</div>
  <div class="campo"><textarea id="ev-n-sala" style="background:#f0fdf4;border-color:#bbf7d0"></textarea><input type="file" id="ev-f-sala" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">👨‍🍳 Note per la cucina</div>
  <div class="campo"><textarea id="ev-n-cucina" style="background:#fff7ed;border-color:#fed7aa"></textarea><input type="file" id="ev-f-cucina" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">📦 Note per il magazzino</div>
  <div class="campo"><textarea id="ev-n-mag" style="background:#f5f3ff;border-color:#ddd6fe"></textarea><input type="file" id="ev-f-mag" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  ${isAdmin?`<div class="divisore-modale">🔒 Cartella privata Admin</div><div class="campo"><textarea id="ev-n-priv" style="background:#fdf4ff;border-color:#f5d0fe"></textarea><input type="file" id="ev-f-priv" multiple accept="image/*,.pdf" style="margin-top:8px"></div>`:''}
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="ev-salva" style="background:#3e765e">💾 Crea Evento</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 /* Quando clicchi sul campo numerico, seleziona il valore */
 ['ev-osp','ev-bam','ev-stf'].forEach(id=>{
  const inp=document.getElementById(id);
  if(inp){
   inp.addEventListener('focus',function(){this.select()});
   inp.addEventListener('input',function(){this.value=this.value.replace(/^0+(?=\d)/,'')});
  }
 });
 document.getElementById('ev-salva').onclick=async()=>{
  const btn=document.getElementById('ev-salva');
  btn.disabled=true;btn.textContent='⏳ Salvataggio...';
  const nome=document.getElementById('ev-nome').value.trim();
  if(!nome){alert('Il nome è obbligatorio.');btn.disabled=false;btn.textContent='💾 Crea Evento';return}
  const data=document.getElementById('ev-data').value;
  const ora=document.getElementById('ev-ora').value||'18:30';
  const ev={
   id:'e-'+Date.now(),titolo:nome,inizio:data+'T'+ora+':00',fine:data+'T23:59:00',
   location:document.getElementById('ev-loc').value.trim()||'—',
   ospiti:parseInt(document.getElementById('ev-osp').value)||0,
   bambini:parseInt(document.getElementById('ev-bam').value)||0,
   staff:parseInt(document.getElementById('ev-stf').value)||0,
   stato:'confermato',
   noteTutti:document.getElementById('ev-n-tutti').value,
   noteSala:document.getElementById('ev-n-sala').value,
   noteCucina:document.getElementById('ev-n-cucina').value,
   noteMagazzino:document.getElementById('ev-n-mag').value,
   notePrivata:document.getElementById('ev-n-priv')?document.getElementById('ev-n-priv').value:'',
   allegatiTutti:await leggiAllegati('ev-f-tutti'),
   allegatiSala:await leggiAllegati('ev-f-sala'),
   allegatiCucina:await leggiAllegati('ev-f-cucina'),
   allegatiMagazzino:await leggiAllegati('ev-f-mag'),
   allegatiPrivata:document.getElementById('ev-f-priv')?await leggiAllegati('ev-f-priv'):[],
   creatoDa:user.nome+' ('+user.ruolo+')',creatoIl:new Date().toISOString()
  };
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
  salvati.push(ev);
  localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
  EVENTI.push(ev);
  generaNotifEvento(ev);
  chiudiDrawer();
  alert('✅ Evento creato!');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}
  /* ============================================================
   FIX: MAGAZZINO2 VEDE PREZZO INVENTARIO
   ============================================================ */
function cardProd(p,isAdmin,vedePrezzo){
 const hasFoto=!!p.foto;
 return `<div class="inv-card">
  <div class="inv-foto">${hasFoto?`<img loading="lazy" src="${p.foto}">`:''}<span class="inv-badge-cat">${p.categoria||'—'}</span></div>
  <div class="inv-body">
   <div class="inv-nome">${p.nome||''}</div>
   <div class="inv-codice">Cod. ${p.codice||'—'}</div>
   <div class="inv-qta">📦 ${p.quantita||0}</div>
   <div class="inv-info">📍 <b>${p.posizione||'—'}</b></div>
   ${vedePrezzo?`<div class="inv-prezzo">€ ${(p.prezzo||0).toFixed(2)}</div>`:''}
   <div class="inv-azioni">
    <button class="inv-btn primario" data-azione="scheda" data-codice="${p.codice}">📋 Scheda</button>
    ${isAdmin?`<button class="inv-btn" data-azione="modifica" data-codice="${p.codice}">✏️</button>`:''}
    ${isAdmin?`<button class="inv-btn pericolo" data-azione="elimina" data-codice="${p.codice}">🗑️</button>`:''}
   </div>
  </div>
 </div>`;
}

function inv(el){
 let salvati=[];
 try{salvati=JSON.parse(localStorage.getItem('ergo_prodotti'))||[]}catch(e){}
 const tutti=tuttiProds(salvati);
 const filtrati=tutti.filter(p=>{
  const matchCat=invRicerca.trim()!==''||invCategoria==='Tutte'||(p.categoria||'').toUpperCase().includes(invCategoria.toUpperCase());
  const matchTxt=ricercaIntelligente(invRicerca,[p.nome,p.codice,p.categoria,p.posizione,p.note]);
  return matchCat&&matchTxt;
 });
 const isAdmin=user.ruolo==='Amministratore';
 const vedePrezzo=user.ruolo==='Amministratore'||user.ruolo==='Magazzino2';
 el.innerHTML=`<div class="page">
  <div style="margin-bottom:20px"><p class="eyebrow">Catalogo</p><h1 class="title">Inventario</h1><p class="lede">${filtrati.length} prodott${filtrati.length===1?'o':'i'} trovat${filtrati.length===1?'o':'i'}${invRicerca?' per "'+invRicerca+'"':''}</p></div>
  <div class="inv-toolbar">
   <div class="inv-filtri">
    <div class="inv-search"><input id="inv-input-q" placeholder="Cerca nome, codice, categoria…" value="${invRicerca.replace(/"/g,'&quot;')}" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"></div>
    <select class="inv-select" id="inv-select-cat"><option value="Tutte">Tutte le categorie</option>${CATEGORIE_INV.map(c=>`<option value="${c}" ${invCategoria===c?'selected':''}>${c}</option>`).join('')}</select>
   </div>
   ${isAdmin?'<button class="inv-add" id="inv-btn-nuovo">＋ Nuovo prodotto</button>':''}
  </div>
  ${filtrati.length===0
   ?'<div class="inv-vuoto"><span class="emo">🔍</span>Nessun prodotto trovato'+(invRicerca?' per "'+invRicerca+'"':'')+'.</div>'
   :`<div class="inv-griglia" id="inv-griglia">${filtrati.map(p=>cardProd(p,isAdmin,vedePrezzo)).join('')}</div>`}
 </div>`;
 const inp=document.getElementById('inv-input-q');
 const griglia=document.getElementById('inv-griglia');
 const lede=el.querySelector('.lede');
 const riRender=()=>{
  const nf=tutti.filter(p=>{
   const matchCat=invRicerca.trim()!==''||invCategoria==='Tutte'||(p.categoria||'').toUpperCase().includes(invCategoria.toUpperCase());
   const matchTxt=ricercaIntelligente(invRicerca,[p.nome,p.codice,p.categoria,p.posizione,p.note]);
   return matchCat&&matchTxt;
  });
  if(lede)lede.textContent=nf.length+' prodott'+(nf.length===1?'o':'i')+' trovat'+(nf.length===1?'o':'i')+(invRicerca?' per "'+invRicerca+'"':'');
  if(griglia){
   griglia.innerHTML=nf.length===0
    ?'<div class="inv-vuoto" style="grid-column:1/-1"><span class="emo">🔍</span>Nessun prodotto trovato.</div>'
    :nf.map(p=>cardProd(p,isAdmin,vedePrezzo)).join('');
   agganciaBottoniCard(griglia,tutti);
  }
 };
 if(inp)inp.addEventListener('input',e=>{invRicerca=e.target.value;riRender()});
 const sc=document.getElementById('inv-select-cat');
 if(sc)sc.addEventListener('change',e=>{invCategoria=e.target.value;riRender()});
 const bn=document.getElementById('inv-btn-nuovo');
 if(bn)bn.onclick=()=>apriModaleProdotto();
 agganciaBottoniCard(el,tutti);
}
  /* ============================================================
   FIX: MAGAZZINO2 VEDE SOLO NOTIFICHE DI NOLEGGI
   ============================================================ */
function notifichePerUtente(utente){
 const mappa={
  'Amministratore':['tutti','sala','cucina','magazzino','admin'],
  'Wedding':['tutti','sala','cucina','magazzino'],
  'Cucina':['tutti','cucina'],
  'Sala':['tutti','sala'],
  'Magazzino':['tutti','magazzino'],
  'Magazzino2':['tutti','magazzino']
 };
 const rep=mappa[utente.ruolo]||['tutti'];
 return NOTIFICHE.filter(n=>{
  /* Filtro base per reparto */
  if(!rep.includes(n.reparto))return false;
  /* Magazzino2 vede SOLO notifiche di tipo noleggio e allegato */
  if(utente.ruolo==='Magazzino2'){
   if(n.tipo!=='noleggio'&&n.tipo!=='allegato')return false;
  }
  return true;
 });
}
  /* ============================================================
   FIX: DRAWER EVENTO CON NOTE + ALLEGATI + CARTELLA PRIVATA
   ============================================================ */
function apriDrawerEnt(tipo,obj){
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 const isAdmin=user.ruolo==='Amministratore';
 const isWedding=user.ruolo==='Wedding';
 const isMag2=user.ruolo==='Magazzino2';
 const isMag1=user.ruolo==='Magazzino';
 document.getElementById('d-eyebrow').textContent=tipo==='evento'?'Evento Catering':'Noleggio';
 document.getElementById('d-titolo').textContent=obj.titolo;
 const dataI=new Date(obj.inizio).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
 const ora=new Date(obj.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 let h='';
 if(tipo==='evento'){
  h+=`<h4>Dettagli evento</h4><div class="meta-grid"><div><small>Data</small><strong>${dataI}</strong></div><div><small>Orario</small><strong>${ora}</strong></div><div><small>Location</small><strong>${obj.location||'—'}</strong></div><div><small>Ospiti</small><strong>${obj.ospiti||0}${obj.bambini?' · '+obj.bambini+' bimbi':''}${obj.staff?' · '+obj.staff+' staff':''}</strong></div></div>`;
  const vediSala=isAdmin||isWedding||user.ruolo==='Sala';
  const vediCucina=isAdmin||isWedding||user.ruolo==='Cucina';
  const vediMag=isAdmin||isWedding||isMag1||isMag2;
  /* CARTELLA PRIVATA ADMIN - solo admin */
  if(isAdmin&&obj.notePrivata){
   h+=`<h4>🔒 Cartella privata Admin</h4><div class="note-box" style="background:#fdf4ff;border-color:#f5d0fe;color:#86198f">${obj.notePrivata}</div>`;
  }
  if(obj.noteTutti)h+=`<h4>📝 Note per tutti</h4><div class="note-box tutti">${obj.noteTutti}</div>`;
  if(vediSala&&obj.noteSala)h+=`<h4>🍽️ Note per la sala</h4><div class="note-box sala">${obj.noteSala}</div>`;
  if(vediCucina&&obj.noteCucina)h+=`<h4>👨‍🍳 Note per la cucina</h4><div class="note-box cucina">${obj.noteCucina}</div>`;
  if(vediMag&&obj.noteMagazzino)h+=`<h4>📦 Note per il magazzino</h4><div class="note-box magazzino">${obj.noteMagazzino}</div>`;
  /* Allegati visibili per ogni sezione */
  const tuttiAllegati=[];
  (obj.allegatiPrivata||[]).forEach(a=>{if(isAdmin)tuttiAllegati.push({...a,sezione:'🔒 Cartella privata'})});
  (obj.allegatiTutti||[]).forEach(a=>tuttiAllegati.push({...a,sezione:'Note per tutti'}));
  (obj.allegatiSala||[]).forEach(a=>{if(vediSala)tuttiAllegati.push({...a,sezione:'Note per la sala'})});
  (obj.allegatiCucina||[]).forEach(a=>{if(vediCucina)tuttiAllegati.push({...a,sezione:'Note per la cucina'})});
  (obj.allegatiMagazzino||[]).forEach(a=>{if(vediMag)tuttiAllegati.push({...a,sezione:'Note per il magazzino'})});
  if(tuttiAllegati.length>0){
   h+=`<h4>📎 Allegati (${tuttiAllegati.length})</h4>`;
   tuttiAllegati.forEach((a,i)=>{
    h+=`<div class="allegato-riga"><div class="allegato-info"><span class="allegato-icona">${iconaAllegato(a.mime)}</span><div><strong>${a.nome}</strong><small>${a.sezione}</small></div></div><div class="allegato-azioni"><button class="allegato-btn anteprima" data-allega-idx="${i}">👁️ Anteprima</button><button class="allegato-btn" data-allega-down="${i}">⬇️</button></div></div>`;
   });
  }else{
   h+=`<h4>📎 Allegati</h4><p style="color:#94a3b8;font-size:.82rem;padding:8px 0">Nessun allegato per questo evento.</p>`;
  }
 }else{
  const dataF=new Date(obj.fine).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
  h+=`<h4>Dettagli noleggio</h4><div class="meta-grid"><div><small>Dal</small><strong>${dataI} · ${ora}</strong></div><div><small>Al</small><strong>${dataF}</strong></div><div><small>Location</small><strong>${obj.location||'—'}</strong></div><div><small>Stato</small><strong>${obj.stato}</strong></div><div><small>Referente</small><strong>${obj.referente||'—'}</strong></div><div><small>Telefono</small><strong>${obj.telefono||'—'}</strong></div></div>`;
  if(obj.note)h+=`<h4>📝 Note</h4><div class="note-box">${obj.note}</div>`;
  const vediBolla=isAdmin||isMag2;
  const vediDDT=isAdmin||isMag2||isMag1;
  const vediVario=isAdmin||isMag2||isMag1;
  const tuttiAllegati=[];
  if(vediBolla)(obj.allegatiBolla||[]).forEach(a=>tuttiAllegati.push({...a,sezione:'💰 Bolla con prezzo'}));
  if(vediDDT)(obj.allegatiDDT||[]).forEach(a=>tuttiAllegati.push({...a,sezione:'📄 DDT'}));
  if(vediVario)(obj.allegatiVario||[]).forEach(a=>tuttiAllegati.push({...a,sezione:'📎 Vario'}));
  if(tuttiAllegati.length>0){
   h+=`<h4>📎 Allegati (${tuttiAllegati.length})</h4>`;
   tuttiAllegati.forEach((a,i)=>{
    h+=`<div class="allegato-riga"><div class="allegato-info"><span class="allegato-icona">${iconaAllegato(a.mime)}</span><div><strong>${a.nome}</strong><small>${a.sezione}</small></div></div><div class="allegato-azioni"><button class="allegato-btn anteprima" data-allega-idx="${i}">👁️ Anteprima</button><button class="allegato-btn" data-allega-down="${i}">⬇️</button></div></div>`;
   });
  }else{
   h+=`<h4>📎 Allegati</h4><p style="color:#94a3b8;font-size:.82rem;padding:8px 0">Nessun allegato per questo noleggio.</p>`;
  }
 }
 document.getElementById('d-body').innerHTML=h;
 /* Footer con Modifica + Elimina */
 const puoMod=(tipo==='evento'&&(isAdmin||isWedding))||(tipo==='noleggio'&&(isAdmin||isMag2));
 let footHtml=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 if(puoMod)footHtml+=`<button class="btn-primary" id="d-modifica">✏️ Modifica</button>`;
 if(puoMod)footHtml+=`<button class="btn-primary" id="d-elimina" style="background:#dc2626;flex:0 0 auto">🗑️</button>`;
 document.getElementById('d-foot').innerHTML=footHtml;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 const bm=document.getElementById('d-modifica');
 if(bm)bm.onclick=()=>{chiudiDrawer();if(tipo==='evento')apriModaleModificaEvento(obj);else alert('Modifica noleggio: in arrivo')};
 const bel=document.getElementById('d-elimina');
 if(bel)bel.onclick=()=>{chiudiDrawer();confermaElimEnt(tipo,obj)};
 /* Anteprima allegati */
 const allVisible=[];
 if(tipo==='evento'){
  (obj.allegatiPrivata||[]).forEach(a=>{if(isAdmin)allVisible.push({...a,sezione:'🔒 Cartella privata'})});
  (obj.allegatiTutti||[]).forEach(a=>allVisible.push({...a,sezione:'Note per tutti'}));
  (obj.allegatiSala||[]).forEach(a=>{if(isAdmin||isWedding||user.ruolo==='Sala')allVisible.push({...a,sezione:'Note per la sala'})});
  (obj.allegatiCucina||[]).forEach(a=>{if(isAdmin||isWedding||user.ruolo==='Cucina')allVisible.push({...a,sezione:'Note per la cucina'})});
  (obj.allegatiMagazzino||[]).forEach(a=>{if(isAdmin||isWedding||isMag1||isMag2)allVisible.push({...a,sezione:'Note per il magazzino'})});
 }else{
  if(isAdmin||isMag2)(obj.allegatiBolla||[]).forEach(a=>allVisible.push({...a,sezione:'💰 Bolla con prezzo'}));
  if(isAdmin||isMag2||isMag1)(obj.allegatiDDT||[]).forEach(a=>allVisible.push({...a,sezione:'📄 DDT'}));
  if(isAdmin||isMag2||isMag1)(obj.allegatiVario||[]).forEach(a=>allVisible.push({...a,sezione:'📎 Vario'}));
 }
 document.querySelectorAll('[data-allega-idx]').forEach(b=>{
  b.onclick=()=>{const idx=parseInt(b.dataset.allegaIdx);if(allVisible[idx])apriAnteprimaAllega(allVisible[idx])};
 });
 document.querySelectorAll('[data-allega-down]').forEach(b=>{
  b.onclick=()=>{const idx=parseInt(b.dataset.allegaDown);if(allVisible[idx])scaricaAllega(allVisible[idx])};
 });
}
  /* ============================================================
   FIX: MODALE MODIFICA EVENTO
   ============================================================ */
function apriModaleModificaEvento(ev){
 const isAdmin=user.ruolo==='Amministratore';
 const dataIso=new Date(ev.inizio).toISOString().slice(0,10);
 const ora=String(new Date(ev.inizio).getHours()).padStart(2,'0')+':'+String(new Date(ev.inizio).getMinutes()).padStart(2,'0');
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Modifica evento';
 document.getElementById('d-titolo').textContent='✏️ '+ev.titolo;
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Nome evento <span style="color:#dc2626">*</span></label><input id="me-nome" value="${(ev.titolo||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo-2">
   <div class="campo"><label>Data</label><input id="me-data" type="date" value="${dataIso}"></div>
   <div class="campo"><label>Orario</label><input id="me-ora" type="time" value="${ora}"></div>
  </div>
  <div class="campo"><label>Location</label><input id="me-loc" value="${(ev.location||'').replace(/"/g,'&quot;')}"></div>
  <div class="divisore-modale">👥 Persone</div>
  <div class="campo-3">
   <div class="campo"><label>Ospiti</label><input id="me-osp" type="number" min="0" value="${ev.ospiti||0}" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
   <div class="campo"><label>Bambini</label><input id="me-bam" type="number" min="0" value="${ev.bambini||0}" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
   <div class="campo"><label>Staff</label><input id="me-stf" type="number" min="0" value="${ev.staff||0}" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
  </div>
  <div class="divisore-modale">📝 Note per tutti</div><div class="campo"><textarea id="me-n-tutti" style="background:#eef2ff;border-color:#c7d2fe">${(ev.noteTutti||'').replace(/</g,'&lt;')}</textarea></div>
  <div class="divisore-modale">🍽️ Note per la sala</div><div class="campo"><textarea id="me-n-sala" style="background:#f0fdf4;border-color:#bbf7d0">${(ev.noteSala||'').replace(/</g,'&lt;')}</textarea></div>
  <div class="divisore-modale">👨‍🍳 Note per la cucina</div><div class="campo"><textarea id="me-n-cucina" style="background:#fff7ed;border-color:#fed7aa">${(ev.noteCucina||'').replace(/</g,'&lt;')}</textarea></div>
  <div class="divisore-modale">📦 Note per il magazzino</div><div class="campo"><textarea id="me-n-mag" style="background:#f5f3ff;border-color:#ddd6fe">${(ev.noteMagazzino||'').replace(/</g,'&lt;')}</textarea></div>
  ${isAdmin?`<div class="divisore-modale">🔒 Cartella privata Admin</div><div class="campo"><textarea id="me-n-priv" style="background:#fdf4ff;border-color:#f5d0fe">${(ev.notePrivata||'').replace(/</g,'&lt;')}</textarea></div>`:''}
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="me-salva" style="background:#3e765e">💾 Salva modifiche</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 /* Rimuove zero iniziali */
 ['me-osp','me-bam','me-stf'].forEach(id=>{
  const inp=document.getElementById(id);
  if(inp){
   inp.addEventListener('focus',function(){this.select()});
   inp.addEventListener('input',function(){this.value=this.value.replace(/^0+(?=\d)/,'')});
  }
 });
 document.getElementById('me-salva').onclick=()=>{
  const nome=document.getElementById('me-nome').value.trim();
  if(!nome){alert('Il nome è obbligatorio.');return}
  ev.titolo=nome;
  ev.inizio=document.getElementById('me-data').value+'T'+(document.getElementById('me-ora').value||'18:30')+':00';
  ev.location=document.getElementById('me-loc').value.trim()||'—';
  ev.ospiti=parseInt(document.getElementById('me-osp').value)||0;
  ev.bambini=parseInt(document.getElementById('me-bam').value)||0;
  ev.staff=parseInt(document.getElementById('me-stf').value)||0;
  ev.noteTutti=document.getElementById('me-n-tutti').value;
  ev.noteSala=document.getElementById('me-n-sala').value;
  ev.noteCucina=document.getElementById('me-n-cucina').value;
  ev.noteMagazzino=document.getElementById('me-n-mag').value;
  if(isAdmin&&document.getElementById('me-n-priv'))ev.notePrivata=document.getElementById('me-n-priv').value;
  let salv=[];
  try{salv=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
  const idx=salv.findIndex(e=>e.id===ev.id);
  if(idx>=0)salv[idx]=ev;else salv.push(ev);
  localStorage.setItem('ergo_eventi',JSON.stringify(salv));
  chiudiDrawer();
  alert('✅ Evento aggiornato!');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}
  /* ============================================================
   FIX: SCHEDA PRODOTTO CON QR + TECNICA + ANTEPRIMA
   ============================================================ */
function apriSchedaProd(p){
 const scheda=p.scheda||{};
 const hasFoto=!!p.foto;
 const fotoHtml=hasFoto?`<img loading="lazy" src="${p.foto}" style="width:100%;height:100%;object-fit:cover">`:`<div style="font-size:4rem;opacity:.4">📦</div>`;
 let righe='';
 [['Materiale',scheda.materiale],['Colore',scheda.colore],['Dimensione',scheda.dimensione]].forEach(([k,v])=>{
  if(v&&v.trim())righe+=`<div style="display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-bottom:1px dashed #c9dcf0;font-size:.82rem"><span style="color:#6b778c;font-weight:600">${k}</span><span style="color:#344054;font-weight:700;text-align:right">${v}</span></div>`;
 });
 const tech=righe?`<div style="background:#f3f8ff;border:1px solid #d7e7fa;border-radius:12px;padding:14px;margin-top:14px"><div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#083278;font-weight:800;margin-bottom:10px">📋 Scheda tecnica</div>${righe}</div>`:'';

 /* Mostra prezzo se Admin o Magazzino2 */
 const vedePrezzo=user.ruolo==='Amministratore'||user.ruolo==='Magazzino2';

 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Scheda prodotto';
 document.getElementById('d-titolo').textContent=p.nome;
 document.getElementById('d-body').innerHTML=`
  <div style="width:100%;aspect-ratio:1;background:linear-gradient(145deg,#eef4fa,#f8fafc);border-radius:14px;display:grid;place-items:center;overflow:hidden;color:#9ab1c9;margin-bottom:14px">${fotoHtml}</div>
  <div style="font-size:.75rem;color:#98a2b3;letter-spacing:.06em;margin-bottom:14px;text-transform:uppercase;font-weight:700">COD. ${p.codice}</div>
  <div class="meta-grid">
   <div><small>Quantità</small><strong>📦 ${p.quantita||0}</strong></div>
   <div><small>Categoria</small><strong>${p.categoria||'—'}</strong></div>
   <div><small>Posizione</small><strong>📍 ${p.posizione||'—'}</strong></div>
   ${vedePrezzo?`<div><small>Prezzo noleggio</small><strong>€ ${(p.prezzo||0).toFixed(2)}</strong></div>`:''}
  </div>
  ${p.note?`<h4>📝 Note</h4><div class="note-box" style="background:#f3f8ff;border-color:#d7e7fa">${p.note}</div>`:''}
  ${tech}
  <div style="background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center;margin-top:14px">
   <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#083278;font-weight:800;margin-bottom:10px">🎫 QR Code prodotto</div>
   <canvas id="qr-canvas" width="180" height="180" style="display:block;margin:0 auto;border-radius:8px;border:1px solid var(--line)"></canvas>
   <div style="margin-top:12px"><button class="inv-btn primario" id="qr-scarica" style="padding:10px 16px">⬇️ Scarica QR</button></div>
   <div style="font-size:.65rem;color:#94a3b8;margin-top:10px">Scansionalo per aprire la scheda sul telefono</div>
  </div>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 /* Genera QR */
 setTimeout(()=>{
  const c=document.getElementById('qr-canvas');
  if(c){
   const url=location.origin+location.pathname+'?codice='+encodeURIComponent(p.codice||'');
   const img=new Image();
   img.crossOrigin='anonymous';
   img.onload=()=>{
    const x=c.getContext('2d');
    x.fillStyle='#fff';x.fillRect(0,0,180,180);
    x.drawImage(img,0,0,180,180);
   };
   img.onerror=()=>{
    const x=c.getContext('2d');
    x.fillStyle='#f8fafc';x.fillRect(0,0,180,180);
    x.fillStyle='#98a2b3';
    x.font='12px sans-serif';
    x.textAlign='center';
    x.fillText('QR non disponibile',90,84);
    x.fillText('(richiede internet)',90,102);
   };
   img.src='https://api.qrserver.com/v1/create-qr-code/?size=180x180&data='+encodeURIComponent(url);
  }
  const bd=document.getElementById('qr-scarica');
  if(bd)bd.onclick=()=>{
   const c2=document.getElementById('qr-canvas');
   if(!c2)return;
   const a=document.createElement('a');
   a.download='QR_'+(p.codice||'prodotto')+'.png';
   a.href=c2.toDataURL('image/png');
   a.click();
  };
 },100);
}
  /* ============================================================
   FIX: ANTEPRIMA ALLEGATI CON FRECCIA INDIETRO
   ============================================================ */
let _allegatoApertoDa=null;
let _allegatoApertoTipo=null;
let _allegatoApertoObj=null;

function apriAnteprimaAllega(allegato){
 _allegatoApertoDa=allegato.sezione||'Allegati';
 _allegatoApertoTipo=window._tipoAperto||'evento';
 _allegatoApertoObj=window._objAperto||null;

 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Anteprima';
 document.getElementById('d-titolo').textContent=allegato.nome||'Allegato';
 const mime=allegato.mime||'';
 let contenuto='';
 if(mime.startsWith('image/')){
  contenuto=`<div style="background:#f3f5f8;border-radius:14px;padding:14px;text-align:center"><img src="${allegato.data||allegato.url}" style="max-width:100%;max-height:60vh;border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,0.1)"></div>`;
 }else if(mime.includes('pdf')){
  contenuto=`<div style="background:#f3f5f8;border-radius:14px;padding:14px"><iframe src="${allegato.data||allegato.url}" style="width:100%;height:55vh;border:0;border-radius:10px;background:#fff"></iframe></div>`;
 }else{
  contenuto=`<div class="note-box" style="text-align:center;padding:30px"><div style="font-size:2.5rem;margin-bottom:10px">📎</div><p>Anteprima non disponibile per questo tipo di file.</p></div>`;
 }
 document.getElementById('d-body').innerHTML=contenuto+`<div style="margin-top:14px;padding:12px;background:#f3f8ff;border:1px solid #d7e7fa;border-radius:10px;font-size:.78rem;color:#4b5563;display:flex;justify-content:space-between;align-items:center;gap:10px"><span>📌 <b>${allegato.sezione}</b>${allegato.size?' · '+Math.round(allegato.size/1024)+' KB':''}</span></div>`;
 document.getElementById('d-foot').innerHTML=`
  <button class="btn-ghost" id="d-indietro" style="display:inline-flex;align-items:center;gap:6px">← Indietro</button>
  <button class="btn-primary" id="d-scarica">⬇️ Scarica</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 /* Freccia indietro: torna al drawer dell'evento/noleggio */
 document.getElementById('d-indietro').onclick=()=>{
  if(_allegatoApertoObj){
   apriDrawerEnt(_allegatoApertoTipo,_allegatoApertoObj);
  }else{
   chiudiDrawer();
  }
 };
 document.getElementById('d-scarica').onclick=()=>scaricaAllega(allegato);
}
  /* ============================================================
   FIX: NOTIFICHE - SOLO NON LETTE ALLA RIENTRO
   ============================================================ */
(function(){
 /* Quando l'utente cambia vista o fa login, resetta il filtro a "solo nuove" */
 const _origApp=window.app;
 if(_origApp){
  window.app=function(){
   /* Imposta automaticamente "Solo nuove" all'apertura */
   filtroFeed='nuove';
   return _origApp.apply(this,arguments);
  };
 }
})();
  /* ============================================================
   FIX: NOTIFICA "LISTA INVIATA" → APRI ALLEGATO + VAI ALL'EVENTO
   ============================================================ */
function apriDrawerNotif(id){
 const n=NOTIFICHE.find(x=>x.id===id);if(!n)return;
 segnaLetta(user.username,n.id);
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent=labelTipo(n.tipo);
 document.getElementById('d-titolo').textContent=n.titolo;
 document.getElementById('d-body').innerHTML=renderDetNotif(n);

 /* Pulsanti footer: se è una notifica con evento collegato, mostra "Vai all'evento" */
 const dettagli=n.dettagli||{};
 const nomeEvento=dettagli.evento;
 let eventoCollegato=null;
 if(nomeEvento){
  eventoCollegato=EVENTI.find(e=>e.titolo===nomeEvento);
 }
 let footerHtml=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 if(eventoCollegato){
  footerHtml+=`<button class="btn-primary" id="d-vai-evento">📅 Vai all'evento</button>`;
 }
 document.getElementById('d-foot').innerHTML=footerHtml;

 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;

 /* Pulsante "Vai all'evento" */
 const bv=document.getElementById('d-vai-evento');
 if(bv)bv.onclick=()=>{
  chiudiDrawer();
  view='calendario';
  app();
  /* Apri subito il drawer dell'evento */
  setTimeout(()=>{
   apriDrawerEnt('evento',eventoCollegato);
  },350);
 };

 setTimeout(()=>{if(view==='dashboard'){const pc=document.getElementById('pc');if(pc)dash(pc)}},200);
}

/* Aggiorna renderDetNotif per mostrare i dettagli della lista */
function renderDetNotif(n){
 const d=n.dettagli||{};let h='';
 if(d.evento){
  h+=`<h4>Evento</h4><div class="note-box tutti"><strong style="font-family:Georgia,serif;font-size:1rem">${d.evento}</strong>${d.location?`<br><span style="color:#667085;font-size:.8rem">📍 ${d.location}</span>`:''}</div>`;
 }
 if(d.noleggio){
  h+=`<h4>Noleggio</h4><div class="note-box"><strong style="font-family:Georgia,serif;font-size:1rem">${d.noleggio}</strong></div>`;
 }
 if(d.testoNota){
  const cls=n.reparto==='cucina'?'cucina':n.reparto==='sala'?'sala':n.reparto==='magazzino'?'magazzino':'tutti';
  h+=`<h4>Testo della nota</h4><div class="note-box ${cls}">${d.testoNota}</div>`;
 }
 if(d.utente){
  h+=`<h4>Utente</h4><div class="note-box tutti"><strong>${d.utente}</strong><br><span style="color:#667085;font-size:.8rem">Ruolo: ${d.ruolo}</span></div>`;
 }
 if(d.allegato){
  h+=`<h4>📎 Allegato inviato</h4><div style="background:#f0f6ff;border:1px solid #d7e7fa;border-radius:10px;padding:12px;display:flex;align-items:center;gap:10px"><span style="font-size:1.4rem">📄</span><div><strong style="font-size:.85rem;color:#083278">${d.allegato}</strong><div style="font-size:.7rem;color:#6b778c;margin-top:3px">Apri l'evento per visualizzarlo</div></div></div>`;
 }
 h+=`<h4>Info</h4><div class="meta-grid"><div><small>Da</small><strong>${n.da||'—'}</strong></div><div><small>Quando</small><strong>${tempoFa(n.quando)}</strong></div></div>`;
 return h;
}
  /* ============================================================
   FIX: METEO IN TEMPO REALE NELLA DASHBOARD
   ============================================================ */
async function trovaCoordinate(location){
 if(!location||location==='—')return null;
 try{
  const url='https://nominatim.openstreetmap.org/search?format=json&limit=1&q='+encodeURIComponent(location);
  const risposta=await fetch(url,{headers:{'User-Agent':'ErgoGestionale/1.0'}});
  const dati=await risposta.json();
  if(dati&&dati[0])return{lat:parseFloat(dati[0].lat),lon:parseFloat(dati[0].lon)};
 }catch(e){}
 return null;
}

async function getMeteo(lat,lon,dataEvento){
 try{
  const dataStr=dataEvento.slice(0,10);
  const oggi=new Date();
  const diffGiorni=Math.floor((new Date(dataEvento)-oggi)/(1000*60*60*24));
  /* Se l'evento è oltre 16 giorni, usiamo solo previsione generica */
  if(diffGiorni>16||diffGiorni<-1)return null;
  const url='https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&daily=temperature_2m_max,temperature_2m_min,weathercode,precipitation_probability_max&timezone=auto&start_date='+dataStr+'&end_date='+dataStr;
  const risposta=await fetch(url);
  const dati=await risposta.json();
  if(dati&&dati.daily&&dati.daily.time&&dati.daily.time.length>0){
   return{
    tmax:Math.round(dati.daily.temperature_2m_max[0]),
    tmin:Math.round(dati.daily.temperature_2m_min[0]),
    code:dati.daily.weathercode[0],
    pioggia:dati.daily.precipitation_probability_max[0]||0
   };
  }
 }catch(e){}
 return null;
}

function iconaMeteo(code){
 if(code===0)return'☀️';
 if(code<=2)return'🌤️';
 if(code===3)return'☁️';
 if(code<=48)return'🌫️';
 if(code<=55)return'🌧️';
 if(code<=65)return'🌧️';
 if(code<=75)return'❄️';
 if(code<=82)return'🌧️';
 if(code<=95)return'⛈️';
 return'🌩️';
}

function labelMeteo(code){
 if(code===0)return'Sereno';
 if(code<=2)return'Poco nuvoloso';
 if(code===3)return'Nuvoloso';
 if(code<=48)return'Nebbia';
 if(code<=55)return'Pioggerella';
 if(code<=65)return'Pioggia';
 if(code<=75)return'Neve';
 if(code<=82)return'Rovesci';
 if(code<=95)return'Temporale';
 return'Temporale forte';
}

async function mostraMeteo(idElemento,location,dataEvento){
 const el=document.getElementById(idElemento);
 if(!el)return;
 el.innerHTML='<div style="font-size:.7rem;color:#94a3b8;padding:8px 0;text-align:center">🌤️ Carico meteo…</div>';
 const coord=await trovaCoordinate(location);
 if(!coord){el.innerHTML='';return}
 const meteo=await getMeteo(coord.lat,coord.lon,dataEvento);
 if(!meteo){el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:8px 0;text-align:center">📅 Meteo disponibile solo per i prossimi 16 giorni</div>';return}
 el.innerHTML=`
  <div style="background:linear-gradient(135deg,#f0f6ff,#eaf1fb);border:1px solid #cfe0f5;border-radius:12px;padding:12px;display:flex;align-items:center;gap:12px;margin-top:12px">
   <div style="font-size:2.2rem;line-height:1">${iconaMeteo(meteo.code)}</div>
   <div style="flex:1;min-width:0">
    <div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:#6b778c;font-weight:800">Meteo previsto</div>
    <div style="font-size:.85rem;color:#083278;font-weight:700;margin-top:2px">${labelMeteo(meteo.code)}</div>
    <div style="font-size:.7rem;color:#6b778c;margin-top:2px">${meteo.tmin}° / ${meteo.tmax}° · Pioggia ${meteo.pioggia}%</div>
   </div>
  </div>`;
}

/* Override della dashboard: aggiunge meteo dopo i countdown */
(function(){
 const _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   const risultato=_origDash.apply(this,arguments);
   /* Dopo che la dashboard è renderizzata, aggiungi meteo */
   setTimeout(()=>{
    /* Trova prossimo evento */
    const oggi=new Date();oggi.setHours(0,0,0,0);
    let prossimoEv=null,prossimoNl=null;
    EVENTI.forEach(e=>{const d=new Date(e.inizio);if(d>=oggi&&(!prossimoEv||new Date(e.inizio)<new Date(prossimoEv.inizio)))prossimoEv=e});
    NOLEGGI.forEach(n=>{const d=new Date(n.inizio);if(d>=oggi&&(!prossimoNl||new Date(n.inizio)<new Date(prossimoNl.inizio)))prossimoNl=n});
    /* Aggiungi div meteo nella card evento */
    const cdEv=document.getElementById('cd-e');
    if(cdEv&&prossimoEv&&prossimoEv.location){
     const meteoDiv=document.createElement('div');
     meteoDiv.id='meteo-evento';
     cdEv.parentNode.appendChild(meteoDiv);
     mostraMeteo('meteo-evento',prossimoEv.location,prossimoEv.inizio);
    }
    const cdNl=document.getElementById('cd-n');
    if(cdNl&&prossimoNl&&prossimoNl.location){
     const meteoDiv2=document.createElement('div');
     meteoDiv2.id='meteo-noleggio';
     cdNl.parentNode.appendChild(meteoDiv2);
     mostraMeteo('meteo-noleggio',prossimoNl.location,prossimoNl.inizio);
    }
   },200);
   return risultato;
  };
 }
})();
  /* ============================================================
   FIX: TENDINA ANNO CALENDARIO PULITA
   ============================================================ */
(function(){
 const stile=document.createElement('style');
 stile.textContent=`
  .cal-nav .mese{font-family:'DM Sans',sans-serif;font-size:.85rem;color:var(--muted);font-weight:800;display:flex;align-items:center;gap:8px;text-transform:uppercase;letter-spacing:.1em}
  .cal-nav .mese select{font-family:'DM Sans',sans-serif !important;font-size:.9rem !important;font-weight:800 !important;color:var(--blue) !important;background:#f4f7fc !important;border:1.5px solid #cfe0f5 !important;border-radius:9px !important;padding:6px 28px 6px 12px !important;cursor:pointer !important;outline:none !important;transition:all .18s !important;box-shadow:0 1px 3px rgba(8,50,120,0.06) !important;appearance:none !important;-webkit-appearance:none !important;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 24 24' fill='none' stroke='%23083278' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E") !important;background-repeat:no-repeat !important;background-position:right 9px center !important;background-size:10px !important;letter-spacing:.02em !important;min-width:80px}
  .cal-nav .mese select:hover{background-color:#eaf1fb !important;border-color:var(--blue) !important}
  .cal-nav .mese select:focus{border-color:var(--blue) !important;box-shadow:0 0 0 3px rgba(8,50,120,0.1) !important;background-color:#fff !important}
  .cal-nav .mese select option{font-family:'DM Sans',sans-serif;font-size:.9rem;font-weight:600;color:#152238;padding:8px}
 `;
 document.head.appendChild(stile);
})();
  /* ============================================================
   FIX METEO v3 — usa Open-Meteo Geocoding (funziona da file://)
   ============================================================ */
function iconaMeteo(code){
 if(code===0)return'☀️';
 if(code<=2)return'🌤️';
 if(code===3)return'☁️';
 if(code<=48)return'🌫️';
 if(code<=55)return'🌦️';
 if(code<=65)return'🌧️';
 if(code<=75)return'❄️';
 if(code<=82)return'🌧️';
 if(code<=95)return'⛈️';
 return'🌩️';
}
function labelMeteo(code){
 if(code===0)return'Sereno';
 if(code<=2)return'Poco nuvoloso';
 if(code===3)return'Nuvoloso';
 if(code<=48)return'Nebbia';
 if(code<=55)return'Pioggerella';
 if(code<=65)return'Pioggia';
 if(code<=75)return'Neve';
 if(code<=82)return'Rovesci';
 if(code<=95)return'Temporale';
 return'Temporale forte';
}

async function mostraMeteoIn(idElemento,location,dataEvento){
 const el=document.getElementById(idElemento);
 if(!el)return;
 el.innerHTML='<div style="font-size:.7rem;color:#94a3b8;padding:10px 0;text-align:center">🌤️ Cerco il meteo…</div>';
 try{
  /* 1. Trova coordinate con Open-Meteo Geocoding */
  const urlGeo='https://geocoding-api.open-meteo.com/v1/search?name='+encodeURIComponent(location)+'&count=1&language=it&format=json';
  const rispGeo=await fetch(urlGeo);
  const datiGeo=await rispGeo.json();
  if(!datiGeo||!datiGeo.results||datiGeo.results.length===0){
   el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:10px 0;text-align:center">📍 Location non trovata. Scrivi "Nome, Città" (es. "Villa X, Catania")</div>';
   return;
  }
  const lat=datiGeo.results[0].latitude;
  const lon=datiGeo.results[0].longitude;
  const cittàTrovata=datiGeo.results[0].name;
  /* 2. Prendi meteo */
  const oggi=new Date();
  const diffGiorni=Math.floor((new Date(dataEvento)-oggi)/(1000*60*60*24));
  if(diffGiorni>16){
   el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:10px 0;text-align:center">📅 Meteo disponibile solo nei prossimi 16 giorni</div>';
   return;
  }
  const dataStr=new Date(dataEvento).toISOString().slice(0,10);
  const urlMeteo='https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&daily=temperature_2m_max,temperature_2m_min,weathercode,precipitation_probability_max&timezone=auto&start_date='+dataStr+'&end_date='+dataStr;
  const rispMeteo=await fetch(urlMeteo);
  const datiMeteo=await rispMeteo.json();
  if(!datiMeteo||!datiMeteo.daily||!datiMeteo.daily.time||datiMeteo.daily.time.length===0){
   el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:10px 0;text-align:center">📅 Meteo non disponibile</div>';
   return;
  }
  const tmax=Math.round(datiMeteo.daily.temperature_2m_max[0]);
  const tmin=Math.round(datiMeteo.daily.temperature_2m_min[0]);
  const code=datiMeteo.daily.weathercode[0];
  const pioggia=datiMeteo.daily.precipitation_probability_max[0]||0;
  el.innerHTML=`
   <div style="background:linear-gradient(135deg,#f0f6ff,#eaf1fb);border:1px solid #cfe0f5;border-radius:12px;padding:12px;display:flex;align-items:center;gap:12px;margin-top:12px">
    <div style="font-size:2.2rem;line-height:1">${iconaMeteo(code)}</div>
    <div style="flex:1;min-width:0">
     <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.1em;color:#6b778c;font-weight:800">Meteo previsto · ${cittàTrovata}</div>
     <div style="font-size:.88rem;color:#083278;font-weight:700;margin-top:2px">${labelMeteo(code)}</div>
     <div style="font-size:.72rem;color:#6b778c;margin-top:2px">${tmin}° / ${tmax}° · Pioggia ${pioggia}%</div>
    </div>
   </div>`;
 }catch(e){
  el.innerHTML='<div style="font-size:.68rem;color:#b91c1c;padding:10px 0;text-align:center">⚠️ Errore connessione meteo</div>';
 }
}

async function mostraMeteoDashboard(){
 const oggi=new Date();oggi.setHours(0,0,0,0);
 let prossimoEv=null,prossimoNl=null;
 EVENTI.forEach(e=>{const d=new Date(e.inizio);if(d>=oggi&&(!prossimoEv||new Date(e.inizio)<new Date(prossimoEv.inizio)))prossimoEv=e});
 NOLEGGI.forEach(n=>{const d=new Date(n.inizio);if(d>=oggi&&(!prossimoNl||new Date(n.inizio)<new Date(prossimoNl.inizio)))prossimoNl=n});

 const cdEv=document.getElementById('cd-e');
 if(cdEv){
  const vecchio=document.getElementById('meteo-evento');
  if(vecchio)vecchio.remove();
  const div=document.createElement('div');
  div.id='meteo-evento';
  cdEv.parentNode.appendChild(div);
  if(prossimoEv&&prossimoEv.location&&prossimoEv.location!=='—'){
   mostraMeteoIn('meteo-evento',prossimoEv.location,prossimoEv.inizio);
  }
 }
 const cdNl=document.getElementById('cd-n');
 if(cdNl){
  const vecchio2=document.getElementById('meteo-noleggio');
  if(vecchio2)vecchio2.remove();
  const div2=document.createElement('div');
  div2.id='meteo-noleggio';
  cdNl.parentNode.appendChild(div2);
  if(prossimoNl&&prossimoNl.location&&prossimoNl.location!=='—'){
   mostraMeteoIn('meteo-noleggio',prossimoNl.location,prossimoNl.inizio);
  }
 }
}

/* Override dash: chiama meteo dopo render */
(function(){
 const _orig=window.dash;
 if(_orig){
  window.dash=function(el){
   const r=_orig.apply(this,arguments);
   setTimeout(mostraMeteoDashboard,300);
   return r;
  };
 }
})();
  /* ============================================================
   AGGIUNTA: CAMPO "CITTÀ" separato dalla location
   ============================================================ */
/* Sovrascrivo apriModaleEvento per aggiungere campo Città */
function apriModaleEvento(){
 const oggi=new Date().toISOString().slice(0,10);
 const isAdmin=user.ruolo==='Amministratore';
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Nuovo evento';
 document.getElementById('d-titolo').textContent='📅 Crea Evento Catering';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Nome evento / Cliente <span style="color:#dc2626">*</span></label><input id="ev-nome" placeholder="Es. Matrimonio Bianchi"></div>
  <div class="campo-2">
   <div class="campo"><label>Data</label><input id="ev-data" type="date" value="${oggi}"></div>
   <div class="campo"><label>Orario</label><input id="ev-ora" type="time" value="18:30"></div>
  </div>
  <div class="campo"><label>📍 Nome location</label><input id="ev-loc" placeholder="Es. Villa San Giorgio"></div>
  <div class="campo"><label>🌍 Città <span style="font-size:.7rem;font-weight:500;text-transform:none;color:#94a3b8;letter-spacing:0">(serve solo per il meteo)</span></label><input id="ev-citta" placeholder="Es. Catania"></div>
  <div class="divisore-modale">👥 Persone</div>
  <div class="campo-3">
   <div class="campo"><label>Ospiti</label><input id="ev-osp" type="number" min="0" value="0" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
   <div class="campo"><label>Bambini</label><input id="ev-bam" type="number" min="0" value="0" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
   <div class="campo"><label>Staff</label><input id="ev-stf" type="number" min="0" value="0" style="font-size:1rem;font-weight:700;text-align:center;color:#083278"></div>
  </div>
  <div class="divisore-modale">📝 Note per tutti</div>
  <div class="campo"><textarea id="ev-n-tutti" style="background:#eef2ff;border-color:#c7d2fe"></textarea><input type="file" id="ev-f-tutti" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">🍽️ Note per la sala</div>
  <div class="campo"><textarea id="ev-n-sala" style="background:#f0fdf4;border-color:#bbf7d0"></textarea><input type="file" id="ev-f-sala" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">👨‍🍳 Note per la cucina</div>
  <div class="campo"><textarea id="ev-n-cucina" style="background:#fff7ed;border-color:#fed7aa"></textarea><input type="file" id="ev-f-cucina" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  <div class="divisore-modale">📦 Note per il magazzino</div>
  <div class="campo"><textarea id="ev-n-mag" style="background:#f5f3ff;border-color:#ddd6fe"></textarea><input type="file" id="ev-f-mag" multiple accept="image/*,.pdf" style="margin-top:8px"></div>
  ${isAdmin?`<div class="divisore-modale">🔒 Cartella privata Admin</div><div class="campo"><textarea id="ev-n-priv" style="background:#fdf4ff;border-color:#f5d0fe"></textarea><input type="file" id="ev-f-priv" multiple accept="image/*,.pdf" style="margin-top:8px"></div>`:''}
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="ev-salva" style="background:#3e765e">💾 Crea Evento</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 ['ev-osp','ev-bam','ev-stf'].forEach(id=>{
  const inp=document.getElementById(id);
  if(inp){
   inp.addEventListener('focus',function(){this.select()});
   inp.addEventListener('input',function(){this.value=this.value.replace(/^0+(?=\d)/,'')});
  }
 });
 document.getElementById('ev-salva').onclick=async()=>{
  const btn=document.getElementById('ev-salva');
  btn.disabled=true;btn.textContent='⏳ Salvataggio...';
  const nome=document.getElementById('ev-nome').value.trim();
  if(!nome){alert('Il nome è obbligatorio.');btn.disabled=false;btn.textContent='💾 Crea Evento';return}
  const data=document.getElementById('ev-data').value;
  const ora=document.getElementById('ev-ora').value||'18:30';
  const ev={
   id:'e-'+Date.now(),titolo:nome,inizio:data+'T'+ora+':00',fine:data+'T23:59:00',
   location:document.getElementById('ev-loc').value.trim()||'—',
   citta:document.getElementById('ev-citta').value.trim(),
   ospiti:parseInt(document.getElementById('ev-osp').value)||0,
   bambini:parseInt(document.getElementById('ev-bam').value)||0,
   staff:parseInt(document.getElementById('ev-stf').value)||0,
   stato:'confermato',
   noteTutti:document.getElementById('ev-n-tutti').value,
   noteSala:document.getElementById('ev-n-sala').value,
   noteCucina:document.getElementById('ev-n-cucina').value,
   noteMagazzino:document.getElementById('ev-n-mag').value,
   notePrivata:document.getElementById('ev-n-priv')?document.getElementById('ev-n-priv').value:'',
   allegatiTutti:await leggiAllegati('ev-f-tutti'),
   allegatiSala:await leggiAllegati('ev-f-sala'),
   allegatiCucina:await leggiAllegati('ev-f-cucina'),
   allegatiMagazzino:await leggiAllegati('ev-f-mag'),
   allegatiPrivata:document.getElementById('ev-f-priv')?await leggiAllegati('ev-f-priv'):[],
   creatoDa:user.nome+' ('+user.ruolo+')',creatoIl:new Date().toISOString()
  };
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
  salvati.push(ev);
  localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
  EVENTI.push(ev);
  generaNotifEvento(ev);
  chiudiDrawer();
  alert('✅ Evento creato!');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}

/* Sovrascrivo apriModaleNoleggio per aggiungere campo Città */
function apriModaleNoleggio(){
 const oggi=new Date().toISOString().slice(0,10);
 const isAdmin=user.ruolo==='Amministratore';
 const isMag2=user.ruolo==='Magazzino2';
 const vediBolla=isAdmin||isMag2;
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Nuovo noleggio';
 document.getElementById('d-titolo').textContent='🚚 Crea Noleggio';
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Titolo <span style="color:#dc2626">*</span></label><input id="nl-titolo" placeholder="Es. Noleggio tavoli Rossi"></div>
  <div class="campo-2"><div class="campo"><label>Data inizio</label><input id="nl-di" type="date" value="${oggi}"></div><div class="campo"><label>Ora inizio</label><input id="nl-oi" type="time" value="09:00"></div></div>
  <div class="campo-2"><div class="campo"><label>Data fine</label><input id="nl-df" type="date" value="${oggi}"></div><div class="campo"><label>Ora fine</label><input id="nl-of" type="time" value="18:00"></div></div>
  <div class="campo"><label>📍 Nome location <span style="color:#dc2626">*</span></label><input id="nl-loc"></div>
  <div class="campo"><label>🌍 Città <span style="font-size:.7rem;font-weight:500;text-transform:none;color:#94a3b8;letter-spacing:0">(serve solo per il meteo)</span></label><input id="nl-citta" placeholder="Es. Catania"></div>
  <div class="campo-2"><div class="campo"><label>Referente <span style="color:#dc2626">*</span></label><input id="nl-ref"></div><div class="campo"><label>Telefono <span style="color:#dc2626">*</span></label><input id="nl-tel" type="tel"></div></div>
  <div class="campo"><label>Stato</label><select id="nl-stato" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff"><option value="confermato">Confermato</option><option value="non confermato">Non confermato</option></select></div>
  <div class="campo"><label>Note</label><textarea id="nl-note"></textarea></div>
  ${vediBolla?`<div class="divisore-modale">💰 Bolla con prezzo</div><div class="campo"><input type="file" id="nl-f-bolla" multiple accept="image/*,.pdf"></div>`:''}
  <div class="divisore-modale">📄 DDT</div><div class="campo"><input type="file" id="nl-f-ddt" multiple accept="image/*,.pdf"></div>
  <div class="divisore-modale">📎 Vario</div><div class="campo"><input type="file" id="nl-f-vario" multiple accept="image/*,.pdf"></div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="nl-salva">💾 Crea Noleggio</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('nl-salva').onclick=async()=>{
  const btn=document.getElementById('nl-salva');
  btn.disabled=true;btn.textContent='⏳ Salvataggio...';
  const titolo=document.getElementById('nl-titolo').value.trim();
  const loc=document.getElementById('nl-loc').value.trim();
  const ref=document.getElementById('nl-ref').value.trim();
  const tel=document.getElementById('nl-tel').value.trim();
  if(!titolo||!loc||!ref||!tel){alert('Compila tutti i campi obbligatori.');btn.disabled=false;btn.textContent='💾 Crea Noleggio';return}
  const nl={
   id:'n-'+Date.now(),tipo:'noleggio',titolo,
   inizio:document.getElementById('nl-di').value+'T'+(document.getElementById('nl-oi').value||'09:00')+':00',
   fine:document.getElementById('nl-df').value+'T'+(document.getElementById('nl-of').value||'18:00')+':00',
   location:loc,
   citta:document.getElementById('nl-citta').value.trim(),
   referente:ref,telefono:tel,
   stato:document.getElementById('nl-stato').value,
   note:document.getElementById('nl-note').value,
   allegatiBolla:vediBolla?await leggiAllegati('nl-f-bolla'):[],
   allegatiDDT:await leggiAllegati('nl-f-ddt'),
   allegatiVario:await leggiAllegati('nl-f-vario'),
   creatoDa:user.nome+' ('+user.ruolo+')',creatoIl:new Date().toISOString()
  };
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_noleggi'))||[]}catch(e){}
  salvati.push(nl);
  localStorage.setItem('ergo_noleggi',JSON.stringify(salvati));
  NOLEGGI.push(nl);
  generaNotifNoleggio(nl);
  chiudiDrawer();
  alert('✅ Noleggio creato!');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}

/* Aggiorna mostraMeteoDashboard per usare "citta" invece di "location" */
async function mostraMeteoDashboard(){
 const oggi=new Date();oggi.setHours(0,0,0,0);
 let prossimoEv=null,prossimoNl=null;
 EVENTI.forEach(e=>{const d=new Date(e.inizio);if(d>=oggi&&(!prossimoEv||new Date(e.inizio)<new Date(prossimoEv.inizio)))prossimoEv=e});
 NOLEGGI.forEach(n=>{const d=new Date(n.inizio);if(d>=oggi&&(!prossimoNl||new Date(n.inizio)<new Date(prossimoNl.inizio)))prossimoNl=n});

 const cdEv=document.getElementById('cd-e');
 if(cdEv){
  const vecchio=document.getElementById('meteo-evento');
  if(vecchio)vecchio.remove();
  const div=document.createElement('div');
  div.id='meteo-evento';
  cdEv.parentNode.appendChild(div);
  /* Usa "citta" (nuovo campo) oppure "location" (fallback vecchi eventi) */
  const citta=prossimoEv?(prossimoEv.citta||prossimoEv.location):null;
  if(citta&&citta!=='—'){
   mostraMeteoIn('meteo-evento',citta,prossimoEv.inizio);
  }
 }
 const cdNl=document.getElementById('cd-n');
 if(cdNl){
  const vecchio2=document.getElementById('meteo-noleggio');
  if(vecchio2)vecchio2.remove();
  const div2=document.createElement('div');
  div2.id='meteo-noleggio';
  cdNl.parentNode.appendChild(div2);
  const citta2=prossimoNl?(prossimoNl.citta||prossimoNl.location):null;
  if(citta2&&citta2!=='—'){
   mostraMeteoIn('meteo-noleggio',citta2,prossimoNl.inizio);
  }
 }
}
  /* ============================================================
   BLOCCO CORREZIONI v2
   ============================================================ */

/* 1) Blocca topbar sticky che va sopra "Bentornato" */
(function(){
 const s=document.createElement('style');
 s.textContent=`
  .topbar{position:relative !important;top:auto !important;background:#f7f8fb !important;border-bottom:1px solid var(--line) !important}
 `;
 document.head.appendChild(s);
})();

/* 2) Meteo in base all'ORARIO dell'evento */
async function mostraMeteoIn(idElemento,citta,dataEvento){
 const el=document.getElementById(idElemento);
 if(!el)return;
 el.innerHTML='<div style="font-size:.7rem;color:#94a3b8;padding:10px 0;text-align:center">🌤️ Cerco il meteo…</div>';
 try{
  const urlGeo='https://geocoding-api.open-meteo.com/v1/search?name='+encodeURIComponent(citta)+'&count=1&language=it&format=json';
  const rispGeo=await fetch(urlGeo);
  const datiGeo=await rispGeo.json();
  if(!datiGeo||!datiGeo.results||datiGeo.results.length===0){
   el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:10px 0;text-align:center">📍 Città non trovata</div>';
   return;
  }
  const lat=datiGeo.results[0].latitude;
  const lon=datiGeo.results[0].longitude;
  const cittàTrovata=datiGeo.results[0].name;

  const data=new Date(dataEvento);
  const oggi=new Date();
  const diffGiorni=Math.floor((data-oggi)/(1000*60*60*24));
  if(diffGiorni>16){
   el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:10px 0;text-align:center">📅 Meteo disponibile solo nei prossimi 16 giorni</div>';
   return;
  }
  const dataStr=data.toISOString().slice(0,10);
  /* Prendiamo meteo orario per avere quello dell'ora dell'evento */
  const urlMeteo='https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&hourly=temperature_2m,weathercode,precipitation_probability&timezone=auto&start_date='+dataStr+'&end_date='+dataStr;
  const rispMeteo=await fetch(urlMeteo);
  const datiMeteo=await rispMeteo.json();
  if(!datiMeteo||!datiMeteo.hourly||!datiMeteo.hourly.time){
   el.innerHTML='<div style="font-size:.68rem;color:#94a3b8;padding:10px 0;text-align:center">📅 Meteo non disponibile</div>';
   return;
  }
  /* Trova l'ora dell'evento */
  const oraEvento=data.getHours();
  const idxOra=datiMeteo.hourly.time.findIndex(t=>new Date(t).getHours()===oraEvento);
  const idx=idxOra>=0?idxOra:Math.floor(datiMeteo.hourly.time.length/2);
  const temp=Math.round(datiMeteo.hourly.temperature_2m[idx]);
  const code=datiMeteo.hourly.weathercode[idx];
  const pioggia=datiMeteo.hourly.precipitation_probability[idx]||0;
  const oraStr=String(oraEvento).padStart(2,'0')+':00';
  el.innerHTML=`
   <div style="background:linear-gradient(135deg,#f0f6ff,#eaf1fb);border:1px solid #cfe0f5;border-radius:12px;padding:12px;display:flex;align-items:center;gap:12px;margin-top:12px">
    <div style="font-size:2.2rem;line-height:1">${iconaMeteo(code)}</div>
    <div style="flex:1;min-width:0">
     <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.1em;color:#6b778c;font-weight:800">Meteo previsto · ${cittàTrovata} · ${oraStr}</div>
     <div style="font-size:.88rem;color:#083278;font-weight:700;margin-top:2px">${labelMeteo(code)}</div>
     <div style="font-size:.72rem;color:#6b778c;margin-top:2px">${temp}° · Pioggia ${pioggia}%</div>
    </div>
   </div>`;
 }catch(e){
  el.innerHTML='<div style="font-size:.68rem;color:#b91c1c;padding:10px 0;text-align:center">⚠️ Errore connessione meteo</div>';
 }
}

/* 3) Inventario: input quantità senza zero iniziale + più dati nella card */
function cardProd(p,isAdmin,vedePrezzo){
 const hasFoto=!!p.foto;
 return `<div class="inv-card">
  <div class="inv-foto">${hasFoto?`<img loading="lazy" src="${p.foto}">`:''}<span class="inv-badge-cat">${p.categoria||'—'}</span></div>
  <div class="inv-body">
   <div class="inv-nome">${p.nome||''}</div>
   <div class="inv-codice">Cod. ${p.codice||'—'}</div>
   <div class="inv-qta">📦 Quantità: ${p.quantita||0}</div>
   <div class="inv-info">📍 Posizione: <b>${p.posizione||'—'}</b></div>
   ${vedePrezzo?`<div class="inv-prezzo">€ ${(p.prezzo||0).toFixed(2)}</div>`:''}
   ${p.note?`<div style="font-size:.7rem;color:#94a3b8;line-height:1.4;margin-top:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">📝 ${p.note}</div>`:''}
   <div class="inv-azioni">
    <button class="inv-btn primario" data-azione="scheda" data-codice="${p.codice}">📋 Scheda</button>
    ${isAdmin?`<button class="inv-btn" data-azione="modifica" data-codice="${p.codice}">✏️</button>`:''}
    ${isAdmin?`<button class="inv-btn pericolo" data-azione="elimina" data-codice="${p.codice}">🗑️</button>`:''}
   </div>
  </div>
 </div>`;
}

/* 4) Scheda prodotto: solo dati tecnici + QR (quantità, posizione, prezzo li vedi già nella card) */
function apriSchedaProd(p){
 const scheda=p.scheda||{};
 const hasFoto=!!p.foto;
 const fotoHtml=hasFoto?`<img loading="lazy" src="${p.foto}" style="width:100%;height:100%;object-fit:cover">`:`<div style="font-size:4rem;opacity:.4">📦</div>`;
 let righe='';
 [['Materiale',scheda.materiale],['Colore',scheda.colore],['Dimensione',scheda.dimensione]].forEach(([k,v])=>{
  if(v&&v.trim())righe+=`<div style="display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px dashed #c9dcf0;font-size:.85rem"><span style="color:#6b778c;font-weight:600">${k}</span><span style="color:#344054;font-weight:700;text-align:right">${v}</span></div>`;
 });
 if(scheda.note&&scheda.note.trim())righe+=`<div style="padding:10px 0 0"><span style="color:#6b778c;font-weight:600;font-size:.7rem;text-transform:uppercase;letter-spacing:.08em">Note tecniche</span><div style="color:#526783;font-size:.85rem;line-height:1.5;margin-top:6px">${scheda.note}</div></div>`;
 const tech=righe?`<div style="background:#f3f8ff;border:1px solid #d7e7fa;border-radius:12px;padding:14px;margin-top:14px"><div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#083278;font-weight:800;margin-bottom:10px">📋 Scheda tecnica</div>${righe}</div>`:'<div style="background:#f8fafc;border:1px dashed #cbd5e1;border-radius:12px;padding:14px;margin-top:14px;text-align:center;color:#94a3b8;font-size:.8rem">Nessuna scheda tecnica</div>';
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Scheda tecnica';
 document.getElementById('d-titolo').textContent=p.nome;
 document.getElementById('d-body').innerHTML=`
  <div style="width:100%;aspect-ratio:1;background:linear-gradient(145deg,#eef4fa,#f8fafc);border-radius:14px;display:grid;place-items:center;overflow:hidden;color:#9ab1c9;margin-bottom:14px">${fotoHtml}</div>
  <div style="font-size:.75rem;color:#98a2b3;letter-spacing:.06em;margin-bottom:14px;text-transform:uppercase;font-weight:700">COD. ${p.codice}</div>
  ${tech}
  <div style="background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center;margin-top:14px">
   <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.12em;color:#083278;font-weight:800;margin-bottom:10px">🎫 QR Code prodotto</div>
   <canvas id="qr-canvas" width="180" height="180" style="display:block;margin:0 auto;border-radius:8px;border:1px solid var(--line)"></canvas>
   <div style="margin-top:12px"><button class="inv-btn primario" id="qr-scarica" style="padding:10px 16px">⬇️ Scarica QR</button></div>
  </div>`;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Chiudi</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 setTimeout(()=>{
  const c=document.getElementById('qr-canvas');
  if(c){
   const url=location.origin+location.pathname+'?codice='+encodeURIComponent(p.codice||'');
   const img=new Image();img.crossOrigin='anonymous';
   img.onload=()=>{const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,180,180);x.drawImage(img,0,0,180,180)};
   img.onerror=()=>{const x=c.getContext('2d');x.fillStyle='#f8fafc';x.fillRect(0,0,180,180);x.fillStyle='#98a2b3';x.font='12px sans-serif';x.textAlign='center';x.fillText('QR non disponibile',90,84);x.fillText('(richiede internet)',90,102)};
   img.src='https://api.qrserver.com/v1/create-qr-code/?size=180x180&data='+encodeURIComponent(url);
  }
  const bd=document.getElementById('qr-scarica');
  if(bd)bd.onclick=()=>{const c2=document.getElementById('qr-canvas');if(!c2)return;const a=document.createElement('a');a.download='QR_'+(p.codice||'prodotto')+'.png';a.href=c2.toDataURL('image/png');a.click()};
 },100);
}

/* 5) Dashboard: aggiungi data completa evento/noleggio sotto countdown */
(function(){
 const _orig=window.dash;
 if(_orig){
  window.dash=function(el){
   const r=_orig.apply(this,arguments);
   setTimeout(()=>{
    const oggi=new Date();oggi.setHours(0,0,0,0);
    let pe=null,pn=null;
    EVENTI.forEach(e=>{const d=new Date(e.inizio);if(d>=oggi&&(!pe||new Date(e.inizio)<new Date(pe.inizio)))pe=e});
    NOLEGGI.forEach(n=>{const d=new Date(n.inizio);if(d>=oggi&&(!pn||new Date(n.inizio)<new Date(pn.inizio)))pn=n});
    const cdEv=document.getElementById('cd-e');
    if(cdEv&&pe){
     const già=cdEv.parentNode.querySelector('.cd-data-evento');
     if(già)già.remove();
     const dataStr=new Date(pe.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
     const oraStr=new Date(pe.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
     const div=document.createElement('div');
     div.className='cd-data-evento';
     div.style.cssText='font-size:.72rem;color:#3e765e;text-align:center;margin-top:8px;font-weight:700;letter-spacing:.02em';
     div.textContent=dataStr.charAt(0).toUpperCase()+dataStr.slice(1)+' · ore '+oraStr;
     cdEv.parentNode.appendChild(div);
    }
    const cdNl=document.getElementById('cd-n');
    if(cdNl&&pn){
     const già2=cdNl.parentNode.querySelector('.cd-data-noleggio');
     if(già2)già2.remove();
     const dataStr2=new Date(pn.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
     const oraStr2=new Date(pn.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
     const div2=document.createElement('div');
     div2.className='cd-data-noleggio';
     div2.style.cssText='font-size:.72rem;color:#083278;text-align:center;margin-top:8px;font-weight:700;letter-spacing:.02em';
     div2.textContent=dataStr2.charAt(0).toUpperCase()+dataStr2.slice(1)+' · ore '+oraStr2;
     cdNl.parentNode.appendChild(div2);
    }
   },250);
   return r;
  };
 }
})();

/* 6) Modali evento/noleggio: rimuovi "(serve solo per il meteo)" dal campo Città */
(function(){
 /* Usa MutationObserver per modificare le label quando vengono create */
 const obs=new MutationObserver(()=>{
  document.querySelectorAll('label').forEach(l=>{
   if(l.textContent.includes('serve solo per il meteo')){
    l.innerHTML=l.innerHTML.replace(/\s*<span[^>]*>.*?serve solo per il meteo.*?<\/span>/,'');
   }
  });
 });
 obs.observe(document.body,{childList:true,subtree:true});
})();
  /* ============================================================
   FIX PDF LISTA ATTREZZATURE — v2 con grafica vera
   ============================================================ */
function eseguiInvioLista(){
 const idEv=document.getElementById('invio-evento').value;
 const ev=EVENTI.find(e=>e.id===idEv);
 if(!ev){alert('Evento non trovato.');return}

 /* Verifica che jsPDF sia caricato */
 if(!window.jspdf||!window.jspdf.jsPDF){
  alert('⚠️ Libreria PDF non caricata. Ricarica la pagina con Ctrl+Shift+R e riprova.');
  return;
 }

 /* Raggruppa per categoria */
 const gruppi={};
 listaAttrezzature.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });

 /* Genera PDF */
 const {jsPDF}=window.jspdf;
 const doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
 const paginaW=doc.internal.pageSize.getWidth();
 const margine=14;
 const larghezzaUtile=paginaW-margine*2;

 /* === HEADER BLU === */
 doc.setFillColor(8,50,120);
 doc.rect(0,0,paginaW,35,'F');
 doc.setTextColor(255,255,255);
 doc.setFont('helvetica','bold');
 doc.setFontSize(20);
 doc.text('Ergo & Scardaci',margine,16);
 doc.setFont('helvetica','normal');
 doc.setFontSize(10);
 doc.text('Lista Attrezzature',margine,24);
 doc.setFontSize(8);
 doc.text('Gestionale Eventi',paginaW-margine,14,{align:'right'});
 doc.text('Generata il '+new Date().toLocaleDateString('it-IT'),paginaW-margine,20,{align:'right'});

 /* === INFO EVENTO === */
 let y=48;
 doc.setTextColor(21,34,56);
 doc.setFont('helvetica','bold');
 doc.setFontSize(16);
 doc.text(ev.titolo||'Evento',margine,y);
 y+=8;
 doc.setFont('helvetica','normal');
 doc.setFontSize(10);
 doc.setTextColor(107,119,140);
 const dataEv=new Date(ev.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
 const oraEv=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 doc.text('Data: '+dataEv+' · ore '+oraEv,margine,y);y+=5;
 if(ev.location&&ev.location!=='—'){doc.text('Location: '+ev.location,margine,y);y+=5}
 if(ev.ospiti){doc.text('Ospiti: '+ev.ospiti+' · Bambini: '+(ev.bambini||0)+' · Staff: '+(ev.staff||0),margine,y);y+=5}

 /* === TOTALE === */
 y+=4;
 doc.setFillColor(234,241,251);
 doc.roundedRect(margine,y-5,larghezzaUtile,10,3,3,'F');
 doc.setTextColor(8,50,120);
 doc.setFont('helvetica','bold');
 doc.setFontSize(10);
 doc.text('TOTALE: '+listaAttrezzature.length+' articoli · '+Object.keys(gruppi).length+' categorie',margine+4,y+1.5);
 y+=14;

 /* === SEZIONI PER CATEGORIA === */
 Object.keys(gruppi).sort().forEach(cat=>{
  const items=gruppi[cat];
  if(y>250){doc.addPage();y=20}

  /* Titolo categoria con striscia colorata */
  doc.setFillColor(8,50,120);
  doc.rect(margine,y-5,3,9,'F');
  doc.setTextColor(8,50,120);
  doc.setFont('helvetica','bold');
  doc.setFontSize(11);
  doc.text(cat.toUpperCase()+' — '+items.length+' articoli',margine+6,y+1);
  y+=9;

  /* Intestazione tabella */
  doc.setFillColor(240,244,250);
  doc.rect(margine,y-4,larghezzaUtile,7,'F');
  doc.setTextColor(107,119,140);
  doc.setFont('helvetica','bold');
  doc.setFontSize(8);
  doc.text('PRODOTTO',margine+2,y);
  doc.text('CODICE',margine+larghezzaUtile*0.6,y);
  doc.text('POSIZIONE',margine+larghezzaUtile*0.78,y);
  doc.text('Q.TÀ',paginaW-margine-2,y,{align:'right'});
  y+=7;

  /* Righe prodotti */
  doc.setFont('helvetica','normal');
  items.forEach((item,i)=>{
   if(y>270){doc.addPage();y=20}
   /* Sfondo alternato */
   if(i%2===0){
    doc.setFillColor(250,251,253);
    doc.rect(margine,y-4,larghezzaUtile,7,'F');
   }
   doc.setTextColor(21,34,56);
   doc.setFontSize(9);
   doc.setFont('helvetica','bold');
   const nome=item.nome||'—';
   doc.text(nome.length>38?nome.substring(0,36)+'…':nome,margine+2,y);
   doc.setFont('helvetica','normal');
   doc.setFontSize(8);
   doc.setTextColor(107,119,140);
   doc.text(item.codice||'—',margine+larghezzaUtile*0.6,y);
   doc.text(item.posizione||'—',margine+larghezzaUtile*0.78,y);
   doc.setFont('helvetica','bold');
   doc.setFontSize(10);
   doc.setTextColor(8,50,120);
   doc.text('× '+(item.quantitaSelezionata||1),paginaW-margine-2,y,{align:'right'});
   y+=7;
  });
  y+=4;
 });

 /* === FOOTER su ogni pagina === */
 const tot=doc.internal.getNumberOfPages();
 for(let i=1;i<=tot;i++){
  doc.setPage(i);
  doc.setFontSize(7);
  doc.setTextColor(148,163,184);
  doc.text('Ergo & Scardaci · Lista Attrezzature',margine,290);
  doc.text('Pagina '+i+' di '+tot,paginaW-margine,290,{align:'right'});
 }

 /* === SALVA COME ALLEGATO === */
 const pdfBlob=doc.output('blob');
 const reader=new FileReader();
 reader.onload=function(){
  const dataUrl=reader.result;
  const nomePdf='Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf';

  /* Sostituisci TUTTI gli allegati lista esistenti */
  if(!ev.allegatiTutti)ev.allegatiTutti=[];
  ev.allegatiTutti=ev.allegatiTutti.filter(a=>!a.nome||!a.nome.startsWith('Lista_Attrezzature_'));
  ev.allegatiTutti.push({nome:nomePdf,mime:'application/pdf',size:pdfBlob.size,data:dataUrl});

  /* Salva in localStorage */
  let salvati=[];
  try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
  const idx=salvati.findIndex(e=>e.id===ev.id);
  if(idx>=0)salvati[idx]=ev;
  localStorage.setItem('ergo_eventi',JSON.stringify(salvati));

  /* Notifica */
  const nuovo={
   id:'nf-'+Date.now()+'-lista',
   tipo:'allegato',reparto:'tutti',
   titolo:'Lista attrezzature aggiornata: '+ev.titolo,
   sottotitolo:listaAttrezzature.length+' articoli · da '+user.nome,
   quando:new Date().toISOString(),
   da:user.nome+' ('+user.ruolo+')',
   dettagli:{evento:ev.titolo,data:new Date(ev.inizio).toLocaleDateString('it-IT'),location:ev.location,allegato:nomePdf}
  };
  NOTIFICHE.unshift(nuovo);
  let salvateN=[];
  try{salvateN=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
  salvateN.unshift(nuovo);
  localStorage.setItem('ergo_notifiche',JSON.stringify(salvateN.slice(0,200)));

  /* Salva lista anche in localStorage per poterla riaprire e modificare */
  const chiaveLista='ergo_lista_'+ev.id;
  const listaPerSalvare=listaAttrezzature.map(x=>({
   codice:x.codice,nome:x.nome,categoria:x.categoria,
   quantita:x.quantita,posizione:x.posizione,quantitaSelezionata:x.quantitaSelezionata
  }));
  localStorage.setItem(chiaveLista,JSON.stringify(listaPerSalvare));

  chiudiDrawer();
  alert('✅ PDF inviato a "'+ev.titolo+'"!\n\nPuoi riaprire la lista in qualsiasi momento da qui.');
  listaAttrezzature=[];
  lista(document.getElementById('pc'));
 };
 reader.readAsDataURL(pdfBlob);
}

/* ============================================================
   MODALE: SCELTA EVENTO — con opzione "carica lista esistente"
   ============================================================ */
function apriModaleInvioLista(){
 if(listaAttrezzature.length===0){alert('La lista è vuota.');return}
 const eventiDisponibili=EVENTI.slice().sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));
 if(eventiDisponibili.length===0){alert('Non ci sono eventi disponibili. Crea prima un evento.');return}
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Invia lista';
 document.getElementById('d-titolo').textContent='📤 Invia a evento';
 document.getElementById('d-body').innerHTML=`
  <p style="font-size:.85rem;color:#6b778c;margin-bottom:14px">Scegli l'evento a cui inviare questa lista attrezzature (<b>${listaAttrezzature.length} articoli</b>).</p>
  <div class="campo"><label>Evento di destinazione</label>
   <select id="invio-evento" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff">
    ${eventiDisponibili.map((e,i)=>{
     const d2=new Date(e.inizio).toLocaleDateString('it-IT',{day:'2-digit',month:'short',year:'numeric'});
     return `<option value="${e.id}" ${i===0?'selected':''}>${e.titolo} · ${d2}</option>`;
    }).join('')}
   </select>
  </div>
  <div class="campo">
   <label>Modalità</label>
   <div style="display:grid;gap:8px">
    <label style="display:flex;align-items:center;gap:8px;padding:11px;background:#eef2ff;border:1.5px solid #c7d2fe;border-radius:10px;cursor:pointer;font-size:.82rem">
     <input type="radio" name="modalita-invio" value="nuova" checked style="accent-color:#083278">
     <span><b>Invia come nuova lista</b><br><span style="font-size:.7rem;color:#6b778c">Il PDF verrà aggiunto agli allegati dell'evento</span></span>
    </label>
    <label style="display:flex;align-items:center;gap:8px;padding:11px;background:#f0fdf4;border:1.5px solid #bbf7d0;border-radius:10px;cursor:pointer;font-size:.82rem">
     <input type="radio" name="modalita-invio" value="sostituisci" style="accent-color:#3e765e">
     <span><b>Sostituisci lista esistente</b><br><span style="font-size:.7rem;color:#4d7c5a">Sovrascrive il PDF precedente della lista</span></span>
    </label>
   </div>
  </div>
  <div style="background:#f0f6ff;border:1px solid #d7e7fa;border-radius:10px;padding:12px;font-size:.78rem;color:#4b5563;line-height:1.5;margin-top:8px">
   📎 Il PDF verrà salvato nella sezione <b>Note per tutti</b> dell'evento scelto.
  </div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="invio-conferma">📤 Invia PDF</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('invio-conferma').onclick=eseguiInvioLista;
}

/* ============================================================
   RIPRISTINA LISTA ESISTENTE — quando apri un evento con lista
   ============================================================ */
function caricaListaDaEvento(idEvento){
 const chiave='ergo_lista_'+idEvento;
 try{
  const salvata=JSON.parse(localStorage.getItem(chiave));
  if(salvata&&Array.isArray(salvata)&&salvata.length>0){
   return salvata;
  }
 }catch(e){}
 return null;
}
  /* ============================================================
   FIX: LISTA ATTREZZATURE → PDF ELEGANTE + MODIFICABILE
   ============================================================ */

/* Salva lista nell'evento per poterla modificare dopo */
let _eventoListaCorrente=null;

function apriModaleInvioLista(){
 if(listaAttrezzature.length===0){alert('La lista è vuota.');return}
 const eventiDisponibili=EVENTI.slice().sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));
 if(eventiDisponibili.length===0){alert('Non ci sono eventi disponibili.');return}
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Invia lista';
 document.getElementById('d-titolo').textContent='📤 Invia PDF all\'evento';
 document.getElementById('d-body').innerHTML=`
  <p style="font-size:.85rem;color:#6b778c;margin-bottom:14px">Scegli l'evento a cui inviare questa lista (<b>${listaAttrezzature.length} articoli</b>). Verrà salvata come PDF nell'evento.</p>
  <div class="campo"><label>Evento di destinazione</label>
   <select id="invio-evento" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff">
    ${eventiDisponibili.map((e,i)=>{
     const d2=new Date(e.inizio).toLocaleDateString('it-IT',{day:'2-digit',month:'short',year:'numeric'});
     const haLista=e.listaAttrezzature&&e.listaAttrezzature.length>0;
     return `<option value="${e.id}" ${i===0?'selected':''}>${e.titolo} · ${d2}${haLista?' ⚠️ (ha già una lista)':''}</option>`;
    }).join('')}
   </select>
  </div>
  <div style="background:#f0f6ff;border:1px solid #d7e7fa;border-radius:10px;padding:12px;font-size:.78rem;color:#4b5563;line-height:1.5;margin-top:8px">
   📎 Il PDF verrà salvato in <b>Note per tutti</b>. Se l'evento ha già una lista, verrà <b>sostituita</b> con quella nuova (puoi sempre modificarle in seguito).
  </div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="invio-conferma">📤 Genera e invia PDF</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
 document.getElementById('invio-conferma').onclick=eseguiInvioListaPDF;
}

/* Genera PDF elegante della lista */
function generaPdfLista(ev,lista){
 const {jsPDF}=window.jspdf;
 const doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
 const paginaW=doc.internal.pageSize.getWidth();

 /* HEADER */
 doc.setFillColor(8,50,120);
 doc.rect(0,0,paginaW,30,'F');
 doc.setTextColor(255,255,255);
 doc.setFontSize(18);
 doc.setFont('helvetica','bold');
 doc.text('Ergo & Scardaci',14,13);
 doc.setFontSize(9);
 doc.setFont('helvetica','normal');
 doc.text('Lista Attrezzature',14,19);
 doc.text('Generata il '+new Date().toLocaleDateString('it-IT'),paginaW-14,13,{align:'right'});
 doc.text('Gestionale Eventi',paginaW-14,19,{align:'right'});

 /* INFO EVENTO */
 doc.setTextColor(21,34,56);
 doc.setFontSize(14);
 doc.setFont('helvetica','bold');
 doc.text(ev.titolo||'Evento',14,44);
 doc.setFontSize(10);
 doc.setFont('helvetica','normal');
 doc.setTextColor(107,119,140);
 const dataEv=new Date(ev.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
 const oraEv=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 doc.text('📅 '+dataEv+' · ore '+oraEv,14,51);
 if(ev.location)doc.text('📍 '+ev.location,14,57);

 /* Raggruppa per categoria */
 const gruppi={};
 lista.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });

 /* Contatore */
 doc.setTextColor(8,50,120);
 doc.setFontSize(10);
 doc.setFont('helvetica','bold');
 doc.text('TOTALE: '+lista.length+' articoli in '+Object.keys(gruppi).length+' categorie',14,68);

 /* Sezioni */
 let y=78;
 Object.keys(gruppi).sort().forEach(cat=>{
  const items=gruppi[cat];
  if(y>255){doc.addPage();y=20}
  /* Header categoria */
  doc.setFillColor(234,241,251);
  doc.roundedRect(14,y-5,paginaW-28,9,2,2,'F');
  doc.setTextColor(8,50,120);
  doc.setFontSize(11);
  doc.setFont('helvetica','bold');
  doc.text(cat.toUpperCase()+' ('+items.length+')',17,y+1);
  y+=11;
  /* Righe prodotti */
  items.forEach((item,i)=>{
   if(y>275){doc.addPage();y=20}
   /* Sfondo alternato */
   if(i%2===0){
    doc.setFillColor(250,251,253);
    doc.rect(14,y-4.5,paginaW-28,8,'F');
   }
   /* Nome */
   doc.setTextColor(21,34,56);
   doc.setFont('helvetica','bold');
   doc.setFontSize(9.5);
   doc.text((item.nome||'').substring(0,50),17,y);
   /* Codice e posizione piccoli */
   doc.setFont('helvetica','normal');
   doc.setFontSize(7.5);
   doc.setTextColor(148,163,184);
   const sub='Cod. '+(item.codice||'—')+' · Pos. '+(item.posizione||'—');
   doc.text(sub,17,y+3.5);
   /* Quantità grande a destra */
   doc.setFont('helvetica','bold');
   doc.setFontSize(12);
   doc.setTextColor(8,50,120);
   doc.text('× '+(item.quantitaSelezionata||1),paginaW-18,y,{align:'right'});
   /* Linea sottile */
   doc.setDrawColor(234,241,251);
   doc.setLineWidth(0.2);
   doc.line(14,y+5,paginaW-14,y+5);
   y+=9;
  });
  y+=4;
 });

 /* FOOTER */
 const totali=doc.internal.getNumberOfPages();
 for(let i=1;i<=totali;i++){
  doc.setPage(i);
  doc.setFontSize(7);
  doc.setTextColor(148,163,184);
  doc.text('Lista Attrezzature · Ergo & Scardaci',14,290);
  doc.text('Pagina '+i+' di '+totali,paginaW-14,290,{align:'right'});
 }

 return doc.output('blob');
}

function eseguiInvioListaPDF(){
 const idEv=document.getElementById('invio-evento').value;
 const ev=EVENTI.find(e=>e.id===idEv);
 if(!ev){alert('Evento non trovato.');return}
 const btn=document.getElementById('invio-conferma');
 btn.disabled=true;btn.textContent='⏳ Genero PDF...';

 try{
  /* 1. Genera PDF */
  const pdfBlob=generaPdfLista(ev,listaAttrezzature);
  const reader=new FileReader();
  reader.onload=function(){
   const dataUrl=reader.result;
   const nomePdf='Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf';

   /* 2. Rimuovi VECCHIO allegato lista (se esiste) */
   if(!ev.allegatiTutti)ev.allegatiTutti=[];
   ev.allegatiTutti=ev.allegatiTutti.filter(a=>!(a.nome&&a.nome.startsWith('Lista_Attrezzature_')));

   /* 3. Aggiungi nuovo allegato */
   ev.allegatiTutti.push({
    nome:nomePdf,
    mime:'application/pdf',
    size:pdfBlob.size,
    data:dataUrl
   });

   /* 4. Salva la lista DENTRO l'evento (per poterla modificare dopo) */
   ev.listaAttrezzature=listaAttrezzature.slice();

   /* 5. Salva in localStorage */
   let salvati=[];
   try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
   const idx=salvati.findIndex(e=>e.id===ev.id);
   if(idx>=0)salvati[idx]=ev;else salvati.push(ev);
   localStorage.setItem('ergo_eventi',JSON.stringify(salvati));

   /* 6. Rimuovi vecchia notifica lista se esiste */
   NOTIFICHE.forEach(n=>{
    if(n.tipo==='allegato'&&n.dettagli&&n.dettagli.evento===ev.titolo&&n.dettagli.allegato&&n.dettagli.allegato.startsWith('Lista_Attrezzature_'))n._vecchia=true;
   });
   /* 7. Aggiungi nuova notifica */
   const nuovo={
    id:'nf-'+Date.now()+'-lista',
    tipo:'allegato',
    reparto:'tutti',
    titolo:'Lista attrezzature inviata: '+ev.titolo,
    sottotitolo:listaAttrezzature.length+' articoli · da '+user.nome,
    quando:new Date().toISOString(),
    da:user.nome+' ('+user.ruolo+')',
    dettagli:{
     evento:ev.titolo,
     data:new Date(ev.inizio).toLocaleDateString('it-IT'),
     location:ev.location,
     allegato:nomePdf
    }
   };
   NOTIFICHE.unshift(nuovo);
   let salvateN=[];
   try{salvateN=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
   salvateN.unshift(nuovo);
   localStorage.setItem('ergo_notifiche',JSON.stringify(salvateN.slice(0,200)));

   chiudiDrawer();
   alert('✅ PDF generato e inviato a "'+ev.titolo+'"!');
   listaAttrezzature=[];
   lista(document.getElementById('pc'));
  };
  reader.readAsDataURL(pdfBlob);
 }catch(err){
  console.error(err);
  alert('❌ Errore generazione PDF: '+err.message);
  btn.disabled=false;btn.textContent='📤 Genera e invia PDF';
 }
}

/* ============================================================
   APRI LISTA DI UN EVENTO PER MODIFICARLA
   ============================================================ */
function apriListaEvento(ev){
 if(!ev.listaAttrezzature||ev.listaAttrezzature.length===0){
  alert('Questo evento non ha una lista attrezzature salvata.');
  return;
 }
 _eventoListaCorrente=ev;
 listaAttrezzature=ev.listaAttrezzature.slice();
 /* Vai alla sezione Lista Attrezzature */
 view='liste';
 app();
 setTimeout(()=>{
  /* Mostra avviso in cima */
  const pc=document.getElementById('pc');
  if(pc){
   const page=pc.querySelector('.page');
   if(page){
    const banner=document.createElement('div');
    banner.style.cssText='background:#fff4df;border:1.5px solid #fdba74;border-radius:12px;padding:12px 16px;margin-bottom:16px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap';
    banner.innerHTML='<div style="font-size:.8rem;color:#9a3412;font-weight:600">📝 Stai modificando la lista dell\'evento <b>'+ev.titolo+'</b></div><div style="display:flex;gap:8px"><button id="lista-annulla-mod" style="padding:8px 14px;border-radius:9px;border:1.5px solid #fdba74;background:#fff;color:#9a3412;font-weight:700;font-size:.75rem;cursor:pointer">Annulla</button></div>';
    page.insertBefore(banner,page.firstChild);
    document.getElementById('lista-annulla-mod').onclick=()=>{
     _eventoListaCorrente=null;
     listaAttrezzature=[];
     view='calendario';
     app();
    };
   }
  }
  /* Cambia il pulsante "Invia" in "Aggiorna" */
  setTimeout(()=>{
   const btnInv=document.getElementById('lista-invia');
   if(btnInv){
    btnInv.textContent='🔄 Aggiorna evento';
    btnInv.onclick=()=>{
     /* Salva direttamente aggiornando l'evento, senza chiedere di nuovo */
     eseguiAggiornamentoLista(ev);
    };
   }
  },100);
 },300);
}

function eseguiAggiornamentoLista(ev){
 if(listaAttrezzature.length===0){alert('La lista è vuota.');return}
 try{
  const pdfBlob=generaPdfLista(ev,listaAttrezzature);
  const reader=new FileReader();
  reader.onload=function(){
   const dataUrl=reader.result;
   const nomePdf='Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf';
   if(!ev.allegatiTutti)ev.allegatiTutti=[];
   ev.allegatiTutti=ev.allegatiTutti.filter(a=>!(a.nome&&a.nome.startsWith('Lista_Attrezzature_')));
   ev.allegatiTutti.push({nome:nomePdf,mime:'application/pdf',size:pdfBlob.size,data:dataUrl});
   ev.listaAttrezzature=listaAttrezzature.slice();
   let salvati=[];
   try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
   const idx=salvati.findIndex(e=>e.id===ev.id);
   if(idx>=0)salvati[idx]=ev;else salvati.push(ev);
   localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
   _eventoListaCorrente=null;
   listaAttrezzature=[];
   alert('✅ Lista aggiornata per "'+ev.titolo+'"!');
   view='calendario';
   app();
  };
  reader.readAsDataURL(pdfBlob);
 }catch(err){
  alert('❌ Errore: '+err.message);
 }
}

/* Modifica apriDrawerEnt per aggiungere pulsante "Modifica lista" se l'evento ha una lista */
(function(){
 const _orig=window.apriDrawerEnt;
 if(_orig){
  window.apriDrawerEnt=function(tipo,obj){
   const r=_orig.apply(this,arguments);
   if(tipo==='evento'&&obj.listaAttrezzature&&obj.listaAttrezzature.length>0){
    setTimeout(()=>{
     const foot=document.getElementById('d-foot');
     if(foot&&!document.getElementById('d-mod-lista')){
      const b=document.createElement('button');
      b.id='d-mod-lista';
      b.className='btn-ghost';
      b.style.color='#9a3412';
      b.style.borderColor='#fdba74';
      b.style.background='#fff4df';
      b.style.display='inline-flex';
      b.style.alignItems='center';
      b.style.gap='6px';
      b.innerHTML='✏️ Modifica lista';
      b.onclick=()=>{chiudiDrawer();apriListaEvento(obj)};
      foot.appendChild(b);
     }
    },150);
   }
   return r;
  };
 }
})();
  /* ============================================================
   FIX PDF LISTA — Grafica sobria e pulita
   ============================================================ */
function generaPdfLista(ev,lista){
 const {jsPDF}=window.jspdf;
 const doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
 const paginaW=doc.internal.pageSize.getWidth();
 const margine=18;
 const larghezza=paginaW-margine*2;

 /* --- TITOLO --- */
 doc.setTextColor(21,34,56);
 doc.setFont('helvetica','bold');
 doc.setFontSize(22);
 doc.text('LISTA ATTREZZATURE',margine,28);

 /* --- NOME EVENTO --- */
 doc.setFontSize(14);
 doc.setTextColor(8,50,120);
 doc.text(ev.titolo||'Evento',margine,40);

 /* --- INFO EVENTO (piccole, grigie) --- */
 doc.setFont('helvetica','normal');
 doc.setFontSize(10);
 doc.setTextColor(107,119,140);
 const dataEv=new Date(ev.inizio).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
 const oraEv=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 doc.text('Data: '+dataEv+' - ore '+oraEv,margine,47);
 if(ev.location&&ev.location!=='—')doc.text('Location: '+ev.location,margine,52);

 /* --- LINEA SEPARATRICE --- */
 doc.setDrawColor(200,215,235);
 doc.setLineWidth(0.5);
 doc.line(margine,58,paginaW-margine,58);

 /* --- RAGGRUPPA PER CATEGORIA --- */
 const gruppi={};
 lista.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });

 /* --- SEZIONI --- */
 let y=70;
 Object.keys(gruppi).sort().forEach(cat=>{
  const items=gruppi[cat];
  if(y>240){doc.addPage();y=25}

  /* Titolo categoria */
  doc.setFillColor(8,50,120);
  doc.rect(margine,y-6,larghezza,10,'F');
  doc.setTextColor(255,255,255);
  doc.setFont('helvetica','bold');
  doc.setFontSize(10);
  doc.text(cat.toUpperCase(),margine+4,y+1);
  doc.text(items.length+' articoli',paginaW-margine-4,y+1,{align:'right'});
  y+=14;

  /* Righe prodotti */
  items.forEach((item,i)=>{
   if(y>270){doc.addPage();y=25}

   /* Sfondo alternato leggero */
   if(i%2===0){
    doc.setFillColor(248,250,252);
    doc.rect(margine,y-5,larghezza,9,'F');
   }

   /* Nome prodotto (sx) */
   doc.setTextColor(21,34,56);
   doc.setFont('helvetica','bold');
   doc.setFontSize(10);
   const nome=(item.nome||'').substring(0,45);
   doc.text(nome,margine+2,y);

   /* Codice + posizione (sotto il nome, piccolo) */
   doc.setFont('helvetica','normal');
   doc.setFontSize(8);
   doc.setTextColor(148,163,184);
   const dettagli='Cod. '+(item.codice||'-')+'   Pos. '+(item.posizione||'-');
   doc.text(dettagli,margine+2,y+3.5);

   /* Quantità (accanto al nome, non a destra dello schermo) */
   doc.setFont('helvetica','bold');
   doc.setFontSize(11);
   doc.setTextColor(8,50,120);
   doc.text('x '+(item.quantitaSelezionata||1),paginaW-margine-4,y,{align:'right'});

   /* Linea sottile */
   doc.setDrawColor(230,236,244);
   doc.setLineWidth(0.2);
   doc.line(margine,y+5.5,paginaW-margine,y+5.5);

   y+=11;
  });
  y+=6;
 });

 /* --- TOTALE FINALE --- */
 if(y>260){doc.addPage();y=25}
 doc.setDrawColor(200,215,235);
 doc.setLineWidth(0.5);
 doc.line(margine,y-4,paginaW-margine,y-4);
 doc.setTextColor(8,50,120);
 doc.setFont('helvetica','bold');
 doc.setFontSize(11);
 doc.text('Totale: '+lista.length+' articoli in '+Object.keys(gruppi).length+' categorie',margine,y+4);

 /* --- FOOTER --- */
 const totali=doc.internal.getNumberOfPages();
 for(let i=1;i<=totali;i++){
  doc.setPage(i);
  doc.setFontSize(8);
  doc.setTextColor(148,163,184);
  doc.setFont('helvetica','normal');
  doc.text('Lista Attrezzature - '+ev.titolo,margine,290);
  doc.text('Pagina '+i+' di '+totali,paginaW-margine,290,{align:'right'});
 }

 return doc.output('blob');
}
  /* ============================================================
   FIX MAGAZZINO2 — Solo noleggi, niente eventi
   ============================================================ */

/* 1) Dashboard: nascondi card evento per Magazzino2 */
(function(){
 const _orig=window.dash;
 if(_orig){
  window.dash=function(el){
   /* Se è Magazzino2, dopo il render nascondi la card evento */
   if(user.ruolo==='Magazzino2'){
    const risultato=_orig.apply(this,arguments);
    setTimeout(()=>{
     /* Nascondi card evento */
     const cdEv=document.getElementById('cd-e');
     if(cdEv){
      const cardEvento=cdEv.closest('.cd-card');
      if(cardEvento){
       cardEvento.style.display='none';
       /* Se c'è solo la card evento visibile, nascondi anche il contenitore */
       const container=cardEvento.parentNode;
       if(container&&container.querySelectorAll('.cd-card:not([style*="display: none"])').length===0){
        container.style.display='none';
       }
      }
     }
     /* Nascondi meteo evento */
     const meteoEv=document.getElementById('meteo-evento');
     if(meteoEv)meteoEv.remove();
     /* Nascondi titolo "Prossimo evento" */
     document.querySelectorAll('.cd-card').forEach(c=>{
      const label=c.querySelector('.cd-label');
      if(label&&label.textContent.includes('Prossimo evento'))c.style.display='none';
     });
    },150);
    return risultato;
   }
   return _orig.apply(this,arguments);
  };
 }
})();

/* 2) Notifiche Magazzino2: SOLO noleggio (creato/modificato) */
function notifichePerUtente(utente){
 const mappa={
  'Amministratore':['tutti','sala','cucina','magazzino','admin'],
  'Wedding':['tutti','sala','cucina','magazzino'],
  'Cucina':['tutti','cucina'],
  'Sala':['tutti','sala'],
  'Magazzino':['tutti','magazzino','admin'],
  'Magazzino2':['magazzino']
 };
 const rep=mappa[utente.ruolo]||['tutti'];
 return NOTIFICHE.filter(n=>{
  if(!rep.includes(n.reparto))return false;
  /* Magazzino2 vede SOLO notifiche di tipo "noleggio" */
  if(utente.ruolo==='Magazzino2'){
   return n.tipo==='noleggio';
  }
  return true;
 });
}

/* 3) Calendario: Magazzino2 vede solo noleggi */
function cal(el){
 if(user.ruolo==='Magazzino2'){
  /* Forza filtro su noleggi */
  calFiltro='noleggi';
 }
 const anno=calAnno,mese=calMese;
 const oggi=new Date();oggi.setHours(0,0,0,0);
 const primo=new Date(anno,mese,1);
 const inizioSett=(primo.getDay()+6)%7;
 const ggMese=new Date(anno,mese+1,0).getDate();
 const celle=[];
 for(let i=0;i<inizioSett;i++)celle.push(null);
 for(let d=1;d<=ggMese;d++)celle.push(new Date(anno,mese,d));
 while(celle.length%7!==0)celle.push(null);
 const filtroAttivo=calFiltro||'tutti';
 const mostraEventi=filtroAttivo==='tutti'||filtroAttivo==='catering';
 const mostraNoleggi=filtroAttivo==='tutti'||filtroAttivo==='noleggi';
 const vedE=puoVedere(user.ruolo,'evento')&&mostraEventi;
 const vedN=puoVedere(user.ruolo,'noleggio')&&mostraNoleggi;
 const creaE=puoCreare(user.ruolo,'evento');
 const creaN=puoCreare(user.ruolo,'noleggio');
 let bottoni='';
 if(creaE)bottoni+=`<button class="btn-crea evento" id="btn-nuovo-evento">＋ Crea Evento</button>`;
 if(creaN)bottoni+=`<button class="btn-crea noleggio" id="btn-nuovo-noleggio">＋ Crea Noleggio</button>`;
 let legenda='';
 if(vedE)legenda+=`<span><i style="background:#bbf7d0"></i>Evento</span>`;
 if(vedN)legenda+=`<span><i style="background:#bfdbfe"></i>Noleggio</span><span><i style="background:#fed7aa"></i>Da confermare</span>`;
 /* Magazzino2 NON deve vedere il filtro perché vede solo noleggi */
 const puoFiltrare=puoVedere(user.ruolo,'evento')&&puoVedere(user.ruolo,'noleggio')&&user.ruolo!=='Magazzino2';
 const filtroHtml=puoFiltrare?`<div class="cal-filtro"><button class="${filtroAttivo==='tutti'?'active':''}" data-filtro="tutti">Tutti</button><button class="${filtroAttivo==='catering'?'active':''}" data-filtro="catering">🍽️ Catering</button><button class="${filtroAttivo==='noleggi'?'active':''}" data-filtro="noleggi">🚚 Noleggi</button></div>`:'';
 el.innerHTML=`<div class="page">
  <div style="margin-bottom:22px"><p class="eyebrow">Pianificazione</p><h1 class="title">Calendario ${user.ruolo==='Magazzino2'?'Noleggi':''}</h1><p class="lede">${filtroAttivo==='catering'?'Solo eventi catering.':filtroAttivo==='noleggi'?'Solo noleggi.':'Eventi e noleggi in un\'unica vista mensile.'}</p></div>
  <div class="cal-toolbar">
   <div class="cal-nav">
    <button id="cal-prev">‹</button>
    <span class="mese">${MESI[mese]} <select id="cal-anno-sel">${[2025,2026,2027,2028,2029,2030,2031,2032].map(a=>`<option value="${a}" ${a===anno?'selected':''}>${a}</option>`).join('')}</select></span>
    <button id="cal-next">›</button>
    <button id="cal-oggi" style="width:auto;padding:0 12px;font-size:.72rem;font-weight:700">Oggi</button>
   </div>
   <div class="cal-azioni">${bottoni}</div>
  </div>
  ${filtroHtml}
  <div class="cal-legenda">${legenda}</div>
  <div style="overflow-x:auto"><div class="cal-griglia">
   ${GIORNI.map(g=>`<div class="cal-int">${g}</div>`).join('')}
   ${celle.map((d,i)=>{
     if(!d)return `<div class="cal-giorno vuoto"></div>`;
     const eventiG=vedE?EVENTI.filter(e=>stessaData(e.inizio,d)):[];
     const nolG=vedN?NOLEGGI.filter(n=>inRange(d,n)):[];
     const isOggi=d.getTime()===oggi.getTime();
     let cls='cal-giorno';
     if(eventiG.length&&nolG.length)cls+=' ha-entrambi';
     else if(eventiG.length)cls+=' ha-eventi';
     else if(nolG.length)cls+=' ha-noleggi';
     if(isOggi)cls+=' oggi';
     let chips='';
     eventiG.slice(0,2).forEach(e=>{chips+=`<span class="cal-chip evento" data-id="${e.id}" data-tipo="evento">${e.titolo}</span>`});
     nolG.slice(0,2).forEach(n=>{const pend=n.stato!=='confermato';chips+=`<span class="cal-chip noleggio ${pend?'pending':''}" data-id="${n.id}" data-tipo="noleggio">${n.titolo}</span>`});
     const tot=eventiG.length+nolG.length;
     if(tot>2)chips+=`<span class="cal-chip piu">+${tot-2}</span>`;
     return `<div class="${cls}" data-giorno="${d.toISOString()}"><span class="num">${d.getDate()}</span>${chips}</div>`;
   }).join('')}
  </div></div>
  <div class="cal-pannello" id="cal-pannello"></div>
 </div>`;
 document.getElementById('cal-prev').onclick=()=>{calMese--;if(calMese<0){calMese=11;calAnno--}cal(el)};
 document.getElementById('cal-next').onclick=()=>{calMese++;if(calMese>11){calMese=0;calAnno++}cal(el)};
 document.getElementById('cal-oggi').onclick=()=>{const n=new Date();calMese=n.getMonth();calAnno=n.getFullYear();cal(el)};
 document.getElementById('cal-anno-sel').onchange=e=>{calAnno=parseInt(e.target.value);cal(el)};
 const be=document.getElementById('btn-nuovo-evento'),bn=document.getElementById('btn-nuovo-noleggio');
 if(be)be.onclick=()=>apriModaleEvento();
 if(bn)bn.onclick=()=>apriModaleNoleggio();
 el.querySelectorAll('.cal-filtro button').forEach(b=>{b.onclick=()=>{calFiltro=b.dataset.filtro;cal(el)}});
 document.querySelectorAll('.cal-chip[data-id]').forEach(c=>{
  c.onclick=e=>{e.stopPropagation();const id=c.dataset.id,tipo=c.dataset.tipo;
   if(tipo==='evento'){const ev=EVENTI.find(x=>x.id===id);if(ev)apriDrawerEnt('evento',ev)}
   else{const nl=NOLEGGI.find(x=>x.id===id);if(nl)apriDrawerEnt('noleggio',nl)}
  };
 });
 document.querySelectorAll('.cal-giorno[data-giorno]').forEach(g=>{
  g.onclick=()=>{const dt=new Date(g.dataset.giorno);mostraPann(dt);document.querySelectorAll('.cal-giorno').forEach(x=>x.style.outline='');g.style.outline='2px solid var(--blue)'};
 });
}
  /* ============================================================
   PDF LISTA ATTREZZATURE — versione DEFINITIVA v3
   ============================================================ */
function generaPdfLista(ev,lista){
 const {jsPDF}=window.jspdf;
 const doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
 const paginaW=doc.internal.pageSize.getWidth();
 const margine=18;
 const larghezza=paginaW-margine*2;

 /* TITOLO */
 doc.setTextColor(21,34,56);
 doc.setFont('helvetica','bold');
 doc.setFontSize(22);
 doc.text('LISTA ATTREZZATURE',margine,28);

 /* NOME EVENTO */
 doc.setFontSize(14);
 doc.setTextColor(8,50,120);
 doc.text(ev.titolo||'Evento',margine,40);

 /* INFO EVENTO */
 doc.setFont('helvetica','normal');
 doc.setFontSize(10);
 doc.setTextColor(107,119,140);
 const dataEv=new Date(ev.inizio).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
 const oraEv=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 doc.text('Data: '+dataEv+' - ore '+oraEv,margine,47);
 if(ev.location&&ev.location!=='—')doc.text('Location: '+ev.location,margine,52);

 /* LINEA */
 doc.setDrawColor(200,215,235);
 doc.setLineWidth(0.5);
 doc.line(margine,58,paginaW-margine,58);

 /* RAGGRUPPA */
 const gruppi={};
 lista.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });

 /* SEZIONI */
 let y=70;
 Object.keys(gruppi).sort().forEach(cat=>{
  const items=gruppi[cat];
  if(y>240){doc.addPage();y=25}
  /* Titolo categoria */
  doc.setFillColor(8,50,120);
  doc.rect(margine,y-6,larghezza,10,'F');
  doc.setTextColor(255,255,255);
  doc.setFont('helvetica','bold');
  doc.setFontSize(10);
  doc.text(cat.toUpperCase(),margine+4,y+1);
  doc.text(items.length+' articoli',paginaW-margine-4,y+1,{align:'right'});
  y+=14;
  /* Righe */
  items.forEach((item,i)=>{
   if(y>270){doc.addPage();y=25}
   if(i%2===0){
    doc.setFillColor(248,250,252);
    doc.rect(margine,y-5,larghezza,9,'F');
   }
   doc.setTextColor(21,34,56);
   doc.setFont('helvetica','bold');
   doc.setFontSize(10);
   doc.text((item.nome||'').substring(0,45),margine+2,y);
   doc.setFont('helvetica','normal');
   doc.setFontSize(8);
   doc.setTextColor(148,163,184);
   doc.text('Cod. '+(item.codice||'-')+'   Pos. '+(item.posizione||'-'),margine+2,y+3.5);
   doc.setFont('helvetica','bold');
   doc.setFontSize(11);
   doc.setTextColor(8,50,120);
   doc.text('x '+(item.quantitaSelezionata||1),paginaW-margine-4,y,{align:'right'});
   doc.setDrawColor(230,236,244);
   doc.setLineWidth(0.2);
   doc.line(margine,y+5.5,paginaW-margine,y+5.5);
   y+=11;
  });
  y+=6;
 });

 /* TOTALE */
 if(y>260){doc.addPage();y=25}
 doc.setDrawColor(200,215,235);
 doc.setLineWidth(0.5);
 doc.line(margine,y-4,paginaW-margine,y-4);
 doc.setTextColor(8,50,120);
 doc.setFont('helvetica','bold');
 doc.setFontSize(11);
 doc.text('Totale: '+lista.length+' articoli in '+Object.keys(gruppi).length+' categorie',margine,y+4);

 /* FOOTER */
 const totali=doc.internal.getNumberOfPages();
 for(let i=1;i<=totali;i++){
  doc.setPage(i);
  doc.setFontSize(8);
  doc.setTextColor(148,163,184);
  doc.setFont('helvetica','normal');
  doc.text('Lista Attrezzature - '+ev.titolo,margine,290);
  doc.text('Pagina '+i+' di '+totali,paginaW-margine,290,{align:'right'});
 }

 return doc.output('blob');
}

/* Forza eseguiInvioListaPDF a usare SOLO la versione nuova */
function eseguiInvioListaPDF(){
 const idEv=document.getElementById('invio-evento').value;
 const ev=EVENTI.find(e=>e.id===idEv);
 if(!ev){alert('Evento non trovato.');return}
 const btn=document.getElementById('invio-conferma');
 btn.disabled=true;btn.textContent='⏳ Genero PDF...';
 try{
  const pdfBlob=generaPdfLista(ev,listaAttrezzature);
  const reader=new FileReader();
  reader.onload=function(){
   const dataUrl=reader.result;
   const nomePdf='Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf';
   if(!ev.allegatiTutti)ev.allegatiTutti=[];
   ev.allegatiTutti=ev.allegatiTutti.filter(a=>!(a.nome&&a.nome.startsWith('Lista_Attrezzature_')));
   ev.allegatiTutti.push({nome:nomePdf,mime:'application/pdf',size:pdfBlob.size,data:dataUrl});
   ev.listaAttrezzature=listaAttrezzature.slice();
   let salvati=[];
   try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
   const idx=salvati.findIndex(e=>e.id===ev.id);
   if(idx>=0)salvati[idx]=ev;else salvati.push(ev);
   localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
   const nuovo={
    id:'nf-'+Date.now()+'-lista',
    tipo:'allegato',reparto:'tutti',
    titolo:'Lista attrezzature inviata: '+ev.titolo,
    sottotitolo:listaAttrezzature.length+' articoli · da '+user.nome,
    quando:new Date().toISOString(),
    da:user.nome+' ('+user.ruolo+')',
    dettagli:{evento:ev.titolo,data:new Date(ev.inizio).toLocaleDateString('it-IT'),location:ev.location,allegato:nomePdf}
   };
   NOTIFICHE.unshift(nuovo);
   let salvateN=[];
   try{salvateN=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
   salvateN.unshift(nuovo);
   localStorage.setItem('ergo_notifiche',JSON.stringify(salvateN.slice(0,200)));
   chiudiDrawer();
   alert('✅ PDF generato e inviato a "'+ev.titolo+'"!');
   listaAttrezzature=[];
   lista(document.getElementById('pc'));
  };
  reader.readAsDataURL(pdfBlob);
 }catch(err){
  console.error(err);
  alert('❌ Errore generazione PDF: '+err.message);
  btn.disabled=false;btn.textContent='📤 Genera e invia PDF';
 }
}
  /* ============================================================
   LISTA ATTREZZATURE → PDF PROFESSIONALE (v4 DEFINITIVA)
   Sovrascrive completamente qualsiasi versione precedente
   ============================================================ */

/* Blocca tutte le versioni precedenti */
window.eseguiInvioLista=null;
window.eseguiInvioListaPDF=null;
window.generaPdfLista=null;

/* Generatore PDF pulito e professionale */
function generaPdfListaNuovo(ev,lista){
 const {jsPDF}=window.jspdf;
 const doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
 const paginaW=doc.internal.pageSize.getWidth();
 const margine=18;
 const larghezza=paginaW-margine*2;

 /* Intestazione: solo titolo + nome evento */
 doc.setTextColor(21,34,56);
 doc.setFont('helvetica','bold');
 doc.setFontSize(22);
 doc.text('LISTA ATTREZZATURE',margine,28);

 doc.setFontSize(14);
 doc.setTextColor(8,50,120);
 doc.text(ev.titolo||'Evento',margine,40);

 doc.setFont('helvetica','normal');
 doc.setFontSize(10);
 doc.setTextColor(107,119,140);
 const dataEv=new Date(ev.inizio).toLocaleDateString('it-IT',{day:'numeric',month:'long',year:'numeric'});
 const oraEv=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
 doc.text('Data: '+dataEv+' - ore '+oraEv,margine,47);
 if(ev.location&&ev.location!=='—')doc.text('Location: '+ev.location,margine,52);

 doc.setDrawColor(200,215,235);
 doc.setLineWidth(0.5);
 doc.line(margine,58,paginaW-margine,58);

 /* Raggruppa per categoria */
 const gruppi={};
 lista.forEach(item=>{
  const cat=item.categoria||'ALTRO';
  if(!gruppi[cat])gruppi[cat]=[];
  gruppi[cat].push(item);
 });

 let y=70;
 Object.keys(gruppi).sort().forEach(cat=>{
  const items=gruppi[cat];
  if(y>240){doc.addPage();y=25}

  /* Barra categoria */
  doc.setFillColor(8,50,120);
  doc.rect(margine,y-6,larghezza,10,'F');
  doc.setTextColor(255,255,255);
  doc.setFont('helvetica','bold');
  doc.setFontSize(10);
  doc.text(cat.toUpperCase(),margine+4,y+1);
  doc.text(items.length+' articoli',paginaW-margine-4,y+1,{align:'right'});
  y+=14;

  items.forEach((item,i)=>{
   if(y>270){doc.addPage();y=25}
   if(i%2===0){
    doc.setFillColor(248,250,252);
    doc.rect(margine,y-5,larghezza,9,'F');
   }
   /* Nome a sinistra */
   doc.setTextColor(21,34,56);
   doc.setFont('helvetica','bold');
   doc.setFontSize(10);
   doc.text((item.nome||'').substring(0,45),margine+2,y);

   /* Codice e posizione sotto, piccoli */
   doc.setFont('helvetica','normal');
   doc.setFontSize(8);
   doc.setTextColor(148,163,184);
   doc.text('Cod. '+(item.codice||'-')+'   Pos. '+(item.posizione||'-'),margine+2,y+3.5);

   /* Quantità a destra, sempre nella stessa riga */
   doc.setFont('helvetica','bold');
   doc.setFontSize(11);
   doc.setTextColor(8,50,120);
   doc.text('x '+(item.quantitaSelezionata||1),paginaW-margine-4,y,{align:'right'});

   doc.setDrawColor(230,236,244);
   doc.setLineWidth(0.2);
   doc.line(margine,y+5.5,paginaW-margine,y+5.5);
   y+=11;
  });
  y+=6;
 });

 if(y>260){doc.addPage();y=25}
 doc.setDrawColor(200,215,235);
 doc.setLineWidth(0.5);
 doc.line(margine,y-4,paginaW-margine,y-4);
 doc.setTextColor(8,50,120);
 doc.setFont('helvetica','bold');
 doc.setFontSize(11);
 doc.text('Totale: '+lista.length+' articoli in '+Object.keys(gruppi).length+' categorie',margine,y+4);

 const totali=doc.internal.getNumberOfPages();
 for(let i=1;i<=totali;i++){
  doc.setPage(i);
  doc.setFontSize(8);
  doc.setTextColor(148,163,184);
  doc.setFont('helvetica','normal');
  doc.text('Lista Attrezzature - '+ev.titolo,margine,290);
  doc.text('Pagina '+i+' di '+totali,paginaW-margine,290,{align:'right'});
 }
 return doc.output('blob');
}

/* Funzione che genera e salva il PDF */
function eseguiInvioListaV4(){
 const idEv=document.getElementById('invio-evento').value;
 const ev=EVENTI.find(e=>e.id===idEv);
 if(!ev){alert('Evento non trovato.');return}
 const btn=document.getElementById('invio-conferma');
 btn.disabled=true;btn.textContent='⏳ Genero PDF...';
 try{
  const pdfBlob=generaPdfListaNuovo(ev,listaAttrezzature);
  const reader=new FileReader();
  reader.onload=function(){
   const dataUrl=reader.result;
   const nomePdf='Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf';
   if(!ev.allegatiTutti)ev.allegatiTutti=[];
   ev.allegatiTutti=ev.allegatiTutti.filter(a=>!(a.nome&&a.nome.startsWith('Lista_Attrezzature_')));
   ev.allegatiTutti.push({nome:nomePdf,mime:'application/pdf',size:pdfBlob.size,data:dataUrl});
   ev.listaAttrezzature=listaAttrezzature.slice();
   let salvati=[];
   try{salvati=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
   const idx=salvati.findIndex(e=>e.id===ev.id);
   if(idx>=0)salvati[idx]=ev;else salvati.push(ev);
   localStorage.setItem('ergo_eventi',JSON.stringify(salvati));
   const nuovo={
    id:'nf-'+Date.now()+'-lista',
    tipo:'allegato',reparto:'tutti',
    titolo:'Lista attrezzature inviata: '+ev.titolo,
    sottotitolo:listaAttrezzature.length+' articoli · da '+user.nome,
    quando:new Date().toISOString(),
    da:user.nome+' ('+user.ruolo+')',
    dettagli:{evento:ev.titolo,data:new Date(ev.inizio).toLocaleDateString('it-IT'),location:ev.location,allegato:nomePdf}
   };
   NOTIFICHE.unshift(nuovo);
   let salvateN=[];
   try{salvateN=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
   salvateN.unshift(nuovo);
   localStorage.setItem('ergo_notifiche',JSON.stringify(salvateN.slice(0,200)));
   chiudiDrawer();
   alert('✅ PDF generato e inviato a "'+ev.titolo+'"!');
   listaAttrezzature=[];
   lista(document.getElementById('pc'));
  };
  reader.readAsDataURL(pdfBlob);
 }catch(err){
  console.error(err);
  alert('❌ Errore: '+err.message);
  btn.disabled=false;btn.textContent='📤 Genera e invia PDF';
 }
}

/* Rileva il click sul pulsante invio-conferma e forza la nuova funzione */
document.addEventListener('click',function(e){
 if(e.target&&e.target.id==='invio-conferma'){
  e.preventDefault();
  e.stopImmediatePropagation();
  eseguiInvioListaV4();
 }
},true);

/* Override definitivo di apriModaleInvioLista */
function apriModaleInvioLista(){
 if(listaAttrezzature.length===0){alert('La lista è vuota.');return}
 const eventiDisponibili=EVENTI.slice().sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));
 if(eventiDisponibili.length===0){alert('Non ci sono eventi disponibili.');return}
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Invia lista';
 document.getElementById('d-titolo').textContent='📤 Invia PDF all\'evento';
 document.getElementById('d-body').innerHTML=`
  <p style="font-size:.85rem;color:#6b778c;margin-bottom:14px">Scegli l'evento a cui inviare questa lista (<b>${listaAttrezzature.length} articoli</b>). Verrà salvata come PDF nell'evento.</p>
  <div class="campo"><label>Evento di destinazione</label>
   <select id="invio-evento" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff">
    ${eventiDisponibili.map((e,i)=>{
     const d2=new Date(e.inizio).toLocaleDateString('it-IT',{day:'2-digit',month:'short',year:'numeric'});
     const haLista=e.listaAttrezzature&&e.listaAttrezzature.length>0;
     return `<option value="${e.id}" ${i===0?'selected':''}>${e.titolo} · ${d2}${haLista?' (ha già una lista)':''}</option>`;
    }).join('')}
   </select>
  </div>
  <div style="background:#f0f6ff;border:1px solid #d7e7fa;border-radius:10px;padding:12px;font-size:.78rem;color:#4b5563;line-height:1.5;margin-top:8px">
   Il PDF verrà salvato in <b>Note per tutti</b>. Se l'evento ha già una lista, verrà <b>sostituita</b>.
  </div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="invio-conferma">📤 Genera e invia PDF</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;
}
  /* ============================================================
   MODIFICA EVENTO/NOLEGGIO — con gestione allegati completa
   ============================================================ */

/* ============== MODIFICA EVENTO ============== */
function apriModaleModificaEvento(ev){
 const isAdmin=user.ruolo==='Amministratore';
 const dataIso=new Date(ev.inizio).toISOString().slice(0,10);
 const ora=String(new Date(ev.inizio).getHours()).padStart(2,'0')+':'+String(new Date(ev.inizio).getMinutes()).padStart(2,'0');
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Modifica evento';
 document.getElementById('d-titolo').textContent='✏️ '+ev.titolo;
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Nome evento <span style="color:#dc2626">*</span></label><input id="me-nome" value="${(ev.titolo||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo-2">
   <div class="campo"><label>Data</label><input id="me-data" type="date" value="${dataIso}"></div>
   <div class="campo"><label>Orario</label><input id="me-ora" type="time" value="${ora}"></div>
  </div>
  <div class="campo"><label>Location</label><input id="me-loc" value="${(ev.location||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo"><label>Città (per il meteo)</label><input id="me-citta" value="${(ev.citta||'').replace(/"/g,'&quot;')}" placeholder="Es. Catania"></div>
  <div class="divisore-modale">👥 Persone</div>
  <div class="campo-3">
   <div class="campo"><label>Ospiti</label><input id="me-osp" type="number" min="0" value="${ev.ospiti||0}"></div>
   <div class="campo"><label>Bambini</label><input id="me-bam" type="number" min="0" value="${ev.bambini||0}"></div>
   <div class="campo"><label>Staff</label><input id="me-stf" type="number" min="0" value="${ev.staff||0}"></div>
  </div>
  <div class="divisore-modale">📝 Note per tutti</div>
  <div class="campo">
   <textarea id="me-n-tutti" style="background:#eef2ff;border-color:#c7d2fe">${(ev.noteTutti||'').replace(/</g,'&lt;')}</textarea>
   ${listaAllegatiEsistenti(ev.allegatiTutti||[],'me-al-tutti')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="me-f-tutti" multiple accept="image/*,.pdf">
  </div>
  <div class="divisore-modale">🍽️ Note per la sala</div>
  <div class="campo">
   <textarea id="me-n-sala" style="background:#f0fdf4;border-color:#bbf7d0">${(ev.noteSala||'').replace(/</g,'&lt;')}</textarea>
   ${listaAllegatiEsistenti(ev.allegatiSala||[],'me-al-sala')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="me-f-sala" multiple accept="image/*,.pdf">
  </div>
  <div class="divisore-modale">👨‍🍳 Note per la cucina</div>
  <div class="campo">
   <textarea id="me-n-cucina" style="background:#fff7ed;border-color:#fed7aa">${(ev.noteCucina||'').replace(/</g,'&lt;')}</textarea>
   ${listaAllegatiEsistenti(ev.allegatiCucina||[],'me-al-cucina')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="me-f-cucina" multiple accept="image/*,.pdf">
  </div>
  <div class="divisore-modale">📦 Note per il magazzino</div>
  <div class="campo">
   <textarea id="me-n-mag" style="background:#f5f3ff;border-color:#ddd6fe">${(ev.noteMagazzino||'').replace(/</g,'&lt;')}</textarea>
   ${listaAllegatiEsistenti(ev.allegatiMagazzino||[],'me-al-mag')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="me-f-mag" multiple accept="image/*,.pdf">
  </div>
  ${isAdmin?`
  <div class="divisore-modale">🔒 Cartella privata Admin</div>
  <div class="campo">
   <textarea id="me-n-priv" style="background:#fdf4ff;border-color:#f5d0fe">${(ev.notePrivata||'').replace(/</g,'&lt;')}</textarea>
   ${listaAllegatiEsistenti(ev.allegatiPrivata||[],'me-al-priv')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#8338ec;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="me-f-priv" multiple accept="image/*,.pdf">
  </div>`:''}
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="me-salva" style="background:#3e765e">💾 Salva modifiche</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;

 /* Aggancia pulsanti 🗑️ rimuovi allegato */
 agganciaRimuoviAllegati(ev);

 /* Salva */
 document.getElementById('me-salva').onclick=async()=>{
  const nome=document.getElementById('me-nome').value.trim();
  if(!nome){alert('Il nome è obbligatorio.');return}
  ev.titolo=nome;
  ev.inizio=document.getElementById('me-data').value+'T'+(document.getElementById('me-ora').value||'18:30')+':00';
  ev.location=document.getElementById('me-loc').value.trim()||'—';
  ev.citta=document.getElementById('me-citta').value.trim();
  ev.ospiti=parseInt(document.getElementById('me-osp').value)||0;
  ev.bambini=parseInt(document.getElementById('me-bam').value)||0;
  ev.staff=parseInt(document.getElementById('me-stf').value)||0;
  ev.noteTutti=document.getElementById('me-n-tutti').value;
  ev.noteSala=document.getElementById('me-n-sala').value;
  ev.noteCucina=document.getElementById('me-n-cucina').value;
  ev.noteMagazzino=document.getElementById('me-n-mag').value;
  if(isAdmin&&document.getElementById('me-n-priv'))ev.notePrivata=document.getElementById('me-n-priv').value;
  /* Aggiungi nuovi allegati a ciascuna sezione */
  const nuoviTutti=await leggiAllegati('me-f-tutti');
  if(nuoviTutti.length)ev.allegatiTutti=(ev.allegatiTutti||[]).concat(nuoviTutti);
  const nuoviSala=await leggiAllegati('me-f-sala');
  if(nuoviSala.length)ev.allegatiSala=(ev.allegatiSala||[]).concat(nuoviSala);
  const nuoviCucina=await leggiAllegati('me-f-cucina');
  if(nuoviCucina.length)ev.allegatiCucina=(ev.allegatiCucina||[]).concat(nuoviCucina);
  const nuoviMag=await leggiAllegati('me-f-mag');
  if(nuoviMag.length)ev.allegatiMagazzino=(ev.allegatiMagazzino||[]).concat(nuoviMag);
  if(isAdmin&&document.getElementById('me-f-priv')){
   const nuoviPriv=await leggiAllegati('me-f-priv');
   if(nuoviPriv.length)ev.allegatiPrivata=(ev.allegatiPrivata||[]).concat(nuoviPriv);
  }
  let salv=[];
  try{salv=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
  const idx=salv.findIndex(e=>e.id===ev.id);
  if(idx>=0)salv[idx]=ev;else salv.push(ev);
  localStorage.setItem('ergo_eventi',JSON.stringify(salv));
  chiudiDrawer();
  alert('✅ Evento aggiornato!');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}

/* ============== MODIFICA NOLEGGIO ============== */
function apriModaleModificaNoleggio(nl){
 const isAdmin=user.ruolo==='Amministratore';
 const isMag2=user.ruolo==='Magazzino2';
 const vediBolla=isAdmin||isMag2;
 const dataIso=new Date(nl.inizio).toISOString().slice(0,10);
 const ora=String(new Date(nl.inizio).getHours()).padStart(2,'0')+':'+String(new Date(nl.inizio).getMinutes()).padStart(2,'0');
 const dataF=new Date(nl.fine).toISOString().slice(0,10);
 const oraF=String(new Date(nl.fine).getHours()).padStart(2,'0')+':'+String(new Date(nl.fine).getMinutes()).padStart(2,'0');
 const d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
 document.getElementById('d-eyebrow').textContent='Modifica noleggio';
 document.getElementById('d-titolo').textContent='✏️ '+nl.titolo;
 document.getElementById('d-body').innerHTML=`
  <div class="campo"><label>Titolo <span style="color:#dc2626">*</span></label><input id="mn-titolo" value="${(nl.titolo||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo-2"><div class="campo"><label>Data inizio</label><input id="mn-di" type="date" value="${dataIso}"></div><div class="campo"><label>Ora inizio</label><input id="mn-oi" type="time" value="${ora}"></div></div>
  <div class="campo-2"><div class="campo"><label>Data fine</label><input id="mn-df" type="date" value="${dataF}"></div><div class="campo"><label>Ora fine</label><input id="mn-of" type="time" value="${oraF}"></div></div>
  <div class="campo"><label>Location <span style="color:#dc2626">*</span></label><input id="mn-loc" value="${(nl.location||'').replace(/"/g,'&quot;')}"></div>
  <div class="campo"><label>Città (per il meteo)</label><input id="mn-citta" value="${(nl.citta||'').replace(/"/g,'&quot;')}" placeholder="Es. Catania"></div>
  <div class="campo-2"><div class="campo"><label>Referente</label><input id="mn-ref" value="${(nl.referente||'').replace(/"/g,'&quot;')}"></div><div class="campo"><label>Telefono</label><input id="mn-tel" value="${(nl.telefono||'').replace(/"/g,'&quot;')}"></div></div>
  <div class="campo"><label>Stato</label>
   <select id="mn-stato" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;font-size:.88rem;background:#fff">
    <option value="confermato" ${nl.stato==='confermato'?'selected':''}>Confermato</option>
    <option value="non confermato" ${nl.stato!=='confermato'?'selected':''}>Non confermato</option>
   </select>
  </div>
  <div class="campo"><label>Note</label><textarea id="mn-note">${(nl.note||'').replace(/</g,'&lt;')}</textarea></div>
  ${vediBolla?`
  <div class="divisore-modale">💰 Bolla con prezzo</div>
  <div class="campo">
   ${listaAllegatiEsistenti(nl.allegatiBolla||[],'mn-al-bolla')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="mn-f-bolla" multiple accept="image/*,.pdf">
  </div>`:''}
  <div class="divisore-modale">📄 DDT</div>
  <div class="campo">
   ${listaAllegatiEsistenti(nl.allegatiDDT||[],'mn-al-ddt')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="mn-f-ddt" multiple accept="image/*,.pdf">
  </div>
  <div class="divisore-modale">📎 Vario</div>
  <div class="campo">
   ${listaAllegatiEsistenti(nl.allegatiVario||[],'mn-al-vario')}
   <label style="display:block;font-size:.7rem;font-weight:700;color:#083278;margin-top:10px">+ Aggiungi nuovi allegati</label>
   <input type="file" id="mn-f-vario" multiple accept="image/*,.pdf">
  </div>
 `;
 document.getElementById('d-foot').innerHTML=`<button class="btn-ghost" onclick="chiudiDrawer()">Annulla</button><button class="btn-primary" id="mn-salva">💾 Salva modifiche</button>`;
 d.classList.add('open');bg.classList.add('open');
 document.getElementById('d-close').onclick=chiudiDrawer;
 bg.onclick=chiudiDrawer;

 agganciaRimuoviAllegatiNoleggio(nl);

 document.getElementById('mn-salva').onclick=async()=>{
  const titolo=document.getElementById('mn-titolo').value.trim();
  if(!titolo){alert('Il titolo è obbligatorio.');return}
  nl.titolo=titolo;
  nl.inizio=document.getElementById('mn-di').value+'T'+(document.getElementById('mn-oi').value||'09:00')+':00';
  nl.fine=document.getElementById('mn-df').value+'T'+(document.getElementById('mn-of').value||'18:00')+':00';
  nl.location=document.getElementById('mn-loc').value.trim();
  nl.citta=document.getElementById('mn-citta').value.trim();
  nl.referente=document.getElementById('mn-ref').value.trim();
  nl.telefono=document.getElementById('mn-tel').value.trim();
  nl.stato=document.getElementById('mn-stato').value;
  nl.note=document.getElementById('mn-note').value;
  if(vediBolla){
   const nb=await leggiAllegati('mn-f-bolla');
   if(nb.length)nl.allegatiBolla=(nl.allegatiBolla||[]).concat(nb);
  }
  const nd=await leggiAllegati('mn-f-ddt');
  if(nd.length)nl.allegatiDDT=(nl.allegatiDDT||[]).concat(nd);
  const nv=await leggiAllegati('mn-f-vario');
  if(nv.length)nl.allegatiVario=(nl.allegatiVario||[]).concat(nv);
  let salv=[];
  try{salv=JSON.parse(localStorage.getItem('ergo_noleggi'))||[]}catch(e){}
  const idx=salv.findIndex(n=>n.id===nl.id);
  if(idx>=0)salv[idx]=nl;else salv.push(nl);
  localStorage.setItem('ergo_noleggi',JSON.stringify(salv));
  chiudiDrawer();
  alert('✅ Noleggio aggiornato!');
  const pc=document.getElementById('pc');
  if(pc){if(view==='calendario')cal(pc);else if(view==='dashboard')dash(pc)}
 };
}

/* ============== HELPERS ============== */
function listaAllegatiEsistenti(allegati,prefisso){
 if(!allegati||allegati.length===0){
  return '<div style="font-size:.72rem;color:#94a3b8;padding:8px 0">Nessun allegato</div>';
 }
 return allegati.map((a,i)=>{
  const icona=(a.mime||'').startsWith('image/')?'🖼️':(a.mime||'').includes('pdf')?'📄':'📎';
  const kb=a.size?Math.round(a.size/1024)+' KB':'';
  return `<div class="allegato-riga" style="margin-top:6px">
   <div class="allegato-info">
    <span class="allegato-icona">${icona}</span>
    <div><strong>${a.nome}</strong><small>${kb}</small></div>
   </div>
   <button type="button" class="allegato-btn" data-rimuovi-allegato="${prefisso}" data-idx="${i}" style="color:#b91c1c;border-color:#fecaca;background:#fef2f2">🗑️</button>
  </div>`;
 }).join('');
}

function agganciaRimuoviAllegati(ev){
 document.querySelectorAll('[data-rimuovi-allegato]').forEach(b=>{
  b.onclick=()=>{
   const pref=b.dataset.rimuoviAllegato;
   const idx=parseInt(b.dataset.idx);
   let campo='';
   if(pref==='me-al-tutti')campo='allegatiTutti';
   else if(pref==='me-al-sala')campo='allegatiSala';
   else if(pref==='me-al-cucina')campo='allegatiCucina';
   else if(pref==='me-al-mag')campo='allegatiMagazzino';
   else if(pref==='me-al-priv')campo='allegatiPrivata';
   if(!campo)return;
   if(confirm('Eliminare questo allegato?')){
    ev[campo]=(ev[campo]||[]).filter((_,i)=>i!==idx);
    let salv=[];
    try{salv=JSON.parse(localStorage.getItem('ergo_eventi'))||[]}catch(e){}
    const id=salv.findIndex(x=>x.id===ev.id);
    if(id>=0)salv[id]=ev;
    localStorage.setItem('ergo_eventi',JSON.stringify(salv));
    /* Ricarica il modale per mostrare la lista aggiornata */
    apriModaleModificaEvento(ev);
   }
  };
 });
}

function agganciaRimuoviAllegatiNoleggio(nl){
 document.querySelectorAll('[data-rimuovi-allegato]').forEach(b=>{
  b.onclick=()=>{
   const pref=b.dataset.rimuoviAllegato;
   const idx=parseInt(b.dataset.idx);
   let campo='';
   if(pref==='mn-al-bolla')campo='allegatiBolla';
   else if(pref==='mn-al-ddt')campo='allegatiDDT';
   else if(pref==='mn-al-vario')campo='allegatiVario';
   if(!campo)return;
   if(confirm('Eliminare questo allegato?')){
    nl[campo]=(nl[campo]||[]).filter((_,i)=>i!==idx);
    let salv=[];
    try{salv=JSON.parse(localStorage.getItem('ergo_noleggi'))||[]}catch(e){}
    const id=salv.findIndex(x=>x.id===nl.id);
    if(id>=0)salv[id]=nl;
    localStorage.setItem('ergo_noleggi',JSON.stringify(salv));
    apriModaleModificaNoleggio(nl);
   }
  };
 });
}
  /* ============================================================
   RIMOZIONE "(per il meteo)" da tutti i campi Città
   ============================================================ */
(function(){
 /* CSS per nascondere la scritta in tutte le versioni */
 const s=document.createElement('style');
 s.textContent=`
  /* Nasconde qualsiasi scritta con "per il meteo" nelle label */
  label span[style*="serve solo per il meteo"],
  label span:has(> i.per-meteo),
  label i.per-meteo{display:none !important}
 `;
 document.head.appendChild(s);

 /* Sostituzione testo al caricamento della pagina */
 const correggi=()=>{
  document.querySelectorAll('label').forEach(l=>{
   if(l.textContent.includes('per il meteo')){
    /* Rimuovi lo <span> che contiene "serve solo per il meteo" o "(per il meteo)" */
    l.querySelectorAll('span').forEach(sp=>{
     if(sp.textContent.includes('per il meteo'))sp.remove();
    });
    /* Rimuovi anche eventuali residui di testo tipo "(serve solo per il meteo)" */
    l.childNodes.forEach(n=>{
     if(n.nodeType===3&&n.textContent.includes('per il meteo')){
      n.textContent=n.textContent.replace(/\s*\(.*per il meteo.*\)/gi,'').replace(/per il meteo/gi,'');
     }
    });
   }
  });
 };

 /* Esegui subito e ogni volta che il DOM cambia (per modali che si aprono dopo) */
 correggi();
 const obs=new MutationObserver(correggi);
 obs.observe(document.body,{childList:true,subtree:true});
})();
  /* ============================================================
   FIX: SALA e CUCINA vedono SOLO eventi
   ============================================================ */

/* 1) Notifiche: Sala e Cucina vedono solo notifiche di eventi/note */
function notifichePerUtente(utente){
 const mappa={
  'Amministratore':['tutti','sala','cucina','magazzino','admin'],
  'Wedding':['tutti','sala','cucina','magazzino'],
  'Cucina':['tutti','cucina'],
  'Sala':['tutti','sala'],
  'Magazzino':['tutti','magazzino','admin'],
  'Magazzino2':['magazzino']
 };
 const rep=mappa[utente.ruolo]||['tutti'];
 return NOTIFICHE.filter(n=>{
  if(!rep.includes(n.reparto))return false;
  /* Magazzino2 vede SOLO notifiche di tipo "noleggio" */
  if(utente.ruolo==='Magazzino2'){
   return n.tipo==='noleggio';
  }
  /* Sala e Cucina NON vedono notifiche di tipo "noleggio" */
  if(utente.ruolo==='Sala'||utente.ruolo==='Cucina'){
   return n.tipo!=='noleggio';
  }
  return true;
 });
}

/* 2) Dashboard: nascondi card noleggio per Sala, Cucina, Wedding (e altri senza permesso) */
(function(){
 const _orig=window.dash;
 if(_orig){
  window.dash=function(el){
   const risultato=_orig.apply(this,arguments);
   const ruolo=user.ruolo;
   /* Ruoli che NON devono vedere il noleggio nella dashboard */
   const nascondiNoleggio=(ruolo==='Sala'||ruolo==='Cucina'||ruolo==='Wedding');
   /* Ruoli che NON devono vedere l'evento nella dashboard */
   const nascondiEvento=(ruolo==='Magazzino2');
   if(nascondiNoleggio||nascondiEvento){
    setTimeout(()=>{
     if(nascondiNoleggio){
      /* Nascondi card noleggio */
      const cdNl=document.getElementById('cd-n');
      if(cdNl){
       const card=cdNl.closest('.cd-card');
       if(card)card.style.display='none';
      }
      /* Nascondi anche il meteo noleggio */
      const meteoNl=document.getElementById('meteo-noleggio');
      if(meteoNl)meteoNl.remove();
      /* Nascondi anche il titolo "Prossimo noleggio" (label) */
      document.querySelectorAll('.cd-card').forEach(c=>{
       const label=c.querySelector('.cd-label');
       if(label&&label.textContent.includes('Prossimo noleggio'))c.style.display='none';
      });
      /* Se tutti i cd-card sono nascosti, nascondi il contenitore */
      const griglia=document.querySelector('.cd-grid');
      if(griglia){
       const visibili=griglia.querySelectorAll('.cd-card:not([style*="display: none"])');
       if(visibili.length===0)griglia.style.display='none';
      }
     }
     if(nascondiEvento){
      /* Nascondi card evento */
      const cdEv=document.getElementById('cd-e');
      if(cdEv){
       const card=cdEv.closest('.cd-card');
       if(card)card.style.display='none';
      }
      const meteoEv=document.getElementById('meteo-evento');
      if(meteoEv)meteoEv.remove();
      document.querySelectorAll('.cd-card').forEach(c=>{
       const label=c.querySelector('.cd-label');
       if(label&&label.textContent.includes('Prossimo evento'))c.style.display='none';
      });
      const griglia=document.querySelector('.cd-grid');
      if(griglia){
       const visibili=griglia.querySelectorAll('.cd-card:not([style*="display: none"])');
       if(visibili.length===0)griglia.style.display='none';
      }
     }
    },200);
   }
   return risultato;
  };
 }
})();

/* 3) Calendario: Sala e Cucina vedono solo eventi (nessun noleggio) */
(function(){
 const _origCal=window.cal;
 if(_origCal){
  window.cal=function(el){
   if(user.ruolo==='Sala'||user.ruolo==='Cucina'||user.ruolo==='Wedding'){
    /* Forza filtro su solo eventi catering */
    calFiltro='catering';
   }
   return _origCal.apply(this,arguments);
  };
 }
})();
  /* ============================================================
   NOTIFICHE DETTAGLIATE — note + allegati + chi le ha create
   ============================================================ */

/* Funzione che genera le notifiche per un evento (creato o modificato) */
function generaNotificheEventoCompleto(ev,azione){
 const nuovi=[];
 const daChi=ev.creatoDa||(user?user.nome+' ('+user.ruolo+')':'Sistema');
 const azioneTxt=azione==='creato'?'creato':'aggiornato';

 /* 1) Notifica evento (per tutti) */
 nuovi.push({
  id:'nf-'+Date.now()+'-ev-'+Math.random().toString(36).slice(2,6),
  tipo:'evento',
  reparto:'tutti',
  titolo:'Evento '+azioneTxt+': '+ev.titolo,
  sottotitolo:'Da '+daChi+' · '+(ev.location||'—'),
  quando:new Date().toISOString(),
  da:daChi,
  dettagli:{
   evento:ev.titolo,
   data:formattaDataIt(ev.inizio),
   location:ev.location,
   ospiti:ev.ospiti
  }
 });

 /* 2) Note per tutti + allegati */
 if(ev.noteTutti&&ev.noteTutti.trim()){
  nuovi.push({
   id:'nf-'+Date.now()+'-nt-'+Math.random().toString(36).slice(2,6),
   tipo:'nota',reparto:'tutti',
   titolo:'Nuova nota per tutti',
   sottotitolo:'Da '+daChi+' · '+ev.titolo,
   quando:new Date().toISOString(),
   da:daChi,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteTutti,sezione:'Note per tutti'}
  });
 }
 if(ev.allegatiTutti&&ev.allegatiTutti.length>0){
  ev.allegatiTutti.forEach((a,i)=>{
   nuovi.push({
    id:'nf-'+Date.now()+'-at-'+i+'-'+Math.random().toString(36).slice(2,6),
    tipo:'allegato',reparto:'tutti',
    titolo:'Nuovo allegato: '+a.nome,
    sottotitolo:'Da '+daChi+' · '+ev.titolo,
    quando:new Date().toISOString(),
    da:daChi,
    dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),allegato:a.nome,sezione:'Note per tutti'}
   });
  });
 }

 /* 3) Note sala + allegati */
 if(ev.noteSala&&ev.noteSala.trim()){
  nuovi.push({
   id:'nf-'+Date.now()+'-ns-'+Math.random().toString(36).slice(2,6),
   tipo:'nota',reparto:'sala',
   titolo:'Nuova nota per la sala',
   sottotitolo:'Da '+daChi+' · '+ev.titolo,
   quando:new Date().toISOString(),
   da:daChi,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteSala,sezione:'Note per la sala'}
  });
 }
 if(ev.allegatiSala&&ev.allegatiSala.length>0){
  ev.allegatiSala.forEach((a,i)=>{
   nuovi.push({
    id:'nf-'+Date.now()+'-as-'+i+'-'+Math.random().toString(36).slice(2,6),
    tipo:'allegato',reparto:'sala',
    titolo:'Nuovo allegato sala: '+a.nome,
    sottotitolo:'Da '+daChi+' · '+ev.titolo,
    quando:new Date().toISOString(),
    da:daChi,
    dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),allegato:a.nome,sezione:'Note per la sala'}
   });
  });
 }

 /* 4) Note cucina + allegati */
 if(ev.noteCucina&&ev.noteCucina.trim()){
  nuovi.push({
   id:'nf-'+Date.now()+'-nc-'+Math.random().toString(36).slice(2,6),
   tipo:'nota',reparto:'cucina',
   titolo:'Nuova nota per la cucina',
   sottotitolo:'Da '+daChi+' · '+ev.titolo,
   quando:new Date().toISOString(),
   da:daChi,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteCucina,sezione:'Note per la cucina'}
  });
 }
 if(ev.allegatiCucina&&ev.allegatiCucina.length>0){
  ev.allegatiCucina.forEach((a,i)=>{
   nuovi.push({
    id:'nf-'+Date.now()+'-ac-'+i+'-'+Math.random().toString(36).slice(2,6),
    tipo:'allegato',reparto:'cucina',
    titolo:'Nuovo allegato cucina: '+a.nome,
    sottotitolo:'Da '+daChi+' · '+ev.titolo,
    quando:new Date().toISOString(),
    da:daChi,
    dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),allegato:a.nome,sezione:'Note per la cucina'}
   });
  });
 }

 /* 5) Note magazzino + allegati */
 if(ev.noteMagazzino&&ev.noteMagazzino.trim()){
  nuovi.push({
   id:'nf-'+Date.now()+'-nm-'+Math.random().toString(36).slice(2,6),
   tipo:'nota',reparto:'magazzino',
   titolo:'Nuova nota per il magazzino',
   sottotitolo:'Da '+daChi+' · '+ev.titolo,
   quando:new Date().toISOString(),
   da:daChi,
   dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.noteMagazzino,sezione:'Note per il magazzino'}
  });
 }
 if(ev.allegatiMagazzino&&ev.allegatiMagazzino.length>0){
  ev.allegatiMagazzino.forEach((a,i)=>{
   nuovi.push({
    id:'nf-'+Date.now()+'-am-'+i+'-'+Math.random().toString(36).slice(2,6),
    tipo:'allegato',reparto:'magazzino',
    titolo:'Nuovo allegato magazzino: '+a.nome,
    sottotitolo:'Da '+daChi+' · '+ev.titolo,
    quando:new Date().toISOString(),
    da:daChi,
    dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),allegato:a.nome,sezione:'Note per il magazzino'}
   });
  });
 }

 /* 6) Cartella privata Admin (solo admin) */
 if(user&&user.ruolo==='Amministratore'){
  if(ev.notePrivata&&ev.notePrivata.trim()){
   nuovi.push({
    id:'nf-'+Date.now()+'-np-'+Math.random().toString(36).slice(2,6),
    tipo:'nota',reparto:'admin',
    titolo:'Nuova nota privata',
    sottotitolo:'Da '+daChi+' · '+ev.titolo,
    quando:new Date().toISOString(),
    da:daChi,
    dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),testoNota:ev.notePrivata,sezione:'Cartella privata Admin'}
   });
  }
  if(ev.allegatiPrivata&&ev.allegatiPrivata.length>0){
   ev.allegatiPrivata.forEach((a,i)=>{
    nuovi.push({
     id:'nf-'+Date.now()+'-ap-'+i+'-'+Math.random().toString(36).slice(2,6),
     tipo:'allegato',reparto:'admin',
     titolo:'Nuovo allegato privato: '+a.nome,
     sottotitolo:'Da '+daChi+' · '+ev.titolo,
     quando:new Date().toISOString(),
     da:daChi,
     dettagli:{evento:ev.titolo,data:formattaDataIt(ev.inizio),allegato:a.nome,sezione:'Cartella privata Admin'}
    });
   });
  }
 }

 /* Aggiungi alle notifiche globali */
 nuovi.forEach(n=>NOTIFICHE.unshift(n));
 let salvate=[];
 try{salvate=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
 nuovi.forEach(n=>salvate.unshift(n));
 localStorage.setItem('ergo_notifiche',JSON.stringify(salvate.slice(0,200)));
}

/* Aggiorna la visualizzazione della notifica per mostrare sezione + da chi */
function renderDetNotif(n){
 const d=n.dettagli||{};let h='';
 if(d.evento){
  h+=`<h4>Evento</h4><div class="note-box tutti"><strong style="font-family:Georgia,serif;font-size:1rem">${d.evento}</strong>${d.location?`<br><span style="color:#667085;font-size:.8rem">📍 ${d.location}</span>`:''}${d.data?`<br><span style="color:#667085;font-size:.8rem">📅 ${d.data}</span>`:''}</div>`;
 }
 if(d.sezione){
  h+=`<h4>Sezione</h4><div style="background:#f3f8ff;border:1px solid #d7e7fa;border-radius:10px;padding:10px 12px;font-size:.82rem;color:#4b5563;font-weight:700">${d.sezione}</div>`;
 }
 if(d.testoNota){
  const cls=n.reparto==='cucina'?'cucina':n.reparto==='sala'?'sala':n.reparto==='magazzino'?'magazzino':n.reparto==='admin'?'':'tutti';
  h+=`<h4>📝 Testo della nota</h4><div class="note-box ${cls}" ${n.reparto==='admin'?'style="background:#fdf4ff;border-color:#f5d0fe"':''}>${d.testoNota}</div>`;
 }
 if(d.allegato){
  h+=`<h4>📎 Allegato</h4><div style="background:#f0f6ff;border:1px solid #d7e7fa;border-radius:10px;padding:12px;display:flex;align-items:center;gap:10px"><span style="font-size:1.4rem">📄</span><div><strong style="font-size:.85rem;color:#083278">${d.allegato}</strong><div style="font-size:.7rem;color:#6b778c;margin-top:3px">Apri l'evento per visualizzarlo</div></div></div>`;
 }
 if(d.noleggio){
  h+=`<h4>Noleggio</h4><div class="note-box"><strong style="font-family:Georgia,serif;font-size:1rem">${d.noleggio}</strong></div>`;
 }
 if(d.utente){
  h+=`<h4>Utente</h4><div class="note-box tutti"><strong>${d.utente}</strong><br><span style="color:#667085;font-size:.8rem">Ruolo: ${d.ruolo}</span></div>`;
 }
 h+=`<h4>Info</h4><div class="meta-grid"><div><small>Da</small><strong>${n.da||'—'}</strong></div><div><small>Quando</small><strong>${tempoFa(n.quando)}</strong></div></div>`;
 return h;
}

/* Override di generaNotifEvento per usare la nuova versione completa */
function generaNotifEvento(ev){
 generaNotificheEventoCompleto(ev,'creato');
}

/* Override di salva evento/modifica per usare la nuova notifica */
(function(){
 /* Trova e sostituisci il salvataggio evento in modifica */
 const _origModifica=window.apriModaleModificaEvento;
 if(_origModifica){
  window.apriModaleModificaEvento=function(ev){
   /* Aggiungi flag per notificare modifiche */
   window._eventoInModifica=ev;
   return _origModifica.apply(this,arguments);
  };
 }
})();
  /* ============================================================
   LOG ACCESSI (solo Admin) + NOTIFICHE LISTA inviata/modificata
   ============================================================ */

/* Log accessi (solo accessi, niente azioni) */
function logAccesso(tipo,extra){
 try{
  const log=JSON.parse(localStorage.getItem('ergo_log_accessi')||'[]');
  log.unshift({
   id:'acc-'+Date.now()+'-'+Math.random().toString(36).slice(2,6),
   quando:new Date().toISOString(),
   tipo:tipo, /* 'accesso' o 'uscita' */
   utente:user?user.username:'anonimo',
   nome:user?user.nome:'—',
   ruolo:user?user.ruolo:'—',
   durataMin:(extra&&extra.durata)?extra.durata:null
  });
  localStorage.setItem('ergo_log_accessi',JSON.stringify(log.slice(0,300)));
 }catch(e){}
}

/* Traccia login */
(function(){
 const _origDoLogin=window.doLogin;
 if(_origDoLogin){
  window.doLogin=function(){
   const r=_origDoLogin.apply(this,arguments);
   if(user&&user.username){
    /* Salva sessione corrente */
    localStorage.setItem('ergo_sessione_'+user.username,JSON.stringify({login:new Date().toISOString()}));
    logAccesso('accesso');
   }
   return r;
  };
 }
})();

/* Traccia logout */
(function(){
 const _origApp=window.app;
 if(_origApp){
  window.app=function(){
   const r=_origApp.apply(this,arguments);
   setTimeout(()=>{
    const btnEsci=document.getElementById('out');
    if(btnEsci&&!btnEsci._loggato){
     btnEsci._loggato=true;
     const _clickOrig=btnEsci.onclick;
     btnEsci.onclick=function(){
      if(user&&user.username){
       try{
        const sess=JSON.parse(localStorage.getItem('ergo_sessione_'+user.username)||'null');
        if(sess&&sess.login){
         const durata=Math.floor((Date.now()-new Date(sess.login).getTime())/60000);
         logAccesso('uscita',{durata});
         /* Aggiungi durata all'accesso più recente */
         const log=JSON.parse(localStorage.getItem('ergo_log_accessi')||'[]');
         for(let i=0;i<log.length;i++){
          if(log[i].utente===user.username&&log[i].tipo==='accesso'&&!log[i].durataMin){
           log[i].durataMin=durata;
           break;
          }
         }
         localStorage.setItem('ergo_log_accessi',JSON.stringify(log));
         localStorage.removeItem('ergo_sessione_'+user.username);
        }
       }catch(e){}
      }
      if(_clickOrig)_clickOrig.call(this);
     };
    }
   },300);
   return r;
  };
 }
})();

/* Notifica lista inviata/modificata + Log azioni essenziali */
(function(){
 const _orig=window.eseguiInvioListaV4;
 if(_orig){
  window.eseguiInvioListaV4=function(){
   const idEv=document.getElementById('invio-evento').value;
   const ev=EVENTI.find(e=>e.id===idEv);
   const eraModifica=ev&&ev.listaAttrezzature&&ev.listaAttrezzature.length>0;
   const numArticoli=listaAttrezzature.length;
   const r=_orig.apply(this,arguments);
   setTimeout(()=>{
    if(ev){
     const titoloNotif=eraModifica
      ?'Lista attrezzature aggiornata: '+ev.titolo
      :'Lista attrezzature inviata: '+ev.titolo;
     const sottoNotif=(eraModifica?'Modificata':'Inviata')+' da '+(user?user.nome:'—')+' · '+numArticoli+' articoli';
     /* Aggiorna eventuale notifica esistente per questo evento */
     let trovata=false;
     NOTIFICHE.forEach(n=>{
      if(n.tipo==='allegato'&&n.dettagli&&n.dettagli.evento===ev.titolo&&n.dettagli.allegato&&n.dettagli.allegato.startsWith('Lista_Attrezzature_')){
       n.titolo=titoloNotif;
       n.sottotitolo=sottoNotif;
       n.quando=new Date().toISOString();
       trovata=true;
      }
     });
     /* Se non esisteva, crea nuova notifica */
     if(!trovata){
      const nuovo={
       id:'nf-'+Date.now()+'-lista',
       tipo:'allegato',reparto:'tutti',
       titolo:titoloNotif,
       sottotitolo:sottoNotif,
       quando:new Date().toISOString(),
       da:user.nome+' ('+user.ruolo+')',
       dettagli:{
        evento:ev.titolo,
        data:new Date(ev.inizio).toLocaleDateString('it-IT'),
        location:ev.location,
        allegato:'Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf'
       }
      };
      NOTIFICHE.unshift(nuovo);
     }
     /* Salva in localStorage */
     let salvateN=[];
     try{salvateN=JSON.parse(localStorage.getItem('ergo_notifiche'))||[]}catch(e){}
     const nomeFile='Lista_Attrezzature_'+(ev.titolo||'evento').replace(/\s+/g,'_')+'.pdf';
     let trovataLS=false;
     salvateN.forEach(n=>{
      if(n.tipo==='allegato'&&n.dettagli&&n.dettagli.evento===ev.titolo&&n.dettagli.allegato&&n.dettagli.allegato.startsWith('Lista_Attrezzature_')){
       n.titolo=titoloNotif;
       n.sottotitolo=sottoNotif;
       n.quando=new Date().toISOString();
       trovataLS=true;
      }
     });
     if(!trovataLS){
      salvateN.unshift({
       id:'nf-'+Date.now()+'-lista',
       tipo:'allegato',reparto:'tutti',
       titolo:titoloNotif,
       sottotitolo:sottoNotif,
       quando:new Date().toISOString(),
       da:user.nome+' ('+user.ruolo+')',
       dettagli:{evento:ev.titolo,data:new Date(ev.inizio).toLocaleDateString('it-IT'),location:ev.location,allegato:nomeFile}
      });
     }
     localStorage.setItem('ergo_notifiche',JSON.stringify(salvateN.slice(0,200)));
    }
   },500);
   return r;
  };
 }
})();

/* Sezione LOG ACCESSI nella Dashboard (solo Admin) */
(function(){
 const _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   const r=_origDash.apply(this,arguments);
   if(user&&user.ruolo==='Amministratore'){
    setTimeout(()=>{
     const feed=el.querySelector('.feed');
     if(!feed||document.getElementById('log-accessi-section'))return;
     let log=[];
     try{log=JSON.parse(localStorage.getItem('ergo_log_accessi')||'[]')}catch(e){}
     if(log.length===0)return;
     const section=document.createElement('div');
     section.id='log-accessi-section';
     section.style.cssText='margin-top:22px;border-top:2px dashed #e5e9f0;padding-top:18px';
     section.innerHTML=`
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:10px">
       <div>
        <p class="eyebrow" style="color:#92400e">🔒 Solo Admin</p>
        <h2 style="font-size:1.15rem;margin-top:5px">👥 Accessi al gestionale</h2>
       </div>
       <button class="btn-mini" id="log-svuota" style="color:#b91c1c;border-color:#fecaca;background:#fef2f2">🗑️ Svuota</button>
      </div>
      <div>
       ${log.slice(0,30).map(l=>{
        const isAcc=l.tipo==='accesso';
        const ico=isAcc?'🟢':'🔴';
        const col=isAcc?'#059669':'#dc2626';
        const colBg=isAcc?'#f0fdf4':'#fef2f2';
        let extra='';
        if(isAcc&&l.durataMin)extra=' · rimasto '+l.durataMin+' min';
        else if(!isAcc&&l.durataMin)extra=' · durata '+l.durataMin+' min';
        return `<div style="display:flex;gap:12px;align-items:flex-start;padding:11px 12px;border-radius:10px;background:#fff;border:1px solid var(--line);margin-bottom:6px">
         <div style="width:34px;height:34px;border-radius:9px;background:${colBg};color:${col};display:grid;place-items:center;font-size:.9rem;flex-shrink:0">${ico}</div>
         <div style="flex:1;min-width:0">
          <div style="font-size:.83rem;font-weight:700;color:#152238">${isAcc?'Accesso':'Uscita'}</div>
          <div style="font-size:.72rem;color:#6b778c;margin-top:2px">${l.nome} · <b>${l.ruolo}</b>${extra}</div>
         </div>
         <div style="font-size:.68rem;color:#a0a9b8;white-space:nowrap">${tempoFa(l.quando)}</div>
        </div>`;
       }).join('')}
      </div>
     `;
     feed.appendChild(section);
     document.getElementById('log-svuota').onclick=()=>{
      if(confirm('Svuotare tutti i log accessi?')){
       localStorage.removeItem('ergo_log_accessi');
       section.remove();
      }
     };
    },400);
   }
   return r;
  };
 }
})();
  /* ============================================================
   FIX UNICO: Modifica + Calendario Magazzino
   ============================================================ */

/* ---- 1) FIX CLICK MODIFICA (evento + noleggio) ---- */
document.addEventListener('click',function(e){
 const target=e.target.closest('#d-modifica');
 if(!target)return;
 e.preventDefault();
 e.stopImmediatePropagation();
 const titolo=document.getElementById('d-titolo').textContent;
 const eyebrow=document.getElementById('d-eyebrow').textContent.toLowerCase();
 if(eyebrow.includes('evento')){
  const ev=EVENTI.find(x=>x.titolo===titolo);
  if(ev){
   chiudiDrawer();
   setTimeout(()=>apriModaleModificaEvento(ev),100);
  }
 }else{
  const nl=NOLEGGI.find(x=>x.titolo===titolo);
  if(nl){
   chiudiDrawer();
   setTimeout(()=>apriModaleModificaNoleggio(nl),100);
  }
 }
},true);

/* ---- 2) FIX CALENDARIO: Magazzino1 vede TUTTI (eventi + noleggi) ---- */
(function(){
 const _origCal=window.cal;
 if(_origCal){
  window.cal=function(el){
   if(user.ruolo==='Magazzino'||user.ruolo==='Wedding'||user.ruolo==='Amministratore'){
    calFiltro='tutti';
   }
   if(user.ruolo==='Sala'||user.ruolo==='Cucina'){
    calFiltro='catering';
   }
   if(user.ruolo==='Magazzino2'){
    calFiltro='noleggi';
   }
   return _origCal.apply(this,arguments);
  };
 }
})();
  /* ============================================================
   FRECCETTE EVENTI/NOLEGGI NELLA DASHBOARD
   ============================================================ */
let _idxEventoCorrente=0;
let _idxNoleggioCorrente=0;

function renderFrecciaEventi(total,idx){
 if(total<=1)return '';
 return `<div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-top:10px">
  <button id="dash-prev-evento" style="width:28px;height:28px;border-radius:8px;border:1px solid #c8e0d2;background:#f3f9f5;color:#3e765e;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem" ${idx===0?'disabled style="opacity:.4;cursor:not-allowed;width:28px;height:28px;border-radius:8px;border:1px solid #c8e0d2;background:#f3f9f5;color:#3e765e;font-weight:800;display:grid;place-items:center;font-size:.9rem"':''}>‹</button>
  <span style="font-size:.72rem;color:#3e765e;font-weight:800">${idx+1} di ${total}</span>
  <button id="dash-next-evento" style="width:28px;height:28px;border-radius:8px;border:1px solid #c8e0d2;background:#f3f9f5;color:#3e765e;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem" ${idx===total-1?'disabled style="opacity:.4;cursor:not-allowed;width:28px;height:28px;border-radius:8px;border:1px solid #c8e0d2;background:#f3f9f5;color:#3e765e;font-weight:800;display:grid;place-items:center;font-size:.9rem"':''}>›</button>
 </div>`;
}

function renderFrecciaNoleggi(total,idx){
 if(total<=1)return '';
 return `<div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-top:10px">
  <button id="dash-prev-noleggio" style="width:28px;height:28px;border-radius:8px;border:1px solid #c4d9f2;background:#f0f6fe;color:#083278;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem" ${idx===0?'disabled style="opacity:.4;cursor:not-allowed;width:28px;height:28px;border-radius:8px;border:1px solid #c4d9f2;background:#f0f6fe;color:#083278;font-weight:800;display:grid;place-items:center;font-size:.9rem"':''}>‹</button>
  <span style="font-size:.72rem;color:#083278;font-weight:800">${idx+1} di ${total}</span>
  <button id="dash-next-noleggio" style="width:28px;height:28px;border-radius:8px;border:1px solid #c4d9f2;background:#f0f6fe;color:#083278;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem" ${idx===total-1?'disabled style="opacity:.4;cursor:not-allowed;width:28px;height:28px;border-radius:8px;border:1px solid #c4d9f2;background:#f0f6fe;color:#083278;font-weight:800;display:grid;place-items:center;font-size:.9rem"':''}>›</button>
 </div>`;
}

/* Override della dash: aggiunge frecce sotto countdown */
(function(){
 const _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   const r=_origDash.apply(this,arguments);
   /* Reset indici all'apertura dashboard */
   _idxEventoCorrente=0;
   _idxNoleggioCorrente=0;
   /* Aggiungi frecce dopo countdown */
   setTimeout(()=>{
    aggiornaFrecceDash(el);
   },250);
   return r;
  };
 }
})();

function aggiornaFrecceDash(el){
 const oggi=new Date();oggi.setHours(0,0,0,0);
 /* Eventi ordinati per data (dal più vicino a oggi) */
 const eventiFuturi=EVENTI.filter(e=>new Date(e.inizio)>=oggi).sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));
 /* Noleggi ordinati per data */
 const noleggiFuturi=NOLEGGI.filter(n=>new Date(n.inizio)>=oggi).sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));

 /* Evento corrente */
 const cdEv=document.getElementById('cd-e');
 if(cdEv&&eventiFuturi.length>0){
  const card=cdEv.closest('.cd-card');
  if(card){
   const ev=eventiFuturi[_idxEventoCorrente]||eventiFuturi[0];
   /* Aggiorna titolo e info */
   const titleEl=card.querySelector('.cd-title');
   const whenEl=card.querySelector('.cd-when');
   if(titleEl)titleEl.textContent=ev.titolo;
   if(whenEl)whenEl.textContent=(ev.location||'—')+' · '+(ev.ospiti||0)+' ospiti';
   /* Countdown */
   cdEv.dataset.target=ev.inizio;
   /* Rimuovi vecchie frecce */
   card.querySelectorAll('.freccia-ev').forEach(x=>x.remove());
   /* Aggiungi frecce se ci sono più eventi */
   if(eventiFuturi.length>1){
    const div=document.createElement('div');
    div.className='freccia-ev';
    div.innerHTML=renderFrecciaEventi(eventiFuturi.length,_idxEventoCorrente);
    cdEv.parentNode.appendChild(div);
    const prev=card.querySelector('#dash-prev-evento');
    const next=card.querySelector('#dash-next-evento');
    if(prev)prev.onclick=()=>{_idxEventoCorrente=Math.max(0,_idxEventoCorrente-1);aggiornaFrecceDash(el)};
    if(next)next.onclick=()=>{_idxEventoCorrente=Math.min(eventiFuturi.length-1,_idxEventoCorrente+1);aggiornaFrecceDash(el)};
   }
  }
 }

 /* Noleggio corrente */
 const cdNl=document.getElementById('cd-n');
 if(cdNl&&noleggiFuturi.length>0){
  const card=cdNl.closest('.cd-card');
  if(card){
   const nl=noleggiFuturi[_idxNoleggioCorrente]||noleggiFuturi[0];
   const titleEl=card.querySelector('.cd-title');
   const whenEl=card.querySelector('.cd-when');
   if(titleEl)titleEl.textContent=nl.titolo;
   if(whenEl)whenEl.textContent=nl.location||'—';
   cdNl.dataset.target=nl.inizio;
   card.querySelectorAll('.freccia-nl').forEach(x=>x.remove());
   if(noleggiFuturi.length>1){
    const div=document.createElement('div');
    div.className='freccia-nl';
    div.innerHTML=renderFrecciaNoleggi(noleggiFuturi.length,_idxNoleggioCorrente);
    cdNl.parentNode.appendChild(div);
    const prev=card.querySelector('#dash-prev-noleggio');
    const next=card.querySelector('#dash-next-noleggio');
    if(prev)prev.onclick=()=>{_idxNoleggioCorrente=Math.max(0,_idxNoleggioCorrente-1);aggiornaFrecceDash(el)};
    if(next)next.onclick=()=>{_idxNoleggioCorrente=Math.min(noleggiFuturi.length-1,_idxNoleggioCorrente+1);aggiornaFrecceDash(el)};
   }
  }
 }
}
  /* ============================================================
   FIX: Aggiorna DATA + METEO quando cambi evento/noleggio
   ============================================================ */
let _idxEventoGlobal=0;
let _idxNoleggioGlobal=0;

/* Funzione che ridisegna completamente la card evento/noleggio corrente */
function aggiornaCardCorrente(){
 const oggi=new Date();oggi.setHours(0,0,0,0);
 const eventiFuturi=EVENTI.filter(e=>new Date(e.inizio)>=oggi).sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));
 const noleggiFuturi=NOLEGGI.filter(n=>new Date(n.inizio)>=oggi).sort((a,b)=>new Date(a.inizio)-new Date(b.inizio));

 /* === EVENTO === */
 const cardEv=document.querySelector('.cd-card.event');
 if(cardEv&&eventiFuturi.length>0){
  const ev=eventiFuturi[_idxEventoGlobal]||eventiFuturi[0];
  /* Aggiorna tag stato */
  const tag=cardEv.querySelector('.cd-tag');
  if(tag)tag.textContent=ev.stato||'confermato';
  /* Aggiorna titolo */
  const title=cardEv.querySelector('.cd-title');
  if(title)title.textContent=ev.titolo;
  /* Aggiorna when */
  const when=cardEv.querySelector('.cd-when');
  if(when)when.textContent=(ev.location||'—')+' · '+(ev.ospiti||0)+' ospiti';
  /* Aggiorna countdown target */
  const cdEv=document.getElementById('cd-e');
  if(cdEv)cdEv.dataset.target=ev.inizio;
  /* Rimuovi data vecchia e meteo vecchio */
  cardEv.querySelectorAll('.cd-data-evento').forEach(x=>x.remove());
  cardEv.querySelectorAll('#meteo-evento').forEach(x=>x.remove());
  /* Aggiungi data nuova */
  const dataStr=new Date(ev.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
  const oraStr=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  const divData=document.createElement('div');
  divData.className='cd-data-evento';
  divData.style.cssText='font-size:.72rem;color:#3e765e;text-align:center;margin-top:8px;font-weight:700';
  divData.textContent=dataStr.charAt(0).toUpperCase()+dataStr.slice(1)+' · ore '+oraStr;
  if(cdEv)cdEv.parentNode.appendChild(divData);
  /* Aggiungi meteo nuovo */
  const divMeteo=document.createElement('div');
  divMeteo.id='meteo-evento';
  if(cdEv)cdEv.parentNode.appendChild(divMeteo);
  const citta=ev.citta||ev.location;
  if(citta&&citta!=='—')mostraMeteoIn('meteo-evento',citta,ev.inizio);
  /* Aggiungi frecce (se non ci sono) */
  cardEv.querySelectorAll('.freccia-ev').forEach(x=>x.remove());
  if(eventiFuturi.length>1){
   const divF=document.createElement('div');
   divF.className='freccia-ev';
   divF.style.cssText='display:flex;align-items:center;justify-content:center;gap:8px;margin-top:10px';
   divF.innerHTML=`
    <button ${_idxEventoGlobal===0?'disabled':''} id="dash-prev-evento" style="width:28px;height:28px;border-radius:8px;border:1px solid #c8e0d2;background:#f3f9f5;color:#3e765e;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem;opacity:${_idxEventoGlobal===0?'0.4':'1'}">‹</button>
    <span style="font-size:.72rem;color:#3e765e;font-weight:800">${_idxEventoGlobal+1} di ${eventiFuturi.length}</span>
    <button ${_idxEventoGlobal===eventiFuturi.length-1?'disabled':''} id="dash-next-evento" style="width:28px;height:28px;border-radius:8px;border:1px solid #c8e0d2;background:#f3f9f5;color:#3e765e;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem;opacity:${_idxEventoGlobal===eventiFuturi.length-1?'0.4':'1'}">›</button>`;
   if(cdEv)cdEv.parentNode.appendChild(divF);
  }
 }

 /* === NOLEGGIO === */
 const cardNl=document.querySelector('.cd-card.rental');
 if(cardNl&&noleggiFuturi.length>0){
  const nl=noleggiFuturi[_idxNoleggioGlobal]||noleggiFuturi[0];
  const tag=cardNl.querySelector('.cd-tag');
  if(tag)tag.textContent=nl.stato||'confermato';
  const title=cardNl.querySelector('.cd-title');
  if(title)title.textContent=nl.titolo;
  const when=cardNl.querySelector('.cd-when');
  if(when)when.textContent=nl.location||'—';
  const cdNl=document.getElementById('cd-n');
  if(cdNl)cdNl.dataset.target=nl.inizio;
  cardNl.querySelectorAll('.cd-data-noleggio').forEach(x=>x.remove());
  cardNl.querySelectorAll('#meteo-noleggio').forEach(x=>x.remove());
  const dataStr=new Date(nl.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
  const oraStr=new Date(nl.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  const divData=document.createElement('div');
  divData.className='cd-data-noleggio';
  divData.style.cssText='font-size:.72rem;color:#083278;text-align:center;margin-top:8px;font-weight:700';
  divData.textContent=dataStr.charAt(0).toUpperCase()+dataStr.slice(1)+' · ore '+oraStr;
  if(cdNl)cdNl.parentNode.appendChild(divData);
  const divMeteo=document.createElement('div');
  divMeteo.id='meteo-noleggio';
  if(cdNl)cdNl.parentNode.appendChild(divMeteo);
  const citta=nl.citta||nl.location;
  if(citta&&citta!=='—')mostraMeteoIn('meteo-noleggio',citta,nl.inizio);
  cardNl.querySelectorAll('.freccia-nl').forEach(x=>x.remove());
  if(noleggiFuturi.length>1){
   const divF=document.createElement('div');
   divF.className='freccia-nl';
   divF.style.cssText='display:flex;align-items:center;justify-content:center;gap:8px;margin-top:10px';
   divF.innerHTML=`
    <button ${_idxNoleggioGlobal===0?'disabled':''} id="dash-prev-noleggio" style="width:28px;height:28px;border-radius:8px;border:1px solid #c4d9f2;background:#f0f6fe;color:#083278;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem;opacity:${_idxNoleggioGlobal===0?'0.4':'1'}">‹</button>
    <span style="font-size:.72rem;color:#083278;font-weight:800">${_idxNoleggioGlobal+1} di ${noleggiFuturi.length}</span>
    <button ${_idxNoleggioGlobal===noleggiFuturi.length-1?'disabled':''} id="dash-next-noleggio" style="width:28px;height:28px;border-radius:8px;border:1px solid #c4d9f2;background:#f0f6fe;color:#083278;font-weight:800;cursor:pointer;display:grid;place-items:center;font-size:.9rem;opacity:${_idxNoleggioGlobal===noleggiFuturi.length-1?'0.4':'1'}">›</button>`;
   if(cdNl)cdNl.parentNode.appendChild(divF);
  }
 }

 /* Ricollega i pulsanti */
 const prevEv=document.getElementById('dash-prev-evento');
 const nextEv=document.getElementById('dash-next-evento');
 const prevNl=document.getElementById('dash-prev-noleggio');
 const nextNl=document.getElementById('dash-next-noleggio');
 if(prevEv)prevEv.onclick=()=>{if(_idxEventoGlobal>0){_idxEventoGlobal--;aggiornaCardCorrente();ricaricaCountdown()}};
 if(nextEv)nextEv.onclick=()=>{if(_idxEventoGlobal<eventiFuturi.length-1){_idxEventoGlobal++;aggiornaCardCorrente();ricaricaCountdown()}};
 if(prevNl)prevNl.onclick=()=>{if(_idxNoleggioGlobal>0){_idxNoleggioGlobal--;aggiornaCardCorrente();ricaricaCountdown()}};
 if(nextNl)nextNl.onclick=()=>{if(_idxNoleggioGlobal<noleggiFuturi.length-1){_idxNoleggioGlobal++;aggiornaCardCorrente();ricaricaCountdown()}};
}

/* Ricarica countdown dopo cambio */
function ricaricaCountdown(){
 if(typeof avviaCD==='function')avviaCD();
}

/* Reset indici alla apertura dashboard */
(function(){
 const _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   const r=_origDash.apply(this,arguments);
   _idxEventoGlobal=0;
   _idxNoleggioGlobal=0;
   return r;
  };
 }
})();
  /* ============================================================
   DASHBOARD ANIMATA — "Prende vita" al login
   ============================================================ */
(function(){
 var st=document.createElement('style');
 st.textContent=[
  /* Sfondo blu profondo che sfuma nel normale */
  '@keyframes dash-bg{0%{background:#0a1628}100%{background:#f7f8fb}}',
  /* Sidebar scivola da sinistra con molla */
  '@keyframes dash-sidebar{0%{transform:translateX(-100%);opacity:0}70%{transform:translateX(6px)}100%{transform:translateX(0);opacity:1}}',
  /* Topbar scende dall'alto */
  '@keyframes dash-topbar{0%{transform:translateY(-100%);opacity:0}100%{transform:translateY(0);opacity:1}}',
  /* Card sale dal basso con overshoot */
  '@keyframes dash-card-su{0%{transform:translateY(50px) scale(0.9);opacity:0}70%{transform:translateY(-5px) scale(1.02)}100%{transform:translateY(0) scale(1);opacity:1}}',
  /* Card cade dall'alto (per il feed) */
  '@keyframes dash-card-giu{0%{transform:translateY(-40px);opacity:0}70%{transform:translateY(4px)}100%{transform:translateY(0);opacity:1}}',
  /* Notifica cade in cascata */
  '@keyframes dash-notifica{0%{transform:translateX(-30px);opacity:0}100%{transform:translateX(0);opacity:1}}',
  /* Icona si "accende" */
  '@keyframes dash-accendi{0%{filter:brightness(0.3) blur(4px);transform:scale(0.8)}50%{filter:brightness(2);transform:scale(1.15)}100%{filter:brightness(1) blur(0);transform:scale(1)}}',
  /* Testo che si scrive lettera per lettera */
  '@keyframes dash-scrivi{0%{clip-path:inset(0 100% 0 0)}100%{clip-path:inset(0 0 0 0)}}',
  /* Glow su titolo */
  '@keyframes dash-glow{0%,100%{text-shadow:0 0 0 transparent}50%{text-shadow:0 0 20px rgba(8,50,120,0.3)}}',
  /* Applicazione animazioni */
  '.dash-anim .sidebar{animation:dash-sidebar 0.7s cubic-bezier(0.34,1.56,0.64,1) 0.1s both}',
  '.dash-anim .topbar{animation:dash-topbar 0.5s cubic-bezier(0.4,0,0.2,1) 0.15s both}',
  '.dash-anim .cd-card:nth-child(1){animation:dash-card-su 0.7s cubic-bezier(0.34,1.56,0.64,1) 0.4s both}',
  '.dash-anim .cd-card:nth-child(2){animation:dash-card-su 0.7s cubic-bezier(0.34,1.56,0.64,1) 0.6s both}',
  '.dash-anim .feed{animation:dash-card-giu 0.6s cubic-bezier(0.4,0,0.2,1) 0.9s both}',
  '.dash-anim .feed-item{animation:dash-notifica 0.5s ease-out both}',
  '.dash-anim .feed-item:nth-child(1){animation-delay:1.1s}',
  '.dash-anim .feed-item:nth-child(2){animation-delay:1.25s}',
  '.dash-anim .feed-item:nth-child(3){animation-delay:1.4s}',
  '.dash-anim .feed-item:nth-child(4){animation-delay:1.55s}',
  '.dash-anim .feed-item:nth-child(5){animation-delay:1.7s}',
  '.dash-anim .feed-item:nth-child(6){animation-delay:1.85s}',
  '.dash-anim .feed-item:nth-child(7){animation-delay:2s}',
  '.dash-anim .metric-icon,.dash-anim .cd-icon{animation:dash-accendi 0.5s ease-out both}',
  '.dash-anim .cd-card:nth-child(1) .cd-icon{animation-delay:1.1s}',
  '.dash-anim .cd-card:nth-child(2) .cd-icon{animation-delay:1.3s}',
  '.dash-anim h1.title{animation:dash-scrivi 1s steps(30) 0.9s both,dash-glow 2s ease-in-out 2s}',
  '.dash-anim .eyebrow{animation:dash-notifica 0.5s ease-out 0.7s both}',
  '.dash-anim .lede{animation:dash-notifica 0.5s ease-out 1.1s both}',
  '@media (max-width:760px){.dash-anim .sidebar{animation:dash-sidebar 0.6s cubic-bezier(0.34,1.56,0.64,1) 0.1s both}}'
 ].join('');
 document.head.appendChild(st);
})();

/* Applica l'animazione solo UNA VOLTA al login */
(function(){
 var _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   var r=_origDash.apply(this,arguments);
   /* Applica classe animazione solo al primo caricamento dopo login */
   if(!window._dashAnimato){
    window._dashAnimato=true;
    setTimeout(function(){
     var app=document.querySelector('.app');
     var pc=document.getElementById('pc');
     if(pc)pc.classList.add('dash-anim');
     /* Rimuovi la classe dopo 4 secondi così non si ripete ogni volta */
     setTimeout(function(){
      if(pc)pc.classList.remove('dash-anim');
     },3000);
    },50);
   }
   return r;
  };
 }
 /* Reset flag al logout così si ripete al prossimo login */
 var _origLogin=window.login;
 if(_origLogin){
  window.login=function(){
   window._dashAnimato=false;
   return _origLogin.apply(this,arguments);
  };
 }
})();
  /* ============================================================
   EFFETTI WOW — 5 in uno
   2. Skeleton loading · 4. Toast elegante · 5. Tooltip vetro
   8. Badge pulsante · 10. Progress bar countdown
   ============================================================ */

/* ============ CSS ============ */
(function(){
 var st=document.createElement('style');
 st.textContent=[
  /* ===== TOAST ===== */
  '@keyframes toast-in{0%{transform:translateY(-100%) scale(0.9);opacity:0}60%{transform:translateY(6px) scale(1.02)}100%{transform:translateY(0) scale(1);opacity:1}}',
  '@keyframes toast-out{0%{transform:translateY(0);opacity:1}100%{transform:translateY(-100%);opacity:0}}',
  '@keyframes toast-bar{0%{width:100%}100%{width:0%}}',
  '.toast-box{position:fixed;top:22px;left:50%;transform:translateX(-50%);z-index:99999;pointer-events:none;display:flex;flex-direction:column;gap:10px;align-items:center;max-width:90vw}',
  '.toast{background:#fff;border:1px solid #e5e9f0;border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;box-shadow:0 20px 50px rgba(8,50,120,0.18),0 6px 16px rgba(21,34,56,0.10);pointer-events:auto;min-width:280px;max-width:420px;animation:toast-in 0.5s cubic-bezier(0.34,1.56,0.64,1) forwards;position:relative;overflow:hidden}',
  '.toast.esce{animation:toast-out 0.4s ease-in forwards}',
  '.toast::after{content:"";position:absolute;bottom:0;left:0;height:3px;background:currentColor;animation:toast-bar 4s linear forwards}',
  '.toast-ico{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;font-size:1.15rem;flex-shrink:0}',
  '.toast-txt{flex:1;min-width:0}',
  '.toast-txt strong{display:block;font-size:.85rem;font-weight:800;color:#152238;line-height:1.25}',
  '.toast-txt span{display:block;font-size:.72rem;color:#6b778c;margin-top:2px}',
  '.toast.ok{color:#059669}',
  '.toast.ok .toast-ico{background:#f0fdf4;color:#059669}',
  '.toast.err{color:#dc2626}',
  '.toast.err .toast-ico{background:#fef2f2;color:#dc2626}',
  '.toast.info{color:#083278}',
  '.toast.info .toast-ico{background:#eaf1fb;color:#083278}',

  /* ===== SKELETON SHIMMER ===== */
  '@keyframes sk-shimmer{0%{background-position:-500px 0}100%{background-position:500px 0}}',
  '.sk-card{background:#fff;border:1px solid #e5e9f0;border-radius:16px;padding:16px;overflow:hidden;position:relative}',
  '.sk-img{width:100%;height:150px;border-radius:10px;background:linear-gradient(90deg,#f1f4f8 25%,#e5eaf1 50%,#f1f4f8 75%);background-size:1000px 100%;animation:sk-shimmer 1.5s linear infinite;margin-bottom:14px}',
  '.sk-line{height:12px;border-radius:6px;background:linear-gradient(90deg,#f1f4f8 25%,#e5eaf1 50%,#f1f4f8 75%);background-size:1000px 100%;animation:sk-shimmer 1.5s linear infinite;margin-bottom:8px}',
  '.sk-line.short{width:60%}',
  '.sk-line.tiny{width:40%;height:10px}',
  '.sk-griglia{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}',

  /* ===== TOOLTIP VETRO ===== */
  '.tt-glass{position:fixed;z-index:99998;background:rgba(255,255,255,0.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.7);border-radius:12px;padding:10px 14px;font-size:.78rem;font-weight:700;color:#152238;box-shadow:0 12px 32px rgba(8,50,120,0.2);pointer-events:none;opacity:0;transform:translateY(6px);transition:opacity .2s,transform .2s;white-space:nowrap;max-width:260px}',
  '.tt-glass.on{opacity:1;transform:translateY(0)}',

  /* ===== BADGE PULSANTE ===== */
  '@keyframes badge-pulse{0%{box-shadow:0 0 0 0 rgba(220,38,38,0.6)}70%{box-shadow:0 0 0 12px rgba(220,38,38,0)}100%{box-shadow:0 0 0 0 rgba(220,38,38,0)}}',
  '.badge-pulse{animation:badge-pulse 1.8s ease-out infinite}',

  /* ===== PROGRESS BAR COUNTDOWN ===== */
  '.cd-progress{margin-top:12px;background:#edf0f3;border-radius:100px;height:5px;overflow:hidden;position:relative}',
  '.cd-progress span{display:block;height:100%;border-radius:inherit;transition:width 1s ease-out}',
  '.cd-card.event .cd-progress span{background:linear-gradient(90deg,#3e765e,#5c9d7e)}',
  '.cd-card.rental .cd-progress span{background:linear-gradient(90deg,#083278,#3a6bb5)}',
  '.cd-progress-label{font-size:.62rem;color:#94a3b8;text-align:right;margin-top:5px;font-weight:600;letter-spacing:.02em}'
 ].join('');
 document.head.appendChild(st);
})();

/* ============ 4. TOAST ELEGANTE ============ */
(function(){
 if(document.getElementById('toast-box'))return;
 var box=document.createElement('div');
 box.className='toast-box';
 box.id='toast-box';
 document.body.appendChild(box);
})();

window.mostraToast=function(tipo,titolo,sottotitolo,durata){
 var box=document.getElementById('toast-box');
 if(!box)return;
 var t=document.createElement('div');
 t.className='toast '+tipo;
 var ico=tipo==='ok'?'✓':tipo==='err'?'✕':'ℹ';
 t.innerHTML=
  '<div class="toast-ico">'+ico+'</div>'+
  '<div class="toast-txt"><strong>'+titolo+'</strong>'+(sottotitolo?'<span>'+sottotitolo+'</span>':'')+'</div>';
 box.appendChild(t);
 setTimeout(function(){
  t.classList.add('esce');
  setTimeout(function(){if(t.parentNode)t.parentNode.removeChild(t)},400);
 },durata||4000);
};

/* Sostituisci alert() con toast in tutta l'app */
(function(){
 var _alert=window.alert;
 window.alert=function(msg){
  /* Rileva se è un errore o un successo */
  var msgStr=String(msg||'');
  var isErr=msgStr.toLowerCase().indexOf('erro')>=0||msgStr.toLowerCase().indexOf('⚠')>=0||msgStr.toLowerCase().indexOf('obbligatorio')>=0||msgStr.toLowerCase().indexOf('non ')>=0&&msgStr.toLowerCase().indexOf('non trovato')>=0;
  var isOk=msgStr.indexOf('✅')>=0;
  if(isOk){
   mostraToast('ok',msgStr.replace('✅','').trim(),'','3500');
  }else if(isErr){
   mostraToast('err',msgStr.replace('❌','').replace('⚠️','').trim(),'','4500');
  }else{
   /* Fallback: alert normale */
   return _alert.apply(window,arguments);
  }
 };
})();

/* ============ 2. SKELETON LOADING ============ */
/* Mostra skeleton quando si apre inventario, poi nasconde */
(function(){
 var _origInv=window.inv;
 if(_origInv){
  window.inv=function(el){
   /* Mostra skeleton per 400ms poi carica vero */
   if(!window._skipSkeleton){
    el.innerHTML='<div class="page"><div style="margin-bottom:20px"><p class="eyebrow" style="visibility:hidden">Catalogo</p><h1 class="title" style="visibility:hidden">Inventario</h1></div><div class="sk-griglia">'+
     Array(6).join().split(',').map(function(){return '<div class="sk-card"><div class="sk-img"></div><div class="sk-line"></div><div class="sk-line short"></div><div class="sk-line tiny"></div></div>';}).join('')+
     '</div></div>';
    window._skipSkeleton=true;
    setTimeout(function(){
     window._skipSkeleton=false;
     _origInv.call(this,el);
    }.bind(this),500);
    return;
   }
   window._skipSkeleton=false;
   return _origInv.apply(this,arguments);
  };
 }
})();

/* ============ 5. TOOLTIP VETRO ============ */
(function(){
 if(document.getElementById('tt-glass'))return;
 var tt=document.createElement('div');
 tt.className='tt-glass';
 tt.id='tt-glass';
 document.body.appendChild(tt);

 var elementoTarget=null;
 document.addEventListener('mouseover',function(e){
  var el=e.target.closest('[title]');
  if(!el||el===elementoTarget)return;
  elementoTarget=el;
  var testo=el.getAttribute('title');
  el.setAttribute('data-original-title',testo);
  el.removeAttribute('title'); /* Rimuovi tooltip nativo */
  tt.textContent=testo;
  var rect=el.getBoundingClientRect();
  tt.style.left=(rect.left+rect.width/2-tt.offsetWidth/2)+'px';
  tt.style.top=(rect.top-tt.offsetHeight-10)+'px';
  /* Correggi se esce dallo schermo */
  if(parseFloat(tt.style.top)<10){
   tt.style.top=(rect.bottom+10)+'px';
  }
  tt.classList.add('on');
 });
 document.addEventListener('mouseout',function(e){
  if(elementoTarget&&!e.relatedTarget){
   tt.classList.remove('on');
   if(elementoTarget.getAttribute('data-original-title')){
    elementoTarget.setAttribute('title',elementoTarget.getAttribute('data-original-title'));
   }
   elementoTarget=null;
  }
 });
 /* Aggiorna posizione se scrolli */
 window.addEventListener('scroll',function(){
  if(elementoTarget){
   tt.classList.remove('on');
  }
 },true);
})();

/* ============ 8. BADGE PULSANTE ============ */
(function(){
 var _origNotif=window.notifRow;
 if(_origNotif){
  window.notifRow=function(n){
   var html=_origNotif.apply(this,arguments);
   /* Aggiungi classe pulse se non letto */
   if(!isLetta(user.username,n.id)){
    html=html.replace('class="feed-item unread"','class="feed-item unread badge-pulse"');
   }
   return html;
  };
 }
 /* Aggiungi pulse anche a eventuali badge contatori non letti */
 var st=document.createElement('style');
 st.textContent='.feed-item.unread{position:relative} .feed-item.unread::after{content:"";position:absolute;top:50%;left:2px;width:8px;height:8px;background:#dc2626;border-radius:50%;transform:translateY(-50%);animation:badge-pulse 1.8s ease-out infinite}';
 document.head.appendChild(st);
})();

/* ============ 10. PROGRESS BAR COUNTDOWN ============ */
(function(){
 var _origAvvia=window.avviaCD;
 if(_origAvvia){
  window.avviaCD=function(){
   var r=_origAvvia.apply(this,arguments);
   /* Aggiungi progress bar alle card countdown */
   setTimeout(aggiungiProgressBar,100);
   return r;
  };
 }
 function aggiungiProgressBar(){
  ['cd-e','cd-n'].forEach(function(id){
   var cd=document.getElementById(id);
   if(!cd)return;
   /* Rimuovi eventuale barra precedente */
   var old=cd.parentNode.querySelector('.cd-progress-wrap');
   if(old)old.remove();
   var target=cd.dataset.target;
   if(!target)return;
   var oggi=new Date();
   var evDate=new Date(target);
   var diffGiorni=Math.round((evDate-oggi)/(1000*60*60*24));
   /* Calcola percentuale: più è vicino, più è pieno (max 30 giorni) */
   var perc=Math.max(5,Math.min(100,100-(diffGiorni/30*100)));
   var wrap=document.createElement('div');
   wrap.className='cd-progress-wrap';
   var label='';
   if(diffGiorni<=0){
    label='Oggi!';
    perc=100;
   }else if(diffGiorni===1){
    label='Domani';
   }else{
    label='Tra '+diffGiorni+' giorni';
   }
   var colore=id==='cd-e'?'#3e765e':'#083278';
   wrap.innerHTML='<div class="cd-progress"><span style="width:'+perc+'%;background:'+colore+'"></span></div>'+
    '<div class="cd-progress-label">'+label+'</div>';
   cd.parentNode.appendChild(wrap);
  });
 }
 /* Richiama ogni volta che la dash si aggiorna */
 var _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   var r=_origDash.apply(this,arguments);
   setTimeout(aggiungiProgressBar,300);
   return r;
  };
 }
 /* Aggiorna quando si cambia evento con le frecce */
 var _origAggiorna=window.aggiornaCardCorrente;
 if(_origAggiorna){
  window.aggiornaCardCorrente=function(){
   var r=_origAggiorna.apply(this,arguments);
   setTimeout(aggiungiProgressBar,150);
   return r;
  };
 }
})();
  /* ============================================================
   FIX: Log accessi corto + Aggiorna data/meteo con frecce
   ============================================================ */

/* ============ 1. FIX LOG ACCESSI (solo ultimi) ============ */
(function(){
 /* Override della sezione log accessi nella dashboard */
 var _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   var r=_origDash.apply(this,arguments);
   /* Rimuovi la vecchia sezione log se c'è */
   setTimeout(function(){
    var vecchia=document.getElementById('log-accessi-section');
    if(vecchia)vecchia.remove();
    /* Crea quella nuova, compatta */
    if(user&&user.ruolo==='Amministratore'){
     var feed=el.querySelector('.feed');
     if(!feed)return;
     var log=[];
     try{log=JSON.parse(localStorage.getItem('ergo_log_accessi')||'[]')}catch(e){}
     if(log.length===0)return;
     var mostrati=6;
     var tuttiVisibili=false;
     var section=document.createElement('div');
     section.id='log-accessi-section';
     section.style.cssText='margin-top:22px;border-top:2px dashed #e5e9f0;padding-top:18px';
     function renderLista(){
      var daMostrare=tuttiVisibili?log:log.slice(0,mostrati);
      var righe=daMostrare.map(function(l){
       var isAcc=l.tipo==='accesso';
       var ico=isAcc?'🟢':'🔴';
       var col=isAcc?'#059669':'#dc2626';
       var colBg=isAcc?'#f0fdf4':'#fef2f2';
       var extra='';
       if(isAcc&&l.durataMin)extra=' · '+l.durataMin+' min';
       else if(!isAcc&&l.durataMin)extra=' · '+l.durataMin+' min';
       return '<div style="display:flex;gap:10px;align-items:center;padding:9px 12px;border-radius:9px;background:#fff;border:1px solid var(--line);margin-bottom:5px">'+
        '<div style="width:28px;height:28px;border-radius:8px;background:'+colBg+';color:'+col+';display:grid;place-items:center;font-size:.8rem;flex-shrink:0">'+ico+'</div>'+
        '<div style="flex:1;min-width:0;font-size:.78rem;color:#152238"><b>'+l.nome+'</b> <span style="color:#6b778c">· '+l.ruolo+'</span><span style="color:#94a3b8;font-size:.7rem">'+extra+'</span></div>'+
        '<div style="font-size:.66rem;color:#a0a9b8;white-space:nowrap">'+tempoFa(l.quando)+'</div>'+
       '</div>';
      }).join('');
      var bottone='';
      if(log.length>mostrati){
       bottone='<button id="log-toggle" style="width:100%;padding:8px;border-radius:9px;border:1.5px dashed #cbd5e1;background:#fafbfd;color:#6b778c;font-size:.75rem;font-weight:700;cursor:pointer;margin-top:4px">'+
        (tuttiVisibili?'▲ Mostra solo ultimi':'▼ Mostra tutti ('+log.length+')')+'</button>';
      }
      section.innerHTML=
       '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:8px">'+
        '<div><p class="eyebrow" style="color:#92400e">🔒 Solo Admin</p>'+
        '<h2 style="font-size:1.05rem;margin-top:4px">👥 Ultimi accessi</h2></div>'+
        '<button class="btn-mini" id="log-svuota" style="color:#b91c1c;border-color:#fecaca;background:#fef2f2">🗑️ Svuota</button>'+
       '</div>'+
       '<div>'+righe+'</div>'+bottone;
      var btnSvuota=document.getElementById('log-svuota');
      if(btnSvuota)btnSvuota.onclick=function(){
       if(confirm('Svuotare tutti i log accessi?')){
        localStorage.removeItem('ergo_log_accessi');
        section.remove();
       }
      };
      var btnToggle=document.getElementById('log-toggle');
      if(btnToggle)btnToggle.onclick=function(){
       tuttiVisibili=!tuttiVisibili;
       renderLista();
      };
     }
     renderLista();
     feed.appendChild(section);
    }
   },400);
   return r;
  };
 }
})();

/* ============ 2. FIX DATA + METEO con frecce ============ */
/* Override completo di aggiornaCardCorrente */
window.aggiornaCardCorrente=function(){
 var oggi=new Date();oggi.setHours(0,0,0,0);
 var eventiFuturi=EVENTI.filter(function(e){return new Date(e.inizio)>=oggi}).sort(function(a,b){return new Date(a.inizio)-new Date(b.inizio)});
 var noleggiFuturi=NOLEGGI.filter(function(n){return new Date(n.inizio)>=oggi}).sort(function(a,b){return new Date(a.inizio)-new Date(b.inizio)});

 /* === EVENTO === */
 var cardEv=document.querySelector('.cd-card.event');
 if(cardEv&&eventiFuturi.length>0){
  var ev=eventiFuturi[window._idxEventoGlobal||0]||eventiFuturi[0];
  var tag=cardEv.querySelector('.cd-tag');
  if(tag)tag.textContent=ev.stato||'confermato';
  var title=cardEv.querySelector('.cd-title');
  if(title)title.textContent=ev.titolo;
  var when=cardEv.querySelector('.cd-when');
  if(when)when.textContent=(ev.location||'—')+' · '+(ev.ospiti||0)+' ospiti';
  var cdEv=document.getElementById('cd-e');
  if(cdEv)cdEv.dataset.target=ev.inizio;
  /* Rimuovi data e meteo VECCHI */
  cardEv.querySelectorAll('.cd-data-evento').forEach(function(x){x.remove()});
  cardEv.querySelectorAll('#meteo-evento').forEach(function(x){x.remove()});
  cardEv.querySelectorAll('.cd-progress-wrap').forEach(function(x){x.remove()});
  /* Aggiungi data NUOVA */
  var dataStr=new Date(ev.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
  var oraStr=new Date(ev.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  var divData=document.createElement('div');
  divData.className='cd-data-evento';
  divData.style.cssText='font-size:.72rem;color:#3e765e;text-align:center;margin-top:8px;font-weight:700';
  divData.textContent=dataStr.charAt(0).toUpperCase()+dataStr.slice(1)+' · ore '+oraStr;
  if(cdEv)cdEv.parentNode.appendChild(divData);
  /* Aggiungi meteo NUOVO */
  var divMeteo=document.createElement('div');
  divMeteo.id='meteo-evento';
  if(cdEv)cdEv.parentNode.appendChild(divMeteo);
  var citta=ev.citta||ev.location;
  if(citta&&citta!=='—'&&typeof mostraMeteoIn==='function'){
   mostraMeteoIn('meteo-evento',citta,ev.inizio);
  }
 }

 /* === NOLEGGIO === */
 var cardNl=document.querySelector('.cd-card.rental');
 if(cardNl&&noleggiFuturi.length>0){
  var nl=noleggiFuturi[window._idxNoleggioGlobal||0]||noleggiFuturi[0];
  var tag2=cardNl.querySelector('.cd-tag');
  if(tag2)tag2.textContent=nl.stato||'confermato';
  var title2=cardNl.querySelector('.cd-title');
  if(title2)title2.textContent=nl.titolo;
  var when2=cardNl.querySelector('.cd-when');
  if(when2)when2.textContent=nl.location||'—';
  var cdNl=document.getElementById('cd-n');
  if(cdNl)cdNl.dataset.target=nl.inizio;
  cardNl.querySelectorAll('.cd-data-noleggio').forEach(function(x){x.remove()});
  cardNl.querySelectorAll('#meteo-noleggio').forEach(function(x){x.remove()});
  var dataStr2=new Date(nl.inizio).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
  var oraStr2=new Date(nl.inizio).toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  var divData2=document.createElement('div');
  divData2.className='cd-data-noleggio';
  divData2.style.cssText='font-size:.72rem;color:#083278;text-align:center;margin-top:8px;font-weight:700';
  divData2.textContent=dataStr2.charAt(0).toUpperCase()+dataStr2.slice(1)+' · ore '+oraStr2;
  if(cdNl)cdNl.parentNode.appendChild(divData2);
  var divMeteo2=document.createElement('div');
  divMeteo2.id='meteo-noleggio';
  if(cdNl)cdNl.parentNode.appendChild(divMeteo2);
  var citta2=nl.citta||nl.location;
  if(citta2&&citta2!=='—'&&typeof mostraMeteoIn==='function'){
   mostraMeteoIn('meteo-noleggio',citta2,nl.inizio);
  }
 }

 /* === Ricollega frecce === */
 var prevEv=document.getElementById('dash-prev-evento');
 var nextEv=document.getElementById('dash-next-evento');
 var prevNl=document.getElementById('dash-prev-noleggio');
 var nextNl=document.getElementById('dash-next-noleggio');
 if(prevEv)prevEv.onclick=function(){if((window._idxEventoGlobal||0)>0){window._idxEventoGlobal--;aggiornaCardCorrente();ricaricaCountdown()}};
 if(nextEv)nextEv.onclick=function(){if((window._idxEventoGlobal||0)<eventiFuturi.length-1){window._idxEventoGlobal++;aggiornaCardCorrente();ricaricaCountdown()}};
 if(prevNl)prevNl.onclick=function(){if((window._idxNoleggioGlobal||0)>0){window._idxNoleggioGlobal--;aggiornaCardCorrente();ricaricaCountdown()}};
 if(nextNl)nextNl.onclick=function(){if((window._idxNoleggioGlobal||0)<noleggiFuturi.length-1){window._idxNoleggioGlobal++;aggiornaCardCorrente();ricaricaCountdown()}};
};
  /* ============================================================
   BLOCCO UNICO v1 — Modifiche 3, 4, 6, 7, 8, 9
   ============================================================ */

/* ===== 7. RIMUOVI FRECCE DASHBOARD: solo 1 evento + 1 noleggio ===== */
(function(){
 /* Blocca l'aggiornamento frecce */
 var _origAggiorna=window.aggiornaCardCorrente;
 if(_origAggiorna){
  window.aggiornaCardCorrente=function(){
   /* Non fa niente: niente frecce */
  };
 }
 /* Rimuovi frecce se presenti */
 var st=document.createElement('style');
 st.textContent='.freccia-ev,.freccia-nl,#dash-prev-evento,#dash-next-evento,#dash-prev-noleggio,#dash-next-noleggio{display:none !important}';
 document.head.appendChild(st);
})();

/* ===== 6. ICONE DIVERSE NEL CALENDARIO (furgone vs piatto) ===== */
(function(){
 /* Override mostraPann per usare icone specifiche */
 var _origPann=window.mostraPann;
 if(_origPann){
  window.mostraPann=function(d){
   var r=_origPann.apply(this,arguments);
   /* Sostituisci icone nel pannello */
   setTimeout(function(){
    var pannello=document.getElementById('cal-pannello');
    if(!pannello)return;
    /* Trova righe noleggio e metti il furgone */
    pannello.querySelectorAll('.cal-riga.noleggio .ico').forEach(function(el){
     el.textContent='🚚';
    });
    /* Trova righe evento e metti piatto + posate */
    pannello.querySelectorAll('.cal-riga.evento .ico').forEach(function(el){
     el.textContent='🍽️';
    });
   },50);
   return r;
  };
 }
})();

/* ===== 3. ADMIN: ultimi aggiornamenti SOLO di altri utenti ===== */
(function(){
 var _origNotifRow=window.notifRow;
 if(_origNotifRow){
  window.notifRow=function(n){
   /* Se l'utente è Admin e la notifica è stata creata da lui, nascondila */
   if(user&&user.ruolo==='Amministratore'){
    var daChi=n.da||'';
    if(daChi.indexOf(user.nome)>=0||daChi.indexOf(user.username)>=0){
     return '';
    }
   }
   return _origNotifRow.apply(this,arguments);
  };
 }
 /* Filtra anche notifichePerUtente */
 var _origNotifUtente=window.notifichePerUtente;
 if(_origNotifUtente){
  window.notifichePerUtente=function(utente){
   var lista=_origNotifUtente.apply(this,arguments);
   if(utente.ruolo==='Amministratore'){
    return lista.filter(function(n){
     var daChi=n.da||'';
     return daChi.indexOf(utente.nome)<0&&daChi.indexOf(utente.username)<0;
    });
   }
   return lista;
  };
 }
})();

/* ===== 8 + 9. SPUNTE note/allegati GIÀ VISTI per utente ===== */
(function(){
 /* Chiave localStorage per le spunte */
 function chiaveVisti(username,tipo){
  return 'ergo_visti_'+tipo+'_'+username;
 }
 function getVisti(username,tipo){
  try{return JSON.parse(localStorage.getItem(chiaveVisti(username,tipo)))||[]}catch(e){return[]}
 }
 function setVisti(username,tipo,arr){
  localStorage.setItem(chiaveVisti(username,tipo),JSON.stringify(arr));
 }
 window.isVisto=function(id,tipo){
  if(!user)return false;
  return getVisti(user.username,tipo).indexOf(id)>=0;
 };
 window.segnaVisto=function(id,tipo){
  if(!user)return;
  var visti=getVisti(user.username,tipo);
  if(visti.indexOf(id)<0){
   visti.push(id);
   setVisti(user.username,tipo,visti);
  }
 };
 /* CSS per spunta */
 var st=document.createElement('style');
 st.textContent='.visto-badge{display:inline-block;font-size:.6rem;font-weight:800;padding:2px 8px;border-radius:100px;letter-spacing:.04em;margin-left:6px;vertical-align:middle}'+
  '.visto-badge.visto{background:#d1fae5;color:#065f46}'+
  '.visto-badge.nuovo{background:#fef3c7;color:#92400e}'+
  '.nota-vista{background:#f0fdf4 !important;border-color:#bbf7d0 !important}'+
  '.nota-vista .nota-header{opacity:.85}';
 document.head.appendChild(st);

 /* Override del drawer evento per aggiungere spunte su note e allegati */
 var _origDrawer=window.apriDrawerEnt;
 if(_origDrawer){
  window.apriDrawerEnt=function(tipo,obj){
   var r=_origDrawer.apply(this,arguments);
   /* Dopo che il drawer è renderizzato, aggiungi spunte */
   setTimeout(function(){
    var body=document.getElementById('d-body');
    if(!body)return;
    /* Aggiungi spunta alle sezioni NOTE */
    var sezioni=body.querySelectorAll('h4');
    sezioni.forEach(function(h){
     var testo=h.textContent.trim();
     if(testo.startsWith('📝')||testo.startsWith('🍽️')||testo.startsWith('👨‍🍳')||testo.startsWith('📦')||testo.startsWith('🔒')){
      var idSezione=obj.id+'-'+testo.replace(/[^a-zA-Z]/g,'');
      var visto=isVisto(idSezione,'note');
      var badge=document.createElement('span');
      badge.className='visto-badge '+(visto?'visto':'nuovo');
      badge.textContent=visto?'✅ vista':'🆕 nuova';
      h.appendChild(badge);
      /* Al click sulla sezione, segna come vista */
      h.style.cursor='pointer';
      h.onclick=function(){
       segnaVisto(idSezione,'note');
       badge.className='visto-badge visto';
       badge.textContent='✅ vista';
      };
      /* Auto-segna come vista dopo 2 secondi (perché l'utente la sta leggendo) */
      setTimeout(function(){
       segnaVisto(idSezione,'note');
       badge.className='visto-badge visto';
       badge.textContent='✅ vista';
      },2000);
     }
    });
    /* Aggiungi spunta agli ALLEGATI */
    body.querySelectorAll('.allegato-riga').forEach(function(riga){
     var nomeEl=riga.querySelector('strong');
     if(!nomeEl)return;
     var nomeFile=nomeEl.textContent.trim();
     var idAllegato=obj.id+'-'+nomeFile;
     var visto=isVisto(idAllegato,'allegato');
     var badge=document.createElement('span');
     badge.className='visto-badge '+(visto?'visto':'nuovo');
     badge.textContent=visto?'✅ visto':'🆕 nuovo';
     badge.style.marginLeft='8px';
     var infoDiv=riga.querySelector('.allegato-info > div');
     if(infoDiv)infoDiv.appendChild(badge);
    });
   },150);
   return r;
  };
 }
 /* Quando si apre anteprima di un allegato, segna come visto */
 var _origAnteprima=window.apriAnteprimaAllega;
 if(_origAnteprima){
  window.apriAnteprimaAllega=function(allegato){
   if(allegato&&allegato.nome){
    segnaVisto('','allegato');
   }
   return _origAnteprima.apply(this,arguments);
  };
 }
})();

/* ===== 4. SCELTA: singoli PDF o unico PDF ===== */
(function(){
 /* Sovrascrivi il click sul pulsante "Scarica tutti" o simile.
    Nelle sezioni allegati con più di 1 file, mostra scelta. */
 window.scaricaAllegatiConScelta=function(lista,sezione){
  if(!lista||lista.length===0){alert('Nessun allegato da scaricare.');return}
  if(lista.length===1){
   scaricaAllega(lista[0]);
   return;
  }
  /* Mostra modale scelta */
  var d=document.getElementById('d-panel'),bg=document.getElementById('d-bg');
  document.getElementById('d-eyebrow').textContent='Scarica allegati';
  document.getElementById('d-titolo').textContent='📥 '+lista.length+' allegati in '+sezione;
  var html='<p style="font-size:.85rem;color:#6b778c;margin-bottom:16px">Scegli come vuoi scaricare gli allegati di <b>'+sezione+'</b>.</p>';
  html+='<div style="display:grid;gap:10px">';
  html+='<button class="choice-btn" data-choice="singoli" style="padding:16px;background:#fff;border:1.5px solid #cfe0f5;border-radius:12px;cursor:pointer;text-align:left;transition:all .18s">'+
   '<div style="font-size:.95rem;font-weight:800;color:#152238">📄 Scarica singoli</div>'+
   '<div style="font-size:.75rem;color:#6b778c;margin-top:4px">Un PDF per ogni allegato ('+lista.length+' file)</div>'+
  '</button>';
  html+='<button class="choice-btn" data-choice="unico" style="padding:16px;background:#f0f6ff;border:1.5px solid #083278;border-radius:12px;cursor:pointer;text-align:left;transition:all .18s">'+
   '<div style="font-size:.95rem;font-weight:800;color:#083278">📚 Unico PDF</div>'+
   '<div style="font-size:.75rem;color:#526783;margin-top:4px">Tutti gli allegati uniti in un solo PDF</div>'+
  '</button>';
  html+='<button class="choice-btn" data-choice="annulla" style="padding:14px;background:#fafbfd;border:1.5px solid #e5e9f0;border-radius:12px;cursor:pointer;text-align:center;color:#6b778c;font-weight:700;font-size:.82rem">Annulla</button>';
  html+='</div>';
  document.getElementById('d-body').innerHTML=html;
  document.getElementById('d-foot').innerHTML='';
  d.classList.add('open');bg.classList.add('open');
  document.getElementById('d-close').onclick=chiudiDrawer;
  bg.onclick=chiudiDrawer;
  document.querySelectorAll('.choice-btn').forEach(function(b){
   b.onmouseover=function(){this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 20px rgba(8,50,120,0.15)'};
   b.onmouseout=function(){this.style.transform='translateY(0)';this.style.boxShadow='none'};
   b.onclick=function(){
    var scelta=b.dataset.choice;
    chiudiDrawer();
    if(scelta==='annulla')return;
    if(scelta==='singoli'){
     lista.forEach(function(a,i){
      setTimeout(function(){scaricaAllega(a)},i*300);
     });
    }else if(scelta==='unico'){
     scaricaUnicoPdf(lista,sezione);
    }
   };
  });
 };
 /* Funzione per unire più PDF in uno */
 window.scaricaUnicoPdf=function(lista,sezione){
  if(!window.jspdf||!window.jspdf.jsPDF){
   alert('Libreria PDF non caricata.');
   return;
  }
  var jsPDF=window.jspdf.jsPDF;
  var doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
  var paginaW=doc.internal.pageSize.getWidth();
  var y=20;
  /* Copertina */
  doc.setFillColor(8,50,120);
  doc.rect(0,0,paginaW,40,'F');
  doc.setTextColor(255,255,255);
  doc.setFont('helvetica','bold');
  doc.setFontSize(20);
  doc.text(sezione||'Allegati',14,22);
  doc.setFontSize(10);
  doc.setFont('helvetica','normal');
  doc.text(lista.length+' allegati · '+new Date().toLocaleDateString('it-IT'),14,32);
  /* Elenco file */
  y=60;
  doc.setTextColor(21,34,56);
  doc.setFont('helvetica','bold');
  doc.setFontSize(14);
  doc.text('Contenuto del documento',14,y);
  y+=10;
  doc.setFontSize(10);
  doc.setFont('helvetica','normal');
  lista.forEach(function(a,i){
   doc.text((i+1)+'. '+a.nome,14,y);
   y+=6;
   if(y>270){doc.addPage();y=20}
  });
  /* Nota finale */
  y+=10;
  doc.setFontSize(9);
  doc.setTextColor(148,163,184);
  doc.text('Nota: per visualizzare il contenuto completo di ogni singolo file, scaricali separatamente.',14,y);
  doc.save('Allegati_'+sezione.replace(/\s+/g,'_')+'.pdf');
  /* In alternativa, se jsPDF supporta pdf uniti, qui si aggiunge
     il contenuto di ogni PDF originale */
 };
})();

/* ===== AGGANCIA LA SCELTA ALLE SEZIONI ALLEGATI ===== */
(function(){
 /* Aggiungi un pulsante "Scarica tutti" per ogni sezione con più di 1 allegato */
 var _origDrawer=window.apriDrawerEnt;
 if(_origDrawer){
  window.apriDrawerEnt=function(tipo,obj){
   var r=_origDrawer.apply(this,arguments);
   setTimeout(function(){
    var body=document.getElementById('d-body');
    if(!body)return;
    /* Raccogli allegati visibili */
    var allegatiPerSezione={};
    body.querySelectorAll('.allegato-riga').forEach(function(riga){
     var nomeEl=riga.querySelector('strong');
     if(!nomeEl)return;
     var nomeFile=nomeEl.textContent.trim();
     var sezione=riga.querySelector('small')?riga.querySelector('small').textContent.trim():'Allegati';
     if(!allegatiPerSezione[sezione])allegatiPerSezione[sezione]=[];
     /* Trova allegato originale */
     var lista=raccogliAllegatiEnt(tipo,obj,true,true,true);
     var allegato=lista.find(function(a){return a.nome===nomeFile});
     if(allegato)allegatiPerSezione[sezione].push(allegato);
    });
    /* Aggiungi pulsante "Scarica tutti" se più di 1 per sezione */
    Object.keys(allegatiPerSezione).forEach(function(sezione){
     var lista=allegatiPerSezione[sezione];
     if(lista.length<2)return;
     /* Trova l'ultimo allegato di questa sezione per inserire il pulsante dopo */
     var righe=body.querySelectorAll('.allegato-riga');
     var ultimaRiga=null;
     righe.forEach(function(r){
      var s=r.querySelector('small');
      if(s&&s.textContent.trim()===sezione)ultimaRiga=r;
     });
     if(ultimaRiga){
      var btn=document.createElement('button');
      btn.style.cssText='width:100%;padding:10px;border-radius:10px;border:1.5px dashed #c4d9f2;background:#f0f6ff;color:#083278;font-weight:700;font-size:.78rem;cursor:pointer;margin-bottom:10px;margin-top:4px';
      btn.innerHTML='📥 Scarica tutti i '+lista.length+' allegati di "'+sezione+'"';
      btn.onclick=function(){window.scaricaAllegatiConScelta(lista,sezione)};
      ultimaRiga.parentNode.insertBefore(btn,ultimaRiga.nextSibling);
     }
    });
   },200);
   return r;
  };
 }
})();
  /* ============================================================
   FIX BUG 1 — Filtro calendario funzionante
   ============================================================ */
document.addEventListener('click',function(e){
 var btn=e.target.closest('.cal-filtro button');
 if(!btn)return;
 e.preventDefault();
 e.stopImmediatePropagation();
 var filtro=btn.dataset.filtro;
 if(!filtro)return;
 /* Aggiorna classe attiva */
 btn.parentNode.querySelectorAll('button').forEach(function(b){b.classList.remove('active')});
 btn.classList.add('active');
 /* Salva filtro globalmente */
 window.calFiltro=filtro;
 /* Ricarica il calendario */
 var pc=document.getElementById('pc');
 if(pc&&typeof cal==='function'){
  cal(pc);
 }
},true);
  /* ============================================================
   FIX BUG 2 — Barra progress countdown proporzionale
   ============================================================ */
(function(){
 /* Override della funzione che aggiunge la barra */
 window.aggiungiProgressBar=function(){
  ['cd-e','cd-n'].forEach(function(id){
   var cd=document.getElementById(id);
   if(!cd)return;
   /* Rimuovi barra precedente */
   var old=cd.parentNode.querySelector('.cd-progress-wrap');
   if(old)old.remove();
   var target=cd.dataset.target;
   if(!target)return;

   var ora=new Date();
   var evDate=new Date(target);
   var diffMs=evDate-ora;
   var diffOre=diffMs/(1000*60*60);
   var diffGiorni=diffMs/(1000*60*60*24);

   /* Se evento passato, barra 100% */
   if(diffMs<=0){
    var wrapPassato=document.createElement('div');
    wrapPassato.className='cd-progress-wrap';
    var colorePassato=id==='cd-e'?'#3e765e':'#083278';
    wrapPassato.innerHTML='<div class="cd-progress"><span style="width:100%;background:'+colorePassato+'"></span></div>'+
     '<div class="cd-progress-label">Oggi</div>';
    cd.parentNode.appendChild(wrapPassato);
    return;
   }

   /* Calcola percentuale:
      - Più di 30 giorni: 5% (appena iniziato)
      - 30 giorni: 5%
      - 0 giorni (oggi): 100%
      - Lineare in mezzo */
   var perc;
   if(diffGiorni>30){
    perc=5;
   }else if(diffGiorni<1){
    /* Meno di 24 ore: barra quasi piena */
    perc=95;
   }else{
    /* Tra 1 e 30 giorni: proporzionale */
    /* 30 giorni = 5%, 1 giorno = 95% */
    perc=5+(100-(diffGiorni/30*100))*0.9;
   }
   perc=Math.max(5,Math.min(100,perc));

   /* Label leggibile */
   var label='';
   if(diffOre<1)label='Meno di 1 ora!';
   else if(diffOre<24)label='Tra '+Math.round(diffOre)+' ore';
   else if(diffGiorni<2)label='Domani';
   else if(diffGiorni<30)label='Tra '+Math.round(diffGiorni)+' giorni';
   else label='Tra più di un mese';

   var colore=id==='cd-e'?'#3e765e':'#083278';
   var wrap=document.createElement('div');
   wrap.className='cd-progress-wrap';
   wrap.innerHTML='<div class="cd-progress"><span style="width:'+perc+'%;background:'+colore+'"></span></div>'+
    '<div class="cd-progress-label">'+label+'</div>';
   cd.parentNode.appendChild(wrap);
  });
 };
 /* Riapplica ogni secondo insieme al countdown */
 var _origAvvia=window.avviaCD;
 if(_origAvvia){
  window.avviaCD=function(){
   var r=_origAvvia.apply(this,arguments);
   /* Aggiorna barra ogni secondo */
   if(window._barTimer)clearInterval(window._barTimer);
   window._barTimer=setInterval(function(){
    if(document.getElementById('cd-e')||document.getElementById('cd-n')){
     window.aggiungiProgressBar();
    }else{
     clearInterval(window._barTimer);
    }
   },1000);
   return r;
  };
 }
})();
  /* === NUOVA FUNZIONE CALENDARIO con filtro funzionante === */
window.cal=function(el){
 var anno=calAnno,mese=calMese;
 var oggi=new Date();oggi.setHours(0,0,0,0);
 var primo=new Date(anno,mese,1);
 var inizioSett=(primo.getDay()+6)%7;
 var ggMese=new Date(anno,mese+1,0).getDate();
 var celle=[];
 for(var i=0;i<inizioSett;i++)celle.push(null);
 for(var d=1;d<=ggMese;d++)celle.push(new Date(anno,mese,d));
 while(celle.length%7!==0)celle.push(null);
 var filtroAttivo=window.calFiltro||'tutti';
 var mostraEventi=filtroAttivo==='tutti'||filtroAttivo==='catering';
 var mostraNoleggi=filtroAttivo==='tutti'||filtroAttivo==='noleggi';
 var vedE=puoVedere(user.ruolo,'evento')&&mostraEventi;
 var vedN=puoVedere(user.ruolo,'noleggio')&&mostraNoleggi;
 var creaE=puoCreare(user.ruolo,'evento');
 var creaN=puoCreare(user.ruolo,'noleggio');
 var bottoni='';
 if(creaE)bottoni+='<button class="btn-crea evento" id="btn-nuovo-evento">+ Crea Evento</button>';
 if(creaN)bottoni+='<button class="btn-crea noleggio" id="btn-nuovo-noleggio">+ Crea Noleggio</button>';
 var legenda='';
 if(vedE)legenda+='<span><i style="background:#bbf7d0"></i>Evento</span>';
 if(vedN)legenda+='<span><i style="background:#bfdbfe"></i>Noleggio</span><span><i style="background:#fed7aa"></i>Da confermare</span>';
 var puoFiltrare=puoVedere(user.ruolo,'evento')&&puoVedere(user.ruolo,'noleggio')&&user.ruolo!=='Magazzino2';
 var filtroHtml=puoFiltrare?'<div class="cal-filtro" id="filtro-cal"><button type="button" data-filtro="tutti" class="'+(filtroAttivo==='tutti'?'active':'')+'">Tutti</button><button type="button" data-filtro="catering" class="'+(filtroAttivo==='catering'?'active':'')+'">🍽️ Catering</button><button type="button" data-filtro="noleggi" class="'+(filtroAttivo==='noleggi'?'active':'')+'">🚚 Noleggi</button></div>':'';

 var html='<div class="page">';
 html+='<div style="margin-bottom:22px"><p class="eyebrow">Pianificazione</p><h1 class="title">Calendario</h1><p class="lede">Vista mensile.</p></div>';
 html+='<div class="cal-toolbar"><div class="cal-nav">';
 html+='<button id="cal-prev">‹</button>';
 html+='<span class="mese">'+MESI[mese]+' <select id="cal-anno-sel">';
 for(var a=2025;a<=2032;a++){html+='<option value="'+a+'"'+(a===anno?' selected':'')+'>'+a+'</option>';}
 html+='</select></span>';
 html+='<button id="cal-next">›</button>';
 html+='<button id="cal-oggi" style="width:auto;padding:0 12px;font-size:.72rem;font-weight:700">Oggi</button>';
 html+='</div><div class="cal-azioni">'+bottoni+'</div></div>';
 html+=filtroHtml;
 html+='<div class="cal-legenda">'+legenda+'</div>';
 html+='<div style="overflow-x:auto"><div class="cal-griglia">';
 for(var g=0;g<GIORNI.length;g++){html+='<div class="cal-int">'+GIORNI[g]+'</div>';}
 for(var i2=0;i2<celle.length;i2++){
  var day=celle[i2];
  if(!day){html+='<div class="cal-giorno vuoto"></div>';continue;}
  var eventiG=vedE?EVENTI.filter(function(e){return stessaData(e.inizio,day)}):[];
  var nolG=vedN?NOLEGGI.filter(function(n){return inRange(day,n)}):[];
  var isOggi=day.getTime()===oggi.getTime();
  var cls='cal-giorno';
  if(eventiG.length&&nolG.length)cls+=' ha-entrambi';
  else if(eventiG.length)cls+=' ha-eventi';
  else if(nolG.length)cls+=' ha-noleggi';
  if(isOggi)cls+=' oggi';
  var chips='';
  eventiG.slice(0,2).forEach(function(e){chips+='<span class="cal-chip evento" data-id="'+e.id+'" data-tipo="evento">'+e.titolo+'</span>'});
  nolG.slice(0,2).forEach(function(n){var pend=n.stato!=='confermato';chips+='<span class="cal-chip noleggio '+(pend?'pending':'')+'" data-id="'+n.id+'" data-tipo="noleggio">'+n.titolo+'</span>'});
  var tot=eventiG.length+nolG.length;
  if(tot>2)chips+='<span class="cal-chip piu">+'+(tot-2)+'</span>';
  html+='<div class="'+cls+'" data-giorno="'+day.toISOString()+'"><span class="num">'+day.getDate()+'</span>'+chips+'</div>';
 }
 html+='</div></div><div class="cal-pannello" id="cal-pannello"></div></div>';
 el.innerHTML=html;

 /* NAVIGAZIONE */
 document.getElementById('cal-prev').onclick=function(){calMese--;if(calMese<0){calMese=11;calAnno--}cal(el)};
 document.getElementById('cal-next').onclick=function(){calMese++;if(calMese>11){calMese=0;calAnno++}cal(el)};
 document.getElementById('cal-oggi').onclick=function(){var n=new Date();calMese=n.getMonth();calAnno=n.getFullYear();cal(el)};
 document.getElementById('cal-anno-sel').onchange=function(e){calAnno=parseInt(e.target.value);cal(el)};
 var be=document.getElementById('btn-nuovo-evento');if(be)be.onclick=function(){apriModaleEvento()};
 var bn=document.getElementById('btn-nuovo-noleggio');if(bn)bn.onclick=function(){apriModaleNoleggio()};

 /* FILTRO — agganciato direttamente su ogni bottone */
 var filtroBox=document.getElementById('filtro-cal');
 if(filtroBox){
  var bottoniFiltro=filtroBox.querySelectorAll('button');
  for(var fb=0;fb<bottoniFiltro.length;fb++){
   bottoniFiltro[fb].onclick=function(ev){
    ev.preventDefault();
    ev.stopPropagation();
    var nuovoFiltro=this.dataset.filtro;
    window.calFiltro=nuovoFiltro;
    /* Ricarica il calendario SUBITO */
    cal(el);
    return false;
   };
  }
 }

 /* CHIP → Drawer */
 var chips=document.querySelectorAll('.cal-chip[data-id]');
 for(var c=0;c<chips.length;c++){
  chips[c].onclick=(function(chip){
   return function(ev){
    ev.stopPropagation();
    var id=chip.dataset.id;
    var tipo=chip.dataset.tipo;
    if(tipo==='evento'){var ev=EVENTI.find(function(x){return x.id===id});if(ev)apriDrawerEnt('evento',ev)}
    else{var nl=NOLEGGI.find(function(x){return x.id===id});if(nl)apriDrawerEnt('noleggio',nl)}
   };
  })(chips[c]);
 }

 /* GIORNO → Pannello */
 var giorni=document.querySelectorAll('.cal-giorno[data-giorno]');
 for(var gg=0;gg<giorni.length;gg++){
  giorni[gg].onclick=function(){
   var dt=new Date(this.dataset.giorno);
   mostraPann(dt);
   document.querySelectorAll('.cal-giorno').forEach(function(x){x.style.outline=''});
   this.style.outline='2px solid #083278';
  };
 }
};
  /* === SPUNTE VERE (solo se clicchi) === */
(function(){
 var st=document.createElement('style');
 st.textContent='.visto-badge{display:none !important}'+
  '.nota-pallino{display:inline-block;width:8px;height:8px;border-radius:50%;margin-left:8px;vertical-align:middle;transition:all .3s}'+
  '.nota-pallino.nuova{background:#f59e0b;box-shadow:0 0 0 3px rgba(245,158,11,0.2);animation:pulse-nuova 1.5s infinite}'+
  '.nota-pallino.vista{background:#10b981;opacity:.5;box-shadow:none;animation:none}'+
  '@keyframes pulse-nuova{0%,100%{box-shadow:0 0 0 3px rgba(245,158,11,0.2)}50%{box-shadow:0 0 0 6px rgba(245,158,11,0)}}'+
  '.h4-nota-wrapper{cursor:pointer;display:flex;align-items:center;user-select:none}'+
  '.h4-nota-wrapper:hover{opacity:.85}';
 document.head.appendChild(st);
})();

(function(){
 var _orig=window.apriDrawerEnt;
 if(_orig){
  window.apriDrawerEnt=function(tipo,obj){
   var r=_orig.apply(this,arguments);
   setTimeout(function(){
    var body=document.getElementById('d-body');
    if(!body)return;
    body.querySelectorAll('.visto-badge').forEach(function(b){b.remove()});
    /* Aggiungi pallino alle sezioni note */
    body.querySelectorAll('h4').forEach(function(h){
     var testo=h.textContent.trim();
     if(!/^(📝|🍽️|👨‍🍳|📦|🔒)/.test(testo))return;
     var oldP=h.querySelector('.nota-pallino');
     if(oldP)oldP.remove();
     var idSez=obj.id+'-'+testo.replace(/[^a-zA-Z]/g,'');
     var visto=isVisto(idSez,'note');
     var p=document.createElement('span');
     p.className='nota-pallino '+(visto?'vista':'nuova');
     h.appendChild(p);
     /* Cliccando su h4 → segna come vista */
     h.style.cursor='pointer';
     h.onclick=function(){
      if(!isVisto(idSez,'note')){
       segnaVisto(idSez,'note');
       p.className='nota-pallino vista';
      }
     };
    });
    /* Allegati: cliccando su un allegato lo segna come visto */
    body.querySelectorAll('.allegato-riga').forEach(function(riga){
     var nomeEl=riga.querySelector('strong');
     if(!nomeEl)return;
     var nomeFile=nomeEl.textContent.trim();
     var idAll=obj.id+'-'+nomeFile;
     if(isVisto(idAll,'allegato'))riga.classList.add('visto');
     /* Click sull'allegato → segna visto */
     var btnAnt=riga.querySelector('.allegato-btn.anteprima');
     if(btnAnt){
      var _origBtn=btnAnt.onclick;
      btnAnt.onclick=function(ev){
       segnaVisto(idAll,'allegato');
       riga.classList.add('visto');
       if(_origBtn)_origBtn.call(this,ev);
      };
     }
    });
   },180);
   return r;
  };
 }
})();
  /* === PDF UNITO VERO con pdf-lib === */
(function(){
 if(document.getElementById('pdf-lib-script'))return;
 var s=document.createElement('script');
 s.id='pdf-lib-script';
 s.src='https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js';
 document.head.appendChild(s);
})();

window.scaricaUnicoPdf=async function(lista,sezione){
 if(!window.PDFLib){
  alert('Attendi 2 secondi e riprova (libreria PDF in caricamento).');
  return;
 }
 try{
  var PDFDocument=window.PDFLib.PDFDocument;
  var rgb=window.PDFLib.rgb;
  var mergedPdf=await PDFDocument.create();

  /* COPERTINA */
  var cover=mergedPdf.addPage([595,842]);
  var fontB=await mergedPdf.embedFont(window.PDFLib.StandardFonts.HelveticaBold);
  var fontR=await mergedPdf.embedFont(window.PDFLib.StandardFonts.Helvetica);
  cover.drawRectangle({x:0,y:782,width:595,height:60,color:rgb(0.03,0.20,0.47)});
  cover.drawText(sezione||'Allegati',{x:30,y:805,size:22,font:fontB,color:rgb(1,1,1)});
  cover.drawText(lista.length+' allegati',{x:30,y:790,size:10,font:fontR,color:rgb(0.8,0.9,1)});
  cover.drawText('Contenuto:',{x:30,y:740,size:13,font:fontB,color:rgb(0.08,0.13,0.22)});
  var yc=720;
  for(var i=0;i<lista.length;i++){
   cover.drawText((i+1)+'. '+(lista[i].nome||'file'),{x:30,y:yc,size:11,font:fontR,color:rgb(0.2,0.25,0.35)});
   yc-=18;
   if(yc<60)break;
  }

  /* Helper: converti dataURL in Uint8Array */
  function dataURLtoUint8(dataURL){
   var base64=dataURL.split(',')[1];
   var bin=atob(base64);
   var len=bin.length;
   var bytes=new Uint8Array(len);
   for(var k=0;k<len;k++)bytes[k]=bin.charCodeAt(k);
   return bytes;
  }

  /* UNISCI OGNI ALLEGATO */
  var uniti=0;
  for(var j=0;j<lista.length;j++){
   var al=lista[j];
   if(!al||!al.data)continue;
   var mime=al.mime||'';
   var nomeFile=(al.nome||'').toLowerCase();
   /* PDF */
   if(mime.indexOf('pdf')>=0||nomeFile.endsWith('.pdf')){
    try{
     var pdfBytes=dataURLtoUint8(al.data);
     var srcDoc=await PDFDocument.load(pdfBytes,{ignoreEncryption:true});
     var copie=await mergedPdf.copyPages(srcDoc,srcDoc.getPageIndices());
     for(var ci=0;ci<copie.length;ci++)mergedPdf.addPage(copie[ci]);
     uniti++;
    }catch(e){console.warn('PDF non unibile:',al.nome,e)}
   }else if(mime.indexOf('image/')===0){
    /* Immagine → pagina */
    try{
     var imgBytes=dataURLtoUint8(al.data);
     var img;
     if(mime.indexOf('png')>=0)img=await mergedPdf.embedPng(imgBytes);
     else img=await mergedPdf.embedJpg(imgBytes);
     var page=mergedPdf.addPage([595,842]);
     var dim=img.scaleToFit(535,800);
     page.drawImage(img,{x:(595-dim.width)/2,y:(842-dim.height)/2,width:dim.width,height:dim.height});
     uniti++;
    }catch(e){console.warn('Immagine non convertibile:',al.nome,e)}
   }
  }

  if(uniti===0){
   alert('Nessun allegato unibile in questa sezione.');
   return;
  }

  /* SALVA */
  var out=await mergedPdf.save();
  var blob=new Blob([out],{type:'application/pdf'});
  var url=URL.createObjectURL(blob);
  var a=document.createElement('a');
  a.href=url;
  a.download='Allegati_'+String(sezione||'').replace(/[^a-zA-Z0-9]/g,'_')+'.pdf';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url)},5000);
 }catch(err){
  alert('Errore: '+err.message);
 }
};
  /* === ALLEGATI PIÙ CHIARI === */
(function(){
 var st=document.createElement('style');
 st.textContent='.allegato-riga{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #e5e9f0;border-radius:12px;padding:12px 14px;margin-bottom:8px;transition:all .15s}'+
  '.allegato-riga:hover{border-color:#c4d9f2;box-shadow:0 4px 12px rgba(8,50,120,0.06);transform:translateX(2px)}'+
  '.allegato-riga.visto{background:#f8fafc;opacity:.85}'+
  '.allegato-icona{width:42px;height:42px;border-radius:10px;display:grid;place-items:center;font-size:1.3rem;flex-shrink:0;background:#eaf1fb;color:#083278}'+
  '.allegato-info{flex:1;min-width:0}'+
  '.allegato-info strong{display:block;font-size:.85rem;font-weight:700;color:#152238;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-bottom:3px}'+
  '.allegato-riga.visto .allegato-info strong{color:#6b778c;font-weight:600}'+
  '.allegato-riga.visto .allegato-info strong::before{content:"✓ ";color:#10b981;font-weight:800}'+
  '.allegato-info small{display:block;font-size:.7rem;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:.03em}'+
  '.allegato-azioni{display:flex;gap:6px;flex-shrink:0}'+
  '.allegato-btn{padding:9px 14px;border-radius:9px;font-size:.75rem;font-weight:700;border:1.5px solid #e5e9f0;background:#fff;color:#152238;cursor:pointer;transition:all .15s;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}'+
  '.allegato-btn:hover{background:#f5f7fb;border-color:#c4d1e5}'+
  '.allegato-btn.anteprima{background:#083278;color:#fff;border-color:#083278}'+
  '.allegato-btn.anteprima:hover{background:#0b438d}'+
  '@media (max-width:520px){.allegato-riga{padding:10px 12px;gap:10px}.allegato-icona{width:36px;height:36px;font-size:1.1rem}.allegato-info strong{font-size:.78rem}.allegato-azioni{flex-direction:column;gap:4px}.allegato-btn{padding:7px 10px;font-size:.68rem}}';
 document.head.appendChild(st);
})();
  /* === SPUNTE ALLEGATI (con pallino) === */
(function(){
 var st=document.createElement('style');
 st.textContent='.allegato-pallino{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px;flex-shrink:0;transition:all .3s}'+
  '.allegato-pallino.nuovo{background:#f59e0b;box-shadow:0 0 0 3px rgba(245,158,11,0.2);animation:pulse-all 1.5s infinite}'+
  '.allegato-pallino.visto{background:#10b981;opacity:.5;box-shadow:none;animation:none}'+
  '@keyframes pulse-all{0%,100%{box-shadow:0 0 0 3px rgba(245,158,11,0.2)}50%{box-shadow:0 0 0 6px rgba(245,158,11,0)}}'+
  '.allegato-riga{position:relative}'+
  '.allegato-riga.visto{background:#f8fafc;opacity:.85}'+
  '.allegato-riga.visto .allegato-info strong{color:#6b778c;font-weight:600}';
 document.head.appendChild(st);
})();

(function(){
 /* Override del drawer per aggiungere pallino agli allegati */
 var _orig=window.apriDrawerEnt;
 if(_orig){
  window.apriDrawerEnt=function(tipo,obj){
   var r=_orig.apply(this,arguments);
   setTimeout(function(){
    var body=document.getElementById('d-body');
    if(!body)return;
    body.querySelectorAll('.allegato-riga').forEach(function(riga){
     var nomeEl=riga.querySelector('strong');
     if(!nomeEl)return;
     var nomeFile=nomeEl.textContent.trim();
     var idAll=obj.id+'-'+nomeFile;
     var visto=isVisto(idAll,'allegato');
     /* Rimuovi pallino vecchio */
     var oldP=riga.querySelector('.allegato-pallino');
     if(oldP)oldP.remove();
     /* Aggiungi pallino all'inizio della riga */
     var p=document.createElement('span');
     p.className='allegato-pallino '+(visto?'visto':'nuovo');
     riga.insertBefore(p,riga.firstChild);
     /* Applica classe visto */
     if(visto)riga.classList.add('visto');
     else riga.classList.remove('visto');
     /* Click su anteprima → segna visto */
     var btn=riga.querySelector('.allegato-btn.anteprima');
     if(btn){
      var _origClick=btn.onclick;
      btn.onclick=function(ev){
       segnaVisto(idAll,'allegato');
       p.className='allegato-pallino visto';
       riga.classList.add('visto');
       if(_origClick)_origClick.call(this,ev);
      };
     }
     /* Anche il click su tutta la riga segna come visto */
     riga.addEventListener('click',function(ev){
      if(ev.target.closest('.allegato-btn'))return;
      if(!isVisto(idAll,'allegato')){
       segnaVisto(idAll,'allegato');
       p.className='allegato-pallino visto';
       riga.classList.add('visto');
      }
     });
    });
   },250);
   return r;
  };
 }
})();
  /* === POPUP BENVENUTO con notifiche nuove === */
(function(){
 var st=document.createElement('style');
 st.textContent='.benvenuto-overlay{position:fixed;inset:0;background:rgba(21,34,56,0.5);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);z-index:99999;display:grid;place-items:center;padding:20px;animation:fadeInB .3s ease-out}'+
  '@keyframes fadeInB{from{opacity:0}to{opacity:1}}'+
  '@keyframes popInB{0%{transform:scale(0.85);opacity:0}60%{transform:scale(1.03)}100%{transform:scale(1);opacity:1}}'+
  '.benvenuto-card{background:#fff;border-radius:24px;padding:36px 32px;max-width:440px;width:100%;text-align:center;box-shadow:0 30px 80px rgba(21,34,56,0.35);animation:popInB .5s cubic-bezier(0.34,1.56,0.64,1)}'+
  '.benvenuto-emoji{font-size:4rem;margin-bottom:16px;display:block;line-height:1}'+
  '.benvenuto-nome{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;color:#083278;margin-bottom:8px}'+
  '.benvenuto-testo{font-size:.9rem;color:#6b778c;line-height:1.5;margin-bottom:24px}'+
  '.benvenuto-notif{background:linear-gradient(135deg,#fff7ed,#fed7aa);border:1.5px solid #fdba74;border-radius:14px;padding:16px;margin-bottom:20px}'+
  '.benvenuto-notif strong{display:block;font-size:1.3rem;font-weight:800;color:#9a3412;margin-bottom:4px}'+
  '.benvenuto-notif span{font-size:.78rem;color:#9a3412;opacity:.85;font-weight:600}'+
  '.benvenuto-btn{width:100%;padding:14px;background:linear-gradient(135deg,#083278,#0b438d);color:#fff;border:0;border-radius:12px;font-weight:800;font-size:.9rem;cursor:pointer;transition:all .18s;box-shadow:0 8px 20px rgba(8,50,120,0.28);letter-spacing:.02em}'+
  '.benvenuto-btn:hover{transform:translateY(-2px);box-shadow:0 12px 26px rgba(8,50,120,0.35)}';
 document.head.appendChild(st);
})();

function mostraPopupBenvenuto(){
 if(!user)return;
 var notifiche=notifichePerUtente(user);
 var nuove=notifiche.filter(function(n){return !isLetta(user.username,n.id)});
 var emoji={'Amministratore':'👑','Wedding':'💍','Cucina':'👨‍🍳','Sala':'🤵','Magazzino':'📦','Magazzino2':'🚚'}[user.ruolo]||'👋';
 var saluto={'Amministratore':'Buon lavoro, capo!','Wedding':'Che emozione!','Cucina':'Ai fornelli!','Sala':'Pronti al servizio!','Magazzino':'Tutto in ordine!','Magazzino2':'Si parte!'}[user.ruolo]||'Bentornato!';
 var ov=document.createElement('div');
 ov.className='benvenuto-overlay';
 var html='<div class="benvenuto-card">';
 html+='<div class="benvenuto-emoji">'+emoji+'</div>';
 html+='<div class="benvenuto-nome">'+saluto+'</div>';
 html+='<div class="benvenuto-testo">Ciao <b>'+user.nome+'</b>, benvenuto nel gestionale</div>';
 if(nuove.length>0){
  html+='<div class="benvenuto-notif"><strong>'+nuove.length+'</strong><span>'+(nuove.length===1?'nuova notifica per te':'nuove notifiche per te')+'</span></div>';
 }else{
  html+='<div class="benvenuto-notif" style="background:linear-gradient(135deg,#f0fdf4,#bbf7d0);border-color:#86efac"><strong style="color:#166534">✓</strong><span style="color:#166534">Nessuna nuova notifica</span></div>';
 }
 html+='<button class="benvenuto-btn" id="benvenuto-chiudi">Inizia a lavorare</button>';
 html+='</div>';
 ov.innerHTML=html;
 document.body.appendChild(ov);
 document.getElementById('benvenuto-chiudi').onclick=function(){
  ov.style.opacity='0';
  ov.style.transition='opacity .3s';
  setTimeout(function(){if(ov.parentNode)ov.parentNode.removeChild(ov)},300);
 };
 /* Chiudi anche cliccando fuori */
 ov.onclick=function(e){if(e.target===ov)document.getElementById('benvenuto-chiudi').click()};
}

/* === AGGANCIA AL LOGIN === */
(function(){
 var _orig=window.doLogin;
 if(_orig){
  window.doLogin=function(){
   var r=_orig.apply(this,arguments);
   if(user&&user.username){
   }
   return r;
  };
 }
})();
  /* === FIX POPUP: 6s + pulsante chiudi funzionante === */
(function(){
 /* Rimuovi override vecchio */
 window._benvenutoMostrato=false;
 var _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   var r=_origDash.apply(this,arguments);
   if(user&&user.username&&!window._benvenutoMostrato){
    window._benvenutoMostrato=true;
    setTimeout(function(){
     if(typeof mostraPopupBenvenuto==='function')mostraPopupBenvenuto();
    },4000);
   }
   return r;
  };
 }
 var _origLogin=window.login;
 if(_origLogin){
  window.login=function(){
   window._benvenutoMostrato=false;
   return _origLogin.apply(this,arguments);
  };
 }
})();

/* Override mostraPopupBenvenuto con pulsante funzionante */
window.mostraPopupBenvenuto=function(){
 if(!user)return;
 /* Rimuovi eventuale popup precedente */
 var oldOv=document.querySelector('.benvenuto-overlay');
 if(oldOv)oldOv.remove();

 var notifiche=notifichePerUtente(user);
 var nuove=notifiche.filter(function(n){return !isLetta(user.username,n.id)});
 var emoji={'Amministratore':'👑','Wedding':'💍','Cucina':'👨‍🍳','Sala':'🤵','Magazzino':'📦','Magazzino2':'🚚'}[user.ruolo]||'👋';
 var saluto={'Amministratore':'Buon lavoro, capo!','Wedding':'Che emozione!','Cucina':'Ai fornelli!','Sala':'Pronti al servizio!','Magazzino':'Tutto in ordine!','Magazzino2':'Si parte!'}[user.ruolo]||'Bentornato!';

 var ov=document.createElement('div');
 ov.className='benvenuto-overlay';

 var html='<div class="benvenuto-card">';
 html+='<div class="benvenuto-emoji">'+emoji+'</div>';
 html+='<div class="benvenuto-nome">'+saluto+'</div>';
 html+='<div class="benvenuto-testo">Ciao <b>'+user.nome+'</b>, benvenuto nel gestionale</div>';
 if(nuove.length>0){
  html+='<div class="benvenuto-notif"><strong>'+nuove.length+'</strong><span>'+(nuove.length===1?'nuova notifica per te':'nuove notifiche per te')+'</span></div>';
 }else{
  html+='<div class="benvenuto-notif" style="background:linear-gradient(135deg,#f0fdf4,#bbf7d0);border-color:#86efac"><strong style="color:#166534">✓</strong><span style="color:#166534">Nessuna nuova notifica</span></div>';
 }
 html+='<button type="button" class="benvenuto-btn" id="benvenuto-chiudi">Inizia a lavorare</button>';
 html+='</div>';

 ov.innerHTML=html;
 document.body.appendChild(ov);

 /* Funzione per chiudere */
 function chiudiPop(){
  ov.style.opacity='0';
  ov.style.transition='opacity .3s';
  setTimeout(function(){if(ov.parentNode)ov.parentNode.removeChild(ov)},300);
 }

 /* Aggancia il click con event listener diretto */
 setTimeout(function(){
  var btn=document.getElementById('benvenuto-chiudi');
  if(btn){
   btn.addEventListener('click',function(ev){
    ev.preventDefault();
    ev.stopPropagation();
    chiudiPop();
   });
  }
 },50);

 /* Click fuori dal popup chiude */
 ov.addEventListener('click',function(ev){
  if(ev.target===ov)chiudiPop();
 });
};
  /* === BLOCCO UNICO: Popup singolo + Anteprima chiudi + Ingrandisci evento === */

/* ===== 1. POPUP BENVENUTO — solo 1 dopo 6 secondi ===== */
(function(){
 /* Blocca qualsiasi altro popup precedente */
 var _tentativoMostra=false;
 /* Override definitivo di mostraPopupBenvenuto */
 window.mostraPopupBenvenuto=function(){
  if(!user)return;
  if(_tentativoMostra)return;
  _tentativoMostra=true;
  /* Rimuovi eventuali popup aperti */
  document.querySelectorAll('.benvenuto-overlay').forEach(function(p){p.remove()});

  var notifiche=notifichePerUtente(user);
  var nuove=notifiche.filter(function(n){return !isLetta(user.username,n.id)});
  var emoji={'Amministratore':'👑','Wedding':'💍','Cucina':'👨‍🍳','Sala':'🤵','Magazzino':'📦','Magazzino2':'🚚'}[user.ruolo]||'👋';
  var saluto={'Amministratore':'Buon lavoro, capo!','Wedding':'Che emozione!','Cucina':'Ai fornelli!','Sala':'Pronti al servizio!','Magazzino':'Tutto in ordine!','Magazzino2':'Si parte!'}[user.ruolo]||'Bentornato!';

  var ov=document.createElement('div');
  ov.className='benvenuto-overlay';
  var html='<div class="benvenuto-card">';
  html+='<div class="benvenuto-emoji">'+emoji+'</div>';
  html+='<div class="benvenuto-nome">'+saluto+'</div>';
  html+='<div class="benvenuto-testo">Ciao <b>'+user.nome+'</b>, benvenuto nel gestionale</div>';
  if(nuove.length>0){
   html+='<div class="benvenuto-notif"><strong>'+nuove.length+'</strong><span>'+(nuove.length===1?'nuova notifica per te':'nuove notifiche per te')+'</span></div>';
  }else{
   html+='<div class="benvenuto-notif" style="background:linear-gradient(135deg,#f0fdf4,#bbf7d0);border-color:#86efac"><strong style="color:#166534">✓</strong><span style="color:#166534">Nessuna nuova notifica</span></div>';
  }
  html+='<button type="button" class="benvenuto-btn" id="benvenuto-chiudi">Inizia a lavorare</button>';
  html+='</div>';
  ov.innerHTML=html;
  document.body.appendChild(ov);
  function chiudi(){
   ov.style.opacity='0';
   ov.style.transition='opacity .3s';
   setTimeout(function(){if(ov.parentNode)ov.parentNode.removeChild(ov)},300);
   setTimeout(function(){_tentativoMostra=false},1000);
  }
  setTimeout(function(){
   var b=document.getElementById('benvenuto-chiudi');
   if(b)b.onclick=chiudi;
  },30);
  ov.onclick=function(e){if(e.target===ov)chiudi()};
 };

 /* Aggancia UNA SOLA VOLTA: solo a 6 secondi dopo dashboard */
 var _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   var r=_origDash.apply(this,arguments);
   if(user&&user.username&&!window._popupMostratoInSessione){
    window._popupMostratoInSessione=true;
    setTimeout(function(){window.mostraPopupBenvenuto()},6000);
   }
   return r;
  };
 }
 /* Reset al logout */
 var _origLogin=window.login;
 if(_origLogin){
  window.login=function(){
   window._popupMostratoInSessione=false;
   _tentativoMostra=false;
   return _origLogin.apply(this,arguments);
  };
 }
})();

/* ===== 2. ANTEPRIMA — X e Indietro chiudono SOLO anteprima ===== */
(function(){
 /* Override di apriAnteprimaAllega per gestire ritorno corretto */
 var _origAnt=window.apriAnteprimaAllega;
 if(_origAnt){
  window.apriAnteprimaAllega=function(allegato){
   /* Salva riferimento all'evento/noleggio corrente per tornare indietro */
   window._entitaApertaAnteprima=window._entitaCorrenteDrawer||null;
   var r=_origAnt.apply(this,arguments);

   /* Override del bottone X del drawer per chiudere solo anteprima */
   setTimeout(function(){
    var btnX=document.getElementById('d-close');
    if(btnX){
     var _origX=btnX.onclick;
     btnX.onclick=function(ev){
      ev.preventDefault();
      ev.stopPropagation();
      /* Torna al drawer evento se c'era, altrimenti chiudi tutto */
      if(window._entitaApertaAnteprima){
       var ent=window._entitaApertaAnteprima;
       window._entitaApertaAnteprima=null;
       apriDrawerEnt(ent.tipo,ent.obj);
      }else{
       chiudiDrawer();
      }
     };
    }
    /* Override bottone Indietro */
    var btnInd=document.getElementById('d-indietro');
    if(btnInd){
     btnInd.onclick=function(ev){
      ev.preventDefault();
      ev.stopPropagation();
      if(window._entitaApertaAnteprima){
       var ent=window._entitaApertaAnteprima;
       window._entitaApertaAnteprima=null;
       apriDrawerEnt(ent.tipo,ent.obj);
      }else{
       chiudiDrawer();
      }
     };
    }
    /* Override background click */
    var bg=document.getElementById('d-bg');
    if(bg){
     bg.onclick=function(ev){
      if(window._entitaApertaAnteprima){
       var ent=window._entitaApertaAnteprima;
       window._entitaApertaAnteprima=null;
       apriDrawerEnt(ent.tipo,ent.obj);
      }else{
       chiudiDrawer();
      }
     };
    }
   },100);
   return r;
  };
 }

 /* Salva il contesto quando si apre il drawer evento/noleggio */
 var _origDrawer=window.apriDrawerEnt;
 if(_origDrawer){
  window.apriDrawerEnt=function(tipo,obj){
   window._entitaCorrenteDrawer={tipo:tipo,obj:obj};
   return _origDrawer.apply(this,arguments);
  };
 }
})();

/* ===== 3. PULSANTE INGRANDISCI evento/noleggio a tutta pagina ===== */
(function(){
 var st=document.createElement('style');
 st.textContent='.drawer.fullscreen{width:100vw !important;max-width:100vw !important;border-radius:0}'+
  '.drawer.fullscreen .drawer-body{max-width:1100px;margin:0 auto;width:100%}'+
  '.drawer.fullscreen .drawer-head,.drawer.fullscreen .drawer-foot{max-width:1100px;margin:0 auto;width:100%}'+
  '.drawer-ingrandisci{width:36px;height:36px;border-radius:10px;border:1px solid #e5e9f0;background:#fff;color:#6b778c;display:grid;place-items:center;font-size:1.05rem;flex-shrink:0;cursor:pointer;transition:all .15s;margin-right:6px}'+
  '.drawer-ingrandisci:hover{color:#083278;background:#f0f6ff;border-color:#c4d9f2}';
 document.head.appendChild(st);
})();

(function(){
 var _origDrawer=window.apriDrawerEnt;
 if(_origDrawer){
  window.apriDrawerEnt=function(tipo,obj){
   var r=_origDrawer.apply(this,arguments);
   setTimeout(function(){
    var head=document.querySelector('.drawer-head');
    if(!head||head.querySelector('.drawer-ingrandisci'))return;
    /* Aggiungi pulsante ingrandisci PRIMA della X */
    var btnExp=document.createElement('button');
    btnExp.className='drawer-ingrandisci';
    btnExp.title='Ingrandisci a tutta pagina';
    btnExp.innerHTML='⛶';
    head.insertBefore(btnExp,head.querySelector('.drawer-close'));
    btnExp.onclick=function(ev){
     ev.stopPropagation();
     var drawer=document.getElementById('d-panel');
     if(!drawer)return;
     drawer.classList.toggle('fullscreen');
     if(drawer.classList.contains('fullscreen')){
      btnExp.innerHTML='⛉';
      btnExp.title='Riduci';
     }else{
      btnExp.innerHTML='⛶';
      btnExp.title='Ingrandisci a tutta pagina';
     }
    };
   },150);
   return r;
  };
 }
 /* Chiudi fullscreen quando si chiude il drawer */
 var _origChiudi=window.chiudiDrawer;
 if(_origChiudi){
  window.chiudiDrawer=function(){
   var drawer=document.getElementById('d-panel');
   if(drawer)drawer.classList.remove('fullscreen');
   return _origChiudi.apply(this,arguments);
  };
 }
})();
  /* === FIX v3: Icona riduci + Popup singolo === */

/* ===== 1. PULSANTE INGRANDISCI con stessa icona ===== */
(function(){
 var st=document.createElement('style');
 st.textContent='.drawer-ingrandisci{width:36px;height:36px;border-radius:10px;border:1px solid #e5e9f0;background:#fff;color:#6b7280;display:grid;place-items:center;flex-shrink:0;cursor:pointer;transition:all .15s;margin-right:6px;padding:0}'+
  '.drawer-ingrandisci:hover{color:#083278;background:#f0f6ff;border-color:#c4d9f2}'+
  '.drawer-ingrandisci svg{display:block;pointer-events:none}';
 document.head.appendChild(st);
})();

(function(){
 var _origDrawer=window.apriDrawerEnt;
 if(_origDrawer){
  window.apriDrawerEnt=function(tipo,obj){
   var r=_origDrawer.apply(this,arguments);
   setTimeout(function(){
    var head=document.querySelector('.drawer-head');
    if(!head)return;
    /* Rimuovi eventuali pulsanti ingrandisci esistenti */
    head.querySelectorAll('.drawer-ingrandisci').forEach(function(b){b.remove()});
    /* Crea pulsante ingrandisci */
    var btnExp=document.createElement('button');
    btnExp.className='drawer-ingrandisci';
    btnExp.title='Ingrandisci a tutta pagina';
    btnExp.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>';
    head.insertBefore(btnExp,head.querySelector('.drawer-close'));
    btnExp.onclick=function(ev){
     ev.stopPropagation();
     var drawer=document.getElementById('d-panel');
     if(!drawer)return;
     var isFull=drawer.classList.toggle('fullscreen');
     if(isFull){
      btnExp.title='Riduci';
      btnExp.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14h6v6"/><path d="M20 10h-6V4"/><path d="M14 10l7-7"/><path d="M3 21l7-7"/></svg>';
     }else{
      btnExp.title='Ingrandisci a tutta pagina';
      btnExp.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>';
     }
    };
   },150);
   return r;
  };
 }
 var _origChiudi=window.chiudiDrawer;
 if(_origChiudi){
  window.chiudiDrawer=function(){
   var drawer=document.getElementById('d-panel');
   if(drawer)drawer.classList.remove('fullscreen');
   return _origChiudi.apply(this,arguments);
  };
 }
})();

/* ===== 2. POPUP SINGOLO — blocca definitivamente il doppione ===== */
(function(){
 /* Intercetta TUTTI i setTimeout che chiamano mostraPopupBenvenuto
    e lascia passare solo quello con delay >= 6000 */
 var _timeoutOriginale=window.setTimeout;
 window.setTimeout=function(fn,delay){
  if(typeof fn==='function'){
   var src=fn.toString();
   if(src.indexOf('mostraPopupBenvenuto')>=0){
    /* Se è un vecchio timeout (< 6000), ignoriamolo */
    if(delay&&delay<6000){
     return _timeoutOriginale(function(){},100);
    }
   }
  }
  return _timeoutOriginale.apply(window,arguments);
 };
})();
  /* === FORZA POPUP A 4 SECONDI === */
(function(){
 /* Intercetta TUTTI i setTimeout e blocca i popup con delay > 4000 */
 var _timeoutOriginale=window.setTimeout;
 window.setTimeout=function(fn,delay){
  if(typeof fn==='function'){
   var src=fn.toString();
   /* Se la funzione contiene "mostraPopupBenvenuto" e il delay è > 4000, blocca */
   if(src.indexOf('mostraPopupBenvenuto')>=0&&delay&&delay>4000){
    return _timeoutOriginale(function(){},100);
   }
  }
  return _timeoutOriginale.apply(window,arguments);
 };

 /* Aspetta che la dashboard sia pronta, poi mostra il popup a 4 secondi */
 var _origDash=window.dash;
 if(_origDash){
  window.dash=function(el){
   var r=_origDash.apply(this,arguments);
   if(user&&user.username&&!window._popupMostrato){
    window._popupMostrato=true;
    _timeoutOriginale(function(){
     if(typeof mostraPopupBenvenuto==='function'){
      mostraPopupBenvenuto();
     }
    },4000);
   }
   return r;
  };
 }

 /* Reset al logout */
 var _origLogin=window.login;
 if(_origLogin){
  window.login=function(){
   window._popupMostrato=false;
   return _origLogin.apply(this,arguments);
  };
 }
})();
/* === PERSONAGGIO CON CARTELLO — benvenuto === */
(function(){
 var _t=window.setTimeout.bind(window);

 /* SVG personaggi per ruolo */
 var SVG={
  'Amministratore':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:110px;height:145px">'+
   '<ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/>'+
   '<rect x="45" y="115" width="12" height="35" rx="6" fill="#2c3e50"/>'+
   '<rect x="63" y="115" width="12" height="35" rx="6" fill="#2c3e50"/>'+
   '<ellipse cx="51" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<ellipse cx="69" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="#083278"/>'+
   '<path d="M 50 55 L 60 70 L 70 55 Z" fill="#fff" opacity="0.95"/>'+
   '<rect x="56" y="70" width="8" height="35" rx="3" fill="#dc2626"/>'+
   '<rect x="22" y="60" width="14" height="45" rx="7" fill="#083278"/>'+
   '<circle cx="29" cy="108" r="8" fill="#f4c8a1"/>'+
   '<rect x="84" y="60" width="14" height="45" rx="7" fill="#083278"/>'+
   '<circle cx="91" cy="108" r="8" fill="#f4c8a1"/>'+
   '<circle cx="60" cy="35" r="24" fill="#f4c8a1"/>'+
   '<path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#2c3e50"/>'+
   '<circle cx="52" cy="35" r="2.5" fill="#152238"/>'+
   '<circle cx="68" cy="35" r="2.5" fill="#152238"/>'+
   '<path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/>'+
   '<circle cx="45" cy="42" r="3" fill="#e8a5a5" opacity="0.5"/>'+
   '<circle cx="75" cy="42" r="3" fill="#e8a5a5" opacity="0.5"/>'+
  '</svg>',

  'Wedding':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:110px;height:145px">'+
   '<ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/>'+
   '<path d="M 40 115 Q 40 150 60 150 Q 80 150 80 115 Z" fill="#fce7f3"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="#9d174d"/>'+
   '<circle cx="60" cy="35" r="24" fill="#f4c8a1"/>'+
   '<path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#4a2c2a"/>'+
   '<circle cx="52" cy="35" r="2.5" fill="#152238"/>'+
   '<circle cx="68" cy="35" r="2.5" fill="#152238"/>'+
   '<path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/>'+
   '<circle cx="45" cy="42" r="3" fill="#e8a5a5" opacity="0.5"/>'+
   '<circle cx="75" cy="42" r="3" fill="#e8a5a5" opacity="0.5"/>'+
   '<circle cx="42" cy="58" r="6" fill="#fff"/><circle cx="42" cy="58" r="3" fill="#9d174d"/>'+
  '</svg>',

  'Cucina':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:110px;height:145px">'+
   '<ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/>'+
   '<rect x="45" y="115" width="12" height="35" rx="6" fill="#2c3e50"/>'+
   '<rect x="63" y="115" width="12" height="35" rx="6" fill="#2c3e50"/>'+
   '<ellipse cx="51" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<ellipse cx="69" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="#f5f5f5"/>'+
   '<rect x="35" y="55" width="50" height="10" fill="#e5e5e5"/>'+
   '<rect x="22" y="60" width="14" height="45" rx="7" fill="#f5f5f5"/>'+
   '<circle cx="29" cy="108" r="8" fill="#f4c8a1"/>'+
   '<rect x="84" y="60" width="14" height="45" rx="7" fill="#f5f5f5"/>'+
   '<circle cx="91" cy="108" r="8" fill="#f4c8a1"/>'+
   '<circle cx="60" cy="35" r="24" fill="#f4c8a1"/>'+
   '<path d="M 36 32 Q 36 8 60 8 Q 84 8 84 32 Q 84 20 60 20 Q 36 20 36 32 Z" fill="#152238"/>'+
   '<path d="M 36 32 L 84 32 L 84 38 L 36 38 Z" fill="#152238"/>'+
   '<circle cx="52" cy="35" r="2.5" fill="#152238"/>'+
   '<circle cx="68" cy="35" r="2.5" fill="#152238"/>'+
   '<path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/>'+
  '</svg>',

  'Sala':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:110px;height:145px">'+
   '<ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/>'+
   '<rect x="45" y="115" width="12" height="35" rx="6" fill="#152238"/>'+
   '<rect x="63" y="115" width="12" height="35" rx="6" fill="#152238"/>'+
   '<ellipse cx="51" cy="150" rx="9" ry="4" fill="#083278"/>'+
   '<ellipse cx="69" cy="150" rx="9" ry="4" fill="#083278"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="#152238"/>'+
   '<path d="M 50 55 L 60 70 L 70 55 Z" fill="#fff" opacity="0.95"/>'+
   '<path d="M 56 70 L 64 70 L 62 100 L 58 100 Z" fill="#fff"/>'+
   '<path d="M 60 100 L 60 108" stroke="#152238" stroke-width="2"/>'+
   '<path d="M 50 100 Q 60 110 70 100" stroke="#152238" stroke-width="2" fill="none"/>'+
   '<rect x="22" y="60" width="14" height="45" rx="7" fill="#152238"/>'+
   '<circle cx="29" cy="108" r="8" fill="#f4c8a1"/>'+
   /* Vassoio */
   '<ellipse cx="97" cy="70" rx="22" ry="5" fill="#c9a961"/>'+
   '<rect x="95" y="70" width="4" height="12" fill="#c9a961"/>'+
   '<rect x="88" y="82" width="18" height="2" rx="1" fill="#c9a961"/>'+
   '<circle cx="97" cy="65" r="3" fill="#dc2626"/>'+
   '<circle cx="103" cy="67" r="2" fill="#fff"/>'+
   '<circle cx="91" cy="67" r="2" fill="#fff"/>'+
   '<rect x="84" y="60" width="14" height="12" rx="7" fill="#152238"/>'+
   '<circle cx="60" cy="35" r="24" fill="#f4c8a1"/>'+
   '<path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#152238"/>'+
   /* Papillon */
   '<path d="M 55 52 L 60 55 L 65 52 L 65 58 L 60 55 L 55 58 Z" fill="#000"/>'+
   '<circle cx="60" cy="55" r="1.5" fill="#c9a961"/>'+
   '<circle cx="52" cy="35" r="2.5" fill="#152238"/>'+
   '<circle cx="68" cy="35" r="2.5" fill="#152238"/>'+
   '<path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/>'+
  '</svg>',

  'Magazzino':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:110px;height:145px">'+
   '<ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/>'+
   '<rect x="45" y="115" width="12" height="35" rx="6" fill="#1e40af"/>'+
   '<rect x="63" y="115" width="12" height="35" rx="6" fill="#1e40af"/>'+
   '<ellipse cx="51" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<ellipse cx="69" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="#facc15"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="none" stroke="#ca8a04" stroke-width="2"/>'+
   '<rect x="35" y="80" width="50" height="6" fill="#ca8a04" opacity="0.6"/>'+
   '<rect x="55" y="55" width="10" height="65" fill="#ca8a04" opacity="0.4"/>'+
   '<rect x="22" y="60" width="14" height="45" rx="7" fill="#facc15"/>'+
   '<circle cx="29" cy="108" r="8" fill="#f4c8a1"/>'+
   '<rect x="84" y="60" width="14" height="45" rx="7" fill="#facc15"/>'+
   '<circle cx="91" cy="108" r="8" fill="#f4c8a1"/>'+
   /* Casella in mano */
   '<rect x="92" y="100" width="22" height="22" rx="2" fill="#a66d24"/>'+
   '<path d="M 92 108 L 114 108" stroke="#7a4d17" stroke-width="2"/>'+
   '<path d="M 103 100 L 103 122" stroke="#7a4d17" stroke-width="2"/>'+
   '<circle cx="60" cy="35" r="24" fill="#f4c8a1"/>'+
   /* Cappellino */
   '<path d="M 34 32 Q 34 10 60 10 Q 86 10 86 32 L 34 32 Z" fill="#1e40af"/>'+
   '<rect x="30" y="30" width="60" height="6" rx="3" fill="#0f2d7a"/>'+
   '<circle cx="52" cy="40" r="2.5" fill="#152238"/>'+
   '<circle cx="68" cy="40" r="2.5" fill="#152238"/>'+
   '<path d="M 52 48 Q 60 55 68 48" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/>'+
  '</svg>',

  'Magazzino2':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:110px;height:145px">'+
   '<ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/>'+
   '<rect x="45" y="115" width="12" height="35" rx="6" fill="#374151"/>'+
   '<rect x="63" y="115" width="12" height="35" rx="6" fill="#374151"/>'+
   '<ellipse cx="51" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<ellipse cx="69" cy="150" rx="9" ry="4" fill="#152238"/>'+
   '<rect x="35" y="55" width="50" height="65" rx="10" fill="#3b82f6"/>'+
   '<rect x="35" y="85" width="50" height="8" fill="#1e40af"/>'+
   '<rect x="22" y="60" width="14" height="45" rx="7" fill="#3b82f6"/>'+
   '<circle cx="29" cy="108" r="8" fill="#f4c8a1"/>'+
   '<rect x="84" y="60" width="14" height="45" rx="7" fill="#3b82f6"/>'+
   '<circle cx="91" cy="108" r="8" fill="#f4c8a1"/>'+
   /* Cappello da camionista */
   '<path d="M 32 32 Q 32 10 60 10 Q 88 10 88 32 L 32 32 Z" fill="#1e40af"/>'+
   '<ellipse cx="60" cy="34" rx="34" ry="5" fill="#1e40af"/>'+
   '<path d="M 32 34 Q 20 36 18 42 L 32 42 Z" fill="#1e40af"/>'+
   '<circle cx="60" cy="35" r="24" fill="#f4c8a1"/>'+
   '<circle cx="52" cy="38" r="2.5" fill="#152238"/>'+
   '<circle cx="68" cy="38" r="2.5" fill="#152238"/>'+
   '<path d="M 52 48 Q 60 55 68 48" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/>'+
   '<path d="M 46 30 Q 60 26 74 30" stroke="#1e40af" stroke-width="3" fill="none"/>'+
  '</svg>'
 };

 function mostraPersonaggio(){
  try{
   if(typeof user==='undefined'||!user||!user.username)return;
   if(document.getElementById('personaggio-attivo'))return;

   var notifiche=[];
   try{if(typeof notifichePerUtente==='function')notifiche=notifichePerUtente(user)}catch(e){}
   var nuove=notifiche.filter(function(n){
    try{return typeof isLetta==='function'?!isLetta(user.username,n.id):true}catch(e){return true}
   });

   var saluto={'Amministratore':'Buon lavoro, capo!','Wedding':'Che emozione!','Cucina':'Ai fornelli!','Sala':'Pronti al servizio!','Magazzino':'Tutto in ordine!','Magazzino2':'Si parte!'}[user.ruolo]||'Bentornato!';
   var nomeRuolo={'Amministratore':'Amministratore','Wedding':'Wedding Planner','Cucina':'Chef','Sala':'Cameriere','Magazzino':'Magazziniere','Magazzino2':'Autista'}[user.ruolo]||user.ruolo;
   var svg=SVG[user.ruolo]||SVG['Amministratore'];

   var wrap=document.createElement('div');
   wrap.id='personaggio-attivo';
   wrap.style.cssText='position:fixed;right:-300px;bottom:24px;z-index:99999;display:flex;align-items:flex-end;gap:0;transition:right .6s cubic-bezier(0.34,1.56,0.64,1);pointer-events:none;max-width:calc(100vw - 24px)';

   /* Personaggio */
   var pers=document.createElement('div');
   pers.style.cssText='flex-shrink:0;filter:drop-shadow(0 8px 20px rgba(8,50,120,0.25));transform:translateY(6px)';
   pers.innerHTML=svg;

   /* Cartello */
   var cartello=document.createElement('div');
   cartello.style.cssText='background:#fff;border:2px solid #083278;border-radius:16px;padding:14px 18px;margin-left:-8px;margin-bottom:30px;box-shadow:0 12px 30px rgba(8,50,120,0.2);min-width:220px;max-width:300px;position:relative;pointer-events:auto';
   /* Freccia del cartello (punta al personaggio) */
   cartello.style.setProperty('--arrow-color','#083278');

   var html='';
   html+='<div style="position:absolute;left:-11px;top:24px;width:0;height:0;border-style:solid;border-width:9px 11px 9px 0;border-color:transparent #083278 transparent transparent"></div>';
   html+='<div style="position:absolute;left:-8px;top:24px;width:0;height:0;border-style:solid;border-width:9px 11px 9px 0;border-color:transparent #fff transparent transparent"></div>';
   html+='<div style="font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.1em;color:#a66d24;margin-bottom:4px">'+nomeRuolo+'</div>';
   html+='<div style="font-family:Georgia,serif;font-size:1.05rem;font-weight:700;color:#083278;line-height:1.2;margin-bottom:8px">'+saluto+'</div>';
   if(nuove.length>0){
    html+='<div style="background:#fff7ed;border:1px solid #fdba74;border-radius:9px;padding:7px 10px;font-size:.75rem;color:#9a3412;font-weight:700;margin-bottom:10px">🔔 '+nuove.length+' nuov'+(nuove.length===1?'a notifica':'e notifiche')+'</div>';
   }else{
    html+='<div style="background:#f0fdf4;border:1px solid #86efac;border-radius:9px;padding:7px 10px;font-size:.75rem;color:#166534;font-weight:700;margin-bottom:10px">✓ Tutto a posto</div>';
   }
   html+='<button type="button" id="pers-inizia" style="width:100%;padding:9px;background:#083278;color:#fff;border:0;border-radius:9px;font-weight:700;font-size:.78rem;cursor:pointer">Inizia a lavorare</button>';
   html+='<button type="button" id="pers-x" style="position:absolute;top:6px;right:6px;background:transparent;border:0;color:#94a3b8;font-size:1rem;cursor:pointer;padding:2px 6px">✕</button>';
   cartello.innerHTML=html;

   wrap.appendChild(pers);
   wrap.appendChild(cartello);
   document.body.appendChild(wrap);

   /* Anima ingresso */
   _t(function(){
    wrap.style.right='24px';
    wrap.style.pointerEvents='auto';
   },50);

   function chiudi(){
    wrap.style.right='-300px';
    wrap.style.pointerEvents='none';
    _t(function(){if(wrap.parentNode)wrap.parentNode.removeChild(wrap)},700);
   }
   document.getElementById('pers-inizia').onclick=chiudi;
   document.getElementById('pers-x').onclick=chiudi;

   /* Auto-chiusura dopo 20 sec */
   _t(function(){if(wrap.parentNode)chiudi()},20000);

  }catch(e){
   console.warn('Errore personaggio:',e);
  }
 }

 /* Aggancia al dash (dopo login) */
 var _d=window.dash;
 if(_d){
  window.dash=function(el){
   var r=_d.apply(this,arguments);
   if(typeof user!=='undefined'&&user&&user.username&&!window._persMostrato){
    window._persMostrato=true;
    _t(mostraPersonaggio,4000);
   }
   return r;
  };
 }

 /* Reset al logout */
 var _l=window.login;
 if(_l){
  window.login=function(){
   window._persMostrato=false;
   return _l.apply(this,arguments);
  };
 }
})();
  /* === MESSAGGI PER FASCIA ORARIA === */
(function(){
 var _t=window.setTimeout.bind(window);
 var _ripeti=window.setInterval.bind(window);

 /* SVGs personaggi (abbreviati, solo i principali) */
 var SVG={
  'Amministratore':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:100px;height:130px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="45" y="115" width="12" height="35" rx="6" fill="#2c3e50"/><rect x="63" y="115" width="12" height="35" rx="6" fill="#2c3e50"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#083278"/><path d="M 50 55 L 60 70 L 70 55 Z" fill="#fff" opacity="0.95"/><rect x="56" y="70" width="8" height="35" rx="3" fill="#dc2626"/><rect x="22" y="60" width="14" height="45" rx="7" fill="#083278"/><rect x="84" y="60" width="14" height="45" rx="7" fill="#083278"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#2c3e50"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Cucina':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:100px;height:130px"><rect x="35" y="55" width="50" height="65" rx="10" fill="#f5f5f5"/><rect x="35" y="55" width="50" height="10" fill="#e5e5e5"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 32 Q 36 8 60 8 Q 84 8 84 32 Q 84 20 60 20 Q 36 20 36 32 Z" fill="#152238"/><path d="M 36 32 L 84 32 L 84 38 L 36 38 Z" fill="#152238"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Sala':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:100px;height:130px"><rect x="35" y="55" width="50" height="65" rx="10" fill="#152238"/><path d="M 50 55 L 60 70 L 70 55 Z" fill="#fff" opacity="0.95"/><path d="M 55 52 L 60 55 L 65 52 L 65 58 L 60 55 L 55 58 Z" fill="#000"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#152238"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Magazzino':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:100px;height:130px"><rect x="35" y="55" width="50" height="65" rx="10" fill="#facc15"/><rect x="35" y="80" width="50" height="6" fill="#ca8a04" opacity="0.6"/><rect x="55" y="55" width="10" height="65" fill="#ca8a04" opacity="0.4"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 34 32 Q 34 10 60 10 Q 86 10 86 32 L 34 32 Z" fill="#1e40af"/><rect x="30" y="30" width="60" height="6" rx="3" fill="#0f2d7a"/><circle cx="52" cy="40" r="2.5" fill="#152238"/><circle cx="68" cy="40" r="2.5" fill="#152238"/><path d="M 52 48 Q 60 55 68 48" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Magazzino2':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:100px;height:130px"><rect x="35" y="55" width="50" height="65" rx="10" fill="#3b82f6"/><rect x="35" y="85" width="50" height="8" fill="#1e40af"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 32 32 Q 32 10 60 10 Q 88 10 88 32 L 32 32 Z" fill="#1e40af"/><ellipse cx="60" cy="34" rx="34" ry="5" fill="#1e40af"/><circle cx="52" cy="38" r="2.5" fill="#152238"/><circle cx="68" cy="38" r="2.5" fill="#152238"/><path d="M 52 48 Q 60 55 68 48" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Wedding':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:100px;height:130px"><rect x="35" y="55" width="50" height="65" rx="10" fill="#9d174d"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#4a2c2a"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/><circle cx="42" cy="58" r="6" fill="#fff"/><circle cx="42" cy="58" r="3" fill="#9d174d"/></svg>'
 };

 /* Funzione mostra messaggio (uguale a prima) */
 function mostraMessaggio(testo,tipo,emojiExtra){
  if(!window.user||!user||!user.username)return;
  if(document.getElementById('personaggio-attivo'))return;
  var adesso=Date.now();
  var ultimo=parseInt(localStorage.getItem('ergo_ultimo_pers_'+user.username)||'0');
  if(adesso-ultimo<5*60*1000)return;
  localStorage.setItem('ergo_ultimo_pers_'+user.username,adesso.toString());

  var nomeRuolo={'Amministratore':'Amministratore','Wedding':'Wedding Planner','Cucina':'Chef','Sala':'Cameriere','Magazzino':'Magazziniere','Magazzino2':'Autista'}[user.ruolo]||user.ruolo;
  var svg=SVG[user.ruolo]||SVG['Amministratore'];
  var colore=(tipo==='evento'?'#3e765e':tipo==='noleggio'?'#083278':tipo==='meteo'?'#0891b2':tipo==='pausa'?'#a66d24':tipo==='buongiorno'?'#f59e0b':tipo==='buonanotte'?'#4c1d95':tipo==='info'?'#6a5a9a':'#6a5a9a');

  var wrap=document.createElement('div');
  wrap.id='personaggio-attivo';
  wrap.style.cssText='position:fixed;right:-320px;bottom:24px;z-index:99999;display:flex;align-items:flex-end;gap:0;transition:right .6s cubic-bezier(0.34,1.56,0.64,1);pointer-events:none;max-width:calc(100vw - 24px)';

  var pers=document.createElement('div');
  pers.style.cssText='flex-shrink:0;filter:drop-shadow(0 8px 20px rgba(8,50,120,0.25));transform:translateY(6px)';
  pers.innerHTML=svg;

  var cartello=document.createElement('div');
  cartello.style.cssText='background:#fff;border:2px solid '+colore+';border-radius:16px;padding:14px 18px;margin-left:-8px;margin-bottom:30px;box-shadow:0 12px 30px rgba(8,50,120,0.2);min-width:220px;max-width:300px;position:relative;pointer-events:auto';

  var html='';
  html+='<div style="position:absolute;left:-11px;top:24px;width:0;height:0;border-style:solid;border-width:9px 11px 9px 0;border-color:transparent '+colore+' transparent transparent"></div>';
  html+='<div style="position:absolute;left:-8px;top:24px;width:0;height:0;border-style:solid;border-width:9px 11px 9px 0;border-color:transparent #fff transparent transparent"></div>';
  html+='<div style="font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.1em;color:'+colore+';margin-bottom:6px">'+nomeRuolo+'</div>';
  html+=emojiExtra?'<div style="font-size:1.5rem;margin-bottom:6px">'+emojiExtra+'</div>':'';
  html+='<div style="font-size:.88rem;color:#152238;line-height:1.45;font-weight:600;margin-bottom:12px">'+testo+'</div>';
  html+='<button type="button" id="pers-ok" style="width:100%;padding:9px;background:'+colore+';color:#fff;border:0;border-radius:9px;font-weight:700;font-size:.78rem;cursor:pointer">Ok, capito!</button>';
  html+='<button type="button" id="pers-x" style="position:absolute;top:6px;right:6px;background:transparent;border:0;color:#94a3b8;font-size:1rem;cursor:pointer;padding:2px 6px">✕</button>';
  cartello.innerHTML=html;

  wrap.appendChild(pers);
  wrap.appendChild(cartello);
  document.body.appendChild(wrap);

  _t(function(){wrap.style.right='24px';wrap.style.pointerEvents='auto';},50);

  function chiudi(){
   wrap.style.right='-320px';
   wrap.style.pointerEvents='none';
   _t(function(){if(wrap.parentNode)wrap.parentNode.removeChild(wrap)},700);
  }
  document.getElementById('pers-ok').onclick=chiudi;
  document.getElementById('pers-x').onclick=chiudi;
  _t(function(){if(wrap.parentNode)chiudi()},25000);
 }

 /* === MESSAGGI PER FASCIA ORARIA === */
 function checkFasciaOraria(){
  if(!window.user||!user)return;
  var ora=new Date().getHours();
  var min=new Date().getMinutes();
  var oggi=new Date().toISOString().slice(0,10);

  var messaggio=null;
  var tipo='info';
  var emoji='';
  var chiave='';

  /* 5:00 - 6:00 → Sveglia presto */
  if(ora>=5&&ora<6){
   chiave='sveglia_presto';
   messaggio='Cavolo, sei già sveglio! Buona giornata! ☕';
   tipo='buongiorno';emoji='🌅';
  }
  /* 6:00 - 8:00 → Buona colazione */
  else if(ora>=6&&ora<8){
   chiave='colazione';
   messaggio='Buona colazione! Inizia la giornata con la carica giusta';
   tipo='buongiorno';emoji='🥐';
  }
  /* 8:00 - 10:00 → Buongiorno */
  else if(ora>=8&&ora<10){
   chiave='buongiorno';
   messaggio='Buongiorno! Pronto per una giornata produttiva?';
   tipo='buongiorno';emoji='☀️';
  }
  /* 10:00 - 11:00 → Spuntino */
  else if(ora>=10&&ora<11){
   chiave='spuntino';
   messaggio='Una piccola pausa con uno spuntino? Ne hai bisogno!';
   tipo='info';emoji='🍎';
  }
  /* 12:30 - 13:30 → Pranzo */
  else if((ora===12&&min>=30)||(ora===13&&min<=30)){
   chiave='pranzo';
   messaggio='È ora di pranzo! Buon appetito 🍝';
   tipo='pausa';emoji='🍝';
  }
  /* 15:00 - 16:00 → Caffè */
  else if(ora>=15&&ora<16){
   chiave='caffe';
   messaggio='Un caffè veloce per riprendere la carica? ☕';
   tipo='pausa';emoji='☕';
  }
  /* 18:00 - 19:00 → Fine giornata */
  else if(ora>=18&&ora<19){
   chiave='fine_giornata';
   messaggio='Quasi fine giornata! Hai fatto un ottimo lavoro';
   tipo='info';emoji='⭐';
  }
  /* 19:30 - 20:30 → Cena */
  else if((ora===19&&min>=30)||(ora===20&&min<=30)){
   chiave='cena';
   messaggio='Buona cena! Goditi la serata 🌙';
   tipo='pausa';emoji='🌙';
  }
  /* 21:00 - 23:00 → Rilassati */
  else if(ora>=21&&ora<23){
   chiave='rilassati';
   messaggio='Ora puoi rilassarti. Il lavoro può aspettare! 🛋️';
   tipo='buonanotte';emoji='🛋️';
  }
  /* 23:00 - 5:00 → Buonanotte */
  else if(ora>=23||ora<5){
   chiave='buonanotte';
   messaggio='È tardi, vai a dormire! Domani sarà un\'altra giornata';
   tipo='buonanotte';emoji='🌙';
  }

  if(!messaggio)return;

  /* Controlla se già mostrato oggi */
  var key='ergo_fascia_'+user.username+'_'+oggi+'_'+chiave;
  if(localStorage.getItem(key))return;
  localStorage.setItem(key,'1');

  /* Aspetta 30 secondi prima di mostrare (per non disturbare subito) */
  _t(function(){mostraMessaggio(messaggio,tipo,emoji)},30000);
 }

 /* === AVVIA === */
 function avviaFasce(){
  if(!window.user||!user)return;
  /* Check subito dopo 30 sec */
  _t(checkFasciaOraria,30000);
  /* Poi ogni 20 minuti (per catturare i cambi di fascia) */
  _ripeti(function(){
   if(window.user&&user)checkFasciaOraria();
  },20*60*1000);
 }

 var _l=window.login;
 if(_l){
  window.login=function(){
   _t(function(){avviaFasce()},5000);
   return _l.apply(this,arguments);
  };
 }

 if(window.user&&user&&user.username){
  _t(avviaFasce,5000);
 }
})();
  /* === FIX SVUOTA + ASSISTENTE PERSONALE === */
(function(){
 var _t=window.setTimeout.bind(window);

 /* === FIX 1: Svuota log accessi funzionante === */
 document.addEventListener('click',function(e){
  var btn=e.target.closest('#log-svuota');
  if(!btn)return;
  e.preventDefault();
  e.stopImmediatePropagation();
  if(confirm('Svuotare tutti i log accessi?')){
   localStorage.removeItem('ergo_log_accessi');
   var sez=document.getElementById('log-accessi-section');
   if(sez)sez.remove();
  }
 },true);

 /* === FIX 2: Assistente personale === */
 /* SVG personaggi */
 var SVG={
  'Amministratore':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:90px;height:120px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="45" y="115" width="12" height="35" rx="6" fill="#2c3e50"/><rect x="63" y="115" width="12" height="35" rx="6" fill="#2c3e50"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#083278"/><path d="M 50 55 L 60 70 L 70 55 Z" fill="#fff" opacity="0.95"/><rect x="56" y="70" width="8" height="35" rx="3" fill="#dc2626"/><rect x="22" y="60" width="14" height="45" rx="7" fill="#083278"/><rect x="84" y="60" width="14" height="45" rx="7" fill="#083278"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#2c3e50"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Cucina':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:90px;height:120px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#f5f5f5"/><rect x="35" y="55" width="50" height="10" fill="#e5e5e5"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 32 Q 36 8 60 8 Q 84 8 84 32 Q 84 20 60 20 Q 36 20 36 32 Z" fill="#152238"/><path d="M 36 32 L 84 32 L 84 38 L 36 38 Z" fill="#152238"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Sala':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:90px;height:120px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#152238"/><path d="M 50 55 L 60 70 L 70 55 Z" fill="#fff" opacity="0.95"/><path d="M 55 52 L 60 55 L 65 52 L 65 58 L 60 55 L 55 58 Z" fill="#000"/><ellipse cx="97" cy="70" rx="20" ry="4" fill="#c9a961"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#152238"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Magazzino':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:90px;height:120px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#facc15"/><rect x="35" y="80" width="50" height="6" fill="#ca8a04" opacity="0.6"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 34 32 Q 34 10 60 10 Q 86 10 86 32 L 34 32 Z" fill="#1e40af"/><rect x="30" y="30" width="60" height="6" rx="3" fill="#0f2d7a"/><circle cx="52" cy="40" r="2.5" fill="#152238"/><circle cx="68" cy="40" r="2.5" fill="#152238"/><path d="M 52 48 Q 60 55 68 48" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Magazzino2':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:90px;height:120px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#3b82f6"/><rect x="35" y="85" width="50" height="8" fill="#1e40af"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 32 32 Q 32 10 60 10 Q 88 10 88 32 L 32 32 Z" fill="#1e40af"/><ellipse cx="60" cy="34" rx="34" ry="5" fill="#1e40af"/><circle cx="52" cy="38" r="2.5" fill="#152238"/><circle cx="68" cy="38" r="2.5" fill="#152238"/><path d="M 52 48 Q 60 55 68 48" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
  'Wedding':'<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" style="width:90px;height:120px"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity="0.15"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#9d174d"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M 36 30 Q 36 8 60 8 Q 84 8 84 30 Q 78 24 60 24 Q 42 24 36 30 Z" fill="#4a2c2a"/><circle cx="52" cy="35" r="2.5" fill="#152238"/><circle cx="68" cy="35" r="2.5" fill="#152238"/><path d="M 52 45 Q 60 52 68 45" stroke="#152238" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'
 };

 /* Funzione che mostra il personaggio con messaggio E azioni opzionali */
 window.assistentePersonale=function(config){
  /* config = { testo, tipo, emoji, colore, bottoni:[{label,colore,azione}] } */
  if(!window.user||!user)return;
  if(document.getElementById('assistente-attivo'))return;

  var colore=config.colore||'#083278';
  var svg=SVG[user.ruolo]||SVG['Amministratore'];
  var nomeRuolo={'Amministratore':'Amministratore','Wedding':'Wedding Planner','Cucina':'Chef','Sala':'Cameriere','Magazzino':'Magazziniere','Magazzino2':'Autista'}[user.ruolo]||user.ruolo;

  var wrap=document.createElement('div');
  wrap.id='assistente-attivo';
  wrap.style.cssText='position:fixed;right:-350px;bottom:24px;z-index:999999;display:flex;align-items:flex-end;gap:0;transition:right .6s cubic-bezier(0.34,1.56,0.64,1);pointer-events:none;max-width:calc(100vw - 24px)';

  var pers=document.createElement('div');
  pers.style.cssText='flex-shrink:0;filter:drop-shadow(0 8px 20px rgba(8,50,120,0.25));transform:translateY(6px)';
  pers.innerHTML=svg;

  var cartello=document.createElement('div');
  cartello.style.cssText='background:#fff;border:2px solid '+colore+';border-radius:16px;padding:14px 18px;margin-left:-8px;margin-bottom:30px;box-shadow:0 12px 30px rgba(8,50,120,0.2);min-width:240px;max-width:320px;position:relative;pointer-events:auto';

  var html='';
  html+='<div style="position:absolute;left:-11px;top:24px;width:0;height:0;border-style:solid;border-width:9px 11px 9px 0;border-color:transparent '+colore+' transparent transparent"></div>';
  html+='<div style="position:absolute;left:-8px;top:24px;width:0;height:0;border-style:solid;border-width:9px 11px 9px 0;border-color:transparent #fff transparent transparent"></div>';
  html+='<div style="font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.1em;color:'+colore+';margin-bottom:6px">'+nomeRuolo+'</div>';
  if(config.emoji)html+='<div style="font-size:1.5rem;margin-bottom:6px">'+config.emoji+'</div>';
  html+='<div style="font-size:.88rem;color:#152238;line-height:1.45;font-weight:600;margin-bottom:12px">'+config.testo+'</div>';
  /* Bottoni */
  var bottoni=config.bottoni||[{label:'Ok, capito!',colore:colore,azione:null}];
  html+='<div style="display:flex;gap:6px;flex-direction:column">';
  bottoni.forEach(function(b,i){
   html+='<button type="button" class="assist-btn-'+i+'" style="width:100%;padding:9px;background:'+(b.colore||colore)+';color:#fff;border:0;border-radius:9px;font-weight:700;font-size:.78rem;cursor:pointer">'+b.label+'</button>';
  });
  html+='</div>';
  html+='<button type="button" id="assist-x" style="position:absolute;top:6px;right:6px;background:transparent;border:0;color:#94a3b8;font-size:1rem;cursor:pointer;padding:2px 6px">✕</button>';
  cartello.innerHTML=html;

  wrap.appendChild(pers);
  wrap.appendChild(cartello);
  document.body.appendChild(wrap);

  _t(function(){wrap.style.right='24px';wrap.style.pointerEvents='auto';},50);

  function chiudi(callback){
   wrap.style.right='-350px';
   wrap.style.pointerEvents='none';
   _t(function(){
    if(wrap.parentNode)wrap.parentNode.removeChild(wrap);
    if(callback)callback();
   },700);
  }
  bottoni.forEach(function(b,i){
   var btn=document.querySelector('.assist-btn-'+i);
   if(btn)btn.onclick=function(){
    chiudi(function(){if(b.azione)b.azione()});
   };
  });
  document.getElementById('assist-x').onclick=function(){chiudi()};
  if(config.autoClose!==false){
   _t(function(){if(wrap.parentNode)chiudi()},25000);
  }
 };

 /* === AGGANCIA CREAZIONE EVENTO === */
 var _origGenEv=window.generaNotifEvento;
 if(_origGenEv){
  window.generaNotifEvento=function(ev){
   var r=_origGenEv.apply(this,arguments);
   /* Dopo 500ms mostra il personaggio */
   _t(function(){
    window.assistentePersonale({
     testo:'<b>Evento creato!</b><br>'+ev.titolo+' è salvato correttamente',
     emoji:'🎉',
     colore:'#3e765e',
     bottoni:[{label:'Ottimo!',colore:'#3e765e'}]
    });
   },500);
   return r;
  };
 }

 /* === AGGANCIA CREAZIONE NOLEGGIO === */
 var _origGenNol=window.generaNotifNoleggio;
 if(_origGenNol){
  window.generaNotifNoleggio=function(nl){
   var r=_origGenNol.apply(this,arguments);
   _t(function(){
    window.assistentePersonale({
     testo:'<b>Noleggio confermato!</b><br>'+nl.titolo+' è salvato',
     emoji:'🚚',
     colore:'#083278',
     bottoni:[{label:'Perfetto!',colore:'#083278'}]
    });
   },500);
   return r;
  };
 }

 /* === AGGANCIA ELIMINAZIONE === */
 var _origConfElim=window.confermaElim;
 if(_origConfElim){
  window.confermaElim=function(obj){
   /* Mostra personaggio che chiede conferma */
   window.assistentePersonale({
    testo:'<b>Sei sicuro?</b><br>Vuoi davvero eliminare "'+obj.nome+'"?',
    emoji:'⚠️',
    colore:'#dc2626',
    autoClose:false,
    bottoni:[
     {label:'Sì, elimina',colore:'#dc2626',azione:function(){_origConfElim.call(window,obj)}},
     {label:'No, annulla',colore:'#94a3b8'}
    ]
   });
  };
 }

 /* === AGGANCIA SCELTA ALLEGATI === */
 var _origScaricaConScelta=window.scaricaAllegatiConScelta;
 if(_origScaricaConScelta){
  window.scaricaAllegatiConScelta=function(lista,sezione){
   if(!lista||lista.length===0){alert('Nessun allegato.');return}
   if(lista.length===1){
    scaricaAllega(lista[0]);
    return;
   }
   /* Personaggio che chiede come scaricare */
   window.assistentePersonale({
    testo:'<b>'+lista.length+' allegati</b> in "'+sezione+'"<br>Come vuoi scaricarli?',
    emoji:'📥',
    colore:'#0891b2',
    autoClose:false,
    bottoni:[
     {label:'📄 Singoli (uno per file)',colore:'#0891b2',azione:function(){
      lista.forEach(function(a,i){_t(function(){scaricaAllega(a)},i*300)});
     }},
     {label:'📚 Unico PDF',colore:'#083278',azione:function(){
      if(typeof scaricaUnicoPdf==='function')scaricaUnicoPdf(lista,sezione);
     }},
     {label:'Annulla',colore:'#94a3b8'}
    ]
   });
  };
 }

 /* === AGGANCIA ELIMINAZIONE EVENTO/NOLEGGIO === */
 var _origConfElimEnt=window.confermaElimEnt;
 if(_origConfElimEnt){
  window.confermaElimEnt=function(tipo,obj){
   window.assistentePersonale({
    testo:'<b>Sei sicuro?</b><br>Vuoi eliminare '+(tipo==='evento'?'l\'evento':'il noleggio')+' "'+obj.titolo+'"?',
    emoji:'⚠️',
    colore:'#dc2626',
    autoClose:false,
    bottoni:[
     {label:'Sì, elimina',colore:'#dc2626',azione:function(){_origConfElimEnt.call(window,tipo,obj)}},
     {label:'No, annulla',colore:'#94a3b8'}
    ]
   });
  };
 }

 console.log('✅ Assistente personale attivo');
})();


/* ============================================================
   ERGO vNext — ottimizzazione finale e integrazione Supabase
   ============================================================ */
(function(){
  'use strict';
  var wait = window.setTimeout.bind(window);

  /*
   * Configurazione: valorizzare uno dei due punti prima del deploy.
   * NON inserire mai la service_role key nel frontend: usare solo anonKey.
   * Esempio:
   * window.ERGO_SUPABASE_CONFIG = {
   *   url: 'https://xxxx.supabase.co',
   *   anonKey: 'eyJ...'
   * };
   */
  var cfg = window.ERGO_SUPABASE_CONFIG || null;
  if(!cfg){
    try{ cfg = JSON.parse(localStorage.getItem('ergo_supabase_config') || 'null'); }catch(e){ cfg=null; }
  }
  var sb = null;
  try{
    if(cfg && cfg.url && cfg.anonKey && window.supabase){
      sb = window.supabase.createClient(cfg.url, cfg.anonKey, {
        auth:{persistSession:false, autoRefreshToken:false}
      });
    }
  }catch(e){ console.warn('Supabase non inizializzato',e); }
  window.ergoSupabase = sb;

  var syncTimer = null;
  var syncing = false;
  var collections = {
    'ergo_eventi':'evento',
    'ergo_noleggi':'noleggio',
    'ergo_notifiche':'notifica',
    'ergo_prodotti':'prodotto'
  };

  function productPayload(p){
    var sh=p.scheda||{};
    return {codice:p.codice,nome:p.nome,categoria:p.categoria||'',quantita:Number(p.quantita||0),posizione:p.posizione||'',costo_noleggio:Number(p.prezzo||p.costo_noleggio||0),note:p.note||'',foto_path:p.foto_path||((p.foto&&/^https?:/.test(p.foto))?'':p.foto)||'',scheda_materiale:sh.materiale||'',scheda_colore:sh.colore||'',scheda_dimensione:sh.dimensione||'',scheda_note:sh.note||''};
  }
  function eventPayload(e){
    return {nome_evento:e.titolo,data:(e.inizio||'').slice(0,10),data_display:e.data_display||e.inizio||'',location:e.location||'',ospiti:Number(e.ospiti||0),bambini:Number(e.bambini||0),staff:Number(e.staff||0),note_tutti:e.noteTutti||'',allegati_tutti:e.allegatiTutti||[],note_sala:e.noteSala||'',allegati_sala:e.allegatiSala||[],note_cucina:e.noteCucina||'',allegati_cucina:e.allegatiCucina||[],note_magazzino:e.noteMagazzino||'',allegati_magazzino:e.allegatiMagazzino||[],allegati_privati:e.allegatiPrivata||[]};
  }
  function firstAttachment(n,key){var a=(n[key]||[])[0]||{};return {name:a.nome||'',url:a.url||'',mime:a.mime||'',path:a.path||''};}
  function rentalPayload(n){
    var b=firstAttachment(n,'allegatiBolla'),d=firstAttachment(n,'allegatiDDT'),v=firstAttachment(n,'allegatiVario');
    return {titolo:n.titolo,inizio:n.inizio,fine:n.fine,stato:n.stato||'confermato',location:n.location||'',referente:n.referente||'',telefono:n.telefono||'',note:n.note||'',bolla:b.name||n.bolla||'Nessun file',ddt:d.name||n.ddt||'Nessun file',vario:v.name||n.vario||'Nessun file',bolla_url:b.url||n.bolla_url||null,ddt_url:d.url||n.ddt_url||null,vario_url:v.url||n.vario_url||null,bolla_path:b.path||n.bolla_path||null,ddt_path:d.path||n.ddt_path||null,vario_path:v.path||n.vario_path||null,bolla_mime:b.mime||n.bolla_mime||null,ddt_mime:d.mime||n.ddt_mime||null,vario_mime:v.mime||n.vario_mime||null};
  }
  async function upsertCollection(kind, rows){
    if(!sb || !Array.isArray(rows) || syncing) return;
    if(kind==='prodotto'){
      var products=rows.filter(function(r){return r && r.codice;}).map(productPayload);
      for(var i=0;i<products.length;i+=500){
        var pr=await sb.from('prodotti_noleggio').upsert(products.slice(i,i+500),{onConflict:'codice'});
        if(pr.error) throw pr.error;
      }
      return;
    }
    /* Eventi e noleggi vengono sincronizzati per chiave naturale: così gli ID
       numerici generati da Supabase restano la fonte ufficiale. */
    if(kind==='evento'){
      for(const e of rows.filter(Boolean)){
        var ep=eventPayload(e), found=await sb.from('eventi_catering').select('id').eq('nome_evento',ep.nome_evento).eq('data',ep.data).limit(1);
        if(found.error) throw found.error;
        var er=found.data&&found.data[0] ? await sb.from('eventi_catering').update(ep).eq('id',found.data[0].id) : await sb.from('eventi_catering').insert(ep);
        if(er.error) throw er.error;
      }
    }
    if(kind==='noleggio'){
      for(const n of rows.filter(Boolean)){
        var np=rentalPayload(n), nf=await sb.from('noleggi').select('id').eq('titolo',np.titolo).eq('inizio',np.inizio).limit(1);
        if(nf.error) throw nf.error;
        var nr=nf.data&&nf.data[0] ? await sb.from('noleggi').update(np).eq('id',nf.data[0].id) : await sb.from('noleggi').insert(np);
        if(nr.error) throw nr.error;
      }
    }
  }
  function scheduleSync(key){
    if(!sb || !collections[key]) return;
    clearTimeout(syncTimer);
    syncTimer=wait(async function(){
      try{
        var rows=JSON.parse(localStorage.getItem(key)||'[]');
        await upsertCollection(collections[key],rows);
      }catch(e){ console.warn('Sincronizzazione Supabase rinviata',e); }
    },700);
  }

  /* Evita richieste ripetute: una singola operazione batch per collezione. */
  var originalSetItem = Storage.prototype.setItem;
  Storage.prototype.setItem = function(key,value){
    originalSetItem.call(this,key,value);
    if(collections[key]) scheduleSync(key);
  };

  window.ergoDataUrlToFile=function(dataUrl,name){
    var parts=String(dataUrl).split(','), mime=(parts[0].match(/:(.*?);/)||[])[1]||'application/octet-stream';
    var raw=atob(parts[1]||''), bytes=new Uint8Array(raw.length);
    for(var i=0;i<raw.length;i++) bytes[i]=raw.charCodeAt(i);
    return new File([bytes],name,{type:mime});
  };
  window.ergoSupabaseUpload = async function(file, folder){
    if(!sb || !file) return null;
    var safe=String(file.name||'file').replace(/[^a-zA-Z0-9._-]/g,'_');
    var bucket=folder==='immagini_prodotti'?'immagini_prodotti':'allegati_noleggi';
    var path=Date.now()+'-'+safe;
    var res=await sb.storage.from(bucket).upload(path,file,{upsert:false,contentType:file.type||undefined});
    if(res.error) throw res.error;
    if(bucket==='immagini_prodotti'){
      var publicUrl=sb.storage.from(bucket).getPublicUrl(path);
      return {url:publicUrl.data.publicUrl,path:path,bucket:bucket,name:file.name,mime:file.type,size:file.size};
    }
    var signed=await sb.storage.from(bucket).createSignedUrl(path,3600);
    if(signed.error) throw signed.error;
    return {url:signed.data.signedUrl,path:path,bucket:bucket,name:file.name,mime:file.type,size:file.size};
  };

  function parseJsonList(value){
    if(Array.isArray(value)) return value;
    if(typeof value==='string'){
      try{ var parsed=JSON.parse(value); return Array.isArray(parsed)?parsed:[]; }catch(e){}
    }
    return [];
  }
  function mapFileList(list){
    return parseJsonList(list).map(function(a){
      var name=a.nome_file||a.nome||'allegato';
      var url=a.url||a.data||'';
      return {nome:name,nome_file:name,mime:a.mime||'application/octet-stream',size:a.size||0,url:url,data:url,path:a.path||'',bucket:a.bucket||'allegati_noleggi',caricato_il:a.caricato_il||''};
    });
  }
  function mapProduct(row){
    var foto=row.foto_path||row.foto_url||'';
    if(foto && !/^https?:|^data:/.test(foto) && sb){
      var pub=sb.storage.from('immagini_prodotti').getPublicUrl(foto);
      foto=pub.data.publicUrl;
    }
    return {id:row.id,codice:row.codice,nome:row.nome,categoria:row.categoria||'',quantita:Number(row.quantita||0),posizione:row.posizione||'',prezzo:Number(row.costo_noleggio||row.prezzo||0),note:row.note||'',foto:foto,foto_path:row.foto_path||'',scheda:{materiale:row.scheda_materiale||'',colore:row.scheda_colore||'',dimensione:row.scheda_dimensione||'',note:row.scheda_note||''}};
  }
  function mapEvent(row){
    return {id:String(row.id),tipo:'evento',titolo:row.nome_evento,inizio:row.inizio||((row.data||'')+'T12:00:00'),fine:row.fine||((row.data||'')+'T23:59:00'),location:row.location||'',ospiti:Number(row.ospiti||0),bambini:Number(row.bambini||0),staff:Number(row.staff||0),noteTutti:row.note_tutti||'',noteSala:row.note_sala||'',noteCucina:row.note_cucina||'',noteMagazzino:row.note_magazzino||'',allegatiTutti:mapFileList(row.allegati_tutti),allegatiSala:mapFileList(row.allegati_sala),allegatiCucina:mapFileList(row.allegati_cucina),allegatiMagazzino:mapFileList(row.allegati_magazzino),allegatiPrivata:mapFileList(row.allegati_privati),stato:'confermato'};
  }
  function mapRental(row){
    return {id:String(row.id),tipo:'noleggio',titolo:row.titolo,inizio:row.inizio,fine:row.fine,stato:row.stato||'confermato',location:row.location||'',referente:row.referente||'',telefono:row.telefono||'',note:row.note||'',bolla_path:row.bolla_path||'',ddt_path:row.ddt_path||'',vario_path:row.vario_path||'',allegatiBolla:mapFileList(row.bolla_url||row.bolla),allegatiDDT:mapFileList(row.ddt_url||row.ddt),allegatiVario:mapFileList(row.vario_url||row.vario)};
  }
  async function purgeExpiredAttachments(){
    if(!sb)return;
    var now=Date.now(), last=Number(localStorage.getItem('ergo_cleanup_at')||0);
    if(now-last<24*60*60*1000)return;
    try{
      var evs=await sb.from('eventi_catering').select('id,data,allegati_tutti,allegati_sala,allegati_cucina,allegati_magazzino,allegati_privati');
      for(const e of (evs.data||[])){
        if(!e.data || new Date(e.data).getTime()+7*86400000>now)continue;
        var cols=['allegati_tutti','allegati_sala','allegati_cucina','allegati_magazzino','allegati_privati'], paths=[];
        cols.forEach(function(c){parseJsonList(e[c]).forEach(function(a){if(a.path)paths.push({bucket:a.bucket||'allegati_noleggi',path:a.path});});});
        for(const g of ['allegati_noleggi','immagini_prodotti']){var gp=paths.filter(function(x){return x.bucket===g}).map(function(x){return x.path});if(gp.length)await sb.storage.from(g).remove(gp);}
        var empty={};cols.forEach(function(c){empty[c]=[]});await sb.from('eventi_catering').update(empty).eq('id',e.id);
      }
      var nls=await sb.from('noleggi').select('id,fine,bolla_url,ddt_url,vario_url');
      for(const n of (nls.data||[])){
        if(!n.fine || new Date(n.fine).getTime()+30*86400000>now)continue;
        var files=[['bolla_path',n.bolla_path],['ddt_path',n.ddt_path],['vario_path',n.vario_path]];
        var paths=files.map(function(x){return x[1]||''}).filter(function(x){return x && !/^https?:/.test(x)});
        if(paths.length)await sb.storage.from('allegati_noleggi').remove(paths);
        await sb.from('noleggi').update({bolla_url:null,ddt_url:null,vario_url:null,bolla_path:null,ddt_path:null,vario_path:null,bolla_dati_b64:null,ddt_dati_b64:null,vario_dati_b64:null}).eq('id',n.id);
      }
      originalSetItem.call(localStorage,'ergo_cleanup_at',String(now));
    }catch(e){console.warn('Pulizia allegati rinviata',e)}
  }
  async function loadSupabase(){
    if(!sb) return;
    try{
      syncing=true;
      var products=await sb.from('prodotti_noleggio').select('id,codice,nome,categoria,quantita,posizione,costo_noleggio,note,foto_path,scheda_materiale,scheda_colore,scheda_dimensione,scheda_note').order('nome');
      var rentals=await sb.from('noleggi').select('id,titolo,inizio,fine,stato,location,referente,telefono,note,bolla,ddt,vario,bolla_url,ddt_url,vario_url,bolla_path,ddt_path,vario_path,bolla_mime,ddt_mime,vario_mime').order('inizio');
      var events=await sb.from('eventi_catering').select('id,nome_evento,data,data_display,location,ospiti,bambini,staff,note_tutti,allegati_tutti,note_sala,allegati_sala,note_cucina,allegati_cucina,note_magazzino,allegati_magazzino,allegati_privati').order('data');
      if(products.error) throw products.error;
      if(rentals.error) throw rentals.error;
      if(events.error) throw events.error;
      var pRows=(products.data||[]).map(mapProduct), nRows=(rentals.data||[]).map(mapRental), eRows=(events.data||[]).map(mapEvent);
      originalSetItem.call(localStorage,'ergo_prodotti',JSON.stringify(pRows));
      originalSetItem.call(localStorage,'ergo_noleggi',JSON.stringify(nRows));
      originalSetItem.call(localStorage,'ergo_eventi',JSON.stringify(eRows));
      EVENTI.splice(0,EVENTI.length,...eRows); NOLEGGI.splice(0,NOLEGGI.length,...nRows);
      if(window.user && typeof app==='function') app();
    }catch(e){ console.warn('Dati Streamlit/Supabase non disponibili: uso il fallback locale',e); }
    finally{ syncing=false; }
  }
  window.ergoSupabaseLoad = loadSupabase;
  wait(async function(){await loadSupabase();await purgeExpiredAttachments();},120);

  /* Assistente: una sola istanza, più leggibile e con azioni reali. */
  var assistantSvg = {
    'Amministratore':'<svg viewBox="0 0 120 160" aria-label="Assistente amministratore"><ellipse cx="60" cy="152" rx="30" ry="5" fill="#152238" opacity=".15"/><rect x="35" y="55" width="50" height="65" rx="10" fill="#083278"/><path d="M50 55l10 15 10-15" fill="#fff"/><rect x="56" y="70" width="8" height="35" rx="3" fill="#dc2626"/><circle cx="60" cy="35" r="24" fill="#f4c8a1"/><path d="M36 30Q36 8 60 8t24 22Q78 24 60 24t-24 6" fill="#2c3e50"/><circle cx="52" cy="35" r="2.5"/><circle cx="68" cy="35" r="2.5"/><path d="M52 45q8 7 16 0" fill="none" stroke="#152238" stroke-width="2" stroke-linecap="round"/></svg>'
  };
  /* Gli SVG di ruolo già presenti restano disponibili tramite fallback. */
  window.assistentePersonale = function(config){
    if(!window.user || !user) return;
    var old=document.getElementById('assistente-attivo'); if(old) old.remove();
    var color=config.colore||'#083278';
    var roleName={'Amministratore':'Amministratore','Wedding':'Wedding Planner','Cucina':'Chef','Sala':'Cameriere','Magazzino':'Magazziniere','Magazzino2':'Autista'}[user.ruolo]||user.ruolo;
    var svg=(typeof SVG!=='undefined'&&SVG[user.ruolo]) || assistantSvg.Amministratore;
    var wrap=document.createElement('div'); wrap.id='assistente-attivo'; wrap.className='assistente-vnext';
    var card=document.createElement('div'); card.className='assistente-card'; card.style.borderColor=color;
    var buttons=config.bottoni||[{label:'Va bene',colore:color}];
    card.innerHTML='<button class="assistente-close" aria-label="Chiudi">×</button><div class="assistente-role" style="color:'+color+'">'+roleName+'</div>'+(config.emoji?'<div class="assistente-emoji">'+config.emoji+'</div>':'')+'<div class="assistente-text">'+(config.testo||'Sono qui per aiutarti.')+'</div><div class="assistente-actions">'+buttons.map(function(b,i){return '<button class="assistente-action" data-i="'+i+'" style="background:'+(b.colore||color)+'">'+b.label+'</button>';}).join('')+'</div>';
    var person=document.createElement('div'); person.className='assistente-person'; person.innerHTML=svg;
    wrap.appendChild(person); wrap.appendChild(card); document.body.appendChild(wrap);
    requestAnimationFrame(function(){wrap.classList.add('visibile');});
    function close(cb){wrap.classList.remove('visibile');wait(function(){if(wrap.parentNode)wrap.remove();if(cb)cb();},350);}
    card.querySelector('.assistente-close').onclick=function(){close();};
    card.querySelectorAll('.assistente-action').forEach(function(btn){btn.onclick=function(){var b=buttons[Number(btn.dataset.i)];close(function(){if(b.azione)b.azione();});};});
    if(config.autoClose!==false) wait(function(){if(wrap.parentNode)close();},config.durata||12000);
  };

  /* Tutti i messaggi passano dal personaggio: nessun alert nativo o toast successivo. */
  window.alert = function(message){
    var text=String(message||'').replace(/\n/g,'<br>');
    var error=/errore|obbligatorio|non trovato|non disponibile|non corrette|massimo|nessun/i.test(text);
    window.assistentePersonale({
      testo:text,
      emoji:error?'⚠️':'✅',
      colore:error?'#b91c1c':'#3e765e',
      autoClose:false,
      bottoni:[{label:'Ho capito',colore:error?'#b91c1c':'#3e765e'}]
    });
  };

  /* Sovrascrive il download per gestire sia Base64 sia URL Storage. */
  window.scaricaAllega = function(allegato){
    if(!allegato || !(allegato.data||allegato.url)) return;
    var a=document.createElement('a'); a.href=allegato.url||allegato.data; a.download=allegato.nome||'allegato'; a.target='_blank'; a.rel='noopener'; document.body.appendChild(a); a.click(); a.remove();
    window.assistentePersonale({testo:'<b>Download avviato</b><br>'+String(allegato.nome||'Allegato').replace(/</g,'&lt;'),emoji:'📥',colore:'#0891b2'});
  };

  /* PDF unico: l’app continua a usare la funzione esistente, ma comunica l’esito. */
  var oldPdf=window.scaricaUnicoPdf;
  if(oldPdf){
    window.scaricaUnicoPdf=async function(lista,sezione){
      var result=await oldPdf.apply(this,arguments);
      window.assistentePersonale({testo:'<b>PDF unito pronto</b><br>'+String(sezione||'Allegati').replace(/</g,'&lt;'),emoji:'📚',colore:'#083278'});
      return result;
    };
  }

  var style=document.createElement('style');
  style.textContent=`
  .assistente-vnext{position:fixed;right:18px;bottom:18px;z-index:1000000;display:flex;align-items:flex-end;gap:0;opacity:0;transform:translateX(40px);transition:opacity .3s ease,transform .35s ease;pointer-events:none;max-width:min(560px,calc(100vw - 20px))}
  .assistente-vnext.visibile{opacity:1;transform:translateX(0);pointer-events:auto}
  .assistente-person{width:138px;min-width:138px;filter:drop-shadow(0 10px 18px rgba(8,50,120,.22));transform:translateY(5px)}
  .assistente-person svg{display:block;width:138px;height:184px}
  .assistente-card{position:relative;background:#fff;border:2px solid #083278;border-radius:18px;padding:16px 18px 15px;min-width:270px;max-width:360px;box-shadow:0 14px 34px rgba(21,34,56,.2)}
  .assistente-card:before{content:"";position:absolute;left:-13px;top:35px;border-style:solid;border-width:10px 13px 10px 0;border-color:transparent currentColor transparent transparent;color:inherit}
  .assistente-close{position:absolute;right:7px;top:5px;border:0;background:transparent;color:#94a3b8;font-size:20px;cursor:pointer}
  .assistente-role{text-transform:uppercase;letter-spacing:.12em;font-size:.65rem;font-weight:800;margin-bottom:5px}
  .assistente-emoji{font-size:1.55rem;margin-bottom:5px}.assistente-text{font-size:.9rem;line-height:1.45;color:#152238;font-weight:600;margin-bottom:12px}.assistente-actions{display:flex;flex-direction:column;gap:7px}.assistente-action{border:0;color:#fff;border-radius:10px;padding:10px 12px;font-weight:800;font-size:.78rem;cursor:pointer}
  @media(max-width:560px){.assistente-vnext{right:8px;bottom:8px;max-width:calc(100vw - 16px)}.assistente-person{width:125px;min-width:125px}.assistente-person svg{width:125px;height:167px}.assistente-card{min-width:0;max-width:calc(100vw - 118px);padding:14px}.assistente-text{font-size:.84rem}}
  /* Correzione visibilità: il personaggio deve essere riconoscibile a colpo d'occhio. */
  .assistente-vnext{right:22px;bottom:22px;max-width:min(700px,calc(100vw - 24px))}
  .assistente-person{width:210px;min-width:210px;transform:translateY(8px);filter:drop-shadow(0 14px 26px rgba(8,50,120,.28))}
  .assistente-person svg{width:210px;height:280px}
  .assistente-card{min-width:330px;max-width:410px;padding:20px 22px 19px;border-width:3px;border-radius:22px}
  .assistente-role{font-size:.75rem}.assistente-text{font-size:1.02rem;line-height:1.5}.assistente-emoji{font-size:2rem}.assistente-action{padding:12px 14px;font-size:.86rem}
  /* Effetto dashboard più lento e leggibile. */
  .dash-anim .sidebar{animation-duration:1.35s !important}
  .dash-anim .topbar{animation-duration:1.05s !important}
  .dash-anim .cd-card:nth-child(1),.dash-anim .cd-card:nth-child(2){animation-duration:1.25s !important}
  .dash-anim .cd-card:nth-child(1){animation-delay:.85s !important}.dash-anim .cd-card:nth-child(2){animation-delay:1.2s !important}
  .dash-anim .feed{animation-duration:1.1s !important;animation-delay:1.65s !important}
  .dash-anim .feed-item{animation-duration:.85s !important}
  .dash-anim .feed-item:nth-child(1){animation-delay:2.35s !important}.dash-anim .feed-item:nth-child(2){animation-delay:2.55s !important}.dash-anim .feed-item:nth-child(3){animation-delay:2.75s !important}.dash-anim .feed-item:nth-child(4){animation-delay:2.95s !important}.dash-anim .feed-item:nth-child(5){animation-delay:3.15s !important}.dash-anim .feed-item:nth-child(6){animation-delay:3.35s !important}.dash-anim .feed-item:nth-child(7){animation-delay:3.55s !important}
  .dash-anim h1.title{animation-duration:1.8s !important;animation-delay:1.45s !important}
  .dash-anim .eyebrow{animation-duration:.9s !important;animation-delay:1.1s !important}.dash-anim .lede{animation-duration:.9s !important;animation-delay:1.7s !important}
  @media(max-width:560px){.assistente-vnext{right:8px;bottom:8px}.assistente-person{width:125px;min-width:125px}.assistente-person svg{width:125px;height:167px}.assistente-card{min-width:0;max-width:calc(100vw - 118px);padding:14px}.assistente-text{font-size:.84rem}}
  `;
  document.head.appendChild(style);

  /* Mantiene l'animazione dashboard abbastanza a lungo da essere percepita. */
  var previousDash = window.dash;
  if(previousDash){
    window.dash=function(el){
      var result=previousDash.apply(this,arguments);
      if(!window._dashVnextShown && typeof view!=='undefined' && view==='dashboard'){
        window._dashVnextShown=true;
        wait(function(){
          var pc=document.getElementById('pc');
          if(pc)pc.classList.add('dash-anim');
          wait(function(){
            if(pc)pc.classList.remove('dash-anim');
            window._dashVnextShown=false;
          },7200);
        },120);
      }
      return result;
    };
  }
  var previousLogin=window.login;
  if(previousLogin){
    window.login=function(){window._dashVnextShown=false;return previousLogin.apply(this,arguments);};
  }

  console.info('Ergo vNext: assistente attivo; Supabase '+(sb?'configurato':'non configurato, fallback localStorage'));
})();

</script>
</body>
</html>
