"""Four selected conceptual models, plus two narrowly scoped accepted-art refinements."""
from .pilot_shapes import Svg,tr,E,INK,TEAL,WARM,GRAY,PALE,RULE
from .volume5 import buttons,wrap_caption
import math
BASE='/assets/visuals/explanatory-v2/'
META={
'V35':('35-sde-wellposedness','35.1','规则、唯一性、寿命不是一回事','A rule, uniqueness and lifetime are different claims'),
'V36':('36-scale-speed','36.14','边界有两个方向的问题','A boundary poses two directional questions'),
'V38':('38-feynman-kac','38.2','一段运动，两份累计','One stopped motion, two contributions'),
'V40':('40-stochastic-geometry','40.1','同样的角度，半径却不同','Same angle, different radius')}
def img(name,alt,attr=''):return f'<img class="ex-svg" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def v35_scene(lang,mode):
 s=Svg(360,270)
 if mode=='many':
  s.text(180,27,'x(0)=0',24,anchor='middle');s.text(180,64,tr(lang,'同一规则，三个合法答案','One rule, three valid answers'),19,anchor='middle')
  s.line(180,77,180,91,TEAL);s.line(55,91,305,91,TEAL)
  for x,value,a in [(55,'4','0'),(180,'1','1'),(305,'0','∞')]:
   s.arrow(x,91,x,111);s.circle(x,153,31,TEAL,'white');s.text(x,164,value,32,anchor='middle');s.text(x,211,'a = '+a,20,anchor='middle')
  s.text(180,256,tr(lang,'在同一时刻 t=2 读取','Read all three at the same time t=2'),18,anchor='middle')
 else:
  s.text(180,27,'x(0)=1',24,anchor='middle');s.text(180,64,tr(lang,'同一条解，四个时刻','One solution, four observation times'),19,anchor='middle')
  for j,(value,t) in enumerate([('1','0'),('2','1/2'),('4','3/4'),('8','7/8')]):
   x=43+90*j;s.circle(x,139,25,TEAL,'white');s.text(x,148,value,27,anchor='middle');s.text(x,190,'t='+t,16,anchor='middle')
   if j<3:s.arrow(x+29,139,x+61,139)
  s.line(350,103,350,209,WARM,2,'5 4');s.text(180,239,tr(lang,'时间间隔减半，寿命止于 ζ=1','Halving gaps; lifetime ζ=1'),18,WARM,anchor='middle')
 return s
def v35(lang):
 for mode in ['many','finite']:v35_scene(lang,mode).save(f'V35-{lang}-{mode}.svg','Nonuniqueness and finite lifetime are separate')
 body='<p class="v5-intro">'+tr(lang,'先把噪声设为0。一个规则没有规定何时出发；另一个规则虽然唯一，却不能持续全部时间。','Set noise to zero first. One rule leaves departure time free; another has a unique solution but only a finite lifetime.')+'</p>'
 body+=buttons('data-rule-model',[('many',tr(lang,'可有多解','Several solutions')),('finite',tr(lang,'唯一但有限寿命','Unique, finite lifetime'))],'many')
 body+='<p class="v5-model" data-rule-equation>'+tr(lang,'x′=2√|x|，从0出发','x′=2√|x|, starting at 0')+'</p><div class="v5-scene">'+img(f'V35-{lang}-many.svg',tr(lang,'同一初值下的三条延迟出发解','Same initial value, three delayed solutions'),'data-rule-model-scene')+'</div><p class="v5-reading" data-rule-model-reading>'+tr(lang,'a是等待时间：可以立即出发、等到1再出发，或永远停在0。','a is the waiting time: depart immediately, wait until 1, or remain at 0 forever.')+'</p>'
 condition=tr(lang,'两例都取σ=0，不是假造随机样本。第一例xᵃ(t)=(t−a)₊²，a∈[0,∞]，在出发处导数两侧均为0，确实满足同一积分方程；在t=2分别读到4、1、0。第二例x′=x²、x(0)=1，局部唯一解1/(1−t)仅在t<1成立；不能在爆炸后填一个有限值续成原方程的解。四个节点只是读数序列，横距不表示相等时长。图不承担一般强弱解、路径唯一性与分布唯一性的分类证明。','Both examples have σ=0, not simulated noise. In the first, xᵃ(t)=(t−a)₊², a∈[0,∞], has derivative 0 on both sides of departure and satisfies the same integral equation; at t=2 the displayed values are 4,1,0. In the second, x′=x² with x(0)=1 has the locally unique solution 1/(1−t) only for t<1. A finite value cannot extend it past explosion as a solution of that equation. The four nodes are observations, not an equally spaced time axis. General strong/weak and uniqueness notions remain the text’s responsibility.')
 return body,condition,[v35_scene(lang,'many'),v35_scene(lang,'finite')]

BOUNDARIES={'regular':(True,True),'exit':(True,False),'entrance':(False,True),'natural':(False,False)}
def boundary_scene(lang,kind):
 reach,enter=BOUNDARIES[kind];s=Svg(360,270);s.rect(22,51,33,185,'#f0f1eb');s.line(55,51,55,236,GRAY,1.4);s.line(55,140,333,140,GRAY,1)
 s.circle(55,140,6,INK);s.text(55,166,'0',18,anchor='middle');s.circle(255,140,6,TEAL);s.text(255,166,'x',18,anchor='middle')
 s.text(163,31,tr(lang,'内部 → 端点','Interior → boundary'),19,anchor='middle');s.text(163,262,tr(lang,'端点 → 内部','Boundary → interior'),19,anchor='middle')
 for ok,upper in [(reach,True),(enter,False)]:
  c=TEAL if ok else GRAY;d='M255 140 Q155 0 55 140' if upper else 'M55 140 Q155 280 255 140'
  s.nodes.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2"'+(' stroke-dasharray="5 4"' if not ok else '')+'/>')
  if ok:
   if upper:s.arrow(88,103,72,121,c)
   else:s.arrow(222,176,238,160,c)
  else:
   y=70 if upper else 210;s.line(147,y-8,163,y+8,WARM,2);s.line(147,y+8,163,y-8,WARM,2)
 return s
def boundary_model(lang,kind):
 return tr(lang,{'regular':'正则：Brownian在(0,1)的0端','exit':'出口：dZ=2√Z dW的0端','entrance':'入口：三维Bessel半径的0端','natural':'自然：dX=X dW的0端'}[kind],{'regular':'Regular: 0 for Brownian motion in (0,1)','exit':'Exit: 0 for dZ=2√Z dW','entrance':'Entrance: 0 for a three-dimensional Bessel radius','natural':'Natural: 0 for dX=X dW'}[kind])
def v36(lang):
 for kind in BOUNDARIES:boundary_scene(lang,kind).save(f'V36-{lang}-{kind}.svg','Two directional boundary tests')
 body='<p class="v5-intro">'+tr(lang,'从内部能否到达0，与能否从0即时进入内部，是两道不同的检验。','Reaching 0 from inside and starting at 0 to enter the interior are two different tests.')+'</p>'
 body+=buttons('data-boundary',[(k,tr(lang,z,e)) for k,z,e in [('regular','正则','Regular'),('exit','出口','Exit'),('entrance','入口','Entrance'),('natural','自然','Natural')]],'entrance')
 body+='<div class="v5-scene">'+img(f'V36-{lang}-entrance.svg',tr(lang,'不可从内部到达的边界，仍可有即时入口','An unreachable boundary can still admit entrance'),'data-boundary-scene')+'</div><p class="v5-model" data-boundary-model>'+boundary_model(lang,'entrance')+'</p><p class="v5-reading" data-boundary-reading>'+tr(lang,'从正位置到不了0，但从0可以立即进入正半轴。','From a positive radius, 0 cannot be hit; starting at 0, the process can enter positive radii immediately.')+'</p>'
 body+='<details class="v5-second-layer"><summary>'+tr(lang,'两份积分检验与边界规则','Integral tests and boundary rules')+'</summary><p data-boundary-tests>Σ = ∞，N &lt; ∞</p><p>'+tr(lang,'正则端点到达后的吸收、反射等规则仍须另选；分类不唯一指定延拓。','At a regular endpoint, absorption, reflection and other admissible rules still require a choice. Classification does not uniquely specify the extension.')+'</p></details>'
 condition=tr(lang,'端点0在状态区间闭包中；入口指扩展状态空间后连续即时进入内部，不是仅在0定义一个常值过程。Σ有限表示内部可达；对不可达端点，N有限给出本章已证的即时入口。四型为(Σ,N)：有限/有限、有限/无穷、无穷/有限、无穷/无穷。正则型表示允许选择相应边界规则，不保证任意既定延拓都会反射返回。出口或自然端也可能定义吸收零过程，这不等于进入内部。使用本章非退化一维扩散的尺度与速度条件，不据此宣称所有奇异边界延拓已构造。','Endpoint 0 lies in the closure of the state interval. Entrance means a continuous immediate entry into its interior after extension of the state space, not merely a constant process at 0. Finite Σ means accessibility; for inaccessible endpoints finite N gives the chapter’s proved entrance. The four (Σ,N) types are finite/finite, finite/infinite, infinite/finite and infinite/infinite. Regularity allows boundary choices; it does not force every extension to reflect. An absorbing zero process at an exit or natural endpoint is not an entrance. The chapter’s nondegenerate one-dimensional scale/speed assumptions apply; no general singular-boundary construction is claimed.')
 return body,condition,[boundary_scene(lang,k) for k in BOUNDARIES]

def fraction(x):
 from fractions import Fraction
 return str(Fraction(x).limit_denominator(256))
def account_scene(lang,x,c):
 s=Svg(400,290);p=40+320*x;s.line(40,58,360,58,GRAY,1);s.circle(p,58,20,TEAL,'white');s.line(p,58,p,45,TEAL,1.5);s.line(p,58,p+11,64,TEAL,1.5);s.text(p,26,'x='+fraction(x),19,anchor='middle')
 s.text(p+45,35,('0' if c==0 else ('τ' if c==1 else '2τ')),22);s.text(200,285,tr(lang,'同一段路径：沿途累计，退出时结算','Accumulate, then settle at exit'),18,anchor='middle')
 for end,prob,value in [(70,1-x,'0'),(330,x,'1')]:
  s.nodes.append(f'<path d="M{p} 81 Q{end} 112 {end} 174" fill="none" stroke="{TEAL}" stroke-width="2"/>');s.arrow(end,153,end,176);s.circle(end,205,26,TEAL,'white');s.text(end,214,value,28,anchor='middle');s.text(end,252,'g('+value+')='+value,18,anchor='middle')
  s.text(120 if end==70 else 280,144,fraction(prob),21,WARM,anchor='middle')
 s.text(200,211,tr(lang,'退出时刻 τ','Exit time τ'),19,anchor='middle')
 return s
def account_reading(lang,x,c):
 b=x;r=c*x*(1-x);return tr(lang,f'边界平均 {fraction(b)} ＋ 沿途平均 {fraction(r)} ＝ u(x) {fraction(b+r)}',f'Boundary mean {fraction(b)} + running mean {fraction(r)} = u(x) {fraction(b+r)}')
def v38(lang):
 for ix,x in enumerate([.25,.5,.75]):
  for c in [0,1,2]:account_scene(lang,x,c).save(f'V38-{lang}-{ix}-{c}.svg','One stopped motion with running and terminal payoffs')
 body='<p class="v5-intro">'+tr(lang,'Brownian在(0,1)运动，到边界停止。每秒累计c，退出到0或1时，再结算0或1。','Brownian motion stops on leaving (0,1). Accumulate c per unit time, then receive 0 or 1 at the corresponding exit boundary.')+'</p><div class="v5-scene">'+img(f'V38-{lang}-1-1.svg',tr(lang,'同一段停止路径同时带来沿途累计和边界结算','The same stopped path carries a clock payoff and an exit payoff'),'data-account-scene')+'</div>'
 body+=buttons('data-account-x',[(str(i),'x='+fraction(x)) for i,x in enumerate([.25,.5,.75])],'1')+buttons('data-account-c',[(str(c),'c='+str(c)) for c in [0,1,2]],'1')
 body+='<p class="v5-reading v5-equation-total" data-account-reading>'+account_reading(lang,.5,1)+'</p><p class="v5-model" data-account-source>'+tr(lang,'−½u″=1；u(0)=0，u(1)=1','−½u″=1; u(0)=0, u(1)=1')+'</p>'
 condition=tr(lang,'这是无折扣q=0的明确区间模型，不是一般Feynman–Kac定理的替代。令τ为标准Brownian首次退出(0,1)，g(0)=0、g(1)=1，f≡c。Pₓ(Bτ=1)=x，Eₓτ=x(1−x)，故u(x)=Eₓ[g(Bτ)+cτ]=x+cx(1−x)，满足−u″/2=c及上述非零边界数据。两项来自同一段路径，通常相关；相加取期望不需独立性。图中钟面表示累计到τ，不是第三种退出结果。箭头概率不由模拟估计；一般正则性、存在与边界实现仍依正文。','This is the explicit undiscounted model q=0, not a substitute for general Feynman–Kac. For standard Brownian exit time τ from (0,1), g(0)=0,g(1)=1 and f≡c, Pₓ(Bτ=1)=x and Eₓτ=x(1−x). Thus u(x)=Eₓ[g(Bτ)+cτ]=x+cx(1−x), satisfying −u″/2=c and the nonzero boundary data. The two contributions share one path and are generally dependent; linearity of expectation needs no independence. The clock is accumulation until τ, not a third exit outcome. Probabilities are exact, not simulated. General regularity, existence and boundary realization remain in the text.')
 return body,condition,[account_scene(lang,.5,1)]

def circle_scene(lang,t,angle):
 s=Svg(360,300);cx,cy,r=180,149,77;R=r*math.exp(t/2)
 s.nodes.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{WARM}" stroke-width="1.8" stroke-dasharray="6 4"/>');s.circle(cx,cy,r,TEAL,'white')
 # Redraw circles as outlines: the helper's white fill would otherwise hide the radial ray.
 x,y=cx+r*math.cos(angle),cy-r*math.sin(angle);u,v=cx+R*math.cos(angle),cy-R*math.sin(angle)
 s.line(cx,cy,u,v,GRAY,1);s.circle(cx,cy,3,GRAY);s.circle(u,v,6,WARM,'white');s.circle(x,y,5,TEAL);s.text(180,296,'t='+fraction(t),18,anchor='middle')
 return s
def v40(lang):
 for ti,t in enumerate([.25,.5,1]):
  for ai,a in enumerate([0,math.pi/4,math.pi/2]):circle_scene(lang,t,a).save(f'V40-{lang}-{ti}-{ai}.svg','Correct circle constraint versus a missing Ito drift')
 body='<p class="v5-intro">'+tr(lang,'同一份角度B。保留正确的Itô向心项，半径始终是1；删去它，就得到另一种运动。','Use the same angular input B. With the correct inward Itô term, radius stays 1. Deleting it creates a different motion.')+'</p><div class="v5-scene">'+img(f'V40-{lang}-2-1.svg',tr(lang,'单位圆与删去Itô修正后的增大半径','Unit circle and enlarged radius when the Ito correction is omitted'),'data-circle-scene')+'</div>'
 body+='<div class="v5-circle-key"><span><i class="v5-dot-solid"></i>'+tr(lang,'保留向心项','With the inward term')+'</span><span><i class="v5-dot-hollow"></i>'+tr(lang,'删去向心项','Without the inward term')+'</span></div>'
 body+=buttons('data-circle-t',[(str(i),'t='+fraction(t)) for i,t in enumerate([.25,.5,1])],'2')+buttons('data-circle-angle',[(str(i),'θ='+v) for i,v in enumerate(['0','π/4','π/2'])],'1')
 body+='<p class="v5-reading" data-circle-reading>'+tr(lang,'正确半径 1；删项后的半径 exp(1/2)≈1.649。改变角度不会修复半径。','Correct radius: 1. Without the term: exp(1/2)≈1.649. Changing the angle cannot fix the radius.')+'</p>'
 condition=tr(lang,'正确模型(X,Y)=(cosB,sinB)，dX=−YdB−Xdt/2，dY=XdB−Ydt/2，故X²+Y²=1。删掉两个dt项后，d(X²+Y²)=(X²+Y²)dt，从(1,0)出发半径为exp(t/2)；它与正确模型有相同角度B，但不是同一过程的另一种坐标写法。θ按钮是同一角度读数的示意，不是模拟轨迹，也不把Bₜ的分布离散化。向心漂移不表示真实路径沿半径内缩。Itô公式本身正确处理坐标变换，错误是遗漏二阶修正；圆周轮廓不表示各角度等概率。','The correct model is (cosB,sinB): dX=−YdB−Xdt/2 and dY=XdB−Ydt/2, so X²+Y²=1. Omitting both dt terms gives d(X²+Y²)=(X²+Y²)dt and radius exp(t/2) from (1,0). Its angle is still B, but it is a different process, not a new coordinate description of the same one. θ buttons illustrate one angular reading, not simulated trajectories or a discrete distribution for Bₜ. Inward Itô drift does not mean the actual path moves radially inward. Itô’s formula handles coordinate changes correctly; omitting the second-order correction is the error. Circle outlines do not assert a uniform angular law.')
 return body,condition,[circle_scene(lang,1,math.pi/4)]

FUNCS={'V35':v35,'V36':v36,'V38':v38,'V40':v40}
def figure(code,lang):
 body,condition,panes=FUNCS[code](lang);title=META[code][2 if lang=='zh' else 3]
 html=f'<figure class="explain-figure" id="visual-{code}" data-explain="{code}" lang="{lang}"><header><span class="ex-kicker">{code}</span><h3>{E(title)}</h3></header>{body}<figcaption id="visual-{code}-end">{E(condition)}</figcaption><nav class="ex-downloads"><a href="{BASE}{code}.{lang}.svg">{tr(lang,"静态矢量版","Static SVG")}</a><a href="/print/{code}.{lang}.html">{tr(lang,"打印页","Print view")}</a></nav></figure>'
 static(code,lang,title,condition,panes);return html,condition
def static(code,lang,title,condition,panes):
 s=Svg(900,1100);s.rect(0,0,900,1100,'white');s.text(30,43,title,27,weight='bold');s.line(30,64,870,64,RULE,1)
 if code=='V35':
  for j,p in enumerate(panes):
   x=30+440*j;s.text(x+195,110,['x′=2√|x|','x′=x²'][j],23,anchor='middle');s.nodes.append(f'<svg x="{x}" y="130" width="390" height="293" viewBox="0 0 360 270">{p.fragment()}</svg>')
  bottom=470
 elif code=='V36':
  for j,(kind,p) in enumerate(zip(BOUNDARIES,panes)):
   x=30+440*(j%2);y=100+350*(j//2);s.text(x+195,y,tr(lang,{'regular':'正则','exit':'出口','entrance':'入口','natural':'自然'}[kind],kind.title()),24,anchor='middle');s.nodes.append(f'<svg x="{x+20}" y="{y+12}" width="350" height="263" viewBox="0 0 360 270">{p.fragment()}</svg>');finite=BOUNDARIES[kind];s.text(x+195,y+307,'Σ '+('< ∞' if finite[0] else '= ∞')+'; N '+('< ∞' if finite[1] else '= ∞'),21,anchor='middle')
  bottom=790
 elif code=='V38':
  s.nodes.append(f'<svg x="135" y="100" width="630" height="457" viewBox="0 0 400 290">{panes[0].fragment()}</svg>');s.text(450,600,'1/2 + 1/4 = 3/4',27,anchor='middle');s.text(450,642,'−½u″=1; u(0)=0, u(1)=1',22,anchor='middle');bottom=680
 else:
  s.nodes.append(f'<svg x="165" y="85" width="570" height="475" viewBox="0 0 360 300">{panes[0].fragment()}</svg>');s.circle(120,580,5,TEAL);s.text(135,587,tr(lang,'保留向心项','With the inward term'),20);s.circle(490,580,5,WARM,'white');s.text(505,587,tr(lang,'删去向心项','Without the inward term'),20);s.text(450,632,tr(lang,'正确半径1；删项后 exp(1/2)≈1.649','Correct radius 1; without the term exp(1/2)≈1.649'),25,anchor='middle');bottom=675
 s.line(30,bottom,870,bottom,RULE,1);lines=wrap_caption(condition,lang)
 for j,line in enumerate(lines):s.text(30,bottom+31+j*24,line,17,GRAY)
 s.h=bottom+64+len(lines)*24;s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';s.save(f'{code}.{lang}.svg',title)
