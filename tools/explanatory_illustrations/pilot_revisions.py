"""Result-first and stateful explanatory artwork, restricted to P01/P02/P05."""
def install(api):
 globals().update({k:api[k] for k in ['Svg','tr','tile','note','card','E','INK','TEAL','WARM','GRAY','PALE','RULE']})
 return {'P01':p01,'P02':p02,'P05':p05},print_new

def choice_scene(k):
 s=Svg(360,220)
 s.line(50,45,310,45,GRAY,1.3)
 for x,v,active in [(50,'1',k!=1),(310,'3',k!=0)]:
  s.circle(x,45,8,TEAL if active else GRAY,None if active else 'white');s.text(x,24,v,23,anchor='middle')
 if k==2:
  s.line(50,60,50,75,TEAL);s.line(50,75,310,75,TEAL);s.line(310,75,310,60,TEAL);s.arrow(180,75,180,113)
 else:
  x=50 if k==0 else 310
  s.nodes.append(f'<path d="M{x} 60 Q{x} 108 163 121" fill="none" stroke="{TEAL}" stroke-width="2"/>') if k==0 else s.nodes.append(f'<path d="M{x} 60 Q{x} 108 197 121" fill="none" stroke="{TEAL}" stroke-width="2"/>')
 s.circle(180,147,30,TEAL,'white');s.text(180,157,str([1,3,2][k]),30,anchor='middle')
 return s

def p01(lang):
 panes=[]
 labels=tr(lang,['左端取值','右端取值','对称端点'],['Left','Right','Symmetric'])
 for k in range(3):
  s=choice_scene(k);s.save(f'P01-{lang}-{k}.svg',labels[k]);panes.append((labels[k],s))
 buttons=''.join(f'<button type="button" data-rule="{k}" aria-pressed="{str(k==0).lower()}"><strong>{result}</strong><span>{labels[k]}</span></button>' for k,result in enumerate([2,6,4]))
 body=f'<p class="r3-intro">{tr(lang,"同一格从1变到3。增量都是2，结果为什么不同？","The same step goes from 1 to 3. Its increment is 2. Why three answers?")}</p><div class="r3-results" role="group" aria-label="{tr(lang,"选择取值规则","Choose a sampling rule")}">{buttons}</div>'
 body+=f'<p class="r3-hint">{tr(lang,"点一个结果，看看它取了哪里。","Choose an answer to see which value it uses.")}</p><div class="r3-choice-scene">{tile(f"P01-{lang}-0.svg",tr(lang,"取左端值1","Use the left value 1")).replace("class=\"ex-svg\"","class=\"ex-svg\" data-rule-scene")}</div>'
 body+=f'<div class="r3-choice-caption" aria-live="polite"><span data-rule-words>{tr(lang,"先取左端的1","Take the left value, 1")}</span><strong data-rule-calc>1 × 2 = 2</strong></div>'
 conditions=tr(lang,'图为确定性单格代数，不是Brownian路径面积。逐格右端−左端=(ΔX)²，对称−左端=(ΔX)²/2。连续半鞅在确定分割网格趋零时，对称端点和以ucp收敛：∫X∘dX=∫X dX+[X]/2；Brownian情形[B]ₜ=t。一般H、X用[H,X]。右端取值一般用到了本格未来；时间中点值未必等于端点值平均。','This is one deterministic cell, not Brownian area. Per cell, right minus left is (ΔX)² and symmetric minus left is (ΔX)²/2. For a continuous semimartingale, deterministic partitions with vanishing mesh give ucp convergence: ∫X∘dX=∫X dX+[X]/2; for Brownian motion [B]ₜ=t. Use [H,X] for general H,X. Right values generally use this cell’s future. A time midpoint need not equal the mean of endpoint values.')
 return body,conditions,panes

def environment_scene(lang,mode):
 s=Svg(360,305);color=WARM if mode=='two' else TEAL
 s.rect(123,6,114,48,PALE,color)
 root={'mixed':'ν ?','one':'ν₁ : R=1','two':'ν₂ : R=2'}[mode]
 s.text(180,37,root,23,color,anchor='middle')
 s.line(180,54,180,74,color);s.line(53,74,307,74,color)
 for j,x in enumerate([53,180,307]):
  s.arrow(x,74,x,107,color);s.text(x,130,['X₁','X₂','X₃'][j],21,anchor='middle')
  s.nodes.append(f'<path d="M{x-45} 148 L{x-40} 228 Q{x} 253 {x+40} 228 L{x+45} 148" fill="none" stroke="{color}" stroke-width="1.5"/>')
  if mode=='mixed':values=[(-20,170,'−1'),(20,170,'+1'),(-20,211,'−2'),(20,211,'+2')]
  else:
   R='1' if mode=='one' else '2';values=[(-20,191,'−'+R),(20,191,'+'+R)]
  for dx,y,v in values:
   c=WARM if '2' in v else TEAL;s.circle(x+dx,y,16,c,'white');s.text(x+dx,y+6,v,17,c,anchor='middle')
  s.text(x,280,tr(lang,'各1/4' if mode=='mixed' else '各1/2','¼ each' if mode=='mixed' else '½ each'),18,anchor='middle')
 return s

def p02(lang):
 labels=tr(lang,['环境未给出','给定ν₁','给定ν₂'],['ν hidden','Given ν₁','Given ν₂']);panes=[]
 for key,lab in zip(['mixed','one','two'],labels):
  s=environment_scene(lang,key);s.save(f'P02-{lang}-{key}.svg',lab);panes.append((lab,s))
 body=f'<p class="r3-intro">{tr(lang,"共同的R只选一次。给定它后，每次独立抽取，允许重复取同一值；碗中取值不被移走。","Choose R once. Given R, draw independently each time, with replacement: possible values are not removed.")}</p>'
 body+='<div class="r3-env-controls" role="group">'+''.join(f'<button type="button" data-env="{key}" aria-pressed="{str(key=="mixed").lower()}">{lab}</button>' for key,lab in zip(['mixed','one','two'],labels))+'</div>'
 body+='<div class="r3-environment">'+tile(f'P02-{lang}-mixed.svg',tr(lang,'共同环境未知；各观测的边缘有四个等可能值','Unknown shared environment; each marginal has four equally likely values')).replace('class="ex-svg"','class="ex-svg" data-env-scene')+'</div>'
 body+=f'<p class="r3-env-law" data-env-law>{tr(lang,"R=1或2各半；碗中显示单次观测的可能值与边缘概率。","R=1 or 2, each with probability ½. Bowls show possible values and one-draw marginal probabilities.")}</p>'
 body+=f'<div class="r3-prediction"><div><span>{tr(lang,"下一次 |X₂|=1","Next: |X₂|=1")}</span><strong data-prob-before>½</strong></div><span class="r3-pred-arrow">→</span><div><span data-after-label>{tr(lang,"看到 |X₁|=1 后","After seeing |X₁|=1")}</span><strong data-prob-after>1</strong></div></div>'
 body+=f'<p class="r3-state-note" data-p02-output aria-live="polite">{tr(lang,"环境未知时，一次观察能揭示幅度，改变下一次预测。","With ν hidden, one observation reveals the magnitude and changes the next prediction.")}</p>'
 conditions=tr(lang,'R取1、2各半，ν=(δ₋R+δR)/2。给定ν，各次iid，每次独立重新抽取，不是无放回；未给ν时，四个值各1/4只是边缘律，不表示无条件独立。例中Cov(X₁,X₂)=0仍依赖。给定ν₂时不可能看到|X₁|=1，图中的“—”不是条件概率0。一般de Finetti表示仍需无限交换与标准Borel条件，有限交换性不够。','P(R=1)=P(R=2)=½ and ν=(δ₋R+δR)/2. Draws are iid given ν: fresh independent draws, not sampling without replacement. Four values of probability ¼ in the hidden state describe marginals, not unconditional independence; here Cov(X₁,X₂)=0 despite dependence. Given ν₂, |X₁|=1 is impossible: “—” is not a conditional probability of zero. The general de Finetti theorem needs infinite exchangeability and standard Borel assumptions, not finite exchangeability alone.')
 return body,conditions,panes

def branch_scene(lang,eps=.05,interactive=False):
 s=Svg(400,310)
 old='M245 135 Q292 75 355 85';new='M245 135 C205 195 130 230 48 195'
 # Ribbons are offset from the fixed geometry: width represents density per unit tree length.
 s.nodes.append(f'<path d="{old}" transform="translate(0,-11)" fill="none" stroke="{TEAL}" stroke-opacity=".30" stroke-width="{24*(1-eps)}" stroke-linecap="round" data-density="old"/>')
 s.nodes.append(f'<path d="{new}" transform="translate(0,-11)" fill="none" stroke="{WARM}" stroke-opacity=".65" stroke-width="{24*eps/2}" stroke-linecap="round" data-density="new"/>')
 s.nodes.append(f'<path d="{old}" fill="none" stroke="{INK}" stroke-width="2" data-geometry="old"/>')
 s.nodes.append(f'<path d="{new}" fill="none" stroke="{INK}" stroke-width="2" data-geometry="new"/>')
 s.circle(245,135,5,INK);s.text(258,161,'ρ = 0',18)
 s.text(322,46,tr(lang,'原枝 · 长1','Old · length 1'),18,anchor='middle')
 s.text(105,146,tr(lang,'长枝 · 长2','Long · length 2'),19,WARM,anchor='middle')
 s.nodes.append(f'<text x="105" y="265" font-size="21" text-anchor="middle" fill="{WARM}" data-mass-label="new">{E(tr(lang,"质量 ","mass "))}{eps:.0%}</text>')
 s.nodes.append(f'<text x="323" y="116" font-size="19" text-anchor="middle" fill="{TEAL}" data-mass-label="old">{1-eps:.0%}</text>')
 s.circle(355,85,3,INK);s.circle(48,195,3,INK)
 s.nodes.append('<g data-samples=""/>')
 return s

def p05(lang):
 s=branch_scene(lang);s.save(f'P05-{lang}-branch.svg',tr(lang,'长枝保留，质量带表示密度','The long branch stays; ribbons show mass density'))
 # Inline SVG is necessary: the controls update ribbons and sampled positions in the artwork itself.
 inline=s.document(tr(lang,'几何固定，质量密度可变的树','A fixed tree with adjustable mass density')).replace('<svg ','<svg class="r3-branch-svg" ',1)
 body=f'<p class="r3-intro">{tr(lang,"长枝一直长2。改变的是它承载多少质量，而不是它有多长。","The long branch always has length 2. Its mass changes, its length does not.")}</p><div class="r3-branch-art">{inline}</div>'
 body+=f'<p class="r3-legend r3-legend-keys"><span><i class="geometry-key" aria-hidden="true"></i>{tr(lang,"固定几何细线","Fixed geometry")}</span><span><i class="density-key" aria-hidden="true"></i>{tr(lang,"质量密度宽带（不是空间厚度）","Mass-density ribbon (not spatial thickness)")}</span></p>'
 body+=f'<div class="r3-branch-controls"><label for="eps-{lang}">{tr(lang,"长枝质量","Mass on the long branch")} <output data-eps-label>5%</output><input id="eps-{lang}" data-epsilon type="range" min="0.02" max="0.60" step="0.01" value="0.05"></label><button type="button" data-resample>{tr(lang,"抽取5个点","Draw 5 points")}</button><output data-sample-result aria-live="polite">{tr(lang,"从当前质量分布取样，看看是否落在长枝。","Sample the current mass distribution. Will any point reach the long branch?")}</output></div>'
 body+=f'<p class="r3-miss"><strong data-miss-prob>77.4%</strong><span>{tr(lang,"五次独立抽样，全都没落在长枝的概率","Chance that all five independent samples miss the long branch")}</span></p>'
 body+=f'<details class="r3-second-layer"><summary>{tr(lang,"为什么GH仍能看见，而GP可以忽略？","Why can GH see it while GP may miss it?")}</summary><div class="ex-grid three ex-metrics">'+card('GH',tr(lang,'直径从1变3','Diameter: 1 → 3'),'d<sub>GH</sub> ≥ 1')+card('GP',tr(lang,'匹配原枝上的1−ε质量','Match mass 1−ε on the old branch'),'d<sup>r</sup><sub>GP</sub> ≤ ε')+card('GHP',tr(lang,'同一嵌入保留几何、根、质量','One embedding: geometry, root, mass'),'d<sup>r</sup><sub>GHP</sub> ≥ 1')+'</div></details>'
 conditions=tr(lang,'X只含原枝[0,1]，Y含两枝，内在度量等同[−2,1]，根均为0。μ_ε=(1−ε)Unif[0,1]+εUnif[−2,0]，0<ε<1；拖动前后沿细线的距离不变；宽带不属于空间本身。图示质量连续，宽带不是几何厚度或原子。带宽按密度1−ε与ε/2变化；曲线仅示意内在树距离。五次均未落长枝的概率为(1−ε)⁵；一次模拟不能证明此式。抽样按钮使用新的有限精度均匀数作模拟；随后拖动滑块复用这组数作耦合演示，不表示重新独立抽样。上标r表示带根；GP按支撑加根识别，GHP采用同一嵌入下的max规范。','X is the old branch [0,1]; Y has both branches and is intrinsically [−2,1], with root 0. μ_ε=(1−ε)Unif[0,1]+εUnif[−2,0], 0<ε<1. Distances along the fine line stay fixed. The ribbon is not part of the metric space; mass is continuous, not atomic. Their widths follow densities 1−ε and ε/2; curves illustrate intrinsic tree distances. All five iid samples miss with probability (1−ε)⁵; simulation does not prove it. Draw simulates with fresh finite-precision uniform variates. Moving the slider then reuses those uniforms as a coupling, not a new independent sample. Superscript r denotes rooted distance; GP identifies support plus root, while GHP uses one common embedding and the max convention.')
 return body,conditions,[(tr(lang,'几何固定','Fixed geometry'),s)]

def print_new(code,lang,condition,panes):
 titles={'P01':tr(lang,'同一格，三种结果','One increment. Three results.'),'P02':tr(lang,'共同的是分布，不是每次的答案','A shared law, not shared outcomes'),'P05':tr(lang,'长枝仍在，样本未必看到','The branch stays. Samples may miss it.')}
 S=Svg(900,900);S.rect(0,0,900,900,'white');S.text(30,43,titles[code],28,weight='bold');S.line(30,62,870,62,RULE,1)
 if code=='P05':S.text(450,87,tr(lang,'细线不变；宽带是密度，不是空间厚度。','The fine line stays; the ribbon is density, not spatial thickness.'),18,anchor='middle')
 if code=='P01':
  for j,(lab,sv) in enumerate(panes):
   x=30+290*j;S.text(x+130,144,str([2,6,4][j]),70,TEAL,anchor='middle');S.text(x+130,185,lab,23,anchor='middle');S.nodes.append(f'<svg x="{x}" y="215" width="260" height="159" viewBox="0 0 360 220">{sv.fragment()}</svg>')
  S.text(450,429,tr(lang,'增量同为2，所取的值分别为1、3、2。','The increment is 2; the chosen values are 1, 3 and 2.'),22,anchor='middle');bottom=475
 elif code=='P02':
  # One unchanged shared-input mechanism, with a compact static state key alongside it.
  S.nodes.append(f'<svg x="20" y="90" width="390" height="330" viewBox="0 0 360 305">{panes[0][1].fragment()}</svg>')
  for j,(head,support,prob) in enumerate([(tr(lang,'未知ν','ν hidden'),'±1, ±2',tr(lang,'各1/4','¼ each')),(tr(lang,'给定ν₁','Given ν₁'),'−1, +1',tr(lang,'各1/2','½ each')),(tr(lang,'给定ν₂','Given ν₂'),'−2, +2',tr(lang,'各1/2','½ each'))]):
   y=135+j*104;S.text(460,y,head,22,weight='bold');S.text(460,y+33,support+'   '+prob,22)
  S.text(35,467,tr(lang,'未知ν：P(|X₂|=1)=1/2；看到|X₁|=1后变为1。','ν hidden: P(|X₂|=1)=½; after seeing |X₁|=1 it becomes 1.'),22);bottom=505
 else:
  for j,eps in enumerate([.05,.40]):
   x=20+440*j;sv=branch_scene(lang,eps);S.text(x+200,112,f'ε = {eps:.0%}',25,anchor='middle');S.nodes.append(f'<svg x="{x}" y="128" width="410" height="318" viewBox="0 0 400 310">{sv.fragment()}</svg>');S.text(x+205,467,tr(lang,'五点全未落长枝：','All five miss: ')+f'{(1-eps)**5:.1%}',21,anchor='middle')
  for x,name,tail in [(160,'GH',' ≥ 1'),(450,'GP',' ≤ ε'),(740,'GHP',' ≥ 1')]:
   sup='<tspan baseline-shift="super" font-size="15">r</tspan>' if name!='GH' else ''
   S.nodes.append(f'<text x="{x}" y="512" font-size="23" text-anchor="middle" fill="{INK}">d{sup}<tspan baseline-shift="sub" font-size="16">{name}</tspan>{tail}</text>')
  bottom=545
 S.line(30,bottom,870,bottom,RULE,1)
 # Full conditions remain in print; no interaction needed to understand the illustration.
 import textwrap
 if lang=='en':lines=textwrap.wrap(condition,80,break_long_words=False)
 else:
  lines=[];line='';n=0
  import re
  for c in re.findall(r'[A-Za-z][A-Za-z–-]*|.',condition):
   w=sum(1 if ord(ch)>255 else .52 for ch in c)
   if n+w>48:lines.append(line);line='';n=0
   line+=c;n+=w
  if line:lines.append(line)
 for j,line in enumerate(lines):S.text(30,bottom+31+j*23,line,17,GRAY)
 S.h=bottom+60+len(lines)*23;S.nodes[0]=f'<rect width="900" height="{S.h}" fill="white"/>'
 S.save(f'{code}.{lang}.svg',titles[code])
