"""Review gallery, comparative screenshots and chapter-specific audit; no formal navigation edits."""
from pathlib import Path
from html import escape as E
from urllib.parse import urljoin
import json,re
R=Path(__file__).resolve().parents[1];O=R/'reports/volumes1-5-visual-review-2026-10-31';P=O/'preview';rows=json.loads((O/'manifest.json').read_text(encoding='utf-8'));audit=json.loads((O/'chapter-audit.json').read_text(encoding='utf-8'))
css='''body{margin:0;background:#f8f6ef;color:#173f39;font:17px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1200px;margin:auto;padding:30px}h1{font-size:29px}h2{font-size:23px}a{color:#146d61}section{padding:22px 0;border-top:1px solid #ccd9d1}nav{display:flex;flex-wrap:wrap;gap:16px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px}figure{margin:16px 0}figure img{width:100%;height:auto;border:1px solid #ccd9d1;box-sizing:border-box}.mobile{max-width:390px;margin:auto}figcaption{font-size:15px;color:#52645f}.notice{padding:16px;background:#e9efea}details{margin:20px 0}summary{cursor:pointer;font-weight:bold}.audit-note{max-width:900px}td,th{text-align:left;vertical-align:top;border-bottom:1px solid #ccd9d1;padding:12px}table{border-collapse:collapse;width:100%}.asset{max-width:650px}@media(max-width:700px){main{padding:16px}.pair{grid-template-columns:1fr}h1{font-size:25px}table,tbody,tr,td,th{display:block}thead{display:none}td{padding:8px}}'''
def page(title,body):return f'<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(title)}</title><style>{css}</style><main>{body}</main></html>'
def shot(f,label,mobile=False,reference=False):
 prefix='/references/' if reference else '/shots/'
 return f'<figure'+(' class="mobile"' if mobile else '')+f'><a href="{prefix}{f}"><img loading="lazy" src="{prefix}{f}" alt="{E(label)}"></a><figcaption>{E(label)} · 实际浏览器视口截图，点击原尺寸</figcaption></figure>'
critic={'E06':'归组操作直接可见；手机另有紧凑组合。有限阶梯仍可Riemann积分，不用它制造旧方法失败。', 'E08':'关系三角比公式更直接；读者仍需图注中的二点联合律，不能凭一条记录证明不可能。', 'E16':'遮住未来使信息限制成为动作。时刻标签与位置值已分开，但首次/末次术语仍需试读。', 'E20':'固定树上移动标记并改变概率面积；联合概率与给定树后的均匀概率容易混淆，图注不可删。', 'E24':'时间箭头真正实现复合操作；极窄脉冲会接近像素尺度，可切较宽状态，结论仍由满射性论证。'}
index='<h1>第一至第五卷视觉审查 · 五组试点</h1><p class="notice">本轮审查1–40章，不进入第六卷。只在第一至第四卷制作五组候选，原图、数学母稿与正式网站不变。全部新图作者视觉待审；数学自查和浏览器检查不代替审美批准。</p><nav><a href="/audit.html">40章逐章清单</a><a href="/priorities.html">缺口优先级</a><a href="/existing.html">现有图与保护判断</a><a href="/references.html">实际设计参照</a></nav><p>第1章骰子图和依赖卡片不是全卷免检依据。第6章原Riemann图、第7章窗口、第9章投影、第10章切片等保护；第五卷两批只处理局部，30章及剩余理论缺口逐章重查。</p>'
for code in critic:
 group=[r for r in rows if r['id']==code];zh=next(r for r in group if r['lang']=='zh')
 index+=f'<section><h2><a href="/compare/{code}.html">{code} · §{zh["section"]} {E(zh["title"])}</a></h2><p>{critic[code]}</p><nav><a href="{zh["chapter_url"]}">中文正文候选</a><a href="{next(r["chapter_url"] for r in group if r["lang"]=="en")}">English in chapter</a><a href="/compare/{code}.html">完整前后对照</a></nav></section>'
 body=f'<nav><a href="/">本批总览</a><a href="/audit.html">逐章审查</a></nav><h1>{code} · {E(zh["title"])}</h1><p class="notice">{critic[code]}<br>当前为作者视觉待审候选，未替换正文母稿。</p>'
 for r in group:
  lg=r['lang'];body+=f'<section><h2>{"中文" if lg=="zh" else "English"}</h2><nav><a href="{r["before"]}">原页面</a><a href="{r["chapter_url"]}">实际正文候选</a><a href="{r["figure"]}">独立交互</a><a href="{r["print"]}">静态打印</a></nav><h3>桌面正文 · 原页面与新增后</h3><div class="pair">'+shot(f'{code}-{lg}-chapter-before-desktop.jpg','实际原页面：文字、公式与该节已有图均保留')+shot(f'{code}-{lg}-chapter-after-desktop.jpg','新图放入实际正文')+'</div><h3>手机正文 · 前后</h3><div class="pair">'+shot(f'{code}-{lg}-chapter-before-mobile.jpg','加入前',True)+shot(f'{code}-{lg}-chapter-after-mobile.jpg','加入后',True)+'</div><details><summary>独立图、交互读数、手机页末与静态完整版</summary>'+shot(f'{code}-{lg}-desktop.jpg','独立图桌面')+'<div class="pair">'+shot(f'{code}-{lg}-mobile.jpg','独立图手机',True)+shot(f'{code}-{lg}-mobile-end.jpg','手机完整条件',True)+'</div>'+shot(f'{code}-{lg}-interaction.jpg','实际切换后的结构与读数')+shot(f'{code}-{lg}-print.jpg','静态完整SVG的打印网页')+shot(f'{code}-{lg}-print-end.jpg','静态页末条件：未作原生打印分页验收')+'</details></section>'
 (P/'compare'/f'{code}.html').write_text(page(zh['title'],body),encoding='utf-8')
index+='<section><h2>核验边界</h2><p>中英文桌面1440×1000、手机390×844与静态SVG网页实际检查；原生打印分页、PDF嵌字及实体印刷未验收。本批不发布、不推送，不自动继续第六卷。</p></section>'
(P/'index.html').write_text(page('第一至第五卷视觉审查',index),encoding='utf-8')
body='<nav><a href="/">本批总览</a><a href="/priorities.html">排序</a></nav><h1>40章逐章审查</h1><p>审查的是解释收益，不是图数。位置、数学困难、保护项与不配图判断分别列出。第1–4章不因少数好图而整体免检，第30–40章不因两批候选而宣布完成。</p>'
for vol in range(1,6):
 body+=f'<section><h2>第{vol}卷</h2>'
 for a in audit:
  if a['volume']!=vol:continue
  slug=Path(a['source']).stem;body+=f'<details id="chapter-{a["chapter"]}"><summary>第{a["chapter"]}章 · §{a["section"]} · {a["priority"]}</summary><div class="audit-note"><p><b>保护与主辅：</b>{a["protect"]}</p><p><b>缺口：</b>{a["gap"]}</p><p><b>不机械配图：</b>{a["no_mechanical_diagram"]}</p><a href="/book/chapters/{slug}.html">读取当前正文</a></div></details>'
 body+='</section>'
(P/'audit.html').write_text(page('逐章视觉缺口',body),encoding='utf-8')
priority=(O/'priorities.md').read_text(encoding='utf-8');(P/'priorities.html').write_text(page('教学价值与潜力排序','<nav><a href="/">本批总览</a></nav><h1>优先级排序</h1><pre style="white-space:pre-wrap;font:inherit">'+E(priority)+'</pre>'),encoding='utf-8')
body='<nav><a href="/">本批总览</a></nav><h1>现有图的作用与保护边界</h1><p>外部图片、内嵌SVG、运行时数值图与交互一并核对。以下源图仍在原位置；史料不以A/B/C决定删除。A为解释骨架，B为记录/计算辅助，C为可增强的混合结构。这是编辑判断，不是作者审美终审。</p>'
ml=['# 现有图的保护、主辅与增强清单','','逐章判断以chapter-audit.md为主。这里补实际资产定位，不以图片文件数量判断覆盖。内嵌骰子、Riemann矩形及二项比较均在此。','']
for a in audit:
 if not a['existing_visuals'] and not a['source_chart_placeholders']:continue
 slug=Path(a['source']).stem;body+=f'<section><h2>第{a["chapter"]}章</h2><p>{a["protect"]}</p>';ml+=['## 第'+str(a['chapter'])+'章','',a['protect'],'']
 raw=(R/'dist/chapters'/(slug+'.html')).read_text(encoding='utf-8');inline=[s for s in re.findall(r'<svg\b.*?</svg>',raw,re.S) if 'aria-label=' in s.split('>',1)[0] and 'focusable="false"' not in s.split('>',1)[0]];idx=0
 for im in a['existing_visuals']:
  src=im['source'];label=im['heading']+' · '+im['kind']
  if im['kind']=='image':
   url=urljoin('/book/chapters/'+slug+'.html',src);body+=f'<figure class="asset"><a href="{url}"><img loading="lazy" src="{url}" alt="{E(label)}"></a><figcaption>{E(label)}</figcaption></figure>'
  elif im['kind']=='inline-svg':
   f=f'source-inline-{a["chapter"]:02d}-{idx}.svg';(O/'references').mkdir(exist_ok=True)
   exported=inline[idx].replace('viewbox=','viewBox=')
   if 'xmlns=' not in exported.split('>',1)[0]:exported=exported.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ',1)
   (O/'references'/f).write_text(exported,encoding='utf-8');idx+=1;body+=f'<figure class="asset"><img src="/references/{f}" alt="{E(src)}"><figcaption>{E(label)} · {E(src)} · 独立导出仅补XML命名空间与viewBox大小写，原页不改</figcaption></figure>'
  else:body+=f'<p><a href="/book/chapters/{slug}.html">{E(label)}：{E(src)}（原交互保留）</a></p>'
  ml.append('- '+label+'：'+src)
 if a['source_chart_placeholders']:ml.append('- 源母稿数值图占位：'+','.join(a['source_chart_placeholders'])+'；核对实际阅读页内嵌图，未当作缺图。')
 body+='</section>';ml.append('')
body+='<section><h2>工程图的具体处理</h2><p>3章分布叠图、4章模拟、11章四格曲线、13章奇偶叠图、14章参数曲线、16章冻结轨迹、20章有限家谱、22章权重柱图、24章双路径、25章插值误差：本轮全部保留。E16/E20补不同机制；E24增加显式时钟。其余重做提案仍待后续，不自动执行。</p></section>'
ml+=['## 不执行的批量替换','','工程/混合布局可改进的位置包括3、4、11、13、14、16、20、22、24、25章。全部原图保留。E16不是冻结图的同义重画，E20不是再造一棵模拟家谱，E24保留旧图并增加显式时钟候选。第19、21、23、26章有真实解释骨架，不因坐标存在就删掉。']
(O/'existing-visuals.md').write_text('\n'.join(ml),encoding='utf-8',newline='\n');(P/'existing.html').write_text(page('现有视觉内容',body),encoding='utf-8')
refs='<nav><a href="/">本批总览</a></nav><h1>设计参照与保护对象</h1><p>参照清楚的映射、可见的条件概率变化和数学操作；不统一套成公式说明卡。P03/P04只读参照，不修改其章节或图稿。</p>'
for name,label in [('dice-mapping-desktop.jpg','骰子映射：结果被函数合并'),('dependence-0.jpg','相同边缘、独立联合律'),('dependence-1.jpg','相同边缘、完全正相关'),('dependence-2.jpg','相同边缘、完全负相关'),('projection.jpg','条件期望投影'),('slice.jpg','密度切片归一化'),('P03-approved.jpg','已采用Palm抽样机制'),('P04-approved.jpg','已采用游程商树映射')]:refs+=shot(name,label,reference=True)
(P/'references.html').write_text(page('优秀解释图参照',refs),encoding='utf-8')
print('Five comparisons, 40 chapter judgments, priority and existing-art gallery built.')
