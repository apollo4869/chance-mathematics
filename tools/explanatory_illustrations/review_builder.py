"""Reusable local-only figure overlays. No writes to canonical chapters or dist."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
import re,json,hashlib,shutil
R=Path(__file__).resolve().parents[2]
SHELL='body{background:#f8f6ef;color:#173f39;font:18px/1.8 "Microsoft YaHei",sans-serif;margin:0}main{max-width:1080px;margin:auto;padding:26px}a{color:#146d61}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}h1{font-size:29px;line-height:1.5}.note{padding:18px;background:#eaf2ee}.twins{display:grid;grid-template-columns:1fr 1fr;gap:20px}.shots img{width:100%;height:auto;border:1px solid #ccd9d1}figure{margin:0}figcaption{font-size:15px}section.review{border-top:1px solid #ccd9d1;padding-top:20px;margin:30px 0}@media(max-width:700px){main{padding:12px}.twins{grid-template-columns:1fr}h1{font-size:25px}}'
def build(report,namespace,registry,title,notes):
 O=R/'reports'/report;P=O/'preview';A=R/'assets/visuals'/namespace;prefix=f'/assets/visuals/{namespace}/local-preview/'
 for d in ['figures','chapters/zh','chapters/en','print','compare']:(P/d).mkdir(parents=True,exist_ok=True)
 def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
 includes=f'<link rel="stylesheet" href="/assets/visuals/{namespace}/figures.css"><script defer src="/assets/visuals/{namespace}/interactions.js"></script>'
 def page(label,body,lg='zh'):return f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(label)}</title><style>{SHELL}</style>{includes}<main>{body}</main></html>'
 rows=json.loads((R/'publication'/registry).read_text(encoding='utf-8'))['figures'];manifest=[];contexts=[]
 for row in rows:
  code,lg,slug=row['id'],row['lang'],row['slug'];src=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');s=src.read_text(encoding='utf-8')
  s=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',s)
  base='/book/'+('en/' if lg=='en' else '')+'chapters/'+slug+'.html'
  def rootlink(m):
   v=m.group(2)
   if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
   return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
  before=re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',rootlink,s).replace('</head>',includes+'</head>',1)
  h=re.search(r'<h[23] id="([^"]+)">'+re.escape(row['section'])+r'\s[^<]+</h[23]>',before);assert h,(code,lg)
  start=before.rfind('<div class="reading-unit"',0,h.start());end=before.find('<div class="reading-unit"',h.end());assert start>=0 and end>start
  at=before.rfind('</div>',start,end);after=before[:at]+row['html']+before[at:];assert after.replace(row['html'],'',1)==before
  for suffix,body in [('-before',before),('',after)]:write(P/'chapters'/lg/(slug+suffix+'.html'),body)
  rec={k:row[k] for k in ['id','lang','title','slug','section','status','kind','coverage_sections']};rec.update(before=f'/chapters/{lg}/{slug}-before.html#{h.group(1)}',chapter_url=f'/chapters/{lg}/{slug}.html#visual-{code}',figure=f'/figures/{code}.{lg}.html',print=f'/print/{code}.{lg}.html',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest());manifest.append(rec)
  nav=f'<nav><a href="/">本轮总览</a><a href="{rec["chapter_url"]}">实际章节 / In chapter</a><a href="{rec["print"]}">静态打印</a><a href="/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
  write(P/'figures'/f'{code}.{lg}.html',page(row['title'],nav+row['html'],lg))
  pc='@page{size:A4 portrait;margin:12mm}body{margin:0;font:16px/1.8 sans-serif;background:white}main{max-width:900px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:15px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
  write(P/'print'/f'{code}.{lg}.html',f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(row["title"])} · static</title><style>{pc}</style><main>{nav}<img src="{row["asset_base"]}{code}.{lg}.svg" alt="{E(row["title"])}"><span id="static-end"></span></main></html>')
  md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');parts=re.split(r'(?m)(?=^## )',md.read_text(encoding='utf-8'))
  for sec in row['coverage_sections']:
   chosen=[p for p in parts if p.startswith('## '+sec+' ')];assert len(chosen)==1
   contexts.append(dict(id=code,lang=lg,section=sec,path=md.relative_to(R).as_posix(),sha256=hashlib.sha256(md.read_bytes()).hexdigest(),section_text=chosen[0]))
 write(O/'manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2));write(O/'reading-contexts.json',json.dumps(contexts,ensure_ascii=False,indent=2))
 intro=f'<h1>{E(title)}</h1><p class="note">本轮只有E27与E29两组新候选。全部已采用插图、数学正文、证明与正式dist保持保护；不进入第六卷，不发布、不推送。</p><nav><a href="/review.html">模型、阅读边界与审校记录</a></nav>'
 for code,note in notes.items():
  z=next(r for r in manifest if r['id']==code and r['lang']=='zh');intro+=f'<section class="review"><h2>{code} · {E(z["title"])}</h2><p>{E(note)}</p><nav><a href="/compare/{code}.html">实际章节前后与截图</a><a href="/figures/{code}.zh.html">中文交互</a><a href="/figures/{code}.en.html">English</a><a href="/print/{code}.zh.html">静态打印</a></nav></section>'
 write(P/'index.html',page(title,intro))
 for code in notes:
  body=f'<nav><a href="/">本轮总览</a></nav><h1>{code} · 从原正文到解释图</h1><p>原页面的正文、证明、链接与现有辅助图完整保留，只在对应阅读单元加入一组候选。以下为实际浏览器截图，不是合成网页。</p>'
  for r in [r for r in manifest if r['id']==code]:
   lg=r['lang'];body+=f'<h2>{lg}</h2><nav><a href="{r["before"]}">原正文</a><a href="{r["chapter_url"]}">正文嵌入</a><a href="{r["figure"]}">独立交互</a><a href="{r["print"]}">静态打印</a></nav>'
   for size in ['desktop','mobile']:
    body+='<h3>'+size+' · 实际章节前后</h3><div class="twins">'
    for side in ['before','after']:
     url=f'/shots/{code}-{lg}-chapter-{side}-{size}.jpg';body+=f'<figure class="shots"><a href="{url}"><img loading="lazy" src="{url}" alt="{side}"></a><figcaption>{side}</figcaption></figure>'
    body+='</div>'
   body+='<h3>独立图、交互变化与静态候选</h3><div class="twins">'
   for tag in ['desktop','mobile','desktop-end','mobile-end','interaction-desktop','interaction-mobile','print','print-end']:
    url=f'/shots/{code}-{lg}-{tag}.jpg';body+=f'<figure class="shots"><a href="{url}"><img loading="lazy" src="{url}" alt="{code} {lg} {tag}"></a><figcaption>{tag}</figcaption></figure>'
   body+='</div>'
  write(P/'compare'/f'{code}.html',page(code+' comparison',body))
 write(P/'review.html',page('模型与审校边界','<nav><a href="/">总览</a></nav><h1>本轮的真实数学增量</h1>'+''.join(f'<h2>{c}</h2><p>{E(t)}</p>' for c,t in notes.items())+'<p>完整计算、条件和证明边界见报告MATHEMATICAL_REVIEW.md。数学有限模型核验、浏览器检查、作者视觉审核和专家终审分别记录。手机是浏览器视口，不是真机；静态打印页检查不等于原生分页、PDF字体嵌入或实体纸张。</p>'))
 mirror=A/'local-preview'
 for src in P.rglob('*.html'):
  dest=mirror/src.relative_to(P);dest.parent.mkdir(parents=True,exist_ok=True)
  def mir(m):
   v=m.group(2)
   if v.startswith('/shots/'):v=prefix+'screenshots/'+v[len('/shots/'):]
   elif v.startswith('/') and not v.startswith(('/assets/','/book/')):v=prefix+(v.lstrip('/') or 'index.html')
   else:return m.group(0)
   return m.group(1)+'="'+v+'"'
  write(dest,re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',mir,src.read_text(encoding='utf-8')))
 if (O/'screenshots').exists():
  (mirror/'screenshots').mkdir(exist_ok=True)
  for f in (O/'screenshots').glob('*.jpg'):shutil.copyfile(f,mirror/'screenshots'/f.name)
 write(O/'local-preview-route.json',json.dumps(dict(url='http://127.0.0.1:8861'+prefix+'index.html',scope='Local-only mirror through the existing read-only HTTP service, no formal site injection'),indent=2))
 print(f'{len(manifest)} bilingual overlays; {len(contexts)} actual source sections; independent local mirror')
