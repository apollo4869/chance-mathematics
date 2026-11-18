"""Build reversible chapter overlays and a six-entry review gallery, never dist."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
import re,json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'reports/early-explanations-batch2-2026-10-31';P=O/'preview';BASE='/assets/visuals/explanatory-early-v2/'
for d in ['figures','chapters/zh','chapters/en','print','compare']:(P/d).mkdir(parents=True,exist_ok=True)
style=f'<link rel="stylesheet" href="{BASE}figures.css">';script=f'<script defer src="{BASE}interactions.js"></script>'
SHELL='body{background:#f8f6ef;color:#173f39;font:18px/1.8 "Microsoft YaHei",sans-serif;margin:0}main{max-width:1080px;margin:auto;padding:26px}a{color:#146d61}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}section.review{border-top:1px solid #ccd9d1;margin:30px 0;padding:20px 0}.twins{display:grid;grid-template-columns:1fr 1fr;gap:18px}.twins img{width:100%;height:auto}.shots img{width:100%;height:auto;border:1px solid #ccd9d1}figure{margin:0}figcaption{font-size:15px}details{margin:18px 0}iframe{width:100%;height:900px;border:1px solid #ccd9d1}.note{background:#eaf2ee;padding:16px}@media(max-width:700px){main{padding:12px}.twins{grid-template-columns:1fr}.phone{max-width:390px;margin:auto}h1{font-size:26px}}'
def page(title,body):return f'<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(title)}</title><style>{SHELL}</style><main>{body}</main></html>'
def write(path,txt):path.write_text(txt,encoding='utf-8',newline='\n')
def rewrite(s,lg,slug):
 s=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',s)
 base='/book/'+('en/' if lg=='en' else '')+'chapters/'+slug+'.html'
 def link(m):
  v=m.group(2)
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
  return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 return re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',link,s).replace('</head>',style+'</head>',1).replace('</body>',script+'</body>',1)
reg=json.loads((R/'publication/explanatory-early-batch2-working.json').read_text(encoding='utf-8'))['figures'];manifest=[];contexts=[]
for r in reg:
 code,lg,slug=r['id'],r['lang'],r['slug'];source=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');before=rewrite(source.read_text(encoding='utf-8'),lg,slug)
 h=re.search(r'<h[23] id="([^"]+)">'+re.escape(r['section'])+r'\s[^<]+</h[23]>',before);assert h,(code,lg)
 start=before.rfind('<div class="reading-unit"',0,h.start());end=before.find('<div class="reading-unit"',h.end());assert start>=0 and end>start
 pos=before.rfind('</div>',start,end);after=before[:pos]+r['html']+before[pos:];assert after.replace(r['html'],'',1)==before
 write(P/'chapters'/lg/(slug+'-before.html'),before);write(P/'chapters'/lg/(slug+'.html'),after)
 entry={k:r[k] for k in ['id','chapter','lang','slug','section','title','status','kind']};entry.update(chapter_url=f'/chapters/{lg}/{slug}.html#visual-{code}',before=f'/chapters/{lg}/{slug}-before.html#{h.group(1)}',figure=f'/figures/{code}.{lg}.html',print=f'/print/{code}.{lg}.html',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest());manifest.append(entry)
 nav=f'<nav><a href="/">本批审阅</a><a href="{entry["chapter_url"]}">正文候选 / In chapter</a><a href="{entry["print"]}">静态打印</a><a href="/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
 write(P/'figures'/f'{code}.{lg}.html',f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(r["title"])}</title><style>{SHELL}</style>{style}<main>{nav}{r["html"]}</main>{script}</html>')
 pc='@page{size:A4 portrait;margin:12mm}body{margin:0;background:white;font:16px/1.7 "Microsoft YaHei",sans-serif}main{max-width:900px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:16px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
 write(P/'print'/f'{code}.{lg}.html',f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(r["title"])} · static</title><style>{pc}</style><main>{nav}<img src="{BASE}{code}.{lg}.svg" alt="{E(r["title"])}"><span id="static-end"></span></main></html>')
 md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');ms=md.read_text(encoding='utf-8');parts=re.split(r'(?m)(?=^## )',ms);chosen=[t for t in parts if t.startswith('## '+r['section']+' ')];assert len(chosen)==1
 contexts.append(dict(id=code,lang=lg,path=md.relative_to(R).as_posix(),sha256=hashlib.sha256(md.read_bytes()).hexdigest(),section_text=chosen[0]))
write(O/'manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2));write(O/'reading-contexts.json',json.dumps(contexts,ensure_ascii=False,indent=2))

CRIT={
'E12':'首次越界的互斥分片成为可见分类；右侧保留“某条记录可回零，条件平方均值却不撤销”的反差。符号密度仍需试读。',
'E13':'格点空位、奇偶平移和宽度2同时出现。不是再画一条钟形曲线；小n近似偏差保留，不冒充精确概率。',
'E14':'概率面积缩小与原子位置靠近0是两种不同操作。复制符号仅辅助，不能按图标个数误读行长。',
'E17':'切换真正改变合并关系及预测分支。不是把Markov性画成“删掉所有过去”；双向箭头拥挤处仍可试读。',
'E30':'同一批跳点对dt和dN的不同质量直接可见；手选路径的收益与总体期望明确分开。',
'E24':'改为错位单跳/短暂往返两个主场景，不是换色。手机重新绘制并排结论；时钟移入可展开第二层。'}
intro='<h1>第一至第五卷 · 第二批解释图</h1><p class="note">E06、E08、E16、E20已获作者采用为视觉工作稿，原构图和交互字节保护。本轮只新增E12/E13/E14/E17/E30五组，并重组E24主视觉；全部本轮候选等待作者审美审核。没有修改数学母稿、原图或正式网站。</p><nav><a href="/review.html">范围、数学与批判性说明</a><a href="/previous/">上一批完整预览</a><a href="/references.html">实际设计参照</a></nav>'
for code in ['E24','E12','E13','E14','E17','E30']:
 rows=[r for r in manifest if r['id']==code];z,e=rows
 intro+=f'<section class="review"><h2><a href="/compare/{code}.html">{code} · §{z["section"]} {E(z["title"])}</a></h2><p>{CRIT[code]}</p><nav><a href="{z["chapter_url"]}">中文正文</a><a href="{e["chapter_url"]}">English in chapter</a><a href="/compare/{code}.html">完整前后对照</a><a href="{z["print"]}">静态打印</a></nav></section>'
write(P/'index.html',page('解释图第二批 · 本地审核',intro+'<p>已做的工程和数学检查不等于审美通过；原生打印分页、实体打印和多款真机仍未验收。不发布、不推送，不自动进入第六卷。</p>'))

for code in CRIT:
 rows=[r for r in manifest if r['id']==code];z=rows[0]
 body=f'<nav><a href="/">本批总览</a><a href="/review.html">数学与视觉记录</a></nav><h1>{code} · {E(z["title"])}</h1><p class="note">{CRIT[code]} 本轮作者视觉待审。</p>'
 if code=='E24':
  body+='<h2>上一版与本版的主视觉</h2><p>以下是相同尺寸的实际浏览器截图，点击可看原尺寸；并排展示不会把网页误触发为手机布局。</p><nav><a href="/previous/figures/E24.zh.html">上一版交互</a><a href="/figures/E24.zh.html">新版交互</a></nav>'
  for size in ['desktop','mobile']:
   body+='<h3>'+('桌面' if size=='desktop' else '手机')+'</h3><div class="twins">'
   for src,label in [(f'/shots/E24-previous-{size}.jpg','上一版：时钟与单一场景'),(f'/shots/E24-zh-{size}.jpg','新版：单跳与往返直接并列')]:body+=f'<figure class="shots {"phone" if size=="mobile" else ""}"><a href="{src}"><img loading="lazy" src="{src}" alt="{label}"></a><figcaption>{label} · 实际视口</figcaption></figure>'
   body+='</div>'
 for r in rows:
  lg=r['lang'];body+=f'<h2>{"中文" if lg=="zh" else "English"}</h2><nav><a href="{r["before"]}">原正文</a><a href="{r["chapter_url"]}">实际正文候选</a><a href="{r["figure"]}">独立交互</a><a href="{r["print"]}">完整静态打印</a></nav>'
  for size,label in [('desktop','桌面正文 · 原页面与加入后'),('mobile','手机正文 · 原页面与加入后')]:
   body+='<h3>'+label+'</h3><div class="twins">'
   for side,cap in [('before','原正文，全部内容保留'),('after','新图放入同一实际正文')]:
    src=f'/shots/{code}-{lg}-chapter-{side}-{size}.jpg';body+=f'<figure class="shots {"phone" if size=="mobile" else ""}"><a href="{src}"><img loading="lazy" src="{src}" alt="{code} {lg} {side} {size}"></a><figcaption>{cap} · 实际浏览器视口</figcaption></figure>'
   body+='</div>'
  body+='<details><summary>独立图、交互变化与静态截图</summary><div class="twins">'
  for tag in ['desktop','mobile','interaction','print']:
   src=f'/shots/{code}-{lg}-{tag}.jpg';body+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}" alt="{code} {lg} {tag}"></a><figcaption>{tag} · actual viewport</figcaption></figure>'
  body+='</div></details>'
 write(P/'compare'/f'{code}.html',page(code+' · 前后对照',body))

write(P/'review.html',page('数学、视觉与执行边界','<nav><a href="/">总览</a></nav><h1>实际增量与限制</h1>'+''.join(f'<h2>{c}</h2><p>{t}</p>' for c,t in CRIT.items())+'<p>五个新位置来自上批40章审计，本轮核读中英文对应小节。都具备直接操作的数学机制，因此选择全部五个；不增加第六个新位置。E24为已授权修订，原版保留。纯技术图继续保留辅助职责，无新图替换旧文件。</p><p>完整精确模型、适用边界及自查在报告MATHEMATICAL_REVIEW.md；不把图像当证明，不升级上游专家终审状态。截图中的手机是浏览器390×844视口，不是真机验收。静态打印图已独立排版，不代表原生分页、PDF嵌字或实体打印已通过。</p>'))
refs='<nav><a href="/">总览</a></nav><h1>本轮实际参照</h1><p>骰子映射、概率依赖交互、P03抽样和P04商树的优秀结构用于比较，不修改这些资产。</p>'
# Existing reference gallery includes genuine screenshots and original inline-SVG exports.
refs+='<p><a href="/previous/references.html">查看上一轮保存的实际参照截图与原图</a></p><p><a href="/previous/compare/E08.html">已采用E08：关系矛盾</a> · <a href="/previous/compare/E20.html">已采用E20：固定家族与概率面积</a></p>'
write(P/'references.html',page('设计参照',refs))
print('12 bilingual chapter overlays, static pages, comparison galleries and source contexts built.')
