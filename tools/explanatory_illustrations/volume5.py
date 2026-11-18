"""Four structural explanations selected from the existing volume-V audit."""
from .pilot_shapes import Svg,tr,tile,E,INK,TEAL,WARM,GRAY,PALE,RULE,wrapped
import math
META={
'V31':('31-ito-integral','31.10','两种括号，是两种读取','Two brackets, two ways to read'),
'V33':('33-brownian-relations','33.2','记录没动，概率重新分配','Same records, different weights'),
'V34':('34-semimartingales','34.14','一跳不能只留下二阶近似','A jump is more than its quadratic approximation'),
'V37':('37-local-time','37.4','一点没有时间，密度却可以非零','Zero time at a point, nonzero density')}
BASE='/assets/visuals/explanatory-v1/'
def image(name,alt,attr=''):
 return f'<img class="ex-svg" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def buttons(attr,items,active):
 return '<div class="v5-controls" role="group">'+''.join(f'<button type="button" {attr}="{key}" aria-pressed="{str(key==active).lower()}">{label}</button>' for key,label in items)+'</div>'
def bracket_scene(lang,mode,t=3):
 s=Svg(360,280);s.text(180,26,'M',25,anchor='middle');s.line(180,36,180,51,TEAL);s.line(90,51,270,51,TEAL);s.arrow(90,51,90,78);s.arrow(270,51,270,78)
 s.text(90,100,tr(lang,'平方增量累积','Square increments'),18,anchor='middle');s.text(270,100,tr(lang,'可预测补偿','Predictable clock'),18,anchor='middle')
 actual=t if mode=='continuous' else sum(x<=t for x in [.6,2.2])
 for x,label,value in [(90,'[M]',actual),(270,'⟨M⟩',t)]:
  s.circle(x,153,40,TEAL,'white');s.text(x,165,str(value),40,anchor='middle');s.text(x,218,label,23,anchor='middle')
 s.text(180,165,'=' if actual==t else '≠',25,WARM,anchor='middle')
 s.line(26,257,334,257,GRAY,1.2)
 for x in [0,1,2,3]:
  p=26+x*102.5;s.line(p,251,p,262,GRAY,1);s.text(p,279,str(x),15,GRAY,anchor='middle')
 if mode=='jump':
  for arrival in [.6,2.2]:
   x=26+arrival*102.5;s.circle(x,257,5,WARM if arrival<=t else GRAY,'white' if arrival>t else None)
 cursor=26+t*102.5;s.line(cursor,241,cursor,267,TEAL,2)
 return s
def v31(lang):
 for mode in ['continuous','jump']:
  for t in [1,2,3]:bracket_scene(lang,mode,t).save(f'V31-{lang}-{mode}-{t}.svg','Path bracket and predictable bracket')
 body='<p class="v5-intro">'+tr(lang,'一个是已经发生的平方变化，一个是相对于信息流的可预测补偿。连续时汇合，有跳时未必。','One reads realized quadratic variation; the other reads its predictable compensation. Continuity makes them agree; jumps need not.')+'</p>'
 body+=buttons('data-bracket-mode', [('continuous',tr(lang,'连续：Brownian','Continuous: Brownian')),('jump',tr(lang,'有跳：Poisson补偿鞅','Jumps: compensated Poisson'))],'jump')
 body+='<div class="v5-scene">'+image(f'V31-{lang}-jump-3.svg',tr(lang,'同一终点，路径计数2与可预测时钟3','At one endpoint: realized count 2, predictable clock 3'),'data-bracket-scene')+'</div>'
 body+=buttons('data-bracket-time',[(str(i),f't = {i}') for i in [1,2,3]],'3')
 body+='<p class="v5-reading" data-bracket-reading>'+tr(lang,'λ=1，示意到达时刻0.6、2.2。在t=3，已经跳了2次，事前时钟是3。','λ=1; illustrative arrivals at 0.6 and 2.2. At t=3 there have been 2 jumps, while the predictable clock reads 3.')+'</p>'
 condition=tr(lang,'连续模型M=B，严格有[B]ₜ=⟨B⟩ₜ=t；一般[M]=⟨M⟩限于本章已证的连续局部鞅。跳跃模型M=N−t，N为率1的Poisson过程：[M]=N，⟨M⟩=t。图中到达记录只是确定性示意，不证明这些定理；“可预测”不是预言实际跳数。一般分割的收敛模式及局部化条件以正文为准。','For M=B, [B]ₜ=⟨B⟩ₜ=t. The general equality in this chapter applies to continuous local martingales. For M=N−t with a rate-one Poisson N, [M]=N and ⟨M⟩=t. The arrival record is illustrative, not a proof; predictable does not mean foretelling the realized count. Partition convergence and localization retain the text’s hypotheses.')
 return body,condition,[bracket_scene(lang,'continuous'),bracket_scene(lang,'jump')]

def weight_scene(lang,p):
 s=Svg(400,290);qs=[p*p,p*(1-p),(1-p)*p,(1-p)**2];labels=['++','+−','−+','−−']
 s.text(10,103,'P',22);s.text(10,222,'Q',22)
 for j,(lab,q) in enumerate(zip(labels,qs)):
  x=67+j*91;s.text(x,29,lab,21,anchor='middle');s.line(x,43,x,78,RULE,1);s.line(x,130,x,183,RULE,1)
  s.circle(x,104,18,TEAL,PALE);s.text(x,153,'1/4',18,anchor='middle')
  s.circle(x,220,36*math.sqrt(q),WARM,'#f1e7df');num=round(q*16);s.text(x,278,str(num)+'/16' if p!=.5 else '1/4',18,WARM,anchor='middle')
 return s
def v33(lang):
 for p,key in [(.25,'25'),(.5,'50'),(.75,'75')]:weight_scene(lang,p).save(f'V33-{lang}-{key}.svg','Same four records with different probability weights')
 body='<p class="v5-intro">'+tr(lang,'先看一个有限模型：两次±1记录不变，圆的面积随它的概率变化。','Start with a finite model: the two-step ±1 records stay fixed; circle area follows probability.')+'</p><div class="v5-scene">'+image(f'V33-{lang}-75.svg',tr(lang,'四条相同记录，在P下等权，在Q下为9、3、3、1份','The same four records: equal P weights, Q weights 9,3,3,1'),'data-weight-scene')+'</div>'
 body+=buttons('data-weight',[(key,'θ = '+lab) for key,lab in [('25','1/4'),('50','1/2'),('75','3/4')]],'75')
 body+='<p class="v5-reading" data-weight-reading>'+tr(lang,'Q下每一步向上的概率为3/4；四条记录的总概率仍是1。','Under Q, each step is up with probability 3/4. The four record probabilities still sum to 1.')+'</p>'
 condition=tr(lang,'图是有限类比，不是Brownian路径模拟。P给四条两步记录各1/4；Qθ给单步向上概率θ，两步独立。Zθ=Qθ/P，所以E_P Zθ=1；圆面积按概率、半径按概率平方根缩放。改变的是权重，不是已有记录。Brownian的有限时间换测度须另证随机指数为均值1真鞅；正局部鞅不自动是密度。此图不替代Girsanov证明，也不主张无限时间等价。','This finite analogy is not a Brownian simulation. P gives each two-step record probability 1/4; under Qθ the steps are independent with up probability θ. Zθ=Qθ/P and E_P Zθ=1. Circle area, not radius, is proportional to probability. Only weights change. Brownian change of measure on a finite horizon separately requires a true density martingale of mean 1; a positive local martingale is insufficient. This is neither a Girsanov proof nor a claim of infinite-horizon equivalence.')
 return body,condition,[weight_scene(lang,.75)]

def jump_scene(lang,stage=2):
 s=Svg(360,280)
 pts=[(40+100*z,235-8*((1+z)**3-1)) for z in [i/50 for i in range(101)]]
 s.nodes.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.2f} {y:.2f}' for i,(x,y) in enumerate(pts)) +f'" fill="none" stroke="{TEAL}" stroke-width="2.5"/>')
 s.line(40,235,240,187,GRAY,1.5);s.text(112,237,tr(lang,'切线','Tangent'),17,GRAY)
 for lo,hi,c,lab in [(235,187,TEAL,'6'),(187,91,WARM,'12'),(91,27,'#7257a4','8')]:
  s.rect(281,hi,17,lo-hi,PALE if c==TEAL else ('#f1e7df' if c==WARM else '#eee8f4'),c);s.text(315,(lo+hi)/2+6,lab,20,c,anchor='middle');s.line(244,hi,276,hi,RULE,1)
 s.circle(40,235,5,TEAL);s.circle(240,27,6,TEAL,'white');s.text(243,19,'f(3)=27',17)
 y=[187,91,27][stage];s.line(40,235,240,y,WARM,2,'5 4');s.circle(240,y,6,WARM)
 s.arrow(40,261,240,261,GRAY);s.text(40,251,'x=1',17);s.text(240,251,'3',17,anchor='middle')
 return s
def v34(lang):
 for k in range(3):jump_scene(lang,k).save(f'V34-{lang}-{k}.svg','Cubic function with finite jump and tangent correction')
 body='<p class="v5-intro">'+tr(lang,'f(x)=x³，一次从1跳到3。只留一阶、再加二阶、保留完整变化，得到三份不同的增量。','For f(x)=x³, jump from 1 to 3. The linear term, the quadratic approximation and the full change give different increments.')+'</p>'
 body+='<div class="v5-scene">'+image(f'V34-{lang}-2.svg',tr(lang,'立方函数的完整增量26分成6、12、8','The full cubic increment 26 splits into 6,12,8'),'data-jump-scene')+'</div>'
 body+=buttons('data-jump-stage',[(str(i),lab) for i,lab in enumerate(tr(lang,['一阶：6','到二阶：18','完整：26'],['Linear: 6','Quadratic: 18','Full: 26']))],'2')
 body+='<p class="v5-reading" data-jump-reading>'+tr(lang,'完整跳跃26 = 一阶6 + 二阶12 + 其余8。跳跃修正是后两项之和20。','Full jump 26 = linear 6 + quadratic 12 + residual 8. The jump correction is the last two terms together: 20.')+'</p>'
 condition=tr(lang,'图画的是f的几何，不是时间样本路径；X跳过中间状态，不能沿图中的曲线逐点经过。以x=1、z=2计：f′(1)z=6，f″(1)z²/2=12，其余z³=8。Itô跳跃公式保留f(x+z)−f(x)−f′(x)z=20，不是只保留8，也不能把12作为一般跳跃的全部修正。连续二阶变差项与完整跳跃项的分工依正文定理。','This is the geometry of f, not a time sample path: X jumps over the intermediate states. At x=1,z=2, f′(1)z=6, f″(1)z²/2=12 and the remaining z³=8. The Itô jump correction is f(x+z)−f(x)−f′(x)z=20, not just 8; the quadratic term 12 alone is also insufficient. The text’s theorem distinguishes continuous quadratic variation from the full jump term.')
 return body,condition,[jump_scene(lang)]

def occupation_scenes(lang,eps):
 s=Svg(320,220);s.line(18,170,302,170,GRAY,1)
 s.nodes.append(f'<path d="M20 170 L160 50 L300 170" fill="none" stroke="{TEAL}" stroke-width="2"/>')
 if eps:
  a,b=160-140*eps,160+140*eps;y=170-120*(1-eps)
  s.nodes.append(f'<path d="M{a} 170 L{a} {y} L160 50 L{b} {y} L{b} 170 Z" fill="{PALE}" stroke="{TEAL}" stroke-width="1"/>')
  for x in [a,b]:s.line(x,170,x,193,TEAL,1)
  s.line(a,187,b,187,TEAL,1.4);s.text(160,216,'2ε',20,anchor='middle')
 else:s.line(160,50,160,170,WARM,2);s.text(160,211,tr(lang,'单点：宽度0','One point: width 0'),18,WARM,anchor='middle')
 s.circle(160,50,4,TEAL);s.text(160,29,'ℓ(0)=1',19,anchor='middle')
 t=Svg(320,220);t.line(64,170,256,170,GRAY,1);t.line(70,50,250,50,GRAY,1.2,'4 4');t.text(268,56,'1',18,GRAY)
 if eps:
  mean=1-eps/2;top=170-120*mean;t.rect(70,top,180,170-top,PALE,TEAL);t.text(160,(top+170)/2+6,tr(lang,'平均高度','Average height'),18,anchor='middle')
 else:
  t.rect(70,75,180,95,'white',GRAY);t.line(85,90,235,155,WARM,1.5);t.text(160,213,tr(lang,'0/0不能定义密度','0/0 is not a density'),18,WARM,anchor='middle')
 return s,t
def v37(lang):
 options=[('half',.5),('quarter',.25),('eighth',.125),('point',0)]
 for key,eps in options:
  for name,sv in zip(['band','average'],occupation_scenes(lang,eps)):sv.save(f'V37-{lang}-{key}-{name}.svg','Occupation band and normalized density')
 body='<p class="v5-intro">'+tr(lang,'先用一份示意连续密度，看清“总量÷带宽”。这不是一条Brownian样本的数值图。','Use a schematic continuous density to see “mass ÷ width”. This is not numerical data from a Brownian sample.')+'</p>'
 body+='<div class="v5-occupation">'+image(f'V37-{lang}-quarter-band.svg',tr(lang,'窄带里的密度面积','Density area inside the narrow band'),'data-occupation-band')+'<div class="v5-divide">÷ 2ε <span>→</span></div>'+image(f'V37-{lang}-quarter-average.svg',tr(lang,'除以带宽后得到平均密度','Dividing by width gives average density'),'data-occupation-average')+'</div>'
 body+=buttons('data-occupation', [('half','ε=1/2'),('quarter','ε=1/4'),('eighth','ε=1/8'),('point',tr(lang,'只取单点','One point'))],'quarter')
 body+='<p class="v5-reading" data-occupation-reading>'+tr(lang,'窄带总量7/16 ÷ 带宽1/2 = 平均密度7/8；不是单点的时间长度。','Band mass 7/16 ÷ width 1/2 = average density 7/8, not the time spent at one point.')+'</p>'
 condition=tr(lang,'示意剖面ℓ(a)=(1−|a|)₊，不是声称Brownian局部时具有这条确定形状。其带内面积2ε−ε²除以2ε为1−ε/2，趋于ℓ(0)=1；单点面积为0，不能用0/0定义密度。正文实际证明Brownian占用公式∫₀ᵗ1{|Bₛ−a|<ε}ds=∫ₐ₋εᵃ₊εLₜʸdy及联合连续性，故窄带平均趋Lₜᵃ。一般连续半鞅须以d[M]而非一概用dt计量。图不代替局部时存在、版本与收敛证明。','The schematic profile ℓ(a)=(1−|a|)₊ is not asserted to be the local time of a Brownian sample. Band area 2ε−ε² divided by 2ε is 1−ε/2, tending to ℓ(0)=1. A point has zero area; 0/0 cannot define density. The text proves the Brownian occupation identity and joint continuity, which justify narrow-band averages tending to Lₜᵃ. General continuous semimartingales use d[M], not automatically dt. This diagram does not prove existence, versions or convergence of local time.')
 return body,condition,list(occupation_scenes(lang,.25))

FUNCS={'V31':v31,'V33':v33,'V34':v34,'V37':v37}
def figure(code,lang):
 body,condition,panes=FUNCS[code](lang);title=META[code][2 if lang=='zh' else 3]
 html=f'<figure class="explain-figure" id="visual-{code}" data-explain="{code}" lang="{lang}"><header><span class="ex-kicker">{code}</span><h3>{E(title)}</h3></header>{body}<figcaption id="visual-{code}-end">{E(condition)}</figcaption><nav class="ex-downloads"><a href="{BASE}{code}.{lang}.svg">{tr(lang,"静态矢量版","Static SVG")}</a><a href="/print/{code}.{lang}.html">{tr(lang,"打印页","Print view")}</a></nav></figure>'
 static(code,lang,title,condition,panes)
 return html,condition
def static(code,lang,title,condition,panes):
 s=Svg(900,900);s.rect(0,0,900,900,'white');s.text(30,43,title,27,weight='bold');s.line(30,64,870,64,RULE,1)
 if code=='V31':
  for j,pane in enumerate(panes):
   x=30+j*440;s.text(x+195,109,tr(lang,['连续：两者都是t','有跳：2不等于3'][j],['Continuous: both read t','Jumps: 2 is not 3'][j]),22,anchor='middle');s.nodes.append(f'<svg x="{x}" y="132" width="390" height="303" viewBox="0 0 360 280">{pane.fragment()}</svg>')
  bottom=470
 elif code=='V33':
  s.nodes.append(f'<svg x="125" y="90" width="650" height="471" viewBox="0 0 400 290">{panes[0].fragment()}</svg>');s.text(450,604,tr(lang,'θ=3/4：同样的记录，归一化后的不同权重。','θ=3/4: identical records, different normalized weights.'),23,anchor='middle');bottom=640
 elif code=='V34':
  s.nodes.append(f'<svg x="40" y="100" width="560" height="436" viewBox="0 0 360 280">{panes[0].fragment()}</svg>')
  for j,label in enumerate(tr(lang,['一阶：6','二阶：12','其余：8','完整增量：26','跳跃修正：20'],['Linear: 6','Quadratic: 12','Residual: 8','Full increment: 26','Jump correction: 20'])):s.text(640,160+75*j,label,23)
  bottom=565
 else:
  for j,pane in enumerate(panes):
   x=25+490*j;s.nodes.append(f'<svg x="{x}" y="130" width="360" height="248" viewBox="0 0 320 220">{pane.fragment()}</svg>')
  s.text(450,251,'÷2ε →',25,anchor='middle');s.text(450,105,tr(lang,'窄带总量，换算为每单位位置的密度','Band mass becomes density per unit position'),24,anchor='middle');s.text(450,442,'(7/16) ÷ (1/2) = 7/8',26,anchor='middle');bottom=480
 lines=wrap_caption(condition,lang);s.line(30,bottom,870,bottom,RULE,1)
 for j,line in enumerate(lines):s.text(30,bottom+32+j*24,line,17,GRAY)
 s.h=bottom+64+24*len(lines);s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';s.save(f'{code}.{lang}.svg',title)


def wrap_caption(text,lang):
 if lang=='en':return wrapped(text,80,lang)
 import re
 lines=[];line='';n=0
 for token in re.findall(r'[\x21-\x7e\u00a0-\u03ff\u2070-\u209f]+|.',text):
  w=sum(1 if ord(c)>255 else .52 for c in token)
  if n+w>48 and line:lines.append(line);line='';n=0
  line+=token;n+=w
 if line:lines.append(line)
 return lines
