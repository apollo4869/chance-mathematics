"""Local reading overlays only. Never write dist or mathematical manuscripts."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape
from html.parser import HTMLParser
import re,json,hashlib
import shutil
R=Path(__file__).resolve().parents[1];O=R/'reports/early-explanations-batch3-2026-11-04';P=O/'preview'
for d in ['figures','chapters/zh','chapters/en','print','compare']:(P/d).mkdir(parents=True,exist_ok=True)
rows=json.loads((R/'publication/explanatory-early-batch3-working.json').read_text(encoding='utf-8'))['figures']
CSS='body{background:#f8f6ef;color:#173f39;font:18px/1.8 "Microsoft YaHei",sans-serif;margin:0}main{max-width:1080px;margin:auto;padding:26px}a{color:#146d61}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}h1{font-size:30px;line-height:1.5}.note{padding:18px;background:#eaf2ee}.twins{display:grid;grid-template-columns:1fr 1fr;gap:20px}img{max-width:100%}.shots img{width:100%;height:auto;border:1px solid #ccd9d1}figure{margin:0}figcaption{font-size:15px}section.review{margin:32px 0;border-top:1px solid #ccd9d1;padding-top:18px}@media(max-width:700px){main{padding:12px}.twins{grid-template-columns:1fr}h1{font-size:25px}}'
includes=''.join(f'<link rel="stylesheet" href="/assets/visuals/{ns}/figures.css"><script defer src="/assets/visuals/{ns}/interactions.js"></script>' for ns in ['explanatory-early-v2','explanatory-early-v3'])
def write(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def page(title,body,lg='zh'):return f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{escape(title)}</title><style>{CSS}</style>{includes}<main>{body}</main></html>'
manifest=[];contexts=[]
for row in rows:
 code,lg,slug=row['id'],row['lang'],row['slug'];src=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');before=src.read_text(encoding='utf-8')
 before=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',before)
 base='/book/'+('en/' if lg=='en' else '')+'chapters/'+slug+'.html'
 def rewrite(m):
  v=m.group(2)
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
  return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 before=re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',rewrite,before).replace('</head>',includes+'</head>',1)
 h=re.search(r'<h[23] id="([^"]+)">'+re.escape(row['section'])+r'\s[^<]+</h[23]>',before);assert h,(code,lg)
 start=before.rfind('<div class="reading-unit"',0,h.start());end=before.find('<div class="reading-unit"',h.end());assert start>=0 and end>start
 at=before.rfind('</div>',start,end);after=before[:at]+row['html']+before[at:];assert after.replace(row['html'],'',1)==before
 for suffix,txt in [('-before',before),('',after)]:write(P/'chapters'/lg/(slug+suffix+'.html'),txt)
 rec={k:row[k] for k in ['id','lang','title','slug','section','status','kind']};rec.update(before=f'/chapters/{lg}/{slug}-before.html#{h.group(1)}',chapter_url=f'/chapters/{lg}/{slug}.html#visual-{code}',figure=f'/figures/{code}.{lg}.html',print=f'/print/{code}.{lg}.html',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest());manifest.append(rec)
 nav=f'<nav><a href="/">本轮总览</a><a href="{rec["chapter_url"]}">实际正文 / In chapter</a><a href="{rec["print"]}">静态打印</a><a href="/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
 write(P/'figures'/f'{code}.{lg}.html',page(row['title'],nav+row['html'],lg))
 pc='@page{size:A4 portrait;margin:12mm}body{margin:0;background:white;font:16px/1.8 sans-serif}main{max-width:900px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:16px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
 write(P/'print'/f'{code}.{lg}.html',f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{pc}</style><title>{escape(row["title"])} · static</title><main>{nav}<img src="{row["asset_base"]}{code}.{lg}.svg" alt="{escape(row["title"])}"><span id="static-end"></span></main></html>')
 md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');sections=re.split(r'(?m)(?=^## )',md.read_text(encoding='utf-8'));chosen=[t for t in sections if t.startswith('## '+row['section']+' ')];assert len(chosen)==1
 contexts.append(dict(id=code,lang=lg,path=md.relative_to(R).as_posix(),sha256=hashlib.sha256(md.read_bytes()).hexdigest(),section_text=chosen[0]))
write(O/'manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2));write(O/'reading-contexts.json',json.dumps(contexts,ensure_ascii=False,indent=2))

CRIT={'E22':'同一跳链对比两种平均等待时钟。特意不把平均长度冒充样本等待或寿命上界；左右示意单位不同，图注不可省略。',
'E28':'同一核的前推和回拉可直接操作。概率条与收益数值分开；单个固定时刻矩阵不能承担整个半群存在论证。',
'E39':'扰动方块在线与平行四边形之间对比，只推动第二份噪声可见不同响应。图不是密度热图，也不暗示路径时间可导。',
'E14':'仅把固定12个方框改为首项、次项、省略号、末项，明确一行恰有n项。概率面积、幅度及原交互机制保持。',
'E30':'直接提示事后跳点选择不是合法可预测策略，明确只在右侧计算路径Stieltjes收益。模型、跳点与归一化保持。'}
intro='<h1>第一至第五卷 · 第三批解释图</h1><p class="note">c7d426b5六组均获作者采用为工作视觉稿。本轮只做E14/E30局部精确化，新增E22/E28/E39三组；新图作者视觉待审。数学母稿、证明与正式站点不变。</p><nav><a href="/review.html">排序、范围与审校记录</a><a href="/e13-resource-check.html">E13原辅助图资源检查</a></nav>'
for code in CRIT:
 z=next(r for r in manifest if r['id']==code and r['lang']=='zh');intro+=f'<section class="review"><h2><a href="/compare/{code}.html">{code} · {z["title"]}</a></h2><p>{CRIT[code]}</p><nav><a href="/figures/{code}.zh.html">中文交互</a><a href="/figures/{code}.en.html">English</a><a href="/compare/{code}.html">前后与桌面／手机截图</a><a href="/print/{code}.zh.html">静态打印</a></nav></section>'
write(P/'index.html',page('本地第三批解释图审核',intro))
for code in CRIT:
 b=f'<nav><a href="/">本轮总览</a></nav><h1>{code} · 实际页面与前后对照</h1><p>{CRIT[code]}</p>'
 for r in [r for r in manifest if r['id']==code]:
  lg=r['lang'];b+=f'<h2>{"中文" if lg=="zh" else "English"}</h2><nav><a href="{r["before"]}">原正文</a><a href="{r["chapter_url"]}">正文嵌入</a><a href="{r["figure"]}">交互</a><a href="{r["print"]}">静态打印</a></nav>'
  if code in ['E14','E30']:
   b+='<h3>已采用版 → 本轮局部精确化</h3><div class="twins">'
   for prefix,tag,caption in [('/previous-shots/','desktop','c7d426b5已采用版'),('/shots/','desktop','本轮局部修订')]:b+=f'<figure class="shots"><a href="{prefix}{code}-{lg}-{tag}.jpg"><img loading="lazy" src="{prefix}{code}-{lg}-{tag}.jpg" alt="{caption}"></a><figcaption>{caption}</figcaption></figure>'
   b+='</div>'
  for size in ['desktop','mobile']:
   b+='<h3>'+size+' · 正文前后</h3><div class="twins">'
   for side in ['before','after']:
    src=f'/shots/{code}-{lg}-chapter-{side}-{size}.jpg';b+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}" alt="{code} {lg} {side} {size}"></a><figcaption>{side}</figcaption></figure>'
   b+='</div>'
  b+='<h3>独立图、交互与静态打印候选</h3><div class="twins">'
  for tag in ['desktop','mobile','mobile-end','interaction-desktop','interaction-mobile','print','print-end']:
   src=f'/shots/{code}-{lg}-{tag}.jpg';b+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}" alt="{code} {lg} {tag}"></a><figcaption>{tag}</figcaption></figure>'
  b+='</div>'
 write(P/'compare'/f'{code}.html',page(code+' comparison',b))
write(P/'review.html',page('排序与状态','<nav><a href="/">总览</a></nav><h1>实际范围与未完成事项</h1>'+''.join(f'<h2>{c}</h2><p>{t}</p>' for c,t in CRIT.items())+'<p>以已有40章审计为基准，剔除已采用组后重排，完整表见本报告REMAINING-PRIORITIES.md。只选择三个新位置，不机械凑五图。静态SVG浏览器检查不等于原生打印、实体纸张、真机或专家数学终审通过；全部原证明终审状态不变。</p>'))

# A missing dependency in a deliberately slim ZIP is not a production-site failure.
class Images(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,attrs):
  if t=='img':self.urls += [v for k,v in attrs if k=='src']
resources=[]
for lg in ['zh','en']:
 src=R/'dist'/('en' if lg=='en' else '')/'chapters/13-rare-events.html';parser=Images();parser.feed(src.read_text(encoding='utf-8'))
 for url in parser.urls:
  if 'local-clt-parity' not in url:continue
  target=(src.parent/url).resolve();assert target.is_file()
  resources.append(dict(lang=lg,page=src.relative_to(R).as_posix(),url=url,target=target.relative_to(R).as_posix(),exists=True,bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
assert len(resources)==2
write(O/'e13-resource-check.json',json.dumps(dict(scope='Actual existing production dist paths checked; no live-site failure inferred and no full production rebuild or cloud deployment performed',resources=resources),ensure_ascii=False,indent=2))
write(P/'e13-resource-check.html',page('E13原图路径','<nav><a href="/">总览</a></nav><h1>E13旧辅助图：构建产物路径有效</h1><p>检查实际dist中英文页面，而非精简审阅ZIP。两处相对路径都解析到存在的SVG。未由此宣称全站重构或外网测试完成；也没有证据据此报告线上故障。</p>'+''.join(f'<h2>{r["lang"]}</h2><p>{escape(r["url"])}</p><img src="/book/{r["target"][5:]}" alt="Existing local central limit auxiliary diagram">' for r in resources)))
print('10 bilingual overlays, gallery, source contexts and actual E13 build resource checks created')

# Reuse the already reachable, read-only batch2 HTTP service without changing it.
# This named local-only mirror is not linked from the formal site or its registry.
mirror=R/'assets/visuals/explanatory-early-v3/local-preview';prefix='/assets/visuals/explanatory-early-v3/local-preview/'
for src in P.rglob('*.html'):
 dst=mirror/src.relative_to(P);dst.parent.mkdir(parents=True,exist_ok=True);text=src.read_text(encoding='utf-8')
 def local_link(m):
  value=m.group(2)
  if value.startswith('/previous-shots/'):return m.group(1)+'="/shots/'+value[len('/previous-shots/'): ]+'"'
  if value.startswith('/shots/'):return m.group(1)+'="'+prefix+'screenshots/'+value[len('/shots/'): ]+'"'
  if value.startswith('/') and not value.startswith(('/assets/','/book/')):return m.group(1)+'="'+prefix+(value.lstrip('/') or 'index.html')+'"'
  return m.group(0)
 write(dst,re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',local_link,text))
if (O/'screenshots').exists():
 (mirror/'screenshots').mkdir(exist_ok=True)
 for f in (O/'screenshots').glob('*.jpg'):shutil.copyfile(f,mirror/'screenshots'/f.name)
write(O/'local-preview-route.json',json.dumps(dict(url='http://127.0.0.1:8861'+prefix+'index.html',scope='Local-only mirror through existing read-only HTTP service; formal dist unchanged'),indent=2))
