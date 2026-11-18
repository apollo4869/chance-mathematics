"""Exact dyadic compensation and finite Bernoulli tilting; no old-asset writes."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
from functools import lru_cache
from math import comb,pi,sin,cos
import json
from .pilot_shapes import Svg,tr,E,INK,TEAL,PALE,WARM,GRAY,RULE
from .volume5 import buttons,wrap_caption
R=Path(__file__).resolve().parents[2];A=R/'assets/visuals/explanatory-early-v4';BASE='/assets/visuals/explanatory-early-v4/'
SOURCE='251fda700d10917876ac9d2e09af6ef541e42379'
META={'E27':('27-levy-processes','27.5','先减有限均值，再接上无穷层','Center finite sums before taking a limit'),
'E29':('29-large-deviations','29.7','换了权重，代价没有消失','Changing weights does not erase the cost')}
def save(s,name,title):(A/name).write_text(s.document(title),encoding='utf-8',newline='\n')
def img(name,alt,attr=''):return f'<img class="b4-svg" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def panel(title,scene):return '<section><h4>'+title+'</h4>'+scene+'</section>'
def pair(a,b):return '<div class="b4-pair">'+a+b+'</div>'
def nest(s,t,x,y,w,h):s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {t.w} {t.h}">{t.fragment()}</svg>')
def frac(n):return f'1/{2**n}'
def superscript(n):return str(n).translate(str.maketrans('-0123456789','⁻⁰¹²³⁴⁵⁶⁷⁸⁹'))
def means(lg,n):
 s=Svg(370,455)
 s.text(110,25,tr(lg,'每层平均位移','Mean displacement'),18,anchor='middle');s.text(282,25,tr(lg,'减去有限均值','Subtract finite mean'),18,WARM,anchor='middle')
 for k in range(1,n+1):
  y=66+(k-1)*54;s.text(7,y+6,f'k={k}',15,GRAY)
  # Exactly 2^k subdivisions of a unit mean, not sampled Poisson counts.
  for j in range(2**k):s.rect(52+120*j/(2**k),y-12,120/(2**k),24,PALE,TEAL)
  s.text(112,y+33,'2'+superscript(k)+' × 2'+superscript(-k)+' = 1',15,TEAL,anchor='middle')
  s.text(196,y+7,'−',27,WARM,anchor='middle');s.rect(222,y-12,120,24,'#fbf0df',WARM);s.text(282,y+7,'1',20,WARM,anchor='middle')
 s.text(185,83+n*54,'⋮',25,GRAY,anchor='middle')
 s.text(185,425,tr(lg,f'先算这 {n} 个有限的差',f'First form these {n} finite differences'),21,anchor='middle',weight='bold')
 s.text(185,451,tr(lg,'移去均值，不是删掉实际跳跃','Center the mean; do not erase the jumps'),16,GRAY,anchor='middle');return s

def energy(lg,n):
 s=Svg(370,455);s.text(185,25,tr(lg,'中心化后的方差可相加','Centered variances can be added'),19,anchor='middle')
 x,y,w,h=42,66,126,252;yy=y
 colors=['#16776d','#398b7c','#65a494','#88b8a7','#a8cbbd','#c0d9cc']
 for k in range(1,n+1):
  dh=h/(2**k);s.rect(x,yy,w,dh,colors[k-1],'white')
  if dh>=25:s.text(x+w/2,yy+dh/2+6,frac(k),19,'white' if k<3 else INK,anchor='middle')
  yy+=dh
 s.rect(x,yy,w,y+h-yy,'white',WARM);s.rect(x,y,w,h,'none',RULE)
 s.text(105,345,tr(lg,'整个方框的面积 = 1','Whole rectangle: area 1'),15,GRAY,anchor='middle')
 s.line(x+w,(yy+y+h)/2,219,273,WARM,1.5)
 s.text(270,208,tr(lg,'未加入的','Unadded'),18,WARM,anchor='middle');s.text(270,236,tr(lg,'平方尾','square tail'),18,WARM,anchor='middle');s.text(270,279,frac(n),33,WARM,anchor='middle',weight='bold')
 s.text(185,395,f'Var(Mᴺ₁) = 1 − {frac(n)}',23,TEAL,anchor='middle')
 s.text(185,438,tr(lg,'均值归零，波动并没有归零','Zero mean does not mean zero fluctuation'),17,anchor='middle');return s

def scope(lg,n,focus):
 s=Svg(370,292);v=1/(2**n);whole=focus=='whole'
 s.text(185,25,tr(lg,'先比较两个有限截断 K>N','First compare two finite cutoffs K>N'),18,anchor='middle')
 for y,iswhole,label in [(81,False,tr(lg,'终点 t=1','Endpoint t=1')),(203,True,tr(lg,'整段 [0,1]','Whole interval [0,1]'))]:
  active=iswhole==whole;c=TEAL if active else GRAY
  s.text(25,y-20,label,18,c);s.line(45,y,325,y,RULE,2)
  if iswhole:s.rect(45,y-8,280,16,PALE if active else 'white',c)
  else:s.circle(325,y,8 if active else 5,c)
  s.text(45,y+31,'0',15,GRAY,anchor='middle');s.text(325,y+31,'1',15,GRAY,anchor='middle')
  s.text(185,y+65,('E sup |D(t)|² ≤ '+f'{4*v:g}') if iswhole else ('E|D(1)|² ≤ '+f'{v:g}'),20,c,anchor='middle')
 s.text(185,171,tr(lg,'鞅结构 + Doob，才能控制整段','Martingale + Doob control the whole interval'),15,WARM,anchor='middle')
 return s

def compact27(lg,n):
 s=Svg(370,362);s.text(91,25,tr(lg,'平均位移','Mean displacement'),17,anchor='middle');s.text(278,25,tr(lg,'中心化方差','Centered variance'),17,anchor='middle')
 s.text(91,51,tr(lg,'每层先减1','Center each layer'),15,WARM,anchor='middle');s.text(278,51,tr(lg,'总量不超过1','Total at most 1'),15,GRAY,anchor='middle')
 for k in range(1,n+1):
  y=91+33*(k-1);s.text(5,y+5,str(k),12,GRAY)
  for j in range(2**k):s.rect(25+48*j/(2**k),y-9,48/(2**k),18,PALE,TEAL)
  s.text(87,y+6,'−',21,WARM,anchor='middle');s.rect(101,y-9,48,18,'#fbf0df',WARM);s.text(125,y+5,'1',14,WARM,anchor='middle')
 s.text(8,70,'k',12,GRAY);s.arrow(169,176,220,176);s.text(195,154,tr(lg,'平方量','Squared'),15,GRAY,anchor='middle')
 yy=80
 for k in range(1,n+1):
  h=210/(2**k);s.rect(245,yy,70,h,TEAL if k%2 else '#65a494','white')
  if h>25:s.text(280,yy+h/2+6,frac(k),17,'white',anchor='middle')
  yy+=h
 s.rect(245,yy,70,290-yy,'white',WARM);s.rect(245,80,70,210,'none',RULE)
 s.text(90,326,'N = '+str(n),24,anchor='middle',weight='bold');s.text(280,326,tr(lg,'尾 ','Tail ')+frac(n),21,WARM,anchor='middle',weight='bold')
 s.text(185,358,tr(lg,'左为均值，右为方差；都不是样本轨迹','Means and variances, not sample paths'),14,GRAY,anchor='middle');return s

def e27(lg):
 for n in [2,4,6]:
  save(means(lg,n),f'E27-{lg}-{n}-means.svg','Finite expected jump mass and its finite centering')
  save(energy(lg,n),f'E27-{lg}-{n}-energy.svg','Geometric centered variance and the exact unadded square tail')
  save(compact27(lg,n),f'E27-{lg}-{n}-compact.svg','Dedicated mobile comparison of finite centering and the remaining square tail')
  for focus in ['end','whole']:save(scope(lg,n,focus),f'E27-{lg}-{n}-{focus}.svg','Endpoint L2 versus whole-window maximal second-moment control')
 body='<p>'+tr(lg,'小跳越来越细，每层平均位移却仍是1。先保留前N层并移去有限均值，剩余方差才有可求和的平方尾。','Smaller jumps, the same mean 1 in each layer. Keep N layers and center finitely; their variances have a geometric tail.')+'</p>'
 body+=buttons('data-cutoff',[(str(n),'N='+str(n)) for n in [2,4,6]],'4')
 body+=pair(panel(tr(lg,'有限截断内的补偿','Compensation inside a finite cutoff'),img(f'E27-{lg}-4-means.svg','Unit mean split into ever smaller jumps, subtracted only within a finite sum','data-means')),
 panel(tr(lg,'可加的是中心化方差','Centered variance is summable'),img(f'E27-{lg}-4-energy.svg','Unit variance rectangle with exact geometric tail','data-energy')))
 body+='<div class="b4-mobile">'+img(f'E27-{lg}-4-compact.svg','Mobile: finite mean subtraction and geometric variance compared together','data-compact')+'</div>'
 body+='<details class="b4-mobile-details"><summary>'+tr(lg,'逐层细看均值与方差','Inspect the individual layers')+'</summary>'+img(f'E27-{lg}-4-means.svg','Full mean structure','data-detail-means')+img(f'E27-{lg}-4-energy.svg','Full variance structure','data-detail-energy')+'</details>'
 body+='<div class="b4-warning">'+tr(lg,'这些分格表示<strong>平均响铃次数 × 单跳大小</strong>，不是一条样本的计数。移去均值不等于波动为零，也不是先写“∞−∞”。','The subdivisions represent <strong>mean count × jump size</strong>, not sampled counts. Centering does not make the fluctuations zero and never starts with “∞−∞”.')+'</div>'
 body+='<h4>'+tr(lg,'从一个时刻，到一整条路径','From one time to a whole path')+'</h4><p class="b4-model">D(t)=Mᴷ(t)−Mᴺ(t), K&gt;N '+tr(lg,'均有限。','both finite.')+'</p>'+buttons('data-scope',[('end',tr(lg,'聚焦终点','Focus on endpoint')),('whole',tr(lg,'聚焦整段','Focus on whole interval'))],'whole')
 body+='<div class="b4-single">'+img(f'E27-{lg}-4-whole.svg','The endpoint marker and the interval-wide band are different observations','data-scope-scene')+'</div>'
 body+='<details><summary>'+tr(lg,'第二层：精确模型与收敛责任','Second layer: exact model and convergence claims')+'</summary><p>'+tr(lg,'Nₖ为独立、速率2ᵏ的Poisson过程，Jₖ(t)=2⁻ᵏNₖ(t)，Mᴺ(t)=Σₖ≤ᴺ[Jₖ(t)−t]，图固定T=1。先对有限K>N取D=Mᴷ−Mᴺ，终端方差准确为2⁻ᴺ−2⁻ᴷ≤2⁻ᴺ；鞅的最大不等式才给E sup₀≤t≤1|D(t)|²≤4·2⁻ᴺ。先有这些有限比较，再构造极限并用Fatou传递估计；不以尚未构造的无穷路径作为自身存在的前提。','Nk are independent Poisson processes of rates 2^k, Jk(t)=2^(-k)Nk(t), and M^N(t)=Σk≤N[Jk(t)−t], with T=1. First take finite K>N and D=M^K−M^N: the terminal variance is exactly 2^(-N)−2^(-K)≤2^(-N). The martingale maximal inequality gives E sup0≤t≤1|D(t)|²≤4·2^(-N). These finite comparisons precede the limit construction; Fatou then transfers the bound. An unconstructed infinite path is not assumed to prove its own existence.')+'</p></details>'
 cap=tr(lg,'模型沿用正文的二进时钟，k≥1，T=1。每层均值1、中心化方差2⁻ᵏ；图中分格是均值结构，不是模拟。Mᴺ=Σₖ≤ᴺJₖ−N是两个有限量之差；原正跳和发散的依据是正文Chebyshev与Borel–Cantelli，不是仅凭无限均值。平方尾vᴺ=Σₖ>ᴺ2⁻ᵏ=2⁻ᴺ。先对两个有限截断K>N比较D=Mᴷ−Mᴺ：终点二阶量=2⁻ᴺ−2⁻ᴷ≤vᴺ；整段E sup₀≤t≤1|D(t)|²≤4vᴺ是鞅最大界，不是等式或确定路径误差。极限构造后才用Fatou传递估计。上确界界经Markov推出ucp；一般构造的局部一致a.s.版本还须正文可求和概率及选列论证。蓝绿面积为已纳入方差，白色尾部保持真实面积，未人为放大。',
 'The dyadic clocks are those in the text: k≥1 and T=1. Each layer has mean 1 and centered variance 2^(-k); subdivisions show means, not a simulation. M^N=Σk≤N Jk−N subtracts two finite quantities. Divergence of the raw positive-jump sum uses the text’s Chebyshev/Borel–Cantelli argument, not infinite expectation alone. The square tail is vN=Σk>N2^(-k)=2^(-N). For finite K>N, compare D=M^K−M^N: its terminal second moment is exactly 2^(-N)−2^(-K)≤vN. E sup0≤t≤1|D(t)|²≤4vN is a martingale maximal bound, not an equality or deterministic path bound. Fatou transfers the estimate only after constructing the limit. Markov yields ucp from this bound; the general locally uniform a.s. construction also needs the text’s summable-probability/subsequence argument. Filled area is included variance; the unfilled tail retains its true area, without enlargement.')
 return body,cap,[('Finite centering',means(lg,4)),('Square tail',energy(lg,4)),('Endpoint and whole-window control',scope(lg,4,'whole'))]

@lru_cache(None)
def tilt(n):
 root={64:4,512:8,4096:16}[n];delta=F(1,2*root);lo=3*n//4-n//(2*root);hi=3*n//4+n//(2*root)
 numeratorP=sum(comb(n,k) for k in range(lo,hi+1));numeratorQ=sum(comb(n,k)*3**k for k in range(lo,hi+1))
 with localcontext() as ctx:
  ctx.prec=75;p=Decimal(numeratorP)/Decimal(2**n);q=Decimal(numeratorQ)/Decimal(4**n);theta=Decimal(3).ln();D=Decimal(3)*theta/4-Decimal(2).ln();rate=-p.ln()/n
  return dict(n=n,root=root,delta=delta,lo=lo,hi=hi,P=p,Q=q,theta=theta,D=D,rate=rate,p_numerator=numeratorP,q_numerator=numeratorQ)
def sci(x):
 if not x:return '0'
 if Decimal('.001')<=x<Decimal('1000'):return f'{x:.4f}'
 m,e=f'{x:.2E}'.split('E');return m+'×10'+str(int(e)).translate(str.maketrans('-0123456789','⁻⁰¹²³⁴⁵⁶⁷⁸⁹'))
def kvalue(model,where):return model['lo'] if where=='low' else model['hi'] if where=='high' else 3*model['n']//4
def weight(n,k):
 with localcontext() as ctx:
  ctx.prec=75;log=Decimal(n)*Decimal(2).ln()-Decimal(k)*Decimal(3).ln();return log.exp(),-log/n

def sector(s,cx,cy,r,p):
 s.circle(cx,cy,r,RULE,'white');p=float(p)
 if p<1e-6:return # Do not inflate a positive but subpixel probability mass.
 a=2*pi*p;xx=cx+r*sin(a);yy=cy-r*cos(a)
 s.nodes.append(f'<path d="M{cx} {cy}L{cx} {cy-r}A{r} {r} 0 {int(p>.5)} 1 {xx} {yy}Z" fill="{TEAL}"/>')
def event_scene(lg,n):
 m=tilt(n);s=Svg(370,365)
 s.text(185,24,tr(lg,'同一n，同一批事件记录 Aₙ','Same n, same event records Aₙ'),18,anchor='middle')
 x=lambda z:35+300*z;d=float(m['delta'])
 s.rect(x(.75-d),51,600*d,28,'#f4e4ca',WARM);s.line(35,65,335,65,GRAY,1)
 for z,lab in [(0,'0'),(.5,'p=1/2'),(.75,'q=3/4'),(1,'1')]:s.circle(x(z),65,3,WARM if z==.75 else GRAY);s.text(x(z),104,lab,14,GRAY,anchor='middle')
 for cx,lab,p in [(94,'Pₙ',m['P']),(276,'Qₙ',m['Q'])]:
  s.text(cx,145,lab,25,anchor='middle',weight='bold');sector(s,cx,216,51,p);s.text(cx,302,'≈ '+sci(p) if p<Decimal('.995') else '≈ 1 − '+sci(1-p),17,TEAL,anchor='middle')
 s.text(94,333,tr(lg,'正概率，可能细于像素','Positive; may be subpixel'),14,WARM,anchor='middle')
 s.text(276,333,tr(lg,'有限n仍不是概率1','Finite n: still below 1'),14,GRAY,anchor='middle')
 s.text(185,362,tr(lg,'实色面积是概率；未放大微小质量','Filled area is probability; tiny masses are not enlarged'),13,GRAY,anchor='middle');return s

def record_scene(lg,n,where):
 m=tilt(n);k=kvalue(m,where);L,r=weight(n,k);s=Svg(370,365);w=310;kx=30+w*k/n
 s.text(185,24,tr(lg,'挑一条记录，按它的H/T次数回权','Reweight one record by its H/T counts'),17,anchor='middle')
 s.rect(30,62,kx-30,43,TEAL);s.rect(kx,62,340-kx,43,WARM)
 s.text((30+kx)/2,90,'H × '+str(k),18,'white',anchor='middle');s.text((kx+340)/2,90,'T × '+str(n-k),16,'white',anchor='middle')
 s.arrow(105,114,105,150,TEAL);s.arrow(285,114,285,150,WARM)
 s.text(105,181,'× (2/3)ᴷ',24,TEAL,anchor='middle');s.text(285,181,'× 2ⁿ⁻ᴷ',24,WARM,anchor='middle')
 s.line(105,197,105,217,TEAL);s.line(285,197,285,217,WARM);s.line(105,217,285,217,GRAY,1);s.arrow(185,217,185,241)
 s.text(185,273,'Lₙ = 2ⁿ / 3ᴷ',26,anchor='middle',weight='bold');s.text(185,309,'≈ '+sci(L),24,TEAL,anchor='middle')
 s.text(185,354,tr(lg,'这是单条记录的比值，不是事件概率','A record likelihood ratio, not an event probability'),14,GRAY,anchor='middle');return s

def rate_scene(lg,n,where):
 m=tilt(n);k=kvalue(m,where);L,r=weight(n,k);s=Svg(370,225);D=float(m['D']);d=float(m['delta']);theta=float(m['theta']);x=lambda z:30+310*(z+.02)/.32
 s.text(185,25,tr(lg,'每样本回权率：−log Lₙ / n','Per-sample return cost: −log Lₙ / n'),18,anchor='middle')
 lo,hi=D-theta*d,D+theta*d;s.line(30,110,340,110,RULE,2);s.rect(x(lo),91,x(hi)-x(lo),38,PALE,TEAL)
 s.line(x(D),70,x(D),148,GRAY,1.5,'3 3');s.text(x(D),59,'D',20,GRAY,anchor='middle')
 s.circle(x(float(r)),110,7,WARM);s.text(x(float(r)),173,f'{float(r):.5f}',18,WARM,anchor='middle')
 s.text(185,211,tr(lg,'窗口缩小 → 这段回权率逼近D','Shrinking window → these record costs approach D'),14,GRAY,anchor='middle');return s

def e29(lg):
 for n in [64,512,4096]:
  save(event_scene(lg,n),f'E29-{lg}-{n}-event.svg','The same event under two finite product laws; exact binomial masses')
  for where in ['low','target','high']:
   save(record_scene(lg,n,where),f'E29-{lg}-{n}-{where}-record.svg','A single ordered record has an explicit finite likelihood ratio')
   save(rate_scene(lg,n,where),f'E29-{lg}-{n}-{where}-rate.svg','Finite per-record rate varies across the shrinking neighborhood')
 m=tilt(512)
 body='<p>'+tr(lg,'固定n时，事件记录没有换，换的是每条记录的概率。倾斜后更容易看见它们；把权重换回去时，指数代价仍在。','For a fixed n the event records stay the same; their weights change. Tilting makes them easier to see, but restoring the old weights retains an exponential cost.')+'</p>'
 body+=buttons('data-sample-n',[(str(n),'n='+str(n)) for n in [64,512,4096]],'512')
 body+='<p class="b4-model" data-event-definition>'+tr(lg,'公平硬币 P；正面率3/4的 Q。A₅₁₂：352≤K≤416，δ₅₁₂=1/16。','P: fair coin. Q: head probability 3/4. A512: 352≤K≤416, δ512=1/16.')+'</p>'
 body+=pair(panel(tr(lg,'同一事件，两份概率','One event, two probabilities'),img(f'E29-{lg}-512-event.svg','A common frequency window and true event probability areas','data-event')),
 panel(tr(lg,'回权要看具体记录','Return weights depend on the record'),img(f'E29-{lg}-512-target-record.svg','Head/tail proportions and their product likelihood ratio','data-record')))
 body+=buttons('data-record-type',[('low',tr(lg,'窗口下沿记录','Lower-edge record')),('target',tr(lg,'目标频率记录','Target-frequency record')),('high',tr(lg,'窗口上沿记录','Upper-edge record'))],'target')
 body+='<div class="b4-warning">'+tr(lg,'Lₙ是<strong>单条记录的似然比</strong>。有限n时，Pₙ(Aₙ)一般不等于Qₙ(Aₙ)e⁻ⁿᴰ。','Lₙ is a <strong>single-record likelihood ratio</strong>. At finite n, Pn(An) generally differs from Qn(An)e^(−nD).')+'</div>'
 body+='<div class="b4-single">'+img(f'E29-{lg}-512-target-rate.svg','A shrinking interval of possible log weights, with the selected record marked','data-rate')+'</div>'
 body+='<output data-finite-rate>'+tr(lg,f'有限事件率 −log Pₙ(Aₙ)/n ≈ {m["rate"]:.5f}；渐近极限 D ≈ {m["D"]:.5f}。',f'Finite event rate −log Pn(An)/n ≈ {m["rate"]:.5f}; limiting rate D ≈ {m["D"]:.5f}.')+'</output>'
 body+='<details><summary>'+tr(lg,'第二层：有限求和、窗口及极限','Second layer: finite sums, the window and the limit')+'</summary><p>'+tr(lg,'P下Xi独立Bernoulli(1/2)，Q下独立Bernoulli(3/4)，K=ΣXi。δₙ=1/(2n¹ᐟ³)，Aₙ={|K/n−3/4|≤δₙ}；切换n也改变窗口及样本空间。显示概率来自含组合系数的二项有限求和，数值只作四舍五入，不用Gaussian近似。图中的代表记录可取HᴷTⁿ⁻ᴷ；具有相同K的每条有序记录都有同一似然比，但不是整个类型的概率。','Under P the Xi are iid Bernoulli(1/2); under Q they are iid Bernoulli(3/4), with K=ΣXi. Set δn=1/(2n^(1/3)) and An={|K/n−3/4|≤δn}. Changing n changes both the window and the sample space. Displayed probabilities are rounded finite binomial sums, including combinatorial coefficients, not Gaussian approximations. H^K T^(n−K) represents one ordered record; all records with that K have the same likelihood ratio, not the same combined type probability.')+'</p><p>'+tr(lg,'θ=log3，D=(3/4)log3−log2，−logLₙ/n=(K/n)log3−log2。在Aₙ内相差D至多θδₙ。另由Chebyshev，Qₙ(Aₙᶜ)≤3/(4n¹ᐟ³)→0，故 −logPₙ(Aₙ)/n→D。一般分布不保证每个目标均值都能由指数倾斜实现；本图仅为可完全核算的Bernoulli内部参数。','Here θ=log3, D=(3/4)log3−log2 and −logLn/n=(K/n)log3−log2. On An this differs from D by at most θδn. Chebyshev gives Qn(An complement)≤3/(4n^(1/3))→0, yielding −logPn(An)/n→D. General laws need not realize every target mean by tilting; this is a fully computable interior Bernoulli example.')+'</p></details>'
 cap=tr(lg,'固定模型p=1/2、q=3/4，n显示64、512、4096。δₙ=1/(2n¹ᐟ³)，Aₙ={|K/n−q|≤δₙ}；同一n下P/Q使用同一事件。概率均由有限二项求和精确建立，显示值四舍五入；小于像素的质量不放大、不视为0。Pₙ/Qₙ对单条记录的密度比Lₙ=2ⁿ/3ᴷ，可随K变化，某些有限参数甚至可大于1；不能把整个事件回权成一个常数。以θ=log3、D=qlog3−log2，有exp[−n(D+θδₙ)]Qₙ(Aₙ)≤Pₙ(Aₙ)≤exp[−n(D−θδₙ)]Qₙ(Aₙ)。δₙ→0且Qₙ(Aₙ)→1才给速度n的极限D。选择单个频率格子不会使其Q概率趋1。本图没有把一般Cramér定理缩成可匹配倾斜的点。',
 'Fixed p=1/2, q=3/4; displayed n are 64, 512, 4096. With δn=1/(2n^(1/3)), An={|K/n−q|≤δn}; P and Q use the same event at the same n. Finite binomial sums give exact probabilities, rounded for display. Subpixel positive masses are not enlarged or treated as zero. The record likelihood ratio Ln=2^n/3^K varies with K and can exceed one for some finite parameters; a whole event cannot be reweighted by one constant. For θ=log3 and D=qlog3−log2, exp[−n(D+θδn)]Qn(An)≤Pn(An)≤exp[−n(D−θδn)]Qn(An). Only δn→0 and Qn(An)→1 give limiting rate D at speed n. A single frequency cell does not have Q-probability tending to one. This does not restrict the general Cramér theorem to tilt-matched targets.')
 return body,cap,[('Same event under P and Q',event_scene(lg,512)),('Reweight one ordered record',record_scene(lg,512,'target')),('Per-sample log cost',rate_scene(lg,512,'target'))]

def static(code,lg,title,cap,panes):
 s=Svg(900,1800);s.rect(0,0,900,1800,'white');s.text(25,43,title,26,weight='bold');y=105
 labels={'Finite centering':('有限截断内补偿','Finite centering'),'Square tail':('平方尾','Square tail'),'Endpoint and whole-window control':('终点与整段控制','Endpoint and whole-window control'),'Same event under P and Q':('同一事件的两份权重','Same event under P and Q'),'Reweight one ordered record':('一条记录的回权','Reweight one ordered record'),'Per-sample log cost':('每样本对数代价','Per-sample log cost')}
 for j,(label,t) in enumerate(panes):
  if j==2:
   y+=35;s.text(450,y,tr(lg,*labels[label]),20,anchor='middle',weight='bold');y+=20;nest(s,t,265,y,370,t.h);y+=t.h+20
  else:
   x=25+j*450;s.text(x+185,y-16,tr(lg,*labels[label]),19,anchor='middle',weight='bold');nest(s,t,x,y,370,t.h)
   if j==1:y+=max(panes[0][1].h,t.h)+35
 # E29's finite event rate is explicitly distinct from D in the print version too.
 if code=='E29':
  m=tilt(512);s.text(450,y+7,tr(lg,f'有限事件率 ≈{m["rate"]:.5f}；渐近D ≈{m["D"]:.5f}',f'Finite event rate ≈{m["rate"]:.5f}; limiting D ≈{m["D"]:.5f}'),20,TEAL,anchor='middle');y+=42
 s.line(25,y,875,y,RULE,1);lines=wrap_caption(cap,lg)
 for i,line in enumerate(lines):s.text(25,y+30+24*i,line,17,GRAY)
 s.h=y+65+24*len(lines);s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';save(s,f'{code}.{lg}.svg',title)

CSS='''.batch4 .b4-mobile,.batch4 .b4-mobile-details{display:none}.batch4{background:#fffefa;color:#173f39;padding:28px;border:1px solid #ccd9d1;margin:2rem 0;font-family:"Microsoft YaHei",sans-serif;box-sizing:border-box}.batch4 *{box-sizing:border-box}.batch4 header span{font-size:13px;color:#65756e}.batch4 h3{font-size:26px;line-height:1.4;margin:0 0 18px}.batch4 p{font-size:18px;line-height:1.8}.batch4 .b4-pair{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin:22px 0}.batch4 h4{font-size:20px;text-align:center;line-height:1.6;margin:12px 0;font-weight:500}.batch4 img.b4-svg{display:block;width:100%;height:auto;max-height:none!important;border:0;box-shadow:none;margin:0;object-fit:contain}.batch4 .b4-single{max-width:480px;margin:18px auto}.batch4 .b4-warning{background:#f7f1e5;border-left:3px solid #a45b30;padding:16px;font-size:17px;line-height:1.8;margin:20px 0}.batch4 .v5-controls{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:18px 0}.batch4 button{font:inherit;font-size:16px;padding:9px 12px;background:#fffefa;color:#173f39;border:1px solid #ccd9d1;border-radius:4px;cursor:pointer}.batch4 button[aria-pressed=true]{background:#eaf2ee;border:2px solid #16776d;padding:8px 11px}.batch4 output{display:block;font-size:20px;line-height:1.8;color:#16776d;border-top:1px solid #ccd9d1;padding:18px 0}.batch4 details{border-top:1px solid #ccd9d1;padding:18px 0}.batch4 summary{font-size:17px;cursor:pointer}.batch4 figcaption{font-size:15px;line-height:1.9;border-top:1px solid #ccd9d1;padding-top:18px;overflow-wrap:anywhere}.batch4 nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;margin-top:18px}.batch4 a{color:#146d61}@media(max-width:700px){.batch4{padding:16px}.batch4 h3{font-size:22px}.batch4 .b4-pair{grid-template-columns:1fr;gap:20px}.batch4[data-batch4=E27] .b4-pair{display:none}.batch4 .b4-mobile,.batch4 .b4-mobile-details{display:block}.batch4 p,.batch4 .b4-warning{font-size:17px}}@media print{.batch4 button{display:none}}'''
JS='''document.querySelectorAll('[data-batch4]').forEach(root=>{const code=root.dataset.batch4,lg=root.lang,B='/assets/visuals/explanatory-early-v4/';let n=code==='E27'?4:512,focus='whole',where='target';const press=(a,b)=>root.querySelectorAll('['+a+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const img=(s,name)=>root.querySelectorAll(s).forEach(x=>x.src=B+name);root.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{if(code==='E27'){if(b.hasAttribute('data-cutoff')){n=Number(b.dataset.cutoff);press('data-cutoff',b);}else{focus=b.dataset.scope;press('data-scope',b);}img('[data-means],[data-detail-means]',`E27-${lg}-${n}-means.svg`);img('[data-energy],[data-detail-energy]',`E27-${lg}-${n}-energy.svg`);img('[data-scope-scene]',`E27-${lg}-${n}-${focus}.svg`);img('[data-compact]',`E27-${lg}-${n}-compact.svg`);}else{if(b.hasAttribute('data-sample-n')){n=Number(b.dataset.sampleN);press('data-sample-n',b);}else{where=b.dataset.recordType;press('data-record-type',b);}const m=window.BATCH4_TILT[n];img('[data-event]',`E29-${lg}-${n}-event.svg`);img('[data-record]',`E29-${lg}-${n}-${where}-record.svg`);img('[data-rate]',`E29-${lg}-${n}-${where}-rate.svg`);root.querySelector('[data-event-definition]').textContent=(lg==='zh'?'公平硬币P；正面率3/4的Q。':'P: fair coin; Q: head probability 3/4. ')+`A${n}: ${m.lo}≤K≤${m.hi}, δ=1/${m.delta_denominator}.`;root.querySelector('[data-finite-rate]').textContent=(lg==='zh'?'有限事件率 −log Pₙ(Aₙ)/n ≈ ':'Finite event rate −log Pn(An)/n ≈ ')+m.rate+'; '+(lg==='zh'?'渐近D ≈ ':'limiting D ≈ ')+m.D;}}));});'''
def main():
 A.mkdir(parents=True,exist_ok=True);rows=[]
 for code,fn in [('E27',e27),('E29',e29)]:
  slug,sec,zh,en=META[code]
  for lg in ['zh','en']:
   title=tr(lg,zh,en);body,cap,panes=fn(lg);static(code,lg,title,cap,panes)
   frag=f'<figure class="batch4" id="visual-{code}" data-batch4="{code}" lang="{lg}"><header><span>{code}</span><h3>{title}</h3></header>{body}<figcaption id="visual-{code}-end">{cap}</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
   rows.append(dict(id=code,lang=lg,chapter=int(slug[:2]),slug=slug,section=sec,coverage_sections=['27.5','27.6'] if code=='E27' else ['29.7'],title=title,html=frag,condition=cap,asset_base=BASE,status='author visual review pending',kind='new explanatory candidate'))
 models={str(n):dict(n=n,lo=tilt(n)['lo'],hi=tilt(n)['hi'],delta_denominator=tilt(n)['delta'].denominator,P=str(tilt(n)['P']),Q=str(tilt(n)['Q']),rate=f'{tilt(n)["rate"]:.5f}',D=f'{tilt(n)["D"]:.5f}') for n in [64,512,4096]}
 (A/'figures.css').write_text(CSS,encoding='utf-8',newline='\n');(A/'interactions.js').write_text('window.BATCH4_TILT='+json.dumps(models)+';\n'+JS,encoding='utf-8',newline='\n')
 (R/'publication/explanatory-early-batch4-working.json').write_text(json.dumps(dict(source_commit=SOURCE,automatic_formal_site_injection=False,canonical_manuscript_changes=False,adopted_and_protected=['E22','E28','E14','E30','E39'],figures=rows),ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
 print('Only E27/E29 bilingual candidate assets generated')
if __name__=='__main__':main()
