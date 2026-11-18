"""Build local E22/E28 revision overlays and genuine screenshot comparison entries."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
import re,json,hashlib,shutil
R=Path(__file__).resolve().parents[1];O=R/'reports/early-explanations-batch3-revision-2026-11-04';P=O/'preview';A=R/'assets/visuals/explanatory-early-v3r2'
PREFIX='/assets/visuals/explanatory-early-v3r2/local-preview/';OLD=R/'reports/early-explanations-batch3-2026-11-04'
for d in ['figures','chapters/zh','chapters/en','print','compare']:(P/d).mkdir(parents=True,exist_ok=True)
(O/'previous-screenshots').mkdir(exist_ok=True)
for code in ['E22','E28']:
 for lg in ['zh','en']:
  for size in ['desktop','mobile']:
   name=f'{code}-{lg}-{size}.jpg';shutil.copyfile(OLD/'screenshots'/name,O/'previous-screenshots'/name)
SHELL='body{background:#f8f6ef;color:#173f39;font:18px/1.8 "Microsoft YaHei",sans-serif;margin:0}main{max-width:1080px;margin:auto;padding:26px}a{color:#146d61}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}h1{font-size:29px;line-height:1.5}.note{padding:18px;background:#eaf2ee}.twins{display:grid;grid-template-columns:1fr 1fr;gap:20px}.shots img{width:100%;height:auto;border:1px solid #ccd9d1}figure{margin:0}figcaption{font-size:15px}section.review{border-top:1px solid #ccd9d1;padding-top:20px;margin:30px 0}@media(max-width:700px){main{padding:12px}.twins{grid-template-columns:1fr}h1{font-size:25px}}'
includes='<link rel="stylesheet" href="/assets/visuals/explanatory-early-v3r2/figures.css"><script defer src="/assets/visuals/explanatory-early-v3r2/interactions.js"></script>'
def write(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def page(title,body,lg='zh'):return f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(title)}</title><style>{SHELL}</style>{includes}<main>{body}</main></html>'
rows=json.loads((R/'publication/explanatory-batch3-revision-working.json').read_text(encoding='utf-8'))['figures'];manifest=[];contexts=[]
for row in rows:
 code,lg,slug=row['id'],row['lang'],row['slug'];src=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');text=src.read_text(encoding='utf-8')
 text=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',text)
 base='/book/'+('en/' if lg=='en' else '')+'chapters/'+slug+'.html'
 def rootlink(m):
  v=m.group(2)
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
  return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 before=re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',rootlink,text).replace('</head>',includes+'</head>',1)
 h=re.search(r'<h[23] id="([^"]+)">'+re.escape(row['section'])+r'\s[^<]+</h[23]>',before);assert h,(code,lg)
 start=before.rfind('<div class="reading-unit"',0,h.start());end=before.find('<div class="reading-unit"',h.end());assert start>=0 and end>start
 at=before.rfind('</div>',start,end);after=before[:at]+row['html']+before[at:];assert after.replace(row['html'],'',1)==before
 for suffix,body in [('-before',before),('',after)]:write(P/'chapters'/lg/(slug+suffix+'.html'),body)
 rec={k:row[k] for k in ['id','lang','title','slug','section','status','kind']};rec.update(before=f'/chapters/{lg}/{slug}-before.html#{h.group(1)}',chapter_url=f'/chapters/{lg}/{slug}.html#visual-{code}',figure=f'/figures/{code}.{lg}.html',print=f'/print/{code}.{lg}.html',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest());manifest.append(rec)
 nav=f'<nav><a href="/">本轮总览</a><a href="{rec["chapter_url"]}">实际章节 / In chapter</a><a href="{rec["print"]}">静态打印</a><a href="/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
 write(P/'figures'/f'{code}.{lg}.html',page(row['title'],nav+row['html'],lg))
 printcss='@page{size:A4 portrait;margin:12mm}body{margin:0;font:16px/1.8 sans-serif;background:white}main{max-width:940px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:15px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
 write(P/'print'/f'{code}.{lg}.html',f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(row["title"])} · static</title><style>{printcss}</style><main>{nav}<img src="{row["asset_base"]}{code}.{lg}.svg" alt="{E(row["title"])}"><span id="static-end"></span></main></html>')
 md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');chosen=[p for p in re.split(r'(?m)(?=^## )',md.read_text(encoding='utf-8')) if p.startswith('## '+row['section']+' ')];assert len(chosen)==1
 contexts.append(dict(id=code,lang=lg,path=md.relative_to(R).as_posix(),sha256=hashlib.sha256(md.read_bytes()).hexdigest(),section_text=chosen[0]))
write(O/'manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2));write(O/'reading-contexts.json',json.dumps(contexts,ensure_ascii=False,indent=2))
intro='<h1>第三批解释图 · E22 / E28 修订</h1><p class="note">只修改这两组的独立候选。E14/E30定点修订、E39及此前成熟图均已采用并保持字节保护；没有新增其他图，没有修改数学母稿。E22批注修订与E28新主视觉供作者审核。</p><nav><a href="/priorities.html">尚未完成的高价值缺口与不必配图处</a></nav>'
for code in ['E22','E28']:
 z=next(r for r in manifest if r['id']==code and r['lang']=='zh');desc='节点与等待段完整保留；将平均等待、非共用刻度与两种寿命结论移到主要阅读区。' if code=='E22' else '同一份二维矩阵居中，概率前推与收益回拉分居两侧；手机先看等式及紧凑比较，技术说明可展开。'
 intro+=f'<section class="review"><h2>{code} · {E(z["title"])}</h2><p>{desc}</p><nav><a href="/compare/{code}.html">原版／新版、正文与截图</a><a href="/figures/{code}.zh.html">中文交互</a><a href="/figures/{code}.en.html">English</a><a href="/print/{code}.zh.html">静态打印</a></nav></section>'
write(P/'index.html',page('E22 / E28 本地修订审核',intro))
for code in ['E22','E28']:
 body=f'<nav><a href="/">本轮总览</a></nav><h1>{code} · 保留原版的实际前后对照</h1><p>原版来自e5ab29b2。以下截图均为实际浏览器页面；源码、参数和审校状态在本轮报告中分别记录。</p>'
 for lg in ['zh','en']:
  r=next(r for r in manifest if r['id']==code and r['lang']==lg);body+=f'<h2>{lg}</h2><nav><a href="{r["figure"]}">交互</a><a href="{r["chapter_url"]}">章节嵌入</a><a href="{r["before"]}">原正文</a><a href="{r["print"]}">静态打印</a><a href="/assets/visuals/explanatory-early-v3/{code}.{lg}.svg">上一版静态SVG</a></nav>'
  for size in ['desktop','mobile']:
   body+='<h3>'+size+' · 原版与修订版</h3><div class="twins">'
   for src,label in [(f'/previous-shots/{code}-{lg}-{size}.jpg','e5ab29b2原版'),(f'/shots/{code}-{lg}-{size}.jpg','本轮修订')]:body+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}" alt="{label}"></a><figcaption>{label}</figcaption></figure>'
   body+='</div><h3>'+size+' · 实际章节前后</h3><div class="twins">'
   for side in ['before','after']:
    src=f'/shots/{code}-{lg}-chapter-{side}-{size}.jpg';body+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}" alt="{side}"></a><figcaption>{side}</figcaption></figure>'
   body+='</div>'
  body+='<h3>交互与静态候选</h3><div class="twins">'
  for tag in ['mobile-end','interaction-desktop','interaction-mobile','print','print-end']:
   src=f'/shots/{code}-{lg}-{tag}.jpg';body+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}" alt="{tag}"></a><figcaption>{tag}</figcaption></figure>'
  body+='</div>'
 write(P/'compare'/f'{code}.html',page(code+' revision comparison',body))
priority=O/'REMAINING-PRIORITIES.md'
write(P/'priorities.html',page('尚未完成的视觉缺口','<nav><a href="/">总览</a></nav><h1>已有40章审计的剩余任务</h1><pre style="white-space:pre-wrap;font:17px/1.9 sans-serif">'+E(priority.read_text(encoding='utf-8') if priority.exists() else '优先级清单整理中；不生产下一批图。')+'</pre>'))
mirror=A/'local-preview'
for src in P.rglob('*.html'):
 dst=mirror/src.relative_to(P);dst.parent.mkdir(parents=True,exist_ok=True)
 def mirror_link(m):
  value=m.group(2)
  if value.startswith('/previous-shots/'):new=PREFIX+'previous-screenshots/'+value[len('/previous-shots/'):]
  elif value.startswith('/shots/'):new=PREFIX+'screenshots/'+value[len('/shots/'):]
  elif value.startswith('/') and not value.startswith(('/assets/','/book/')):new=PREFIX+(value.lstrip('/') or 'index.html')
  else:return m.group(0)
  return m.group(1)+'="'+new+'"'
 write(dst,re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',mirror_link,src.read_text(encoding='utf-8')))
for folder in ['screenshots','previous-screenshots']:
 if not (O/folder).exists():continue
 (mirror/folder).mkdir(exist_ok=True)
 for f in (O/folder).glob('*.jpg'):shutil.copyfile(f,mirror/folder/f.name)
write(O/'local-preview-route.json',json.dumps(dict(url='http://127.0.0.1:8861'+PREFIX+'index.html',scope='Independent localhost-only mirror through existing read-only service; no formal site changes'),indent=2))
print('4 bilingual revision overlays and preserved-original comparison gallery created')
