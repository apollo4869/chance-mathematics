"""Local-only chapter overlays and evidence-linked audit for volumes I–V."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
from html.parser import HTMLParser
import json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from tools.explanatory_illustrations.early_audit import ROWS,PILOTS
O=ROOT/'reports/volumes1-5-visual-review-2026-10-31';P=O/'preview';A=ROOT/'assets/visuals/explanatory-early-v1';BASE='/assets/visuals/explanatory-early-v1/'
for d in ['figures','print','compare','chapters/zh','chapters/en']: (P/d).mkdir(parents=True,exist_ok=True)
reg=json.loads((ROOT/'publication/explanatory-early-pilots-working.json').read_text(encoding='utf-8'))['figures']
style='<link rel="stylesheet" href="'+BASE+'figures.css">';script='<script defer src="'+BASE+'interactions.js"></script>'
shell='body{margin:0;background:#f8f6ef;color:#173f39;font:18px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1060px;margin:auto;padding:24px}a{color:#146d61}nav{display:flex;flex-wrap:wrap;gap:16px;font-size:15px}@media(max-width:700px){main{padding:12px}}'
def rewrite(s,lg,slug):
 s=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',s);base='/book/'+('en/' if lg=='en' else '')+'chapters/'+slug+'.html'
 def link(m):
  v=m.group(2)
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m.group(0)
  return m.group(1)+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 return re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',link,s).replace('</head>',style+'</head>',1).replace('</body>',script+'</body>',1)
manifest=[]
for r in reg:
 code,lg,slug=r['id'],r['lang'],r['slug'];source=ROOT/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');before=rewrite(source.read_text(encoding='utf-8'),lg,slug)
 h=re.search(r'<h[23] id="([^"]+)">'+re.escape(r['section'])+r'\s[^<]+</h[23]>',before);assert h,(code,lg)
 start=before.rfind('<div class="reading-unit"',0,h.start());end=before.find('<div class="reading-unit"',h.end());assert end>start
 pos=before.rfind('</div>',start,end);after=before[:pos]+r['html']+before[pos:];assert after.replace(r['html'],'',1)==before
 dest=P/'chapters'/lg;(dest/(slug+'.html')).write_text(after,encoding='utf-8');(dest/(slug+'-before.html')).write_text(before,encoding='utf-8')
 entry={k:r[k] for k in ['id','chapter','lang','slug','section','title','status']};entry.update(chapter_url=f'/chapters/{lg}/{slug}.html#visual-{code}',before=f'/chapters/{lg}/{slug}-before.html#{h.group(1)}',figure=f'/figures/{code}.{lg}.html',print=f'/print/{code}.{lg}.html',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest());manifest.append(entry)
 nav=f'<nav><a href="/">'+('本批审阅' if lg=='zh' else 'Review')+f'</a><a href="{entry["chapter_url"]}">'+('正文候选' if lg=='zh' else 'In chapter')+f'</a><a href="{entry["print"]}">'+('静态打印' if lg=='zh' else 'Static print')+f'</a><a href="/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
 (P/'figures'/f'{code}.{lg}.html').write_text(f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(r["title"])}</title><style>{shell}</style>{style}<main>{nav}{r["html"]}</main>{script}</html>',encoding='utf-8')
 pc='@page{size:A4 portrait;margin:12mm}body{margin:0;font:16px/1.7 "Microsoft YaHei",sans-serif}main{max-width:900px;margin:20px auto}img{width:100%;height:auto}nav{display:flex;gap:16px;flex-wrap:wrap}@media print{nav{display:none}main{margin:0}img{width:180mm;max-width:100%}}'
 (P/'print'/f'{code}.{lg}.html').write_text(f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(r["title"])} · static</title><style>{pc}</style><main>{nav}<img src="{BASE}{code}.{lg}.svg" alt="{E(r["title"])}"></main></html>',encoding='utf-8')
(O/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

class Parse(HTMLParser):
 def __init__(self):super().__init__();self.main=False;self.heading='';self.h=False;self.buf='';self.items=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='main':self.main=True
  if not self.main:return
  if t in ['h1','h2','h3']:self.h=True;self.buf=''
  kind=None;src=''
  if t=='img':kind='image';src=a.get('src','')
  if t=='svg' and a.get('aria-label') and a.get('focusable')!='false':kind='inline-svg';src=a['aria-label']
  if 'data-widget' in a:kind='interaction';src=a['data-widget']
  if 'data-chart' in a:kind='numeric-chart';src=a['data-chart']
  if a.get('data-visual-id')=='typewriter':kind='interaction';src='typewriter'
  if kind:self.items.append(dict(kind=kind,source=src,heading=self.heading))
 def handle_endtag(self,t):
  if t=='main':self.main=False
  if self.h and t in ['h1','h2','h3']:self.heading=self.buf.strip();self.h=False
 def handle_data(self,d):
  if self.h:self.buf+=d
audit=[]
for n,sec,priority,keep,gap,no in ROWS:
 md=next((ROOT/'chapters').glob(f'{n:02d}-*.md'));s=md.read_text(encoding='utf-8');html=ROOT/'dist/chapters'/md.with_suffix('.html').name;parser=Parse();parser.feed(html.read_text(encoding='utf-8'))
 entry=dict(chapter=n,volume=1 if n<=4 else 2 if n<=14 else 3 if n<=22 else 4 if n<=29 else 5,source=md.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(md.read_bytes()).hexdigest(),section=sec,priority=priority,protect=keep,gap=gap,no_mechanical_diagram=no,existing_visuals=parser.items)
 # Numeric charts can be rendered during build; record the source placeholder too.
 entry['source_chart_placeholders']=re.findall(r'data-chart="([^"]+)"',s)
 audit.append(entry)
(O/'chapter-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 第一至第五卷逐章视觉缺口审查','', '以当前实际正文与阅读页为准；逐节检查概念出现、反例和证明机制，对候选段落加读原文。不是全书证明终审，也没有对40章全部小节做逐屏手机验收。旧审计是线索，不作为免检证据。内嵌SVG、数值图占位及交互均列入新记录；第1章骰子图与第6章Riemann矩形未漏算。','', 'P1为优先解决的学习障碍，P2为后续候选，P3可不加。不是每章图数指标。第五卷“已有候选”不等于作者已经采用，状态按两批真实记录保留。','']
for v in range(1,6):
 lines+=['## 第'+str(v)+'卷','', '| 章与定位 | 应保护与主辅判断 | 真正的缺口及优先级 | 不机械配图的部分 |','|---|---|---|---|']
 for a in audit:
  if a['volume']==v:lines.append(f'| [{a["chapter"]} · §{a["section"]}](../../{a["source"]}) | {a["protect"]} | **{a["priority"]}**：{a["gap"]} | {a["no_mechanical_diagram"]} |')
 lines.append('')
(O/'chapter-audit.md').write_text('\n'.join(lines),encoding='utf-8',newline='\n')
rank=[(6,'E06','新：按值测量，直接接上概念诞生；保护原Riemann图。'),(8,'E08','新：三角矛盾比抽象一致性公式更快暴露缺失的联合律。'),(16,'E16','新机制：与旧冻结图不同，检验当场信息合法性。'),(20,'E20','新机制：树＋标记个体的联合抽样，原谱系图只作辅助。'),(24,'E24','增强：把图注中的时间同胚变成可见操作，不删旧双面板。'),(13,'待后续','奇偶格宽是局部CLT的必要结构，当前曲线不能充分突出。'),(14,'待后续','Feller不排除大跳的反例需要概率原子而非参数折线。'),(17,'待后续','后验足够状态及共同概率成分分别解释预测与长期收敛。'),(22,'待后续','状态停留长度与访问次数分开；爆炸还可另做时钟图。'),(27,'待后续','有限层补偿到L²合成，避免∞−∞误解。'),(28,'待后续','核的双向作用与边界定义域解释算子为什么出现。'),(29,'待后续','指数倾斜必须新增速度n的代价，不能只是普通换权重。'),(12,'待后续','首次越界分片揭示最大不等式的关键步骤。'),(2,'待后续','覆盖概率与固定数据后验不是同一层概率；优于重画混合硬币。'),(30,'第五卷剩余首位','事件前后信息闸门，两批尚未处理。'),(39,'第五卷剩余首位','噪声方向与输出秩，不是时间可微性。'),(35,'第五卷剩余','弱解核与路径唯一收缩，超出已做ODE反例。'),(36,'第五卷剩余','尺度和速度分开，超出已做四型端点。'),(37,'第五卷剩余','逆局部时与游程，超出窄带归一化。'),(33,'第五卷剩余','信息扩大影响表示，超出P/Q换权重。')]
rr=['# 按教学价值与视觉改善潜力排序','', '先完成下面前五项，之后停止。排序考虑：是否直击本章新概念、能否用准确视觉操作减轻困难、是否避开已采用优秀图的重复；不使用机械分数。第一卷也已实际审查，但不强制每卷分配一个生产名额。第2章有后续价值，重画第1章骰子/依赖卡片的增益则很小。','', '| 次序 | 章 | 本轮范围 | 选择依据 |','|---|---|---|---|']
for i,(n,code,why) in enumerate(rank,1):rr.append(f'| {i} | {n} | {code} | {why} |')
rr+=['','第五卷优先级单列，不表示本轮越界制作。其余各章不是默认为通过，具体缺口、可不配图处与保护项见逐章表。']
(O/'priorities.md').write_text('\n'.join(rr),encoding='utf-8',newline='\n')
print('40 chapter judgments, five pilot overlays and truthful before pages ready.')
