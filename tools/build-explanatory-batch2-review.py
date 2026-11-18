"""Build a local-only review gallery from actual viewport screenshots."""
from pathlib import Path
from html import escape as E
import json

ROOT=Path(__file__).resolve().parents[1]
O=ROOT/'reports/volume5-illustrations-batch2-2026-10-31';P=O/'preview'
rows=json.loads((O/'manifest.json').read_text(encoding='utf-8'))
notes={
'V34':('局部精确化：完整跳跃修正','保留原函数构图和三个交互阶段。将12与8共同括为20，明确Taylor高阶余项只有8。','新增主层分组更明确；没有重画曲线。阶段按钮只改变当前近似，完整分解保留供对照。'),
'V37':('局部精确化：窄带归一化手机布局','桌面与静态图保持原样；手机使用专用短画布，保留字号、积分与归一化。','图形区由约505px降至307px。英文图注仍较长，需继续试读；没有把示意密度冒充Brownian样本。'),
'V35':('新增：规则不保证唯一或全局存在','先取噪声为零，用同一初值的三条解与唯一但爆炸的解作结构对照。','分叉映射先让读者看到多解；有限寿命用不等时刻的读数呈现。它不独自承担强解/弱解全部区别，图注保留边界。'),
'V36':('新增：端点的两个方向','分别显示内部能否到达端点、端点能否即时进入内部。四种组合配真实模型。','入口图能直接打破“不能到达就不能出发”的误解。四型静态版信息较密；一般边界延拓不在图中被虚称已构造。'),
'V38':('新增：同一停止路径的两份贡献','一个时钟、两个退出端点；起点与收益率改变精确概率和期望，动力学不变。','图形把沿途累计与边界结算连接起来；不是两次独立实验。手机的完整条件需继续向下阅读，首屏不承担一般Feynman–Kac定理。'),
'V40':('新增：遗漏修正会改变过程','固定同一角度输入，对照半径1与exp(t/2)。角度和时刻按钮实际移动几何读数。','圆周约束比公式板直观；圆轮廓不代表均匀角度分布，也不代表真实轨迹。数学正确不等于作者审美已通过。')}
css='''body{margin:0;background:#f8f6ef;color:#173f39;font:17px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1200px;margin:auto;padding:30px}h1{font-size:30px}h2{font-size:23px}a{color:#146d61}section{padding:24px 0;border-top:1px solid #ccd9d1}nav{display:flex;flex-wrap:wrap;gap:16px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px}figure{margin:16px 0}figure img{width:100%;border:1px solid #ccd9d1;box-sizing:border-box}.mobile{max-width:390px;margin:auto}figcaption{font-size:15px;color:#52645f}.notice{padding:16px;background:#e9efea}details{margin:20px 0}summary{cursor:pointer;font-weight:bold}.links{font-size:15px}.reason{max-width:850px}@media(max-width:700px){main{padding:16px}.pair{grid-template-columns:1fr}h1{font-size:25px}}'''
def page(title,body):return f'<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(title)}</title><style>{css}</style><main>{body}</main></html>'
def shot(name,label,mobile=False):return f'<figure'+(' class="mobile"' if mobile else '')+f'><a href="/shots/{name}"><img loading="lazy" src="/shots/{name}" alt="{E(label)}"></a><figcaption>{E(label)} · 实际浏览器视口截图，点击原尺寸</figcaption></figure>'
index='<h1>第五卷解释图 · 第二批作者审阅</h1><p class="notice">四组新增：35、36、38、40章；两处局部调整：V34、V37。全部仅在本地候选页中。数学母稿与现有工程图未改，未发布、未推送。新图及局部调整等待作者视觉审核。</p><p>第39章本轮不配图：噪声方向扰动是候选，但在最多四组范围内，优先选择能以直接结构对照显著减轻理解困难的位置。不是判定第39章无需图示。V31、V33及P02、P05原资产保持不变。</p>'
(P/'compare').mkdir(exist_ok=True)
for code in notes:
 title,mechanism,critique=notes[code]
 index+=f'<section><h2><a href="/compare/{code}.html">{code} · {title}</a></h2><p>{mechanism}</p><p class="reason">评估：{critique}</p><nav>'
 body=f'<nav><a href="/">本批总览</a></nav><h1>{code} · {title}</h1><p>{mechanism}</p><p class="notice">设计判断：{critique}<br>采用状态：旧构图已有作者工作稿采用；本轮精确化待抽查。' if code in ['V34','V37'] else f'<nav><a href="/">本批总览</a></nav><h1>{code} · {title}</h1><p>{mechanism}</p><p class="notice">设计判断：{critique}<br>采用状态：新增候选，作者审美尚未批准。'
 body+='</p>'
 for lg in ['zh','en']:
  r=next(x for x in rows if x['id']==code and x['lang']==lg)
  index+=f'<a href="{r["chapter"]}">{lg} 正文候选</a>'
  before_label='首批原解释图' if r['before_kind']=='batch1-artwork' else '原纯文字与公式页面'
  body+=f'<section><h2>{"中文" if lg=="zh" else "English"}</h2><nav class="links"><a href="{r["before"]}">原页面</a><a href="{r["chapter"]}">加入正文</a><a href="{r["figure"]}">独立交互图</a><a href="{r["print"]}">静态打印页</a></nav><h3>桌面正文 · {before_label}与候选图</h3><div class="pair">'
  body+=shot(f'{code}-{lg}-chapter-before-desktop.jpg',before_label)+shot(f'{code}-{lg}-chapter-after-desktop.jpg','本轮候选放入实际正文')+'</div><h3>手机正文 · 前后</h3><div class="pair">'
  body+=shot(f'{code}-{lg}-chapter-before-mobile.jpg',before_label,True)+shot(f'{code}-{lg}-chapter-after-mobile.jpg','手机正文候选',True)+'</div><details><summary>独立图、手机后半页、完整静态版与交互读数</summary>'
  body+=shot(f'{code}-{lg}-desktop.jpg','独立图桌面')+'<div class="pair">'+shot(f'{code}-{lg}-mobile.jpg','独立图手机',True)+shot(f'{code}-{lg}-mobile-end.jpg','手机页末完整条件',True)+'</div>'
  body+=shot(f'{code}-{lg}-print.jpg','静态打印网页：未作原生打印分页验收')+shot(f'{code}-{lg}-print-end.jpg','静态页后半部及完整条件')
  if code in ['V35','V36']:
   keys=['finite'] if code=='V35' else ['regular','exit','natural']
   for key in keys:body+=shot(f'{code}-{lg}-state-{key}.jpg','实际交互状态 '+key)
  if code=='V37':
   for key in ['eighth','point']:body+=shot(f'{code}-{lg}-mobile-{key}.jpg','手机实际切换 '+key,True)
  if code=='V38':body+=shot(f'{code}-{lg}-rate2.jpg','x=1/4、c=2时的精确期望')
  if code=='V40':body+=shot(f'{code}-{lg}-angle.jpg','同一时刻改变角度读数')
  body+='</details></section>'
 index+='</nav></section>'
 (P/'compare'/f'{code}.html').write_text(page(title,body),encoding='utf-8')
index+='<section><h2>核验边界</h2><p>截图来自1440×1000桌面与390×844手机视口。静态SVG及打印网页可独立阅读；系统原生打印分页、PDF嵌字、实体纸张和多款手机真机未验收。本批未生成PDF。浏览器交互、数学计算、源码保护检查与作者审美判断分别记录。</p><p>重建、数学依据与批判性评价见本地报告README.md及MATHEMATICAL_REVIEW.md。完成本批即停止，不自动向41–50章推广。</p></section>'
(P/'index.html').write_text(page('第五卷解释图第二批',index),encoding='utf-8')
print('Review gallery: six groups, bilingual actual screenshots, truthful before views.')
