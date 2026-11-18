"""Build only the first volume-V author-review overlay. Never rewrites dist."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[1];O=ROOT/'reports/volume5-illustrations-batch1-2026-10-31';P=O/'preview'
BASE='/assets/visuals/explanatory-v1/'
STYLE='<link rel="stylesheet" href="'+BASE+'figures.css">';JS='<script defer src="'+BASE+'interactions.js"></script>'
rows=json.loads((ROOT/'publication/explanatory-figures-working.json').read_text(encoding='utf-8'))['figures']
shell='body{margin:0;background:#f8f6ef;color:#173f39;font:18px/1.75 "Microsoft YaHei",sans-serif}main{max-width:990px;margin:auto;padding:20px 24px}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}a{color:#146d61}@media(max-width:700px){main{padding:12px}}'
def rewrite(s,lang,slug):
 s=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',s)
 base='/book/'+('en/' if lang=='en' else '')+'chapters/'+slug+'.html'
 def link(m):
  v=m.group(2)
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
  return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 return re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',link,s).replace('</head>',STYLE+'</head>',1).replace('</body>',JS+'</body>',1)
manifest=[]
for row in rows:
 code=row['id'];lang=row['lang'];slug=row['slug'];fig=row['html'];section=row['section'];other='en' if lang=='zh' else 'zh'
 entry={k:row[k] for k in ['id','lang','slug','section','title','status','category','book_preview']}
 entry.update(figure=f'/figures/{code}.{lang}.html',print=f'/print/{code}.{lang}.html',chapter=None,before=None)
 nav=f'<nav><a href="/">'+('本批总览' if lang=='zh' else 'Batch review')+f'</a><a href="/figures/{code}.{other}.html">'+('English' if lang=='zh' else '中文')+'</a>'
 if row['book_preview']:
  source=ROOT/'dist'/('en' if lang=='en' else '')/'chapters'/(slug+'.html');s=rewrite(source.read_text(encoding='utf-8'),lang,slug)
  h=re.search(r'<h[23] id="([^"]+)">'+re.escape(section)+r'\s[^<]+</h[23]>',s);assert h,(code,section)
  start=s.rfind('<div class="reading-unit"',0,h.start());end=s.find('<div class="reading-unit"',h.end());assert end>start
  pos=s.rfind('</div>',start,end);after=s[:pos]+fig+s[pos:];assert after.replace(fig,'',1)==s
  out=P/'chapters'/lang;out.mkdir(parents=True,exist_ok=True)
  (out/(slug+'.html')).write_text(after,encoding='utf-8');(out/(slug+'-before.html')).write_text(s,encoding='utf-8')
  entry.update(chapter=f'/chapters/{lang}/{slug}.html#visual-{code}',before=f'/chapters/{lang}/{slug}-before.html#{h.group(1)}',source_sha=hashlib.sha256(source.read_bytes()).hexdigest())
  nav+=f'<a href="{entry["chapter"]}">'+('放入正文' if lang=='zh' else 'In the chapter')+'</a>'
 nav+=f'<a href="{entry["print"]}">'+('静态打印' if lang=='zh' else 'Static print')+'</a></nav>'
 for name in ['figures','print']:(P/name).mkdir(parents=True,exist_ok=True)
 (P/'figures'/f'{code}.{lang}.html').write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(row["title"])}</title><style>{shell}</style>{STYLE}<main>{nav}{fig}</main>{JS}</html>',encoding='utf-8')
 printcss='@page{size:A4 portrait;margin:12mm}body{font:15px/1.7 "Microsoft YaHei",sans-serif;margin:0}main{max-width:900px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:16px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
 (P/'print'/f'{code}.{lang}.html').write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{printcss}</style><main>{nav}<img src="{BASE}{code}.{lang}.svg" alt="{E(row["title"])}"></main></html>',encoding='utf-8')
 manifest.append(entry)
(O/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('Only chapters 31,32,33,34,37 get local overlays; other pilots remain isolated figures.')
