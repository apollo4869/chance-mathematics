from pathlib import Path
from html import escape as E
import json
ROOT=Path(__file__).resolve().parents[1];O=ROOT/'reports/volume5-illustrations-batch1-2026-10-31';P=O/'preview';(P/'compare').mkdir(exist_ok=True)
rows=json.loads((O/'manifest.json').read_text(encoding='utf-8'))
info={
'V31':('31.10','新增解释缺口','两种括号不是重复命名：连续情形汇合，Poisson跳跃记录显示已发生的2与可预测的3。','仍较依赖两个计数器的类比；图不能替代平方和收敛与补偿唯一性证明。'),
'P01':('32.11','已采用试点的章节嵌入','保留2、6、4的结果优先构图和取值交互，不重做。','此处是将已采用图加入本地章节候选，不是重新宣称审美或数学终审。'),
'V33':('33.2','新增解释缺口','同四条有限记录、相同位置、不同概率面积；拖动模型选择改变权重而不移动记录。','有限类比没有表示连续Brownian测度的全部复杂性；图注明确其边界。'),
'V34':('34.14','新增解释缺口','用立方函数的切线、有限跳跃及6、12、8的几何分解，显示完整跳跃项不能截成二阶。','仍含函数曲线，但服务于几何分解而非展示模拟数据。需作者判断是否足够像解释插图。'),
'V37':('37.4','新增解释缺口','窄带面积映射为平均密度；缩带与单点按钮揭示“极限”不是直接用0/0。','剖面是示意密度，不是Brownian样本。是否需要更少说明文字，留待作者试读判断。'),
'P02':('试点','局部精确化','明确给定环境后独立重新抽取、允许重复，碗中可能值不被移走。','原取值、概率和交互构图不变。'),
'P05':('试点','局部精确化','新增细线与宽带的实体图例，文字明确宽带不属于度量空间，距离不随滑块改变。','原长枝几何和抽样交互受到保护。')}
css='''*{box-sizing:border-box}body{margin:0;background:#f8f6ef;color:#173f39;font:17px/1.75 "Microsoft YaHei",sans-serif}main{max-width:1260px;margin:auto;padding:28px}a{color:#146d61}h1{font-size:29px;line-height:1.4}h2{font-size:23px}section{border-top:1px solid #ccd9d1;margin:32px 0;padding-top:18px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}.three{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.shot{display:block;width:100%;height:auto;border:1px solid #d0ddd4}figure{margin:0}figcaption{font-size:14px;color:#5d6c63;margin:10px 0}nav{display:flex;flex-wrap:wrap;gap:16px;margin:14px 0}details{margin:22px 0}summary{cursor:pointer;font-weight:600}.phone img{max-width:390px;margin:auto}p{max-width:1040px}.state{color:#73582c}@media(max-width:750px){main{padding:16px}.grid,.three{grid-template-columns:1fr}h1{font-size:25px}}'''
def page(t,b):return f'<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(t)}</title><style>{css}</style><main>{b}</main></html>'
def shot(url,label):return f'<figure><a href="{url}"><img class="shot" loading="lazy" src="{url}" alt="{E(label)}"></a><figcaption>{E(label)} · 点击查看实际浏览器原尺寸截图</figcaption></figure>'
def links(r):
 s=f'<nav><a href="{r["figure"]}">{r["lang"]} 独立交互图</a><a href="{r["print"]}">静态打印</a><a href="/assets/visuals/explanatory-v1/{r["id"]}.{r["lang"]}.svg">完整SVG</a>'
 if r['chapter']:s+=f'<a href="{r["chapter"]}">放入正文 §{r["section"]}</a>'
 return s+'</nav>'
index='<h1>第五卷解释图 · 首批作者抽查</h1><p>依据现有审计，本批新增31、33、34、37章的四组解释图，并将已采用P01嵌入32章本地候选。35、36、38、39、40章的其他缺口保留为后续事项，本轮停止后不自动继续。</p><p>两类任务分开记录：本区间原来没有可替换的工程图，因此本批是补充视觉解释；没有把原有公式或文字伪称为旧工程图。P02、P05仅做本次明确授权的试点精确化，不推进41–58章。</p><p class="state">五组试点已采用为当前视觉工作稿；四组新图等待作者抽查，工程检查不等于审美或数学终审。未改数学母稿，未发布、未推送。</p><nav><a href="http://127.0.0.1:8857/">第三轮原样保留</a><a href="http://127.0.0.1:8856/reference.html">早期骰子映射与独立性参考</a></nav>'
for code,(section,kind,why,crit) in info.items():
 zh=next(r for r in rows if r['id']==code and r['lang']=='zh');en=next(r for r in rows if r['id']==code and r['lang']=='en')
 index+=f'<section><h2><a href="/compare/{code}.html">{code} · {E(zh["title"])}</a></h2><p class="state">{kind} · {section}</p><p>{E(why)}</p>'+links(zh)+links(en)+f'<p>具体限制：{E(crit)}</p><div class="grid">'+shot(f'/shots/{code}-zh-desktop.jpg','中文桌面')+shot(f'/shots/{code}-en-desktop.jpg','English desktop')+'</div></section>'
 b=f'<nav><a href="/">← 本批总览</a></nav><h1>{code} · {E(zh["title"])}</h1><p class="state">{kind} · {section}</p><p>{E(why)}</p><p>{E(crit)}</p>'+links(zh)+links(en)
 if zh['chapter']:
  b+='<section><h2>实际章节：加入前 → 加入后</h2><p>原位置无图，左侧为未加入插图的真实文字/公式页面；右侧为本地候选。原段落、数学与链接均保留。</p><div class="grid">'+shot(f'/shots/{code}-zh-before-desktop.jpg','加入前 · 中文正文')+shot(f'/shots/{code}-zh-chapter-desktop.jpg','加入后 · 中文正文')+'</div><details><summary>手机实际章节前后对照</summary><div class="grid phone">'+shot(f'/shots/{code}-zh-before-mobile.jpg','加入前 · 手机正文')+shot(f'/shots/{code}-zh-chapter-mobile.jpg','加入后 · 手机正文')+'</div></details><details><summary>English chapter before / after</summary><div class="grid">'+shot(f'/shots/{code}-en-before-desktop.jpg','English · before')+shot(f'/shots/{code}-en-chapter-desktop.jpg','English · after')+'</div><div class="grid phone">'+shot(f'/shots/{code}-en-before-mobile.jpg','English mobile · before')+shot(f'/shots/{code}-en-chapter-mobile.jpg','English mobile · after')+'</div></details></section>'
 else:
  b+='<section><h2>试点局部精确化：第三轮 → 本轮</h2><div class="grid">'+shot(f'/r3-shots/{code}-zh-desktop.jpg','第三轮已采用工作稿')+shot(f'/shots/{code}-zh-desktop.jpg','本轮局部精确化')+'</div></section>'
 b+='<section><h2>手机与完整条件</h2><div class="three phone">'+shot(f'/shots/{code}-zh-mobile.jpg','中文 · 手机首屏')+shot(f'/shots/{code}-en-mobile.jpg','English · mobile top')+shot(f'/shots/{code}-en-mobile-end.jpg','English · lower conditions')+'</div></section>'
 states={'V31':[('continuous','连续模型'),('jump','跳跃模型')],'V33':[('25','改变Q的权重')],'V34':[('0','只留一阶'),('1','加上二阶仍缺一部分')],'V37':[('eighth','更窄的带'),('point','单点不是直接取极限')]}.get(code)
 if states:b+='<section><h2>图形确实变化的交互状态</h2><div class="grid">'+''.join(shot(f'/shots/{code}-zh-state-{k}.jpg',lab) for k,lab in states)+'</div></section>'
 b+='<section><h2>静态打印仍独立成立</h2><p>以下为静态打印网页截图；不冒充原生打印分页、PDF嵌字或实物印刷验收。</p><div class="grid">'+shot(f'/shots/{code}-zh-print.jpg','中文静态打印')+shot(f'/shots/{code}-en-print.jpg','English static print')+'</div></section>'
 (P/'compare'/f'{code}.html').write_text(page(code+' · 首批前后对照',b),encoding='utf-8')
index+='<section><h2>P03、P04保留</h2><p>已采用构图与第三轮矢量源保持一致；本批未为后续章节制作新图。</p><nav><a href="http://127.0.0.1:8857/compare/P03.html">P03原工作稿</a><a href="http://127.0.0.1:8857/compare/P04.html">P04原工作稿</a></nav></section>'
(P/'index.html').write_text(page('第五卷解释图 · 首批作者抽查',index),encoding='utf-8');print('Batch review with honest no-image before views and two local pilot comparisons ready.')
