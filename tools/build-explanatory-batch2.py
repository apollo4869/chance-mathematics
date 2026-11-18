"""Build six author-review overlays, preserving original and batch-1 before views."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[1];O=ROOT/'reports/volume5-illustrations-batch2-2026-10-31';P=O/'preview';B1=ROOT/'reports/volume5-illustrations-batch1-2026-10-31'
BASE='/assets/visuals/explanatory-v2/';OLD='/assets/visuals/explanatory-v1/'
rows=json.loads((ROOT/'publication/explanatory-figures-batch2-working.json').read_text(encoding='utf-8'))['figures'];prior=json.loads((ROOT/'publication/explanatory-figures-working.json').read_text(encoding='utf-8'))['figures']
STYLE='<link rel="stylesheet" href="'+BASE+'figures.css">';JS='<script defer src="'+BASE+'interactions.js"></script>'
def rewrite(s,lang,slug):
 s=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',s);base='/book/'+('en/' if lang=='en' else '')+'chapters/'+slug+'.html'
 def link(m):
  v=m.group(2)
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
  return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 return re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',link,s).replace('</head>',STYLE+'</head>',1).replace('</body>',JS+'</body>',1)
shell='body{margin:0;background:#f8f6ef;color:#173f39;font:18px/1.75 "Microsoft YaHei",sans-serif}main{max-width:990px;margin:auto;padding:20px 24px}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}a{color:#146d61}@media(max-width:700px){main{padding:12px}}'
manifest=[]
for row in rows:
 if not row['book_preview']:continue
 code=row['id'];lang=row['lang'];slug=row['slug'];fig=row['html'];section=row['section'];other='en' if lang=='zh' else 'zh';entry={k:row[k] for k in ['id','lang','slug','section','title','status','category']}
 source=ROOT/'dist'/('en' if lang=='en' else '')/'chapters'/(slug+'.html')
 if code in ['V34','V37']:
  before=(B1/'preview/chapters'/lang/(slug+'.html')).read_text(encoding='utf-8');old=next(x['html'] for x in prior if x['id']==code and x['lang']==lang);assert before.count(old)==1
  after=before.replace(old,fig,1).replace(OLD+'figures.css',BASE+'figures.css').replace(OLD+'interactions.js',BASE+'interactions.js')
  assert after.replace(fig,'',1).replace(BASE,OLD)==before.replace(old,'',1)
  before_anchor='visual-'+code;kind='batch1-artwork'
 else:
  before=rewrite(source.read_text(encoding='utf-8'),lang,slug);h=re.search(r'<h[23] id="([^"]+)">'+re.escape(section)+r'\s[^<]+</h[23]>',before);assert h
  start=before.rfind('<div class="reading-unit"',0,h.start());end=before.find('<div class="reading-unit"',h.end());assert end>start;pos=before.rfind('</div>',start,end);after=before[:pos]+fig+before[pos:];assert after.replace(fig,'',1)==before
  before_anchor=h.group(1);kind='text-without-illustration'
 d=P/'chapters'/lang;d.mkdir(exist_ok=True,parents=True);(d/(slug+'.html')).write_text(after,encoding='utf-8');(d/(slug+'-before.html')).write_text(before,encoding='utf-8')
 entry.update(figure=f'/figures/{code}.{lang}.html',print=f'/print/{code}.{lang}.html',chapter=f'/chapters/{lang}/{slug}.html#visual-{code}',before=f'/chapters/{lang}/{slug}-before.html#{before_anchor}',before_kind=kind,source_sha=hashlib.sha256(source.read_bytes()).hexdigest())
 nav=f'<nav><a href="/">'+('本批总览' if lang=='zh' else 'Batch review')+f'</a><a href="/figures/{code}.{other}.html">'+('English' if lang=='zh' else '中文')+f'</a><a href="{entry["chapter"]}">'+('放入正文' if lang=='zh' else 'In the chapter')+f'</a><a href="{entry["print"]}">'+('静态打印' if lang=='zh' else 'Static print')+'</a></nav>'
 (P/'figures'/f'{code}.{lang}.html').write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(row["title"])}</title><style>{shell}</style>{STYLE}<main>{nav}{fig}</main>{JS}</html>',encoding='utf-8')
 printcss='@page{size:A4 portrait;margin:12mm}body{font:15px/1.7 "Microsoft YaHei",sans-serif;margin:0}main{max-width:900px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:16px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
 (P/'print'/f'{code}.{lang}.html').write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{printcss}</style><main>{nav}<img src="{BASE}{code}.{lang}.svg" alt="{E(row["title"])}"></main></html>',encoding='utf-8');manifest.append(entry)
(O/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print('Six bilingual overlays ready: four additions, two targeted refinements; no chapter 39 or 41+ edits.')
