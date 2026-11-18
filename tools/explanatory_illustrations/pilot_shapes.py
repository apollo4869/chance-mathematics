"""Five bilingual explanatory figures. Native text reflows; SVG panels stay legible."""
from pathlib import Path
from html import escape as E
import json,re,hashlib,textwrap
R=Path(__file__).resolve().parents[2];A=R/'assets/visuals/explanatory-v1'
INK='#173f39';TEAL='#16776d';PALE='#eaf2ee';WARM='#a45b30';GRAY='#65756e';RULE='#ccd9d1'
def tr(lang,zh,en):return zh if lang=='zh' else en
class Svg:
 def __init__(self,w=320,h=160):
  self.w=w;self.h=h;self.nodes=[]
 def line(self,x,y,u,v,c=INK,sw=2,dash=None):
  self.nodes.append(f'<path d="M{x} {y}L{u} {v}" fill="none" stroke="{c}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
 def arrow(self,x,y,u,v,c=TEAL):
  self.line(x,y,u,v,c,2);import math
  t=math.atan2(v-y,u-x);a=(u-8*math.cos(t-.45),v-8*math.sin(t-.45));b=(u-8*math.cos(t+.45),v-8*math.sin(t+.45));self.line(*a,u,v,c,2);self.line(*b,u,v,c,2)
 def text(self,x,y,s,size=18,c=INK,anchor='start',weight='normal'):
  self.nodes.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{c}">{E(s)}</text>')
 def circle(self,x,y,r=6,c=TEAL,fill=None):self.nodes.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill or c}" stroke="{c}" stroke-width="2"/>')
 def rect(self,x,y,w,h,fill=PALE,stroke=None):self.nodes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.5"' if stroke else '')+'/>')
 def fragment(self):return ''.join(self.nodes)
 def document(self,title):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" role="img" aria-label="{E(title)}"><style>text{{font-family:"Noto Sans SC","Microsoft YaHei",sans-serif}}</style>{self.fragment()}</svg>'
 def save(self,name,title):
  (A/name).write_text(self.document(title),encoding='utf-8');return name

def tile(file,alt):return f'<img class="ex-svg" src="/assets/visuals/explanatory-v1/{file}" alt="{E(alt)}" loading="eager">'
def note(t):return f'<p class="ex-note">{t}</p>'
def card(title,graphic,tail='',cls=''):return f'<section class="ex-card {cls}"><h4>{title}</h4>{graphic}'+(f'<p class="ex-result">{tail}</p>' if tail else '')+'</section>'

META={
'P01':('32-ito-formula','32.11','取值规则改变了累积','The sampling rule changes the sum'),
'P02':('43-exchangeability','43.10','共同的是分布，不是每次的答案','A shared law, not shared outcomes'),
'P03':('50-palm-gibbs','50.15','事件各占一票，时间按长度投票','One vote per event, more time for longer gaps'),
'P04':('54-brownian-crt','54.4','不同时间，同一个祖先','Different times, the same ancestor'),
'P05':('55-metric-measure-limits','55.1','很少抽到，不等于几何上很短','Rarely sampled does not mean geometrically short')}

def p01(lang):
 shared=Svg(320,85);shared.circle(40,40,8);shared.circle(280,40,8,GRAY,'white');shared.arrow(62,40,258,40);shared.text(160,25,'ΔX = 2',20,anchor='middle');shared.text(40,76,'Xᵢ = 1',18,anchor='middle');shared.text(276,76,'Xᵢ₊₁ = 3',18,anchor='middle')
 sharedname=shared.save(f'P01-{lang}-step.svg','One finite increment, from 1 to 3')
 panes=[];html=[]
 for k,(coefficient,result) in enumerate([(1,2),(3,6),(2,4)]):
  s=Svg(320,170);s.line(38,38,282,38,GRAY,1.5)
  for x,value in [(38,'1'),(282,'3')]:s.circle(x,38,7,TEAL if ((k==0 and x==38) or (k==1 and x==282) or k==2) else GRAY,'white' if ((k==0 and x==282) or (k==1 and x==38)) else None);s.text(x,21,value,18,anchor='middle')
  if k==2:s.line(38,52,38,64,TEAL);s.line(38,64,282,64,TEAL);s.line(282,52,282,64,TEAL);s.arrow(160,64,160,90)
  else:s.arrow(38 if k==0 else 282,52,160,90)
  s.circle(160,113,22,TEAL,'white');s.text(160,120,str(coefficient),23,anchor='middle');s.text(215,120,'× 2',20);s.text(265,120,'=',20);s.text(299,120,str(result),25,WARM,anchor='middle');
  title=tr(lang,['左端值','右端值','对称端点'][k],['Left endpoint','Right endpoint','Symmetric endpoints'][k]);name=s.save(f'P01-{lang}-{k}.svg',title);panes.append((title,s));html.append(card(title,tile(name,title),tr(lang,['事前可选','用到了这格的未来','先平均两个端点'][k],['Known before the increment','Uses this interval’s future','Average the two endpoints'][k])))
 caption=tr(lang,'这一格的数值是确定性代数示例，不是Brownian路径的面积。一般每格：右端和−左端和=(ΔX)²；对称和−左端和=(ΔX)²/2。','A deterministic one-step calculation, not an area under a Brownian path. In each cell: right minus left = (ΔX)²; symmetric minus left = (ΔX)²/2.')
 conditions=tr(lang,'连续半鞅、确定分割网格趋零时，对称端点和以ucp收敛到 ∫X∘dX = ∫X dX + [X]/2。对Brownian运动，[B]ₜ=t；一般H与X用[H,X]。右端值不是可预测Itô系数；时间中点取值未必等于端点值平均。','For a continuous semimartingale and deterministic partitions with mesh tending to zero, symmetric endpoint sums converge ucp: ∫X∘dX = ∫X dX + [X]/2. For Brownian motion, [B]ₜ=t; use [H,X] for general H,X. Right endpoints are not predictable Itô coefficients. A time midpoint is a different rule.')
 body=f'<div class="ex-step">{tile(sharedname,tr(lang,"同一格从1到3，增量2","The same step from 1 to 3, increment 2"))}</div><div class="ex-grid three">'+''.join(html)+'</div>'+note(caption)+f'<p class="ex-takeaway">{tr(lang,"Brownian极限中，差别没有消失：半份平方变化累积为 t/2。","For Brownian motion the difference survives: half the quadratic variation accumulates to t/2.")}</p>'
 return body,conditions,panes

def p02(lang):
 s=Svg(320,190);s.text(160,31,'ν',26,anchor='middle');s.line(160,44,160,64,TEAL);s.line(48,64,272,64,TEAL)
 for i,x in enumerate([48,160,272]):
  s.arrow(x,64,x,98);s.circle(x,125,24,TEAL,'white');s.text(x,132,['X₁','X₂','X₃'][i],22,anchor='middle');s.text(x,174,'±R',18,anchor='middle')
 name=s.save(f'P02-{lang}-shared.svg','One directing law feeds three conditionally independent coordinates')
 title=tr(lang,'先选一次R','Choose R once')
 distribution='<span class="ex-math">P(R=1)=P(R=2)=1/2</span><br><span class="ex-math">ν = (δ₋R + δR)/2</span>'
 body='<div class="ex-grid two"><div class="ex-input"><h4>'+title+'</h4><p>'+distribution+'</p><p>'+tr(lang,'每次投出的正负号独立，幅度R却共享。','Independent signs on each draw; a shared magnitude R.')+'</p></div>'+tile(name,tr(lang,'同一个ν分别驱动X1、X2、X3，没有从X1连向X2','The same ν drives X1, X2 and X3 separately'))+'</div>'
 body+='<div class="ex-grid two ex-facts">'+card(tr(lang,'给定ν：独立','Given ν: independent'),'','P(X₁∈A, X₂∈B | ν)=ν(A)ν(B)')+card(tr(lang,'不告诉ν：仍会依赖','Hide ν: dependence remains'),'','P(|X₂|=1)=1/2<br>P(|X₂|=1 | |X₁|=1)=1')+'</div>'
 body+=f'<div class="ex-controls" data-p02-controls><span>{tr(lang,"观察条件：","Condition on:")}</span><button type="button" data-env="mixed" aria-pressed="true">{tr(lang,"不告诉ν","ν hidden")}</button><button type="button" data-env="one" aria-pressed="false">ν₁ (±1)</button><button type="button" data-env="two" aria-pressed="false">ν₂ (±2)</button><output data-p02-output aria-live="polite">{tr(lang,"未给环境：看到|X₁|=1，会把下一次幅度的概率从1/2改为1。","With ν hidden, observing |X₁|=1 changes the probability of the next magnitude from 1/2 to 1.")}</output></div>'
 conditions=tr(lang,'这是§43.10的两环境例子：给定ν各次iid，无条件普通协方差为0却不独立。一般de Finetti结论仍需无限交换与标准Borel等条件，有限交换性不够。按钮只切换精确条件律，不作模拟或证明。','This is the two-environment example in §43.10: conditionally iid given ν; unconditionally uncorrelated but dependent. The general de Finetti theorem requires infinite exchangeability and the chapter’s standard Borel assumptions. Buttons compare exact conditional laws, not simulations or a proof.')
 return body,conditions,[(tr(lang,'一份共同概率','One shared law'),s)]

def sampling_panel(lang,mode):
 s=Svg(320,170);xs=[12,49,160,197,308];lengths=[1,3,1,3]
 for j,L in enumerate(lengths):
  s.rect(xs[j],65,xs[j+1]-xs[j],38,PALE if L==3 else 'white',TEAL if L==3 else GRAY);s.text((xs[j]+xs[j+1])/2,91,str(L),20,TEAL if L==3 else INK,anchor='middle')
 positions=[(xs[j],lengths[j]==3) for j in range(4)] if mode=='event' else [(12+37*(i+.5),i in [1,2,3,5,6,7]) for i in range(8)]
 for x,long in positions:
  if mode=='event':s.circle(x,33,6,TEAL if long else GRAY,'white' if not long else None)
  else:s.rect(x-5,26,10,10,TEAL if long else 'white',TEAL if long else GRAY)
  s.line(x,40,x,59,TEAL if long else GRAY,1.5)
 for x,label in zip(xs,['0','1','4','5','8']):s.text(x,132,label,17,GRAY,anchor='middle')
 s.text(160,163,tr(lang,'同一条记录：间隔长1、3、1、3','Same record: gap lengths 1, 3, 1, 3'),16,GRAY,anchor='middle')
 return s
def p03(lang):
 panes=[];cards=[]
 for mode in ['event','time']:
  s=sampling_panel(lang,mode);title=tr(lang,'按事件：每个起点一票' if mode=='event' else '按时间：每单位时间一票','Events: one vote per start' if mode=='event' else 'Time: one vote per time unit');name=s.save(f'P03-{lang}-{mode}.svg',title);panes.append((title,s));result=tr(lang,'长间隔：2/4 = 1/2' if mode=='event' else '长间隔：6/8 = 3/4','Long gap: 2/4 = 1/2' if mode=='event' else 'Long gap: 6/8 = 3/4');cards.append(card(title,tile(name,title),result,'ex-sampling '+mode))
 body='<div class="ex-grid two">'+''.join(cards)+'</div><p class="ex-takeaway">'+tr(lang,'多出来的是被选中的机会，不是间隔本身变长了。','Long intervals gain more chances to be selected; observation does not lengthen them.')+'</p>'
 body+=f'<div class="ex-controls" data-p03-controls><span>{tr(lang,"突出抽样单位：","Highlight the sampling unit:")}</span><button type="button" data-sample="both" aria-pressed="true">{tr(lang,"并排比较","Compare both")}</button><button type="button" data-sample="event" aria-pressed="false">{tr(lang,"事件","Events")}</button><button type="button" data-sample="time" aria-pressed="false">{tr(lang,"时间","Time")}</button><output data-p03-output aria-live="polite">{tr(lang,"两段长间隔占一半事件，却占四分之三时间。","The two long gaps account for half the events but three quarters of the time.")}</output></div>'
 conditions=tr(lang,'有限记录只示意权重：事件从0、1、4、5中均匀选，时间从[0,8)均匀选。八个方块各代表一单位时间，不是仅八个可选时刻。推广到平稳更新时，事件（Palm）律下间隔须为正、iid且0<E L<∞：P时间(L∈dℓ)=ℓ P事件(L∈dℓ)/E事件L。所见是含时刻的完整间隔，不是余寿命；事件观察读其后一个完整间隔。','The finite record illustrates weights: choose a start uniformly from {0,1,4,5}, or time uniformly from [0,8). Each square stands for a unit of time, not one of only eight possible times. For stationary renewal, the event (Palm) gaps must be positive and iid with 0<E L<∞: P_time(L∈dℓ)=ℓ P_event(L∈dℓ)/E_event L. Time sampling reads the full containing gap, not residual life; event sampling reads the next full gap.')
 return body,conditions,panes

def p04(lang):
 s=Svg(320,225);pts=[(18,180),(74,44),(130,112),(186,44),(298,180)]
 for a,b in zip(pts,pts[1:]):s.line(*a,*b,INK,2.5)
 s.line(18,180,307,180,GRAY,1);s.line(74,112,186,112,WARM,1.5,'5 4');s.text(160,163,'mₕ(s,t)=1',18,WARM,anchor='middle')
 for x,y,label in [(46,112,'a'),(130,112,'b'),(242,112,'c')]:s.circle(x,y,5);s.text(x,y+26,label,20,anchor='middle')
 for x,label in [(74,'s'),(186,'t')]:s.circle(x,44,5,WARM);s.text(x,26,label,20,WARM,anchor='middle')
 s.text(18,209,'0',17);s.text(294,209,'1',17);name1=s.save(f'P04-{lang}-curve.svg','A continuous excursion with three visits to the same ancestor')
 t=Svg(320,225);t.line(160,190,160,112,TEAL,2.5);t.line(160,112,80,32,TEAL,2.5);t.line(160,112,240,32,TEAL,2.5)
 for x,y,label in [(160,190,'ρ'),(160,112,'v'),(80,32,'pₕ(s)'),(240,32,'pₕ(t)')]:t.circle(x,y,6,TEAL if label=='v' else (WARM if label.startswith('p') else INK));t.text(x+(18 if label in ['ρ','v'] else 0),y+(7 if label in ['ρ','v'] else -15),label,19,anchor='start' if label in ['ρ','v'] else 'middle')
 for x,y in [(102,84),(224,84),(183,160)]:t.text(x,y,'1',17,GRAY)
 name2=t.save(f'P04-{lang}-tree.svg','The quotient tree: a, b and c represent v')
 body='<div class="ex-tree-map">'+card(tr(lang,'时间记录 h','Time record h'),tile(name1,tr(lang,'两个峰同高，但中间最低值为1','Equal-height peaks separated by a minimum of 1')))+'<div class="ex-projection"><span>pₕ</span><b class="ex-arrow">→</b></div>'+card(tr(lang,'商空间中的位置','Positions in the quotient'),tile(name2,tr(lang,'a、b、c都被识别成分枝点v','a, b and c are all identified as v')))+'</div>'
 body+='<div class="ex-grid two ex-facts">'+card(tr(lang,'重复访问，同一个点','Repeated visits, one point'),'','pₕ(a)=pₕ(b)=pₕ(c)=v')+card(tr(lang,'同样高，仍是不同枝','Equal height, different branches'),'','dₕ(s,t)=2+2−2×1=2')+'</div>'
 conditions=tr(lang,'确定性连续折线示例：从0升到2、降到1、再升到2、回到0；不是Brownian样本。零距离需两端等高且中间不更低，不是只比较端点高度。实树、唯一弧与紧性仍由正文证明；时间质量不等于枝长。','A deterministic continuous excursion: 0→2→1→2→0, not a Brownian sample. Zero distance requires equal endpoint heights with no lower value between them. Endpoint heights alone are insufficient. The real-tree, unique-arc and compactness claims require the text’s proofs; time mass is not edge length.')
 return body,conditions,[(tr(lang,'时间记录','Time record'),s),(tr(lang,'商树','Quotient tree'),t)]

def p05(lang):
 s=Svg(320,225);s.text(10,24,'X=[0,1]',19);s.line(210,48,290,48,TEAL,3);s.circle(210,48,5);s.text(206,76,'0',17);s.text(286,76,'1',17);s.text(250,28,tr(lang,'质量1','mass 1'),17,anchor='middle')
 s.text(10,110,'Y=[−2,1]',19);s.line(50,160,210,160,WARM,3,'7 4');s.line(210,160,290,160,TEAL,3);s.circle(210,160,5)
 s.text(130,140,tr(lang,'长度2 · 质量ε','length 2 · mass ε'),17,WARM,anchor='middle');s.text(250,140,'1−ε',17,anchor='middle')
 for x,v in [(50,'−2'),(210,'0'),(290,'1')]:s.text(x,193,v,17,anchor='middle')
 name=s.save(f'P05-{lang}-spaces.svg','An extra branch of length 2 carries mass epsilon')
 body='<div class="ex-space">'+tile(name,tr(lang,'两空间原区间长度相同，新增长2的枝只带ε质量','The same original segment, with an extra length-2 branch of mass epsilon'))+'</div>'
 labels=[('GH',tr(lang,'全空间形状','Whole-space geometry'),tr(lang,'直径：1 对 3','Diameters: 1 versus 3'),'d<sub>GH</sub> ≥ 1'),('GP',tr(lang,'质量看到的部分','What mass samples'),tr(lang,'1−ε质量可配成同一位置','Match mass 1−ε at identical positions'),'d<sup>r</sup><sub>GP</sub> ≤ ε'),('GHP',tr(lang,'同场保留三项','Three constraints, one embedding'),tr(lang,'几何 + 根 + 质量','Geometry + root + mass'),'d<sup>r</sup><sub>GHP</sub> ≥ d<sub>GH</sub> ≥ 1')]
 body+='<div class="ex-grid three ex-metrics">'+''.join(card(k+'<span>'+v+'</span>','<p>'+q+'</p>',r) for k,v,q,r in labels)+'</div>'
 body+=f'<div class="ex-controls ex-epsilon"><label for="eps-{lang}">ε <output data-eps-label>0.05</output><input id="eps-{lang}" data-epsilon type="range" min="0.02" max="0.30" step="0.01" value="0.05"></label><div class="ex-massbar" aria-label="{tr(lang,"原段与新枝的质量比例","Mass proportions on old and new segments")}"><span class="ex-oldmass" style="width:95%">1−ε</span><span class="ex-newmass" style="width:5%"></span></div><output data-eps-result aria-live="polite">{tr(lang,"ε=0.05：GP≤0.05；GH≥1。抽5个点，至少一个落入新枝的概率≤0.25。","ε=0.05: GP≤0.05; GH≥1. For 5 samples, the probability that at least one hits the new branch is ≤0.25.")}</output></div>'
 conditions=tr(lang,'根均为0，上标r表示带根。μ_ε=(1−ε)Unif[0,1]+εUnif[−2,0]，0<ε<1。GP按支撑加根识别；GHP采用同一嵌入下的max规范。小质量不使长枝消失；分别优化GH与GP不等于已控制GHP。','Both roots are 0; superscript r means rooted. μ_ε=(1−ε)Unif[0,1]+εUnif[−2,0], 0<ε<1. GP identifies support plus root; GHP uses the chapter’s max convention in one common embedding. Small mass does not remove a long branch. Separate GH and GP optimizations do not by themselves control GHP.')
 # Short text panels for the static print composition.
 panes=[(tr(lang,'相同的长度单位','The same length unit'),s)]
 return body,conditions,panes

from .pilot_revisions import install
REVISED, print_new = install(globals())
FUNCS={'P01':p01,'P02':p02,'P03':p03,'P04':p04,'P05':p05} | REVISED
META['P01']=(*META['P01'][:2], '同一格，三种结果', 'One increment. Three results.')
META['P05']=(*META['P05'][:2], '长枝仍在，样本未必看到', 'The branch stays. Samples may miss it.')
def figure(code,lang):
 body,condition,panes=FUNCS[code](lang);title=META[code][2 if lang=='zh' else 3]
 if code in ['P03','P04']:
  summary=tr(lang,'同一记录：长间隔占一半事件，却占四分之三时间。','Same record: long gaps take half the events, but three quarters of the time.') if code=='P03' else tr(lang,'三个时刻 a、b、c，商树上是同一个祖先 v。','Three times, a, b and c: one ancestor v in the quotient tree.')
  body='<p class="r3-mobile-insight">'+summary+'</p>'+body
 return f'<figure class="explain-figure" id="visual-{code}" data-explain="{code}" lang="{lang}"><header><span class="ex-kicker">{code}</span><h3>{E(title)}</h3></header>{body}<figcaption id="visual-{code}-end">{E(condition)}</figcaption><nav class="ex-downloads"><a href="/assets/visuals/explanatory-v1/{code}.{lang}.svg">{tr(lang,"静态矢量版","Static SVG")}</a><a href="/print/{code}.{lang}.html">{tr(lang,"打印页","Print view")}</a></nav></figure>',condition,panes

def wrapped(text,width,lang):
 if lang=='en':return textwrap.wrap(text,width=width,break_long_words=False)
 # CJK paragraph with Latin/math sequences; avoid cutting very long words only where possible.
 out=[];line='';n=0
 for c in text:
  w=1 if ord(c)>255 else .52
  if n+w>width:out.append(line);line='';n=0
  line+=c;n+=w
 if line:out.append(line)
 return out

def print_svg(code,lang,condition,panes):
 if code in ['P01','P02','P05']:return print_new(code,lang,condition,panes)
 title=META[code][2 if lang=='zh' else 3];S=Svg(900,700);S.rect(0,0,900,700,'white');S.text(30,42,title,27,weight='bold');S.line(30,61,870,61,RULE,1)
 if code=='P01':
  S.text(30,97,tr(lang,'同一格：1 → 3，ΔX=2','The same cell: 1 → 3, ΔX=2'),20)
  for j,(lab,sv) in enumerate(panes):
   x=30+290*j;S.text(x+130,143,lab,20,anchor='middle');S.nodes.append(f'<svg x="{x}" y="156" width="260" height="139" viewBox="0 0 320 170">{sv.fragment()}</svg>')
  S.text(450,357,tr(lang,'左端：2     右端：6     对称端点：4','Left: 2     Right: 6     Symmetric endpoints: 4'),25,anchor='middle')
  S.text(450,404,tr(lang,'累积差别：½Σ(ΔXᵢ)² → ½[X]ₜ','Accumulated difference: ½Σ(ΔXᵢ)² → ½[X]ₜ'),22,anchor='middle')
 elif code=='P02':
  S.rect(35,120,345,160,PALE);S.text(55,155,tr(lang,'只选一次R','Choose R only once'),23);S.text(55,201,'P(R=1)=P(R=2)=1/2',20);S.text(55,243,'ν=(δ₋R+δR)/2',23)
  S.nodes.append(f'<svg x="460" y="100" width="370" height="220" viewBox="0 0 320 190">{panes[0][1].fragment()}</svg>')
  S.text(40,369,tr(lang,'给定ν：P(X₁∈A,X₂∈B | ν)=ν(A)ν(B)','Given ν: P(X₁∈A,X₂∈B | ν)=ν(A)ν(B)'),23)
  S.text(40,420,'P(|X₂|=1)=1/2;  P(|X₂|=1 | |X₁|=1)=1',23)
 elif code=='P03':
  for j,(lab,sv) in enumerate(panes):
   x=30+440*j;S.text(x+200,112,lab,21,anchor='middle');S.nodes.append(f'<svg x="{x}" y="132" width="400" height="213" viewBox="0 0 320 170">{sv.fragment()}</svg>');S.text(x+200,391,tr(lang,'长间隔：1/2' if j==0 else '长间隔：3/4','Long gap: 1/2' if j==0 else 'Long gap: 3/4'),25,anchor='middle')
 elif code=='P04':
  for j,(lab,sv) in enumerate(panes):
   x=20+480*j;S.text(x+180,108,lab,22,anchor='middle');S.nodes.append(f'<svg x="{x}" y="125" width="365" height="257" viewBox="0 0 320 225">{sv.fragment()}</svg>')
  S.arrow(416,240,480,240);S.text(448,221,'pₕ',22,anchor='middle');S.text(450,429,'pₕ(a)=pₕ(b)=pₕ(c)=v;  dₕ(s,t)=2',24,anchor='middle')
 elif code=='P05':
  S.nodes.append(f'<svg x="230" y="80" width="440" height="309" viewBox="0 0 320 225">{panes[0][1].fragment()}</svg>')
  for j,name in enumerate(['GH','GP','GHP']):
   x=155+290*j;S.text(x,410,name,25,anchor='middle')
   sup='<tspan baseline-shift="super" font-size="15">r</tspan>' if j else ''
   tail=' ≤ ε' if j==1 else ' ≥ 1'
   S.nodes.append(f'<text x="{x}" y="452" font-size="23" text-anchor="middle" fill="{INK}">d{sup}<tspan baseline-shift="sub" font-size="16">{name}</tspan>{tail}</text>')
 S.line(30,492,870,492,RULE,1)
 lines=wrapped(condition,78 if lang=='en' else 48,lang)
 for j,line in enumerate(lines):S.text(30,525+24*j,line,17,GRAY)
 # Size determined by actual wrapped labels; no tiny footer reduction.
 S.h=max(590,549+24*len(lines));S.nodes[0]=f'<rect x="0" y="0" width="900" height="{S.h}" fill="white"/>'
 S.save(f'{code}.{lang}.svg',title)

