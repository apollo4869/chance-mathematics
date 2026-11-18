"""Five new exact visual models and a structural revision of E24; no source edits."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb,sqrt,exp,pi
import json
from .pilot_shapes import Svg,tr,E,INK,TEAL,PALE,WARM,GRAY,RULE
from .volume5 import buttons,wrap_caption
from .early_pilots import path24,clock24

R=Path(__file__).resolve().parents[2]
A=R/'assets/visuals/explanatory-early-v2';BASE='/assets/visuals/explanatory-early-v2/'
META={
'E12':('12-infinite-sums','12.2','每条越界记录，只归入一格','Each crossing record belongs to one bin'),
'E13':('13-rare-events','13.14','空格不是少了一点概率','A forbidden site is not a small probability'),
'E14':('14-arrays-and-stability','14.3','方差分散了，大跳仍可能留下','Dispersed variance can still leave jumps'),
'E17':('17-markov-chains','17.2','压缩过去，不能合并不同的预测','Compress the past, preserve the prediction'),
'E30':('30-predictability','30.1','同样在跳点取1，时间规则却不同','Same value at arrivals, different time rules'),
'E24':('24-path-convergence','24.13','对齐一次跳跃，不能删除一次往返','Align a jump; never erase a pulse')}

def save(s,name,title):
 (A/name).write_text(s.document(title),encoding='utf-8',newline='\n');return name
def image(name,alt,attr=''):return f'<img class="ex-svg" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def p(txt,cls=''):return f'<p class="{cls}">{txt}</p>'
def panel(title,img,result='',attr=''):
 return f'<section class="b2-panel"><h4>{title}</h4>{img}'+(f'<p class="b2-result" {attr}>{result}</p>' if result else '')+'</section>'
def pair(parts):return '<div class="b2-pair">'+''.join(parts)+'</div>'
def nest(s,t,x,y,w,h):s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {t.w} {t.h}">{t.fragment()}</svg>')
def tau(bits,u=2):
 v=0
 for k,b in enumerate(bits,1):
  v+=b
  if abs(v)>=u:return k
 return 0

def cross_scene(lg,focus='all'):
 s=Svg(360,450)
 bins=[(2,8),(4,4),(0,4)];words=list(product([1,-1],repeat=4))
 for group,(hit,count) in enumerate(bins):
  y=36+group*139;active=focus=='all' or str(hit)==focus
  s.text(12,y,tr(lg,'未越界' if hit==0 else f'首次在第{hit}步','No crossing' if not hit else f'First crossing: step {hit}'),19,INK if active else GRAY,weight='bold')
  s.text(344,y,f'{count}/16',20,TEAL if active else GRAY,anchor='end')
  for j,b in enumerate([b for b in words if tau(b)==hit]):
   x=12+(j%4)*86;yy=y+15+(j//4)*43
   s.rect(x,yy,78,34,PALE if active and hit else '#f5f4ed',RULE)
   for i,v in enumerate(b):
    on=active and hit and i<hit;s.text(x+12+i*17,yy+23,'+' if v==1 else '−',20,TEAL if on else GRAY,anchor='middle',weight='bold' if on else 'normal')
 s.text(180,442,tr(lg,'深色到首次越界为止；浅色是未来','Dark: through first crossing; pale: future'),16,anchor='middle')
 return s

def tails_scene(lg):
 s=Svg(360,300);s.text(180,30,tr(lg,'已经看到 ++，S₂=2','After ++, S₂=2'),20,anchor='middle')
 s.text(180,53,tr(lg,'下读终点平方 S₄²','Read terminal square S₄² below'),15,GRAY,anchor='middle')
 for j,(tail,sq) in enumerate([('++',16),('+−',4),('−+',4),('−−',0)]):
  x=45+j*88;s.text(x,78,tail,23,anchor='middle');s.arrow(x,90,x,122);s.circle(x,153,25,TEAL,'white');s.text(x,161,str(sq),24,anchor='middle');s.text(x,207,'1/4',18,GRAY,anchor='middle')
 s.text(180,251,'(16 + 4 + 4 + 0) / 4 = 6',21,anchor='middle')
 s.text(180,284,tr(lg,'终点可回0，条件平方均值仍≥4','An endpoint may be 0; mean square is ≥4'),16,WARM,anchor='middle');return s

def e12(lg):
 for f in ['all','2','4','0']:save(cross_scene(lg,f),f'E12-{lg}-{f}.svg','All sixteen equally likely records, sorted by first crossing')
 save(tails_scene(lg),f'E12-{lg}-tails.svg','A centered future does not cancel the crossing in conditional mean square')
 body=p(tr(lg,'途中越界以后，终点仍可能回到0。先按首次越界分片，每条记录就只被计算一次。','A record may cross and still finish at 0. Sorting by its first crossing counts it only once.'))
 body+=buttons('data-bin',[(a,tr(lg,z,e)) for a,z,e in [('all','全部记录','All records'),('2','首次第2步','First at step 2'),('4','首次第4步','First at step 4'),('0','未越界','No crossing')]],'all')
 body+=pair([panel(tr(lg,'16份等概率的记录','16 equally likely records'),image(f'E12-{lg}-all.svg','Sixteen four-step records in disjoint crossing bins','data-bin-scene')),panel(tr(lg,'把同一前缀的未来放在一起','Average the futures of one prefix'),image(f'E12-{lg}-tails.svg','Four possible futures after the prefix ++'))])
 cap=tr(lg,'有限精确模型：4次独立公平±1增量，S₀=0，阈值u=2。16条记录等概率；首次越界第2步、第4步及不越界分别8、4、4条。每条记录归属唯一一格，深色标出截至首次越界的信息。给定前缀++，四种未来各1/4，S₄²依次16、4、4、0，均值6≥S₂²=4；不是每条路径上S₄²≥S₂²。一般证明用Aₖ与未来独立、未来均值0消去交叉项，再把互斥事件求和；图不借用可选停止。','Exact finite model: four independent fair ±1 increments, S0=0, threshold u=2. The 16 equiprobable records split into 8 first crossing at step 2, 4 at step 4, and 4 never crossing. Dark signs mark information through the first crossing. Given ++, the four equiprobable futures give S4²=16,4,4,0, with mean 6≥S2²=4. This is not a pathwise inequality. The general proof cancels the cross term using an independent centered future and sums disjoint events; no optional stopping is used.')
 return body,cap,[('16 records',cross_scene(lg)),('One prefix, four futures',tails_scene(lg))]

def lattice(lg,n):
 s=Svg(370,250);sx=lambda k:185+k*24
 s.text(185,26,f'n = {n}',21,anchor='middle')
 s.line(26,140,344,140,RULE,1)
 for k in range(-6,7):
  allowed=abs(k)<=n and (n+k)%2==0
  if allowed:
   prob=comb(n,(n+k)//2)/2**n;rad=23*sqrt(prob/.375)
   s.circle(sx(k),99,rad,TEAL,PALE);s.text(sx(k),105,f'{comb(n,(n+k)//2)}',15,anchor='middle')
  else:
   s.circle(sx(k),140,3,GRAY,'white')
   if abs(k)<=n:s.line(sx(k)-4,136,sx(k)+4,144,WARM,1.5)
  s.text(sx(k),168,str(k),15,GRAY,anchor='middle')
 for k in range(-n,n+1,2):s.rect(sx(k)-23,186,46,14,PALE,TEAL)
 s.text(185,224,tr(lg,f'圆中数字 / {2**n}；圆面积 ∝ 概率',f'Numerator / {2**n}; disk area ∝ probability'),16,anchor='middle')
 s.text(185,246,tr(lg,'带宽2的格子；允许位置随奇偶移动','Cells of width 2; allowed sites shift with parity'),16,anchor='middle');return s

def cell_scene(lg,n,width=2):
 s=Svg(370,220);k=n%2;standard=k/sqrt(n);density=exp(-standard**2/2)/sqrt(2*pi);exact=comb(n,(n+k)//2)/2**n
 # All coordinates are standardized. The plotted rectangle is the local-density approximation.
 unit=110;cx=185;w=width/sqrt(n)*unit;h=density*200
 s.line(24,126,346,126,RULE,1);s.rect(cx-w/2,126-h,w,h,PALE if width==2 else '#f4e5da',TEAL if width==2 else WARM)
 s.text(cx,126-h-14,'φ('+('0' if not k else f'1/√{n}')+')',20,anchor='middle')
 s.line(cx-w/2,145,cx+w/2,145,TEAL if width==2 else WARM,2);s.text(cx,174,f'{width}/√{n}',21,anchor='middle')
 s.text(185,208,tr(lg,f'局部近似 {width*density/sqrt(n):.3f}；精确 {exact:.3f}',f'Local approx. {width*density/sqrt(n):.3f}; exact {exact:.3f}'),18,anchor='middle');return s

def e13(lg):
 for n in [4,5,6]:
  save(lattice(lg,n),f'E13-{lg}-{n}.svg','Parity shifts the actual support, whose maximal span is two')
  for w in [1,2]:save(cell_scene(lg,n,w),f'E13-{lg}-{n}-w{w}.svg','A local Gaussian density must be multiplied by the actual standardized lattice width')
 body=p(tr(lg,'±1走n步，只能落在与n同奇偶的位置。Gaussian密度给出的不是这些点的概率；还要乘真正的格宽。','After n steps of ±1, only sites of the same parity as n are possible. A Gaussian density needs the actual cell width to approximate an atom.'))
 body+=buttons('data-lattice-n',[(str(n),f'n={n}') for n in [4,5,6]],'4')
 body+=pair([panel(tr(lg,'精确离散质量','Exact discrete masses'),image(f'E13-{lg}-4.svg','Parity lattice with exact binomial masses','data-lattice-scene')),panel(tr(lg,'密度 × 标准化格宽','Density × standardized width'),image(f'E13-{lg}-4-w2.svg','Local-density rectangle with the selected lattice width','data-cell-scene'))])
 body+=buttons('data-cell-width',[('2',tr(lg,'实际格宽2','Actual width 2')),('1',tr(lg,'误用格宽1','Incorrect width 1'))],'2')
 cap=tr(lg,'Xⱼ独立公平取±1，均值0、方差1、最大跨度h=2，a=−1。Sₙ支撑在−n+2ℤ；圆的面积按精确二项概率缩放，圆中为分子，分母2ⁿ。下排相邻允许格子的宽度为2。右图在k=n mod 2处，展示φ(k/√n)乘h/√n的矩形，坐标已标准化；有限n时只是局部近似，并非精确等式。h=1会少一半，奇偶不允许位置的概率严格为0。切换n展示格子的平移，不宣称只用三帧证明局部CLT；一般有限方差一致误差见正文。','Independent fair ±1 variables have mean 0, variance 1 and maximal span h=2, with a=−1. Sn is supported on −n+2Z. Disk areas follow exact binomial masses, with displayed numerator over 2^n; adjacent allowed cells have width 2. At k=n mod 2, the right rectangle has height φ(k/√n) and width h/√n in standardized coordinates. At finite n this is only a local approximation. Using h=1 halves it; forbidden-parity masses are exactly zero. The three n settings illustrate translation of the lattice, not a proof of the local CLT.')
 return body,cap,[('Even n=4',lattice(lg,4)),('Odd n=5',lattice(lg,5)),('Actual standardized width',cell_scene(lg,4,2))]

def atoms(lg,n,rare):
 s=Svg(360,290);amp=1 if rare else 1/sqrt(n);prob=1/(2*n) if rare else .5
 # The atom radii encode probabilities; their positions encode amplitude on a fixed scale.
 y=95;center=180;unit=110
 s.rect(center-55,45,110,100,'#eff3ee')
 s.line(30,y,330,y,RULE,1)
 for value,q in [(-amp,prob),(0,1-2*prob),(amp,prob)]:
  if q>0:
   cy=y if rare else (65 if value<0 else 125)
   s.line(center+value*unit,cy,center+value*unit,y,GRAY,1)
   s.circle(center+value*unit,cy,29*sqrt(q),TEAL if not value else WARM,'#f1e6db' if value else '#e9eeea')
 for x,lab in [(70,'−1'),(125,'−1/2'),(180,'0'),(235,'1/2'),(290,'1')]:s.text(x,173,lab,16,GRAY,anchor='middle')
 s.text(180,25,tr(lg,'一份增量的概率原子','Probability atoms of one increment'),19,anchor='middle')
 s.text(180,207,tr(lg,f'每个非零原子：1/{2*n}' if rare else '两个原子：各1/2',f'Each nonzero atom: 1/{2*n}' if rare else 'Two atoms, probability 1/2 each'),18,anchor='middle')
 symbol='X' if rare else 'Y'
 for x,label in [(28,symbol+'ₙ₁'),(110,symbol+'ₙ₂'),(272,symbol+'ₙₙ')]:
  s.rect(x,228,60,38,PALE,TEAL);s.text(x+30,254,label,19,anchor='middle')
 s.text(230,254,'…',24,GRAY,anchor='middle')
 s.text(180,291,tr(lg,f'一行恰有 n={n} 项；省略中间项',f'Exactly n={n} terms; middle terms omitted'),16,anchor='middle');return s

def e14(lg):
 for n in [4,16,64]:
  for m in ['rare','small']:save(atoms(lg,n,m=='rare'),f'E14-{lg}-{n}-{m}.svg','Fixed-amplitude rare jumps versus genuinely small increments')
 body=p(tr(lg,'两行总方差都为1，每项方差都为1/n。可是一行把方差留在±1，另一行把取值缩进了0附近。','Both rows have total variance 1 and variance 1/n per term. One keeps its nonzero atoms at ±1; the other brings them toward 0.'))
 body+=buttons('data-array-n',[(str(n),f'n={n}') for n in [4,16,64]],'16')
 body+=pair([panel(tr(lg,'稀少，但大小不缩','Rare, fixed-size jumps'),image(f'E14-{lg}-16-rare.svg','Rare atoms stay at minus and plus one','data-rare-scene'),tr(lg,'阈值外二阶贡献：1','Second moment outside threshold: 1')),panel(tr(lg,'每一项真正变小','Every increment gets small'),image(f'E14-{lg}-16-small.svg','Fair small increments move toward zero','data-small-scene'),tr(lg,'阈值外二阶贡献：0','Second moment outside threshold: 0'))])
 body+=p(tr(lg,'淡带：|x|≤1/2。切换n，观察原子的位置和面积分别怎样变化。','Pale band: |x|≤1/2. Change n to separate atom positions from probability areas.'),'b2-note')
 cap=tr(lg,'每行内部独立。左：P(Xₙₖ=±1)=1/(2n)，P(0)=1−1/n。右：P(Yₙₖ=±1/√n)=1/2。两者均中心化、总方差1，Feller最大方差1/n→0；固定ε=1/2，所有所示n≥4时Lindeberg量分别1与0（使用严格>）。左整行有至少一笔非零的概率1−(1−1/n)ⁿ→1−e⁻¹，但非零项可能互相抵消；不把这个概率等同于总和非零。左总和趋于带±1标记、强度1的复合Poisson，右趋于标准Gaussian。圆面积表示概率，横位置表示取值；方框只列第1、第2与第n项，中间项由省略号表示；一行恰有n项。阴影只标阈值，不是概率密度。','Terms are independent within each row. Left: P(Xnk=±1)=1/(2n), P(0)=1−1/n. Right: P(Ynk=±1/√n)=1/2. Both are centered with total variance 1 and maximal variance 1/n→0. At fixed ε=1/2, their Lindeberg quantities are 1 and 0 for all displayed n≥4 (strict >). On the left, the probability of at least one nonzero term tends to 1−e⁻1; cancellation means this is not the probability of a nonzero sum. Its sum tends to compound Poisson with rate 1 and fair ±1 marks; the right sum tends to a standard Gaussian. Disk areas are probabilities and horizontal positions are values. Boxes label terms 1, 2 and n, with an ellipsis for the omitted middle terms; each row has exactly n terms. Shading marks a threshold, not density.')
 return body,cap,[('Fixed-size rare jumps',atoms(lg,16,True)),('Small increments',atoms(lg,16,False))]

def state_scene(lg,posterior):
 s=Svg(390,370);ys=[65,140,230,305];labs=['00','10','01','11'];dest=[65,185,185,305] if posterior else [105,105,265,265]
 s.text(33,24,tr(lg,'历史','History'),17,anchor='middle');s.text(180,24,tr(lg,'保留状态','Retained state'),17,anchor='middle');s.text(326,24,tr(lg,'下一次为1','Next is 1'),17,anchor='middle')
 for i,(lab,y) in enumerate(zip(labs,ys)):
  s.text(33,y+7,lab,24,anchor='middle');s.arrow(58,y,133,dest[i],TEAL if posterior else WARM)
 if posterior:
  for y,q,pred in [(65,'1/10','3/10'),(185,'1/2','1/2'),(305,'9/10','7/10')]:
   s.circle(178,y,35,TEAL,PALE);s.text(178,y+7,q,20,anchor='middle');s.arrow(215,y,279,y);s.text(327,y+8,pred,26,anchor='middle')
 else:
  for y,b in [(105,'0'),(265,'1')]:
   s.circle(178,y,33,WARM,'#f3e9df');s.text(178,y+9,b,27,anchor='middle')
  for sy,ey,pred in [(105,65,'3/10'),(105,140,'1/2'),(265,230,'1/2'),(265,305,'7/10')]:
   s.arrow(215,sy,278,ey,WARM);s.text(327,ey+8,pred,25,WARM,anchor='middle')
 s.text(195,361,tr(lg,'不同历史可合并：但不能丢掉预测差别','Merge histories only when predictions agree'),16,anchor='middle');return s

def e17(lg):
 for m in ['last','posterior']:save(state_scene(lg,m=='posterior'),f'E17-{lg}-{m}.svg','A posterior keeps predictive distinctions that the last bit loses')
 body=p(tr(lg,'00和10的末位都是0，下一次为1的概率却不同。01与10末位不同，却可以共享同一个后验状态。','00 and 10 end in the same bit, yet predict differently. 01 and 10 end differently, yet share the same posterior state.'))
 body+=buttons('data-state',[('last',tr(lg,'只留末位','Keep last bit')),('posterior',tr(lg,'保留后验q','Keep posterior q'))],'last')
 body+='<div class="b2-single wide">'+image(f'E17-{lg}-last.svg','Four histories mapped into the selected information states','data-state-scene')+'</div>'
 body+='<output data-reading>'+tr(lg,'同一个“0”分出两个预测，压缩丢失了信息。','The same state 0 leads to two forecasts: information was lost.')+'</output>'
 cap=tr(lg,'Θ先等概率取1/4、3/4，给定Θ后各次Bernoulli(Θ)独立。q=P(Θ=3/4|历史)。长度2的00、10、01、11依次给q=1/10、1/2、1/2、9/10；预测w(q)=1/4+q/2依次3/10、1/2、1/2、7/10。箭头表示信息映射，不表示历史等概率。只保留末位不能恢复原预测；后验则可依正文T₀、T₁更新并给出Markov核。图没有断言所有模型都具有一维或唯一最小状态，也没有把未画出的未来独立性当作图形结论。','Choose Θ=1/4 or 3/4 with equal probability, then sample conditionally iid Bernoulli(Θ). For histories 00,10,01,11, q=P(Θ=3/4|history) equals 1/10,1/2,1/2,9/10; w(q)=1/4+q/2 gives predictions 3/10,1/2,1/2,7/10. Arrows are information maps, not equiprobable histories. The last bit cannot recover the original forecast; the posterior updates via the text’s T0,T1 and Markov kernel. No universal one-dimensional or unique minimal state is claimed, nor is future independence inferred from the picture.')
 return body,cap,[('Last bit: information lost',state_scene(lg,False)),('Posterior: prediction retained',state_scene(lg,True))]

ARRIVALS={0:[],2:[.7,2.1],3:[.4,1.4,2.7]}
def arrival_scene(lg,after=False,count=2):
 s=Svg(370,275);sx=lambda t:38+98*t
 s.text(185,26,tr(lg,'同一份到达记录，K=3、λ=1','Same arrivals, K=3 and λ=1'),18,anchor='middle')
 s.line(38,76,332,76,GRAY,1)
 for t in ARRIVALS[count]:s.circle(sx(t),76,5,INK)
 s.text(12,81,'N',17)
 for t in [0,1,2,3]:s.text(sx(t),106,str(t),16,GRAY,anchor='middle')
 s.text(12,154,'H',18)
 if not after:
  s.rect(38,130,294,35,PALE,TEAL);s.circle(38,148,4,TEAL,'white');s.circle(332,148,4,TEAL)
 else:
  s.line(38,148,332,148,RULE,1)
  for t in ARRIVALS[count]:s.circle(sx(t),148,7,WARM)
 for t in ARRIVALS[count]:s.line(sx(t),83,sx(t),126,WARM if after else TEAL,1,'3 4')
 s.text(185,201,tr(lg,'只在刚发生的跳点为1' if after else '在整个(0,3]上预先取1','1 only at the just-observed jumps' if after else 'Choose 1 throughout (0,3] in advance'),18,WARM if after else TEAL,anchor='middle')
 s.text(185,238,f'dN: {count}     dt: '+('0' if after else '3'),25,anchor='middle')
 s.text(185,269,tr(lg,'点表示精确时刻，没有正长度','Dots are exact instants, not intervals'),16,GRAY,anchor='middle');return s

def e30(lg):
 for c in [0,2,3]:
  for m in ['pre','after']:save(arrival_scene(lg,m=='after',c),f'E30-{lg}-{m}-{c}.svg','The same arrival weights but different Lebesgue-time costs')
 body=p(tr(lg,'到达时都取值1，不代表使用了同一份信息。全程事先选1，与看见跳跃才取1，时间测度读到的完全不同。','Both rules take value 1 at arrivals. But choosing 1 in advance and selecting only observed jump instants have different time costs.'))
 body+=buttons('data-arrival-count',[(str(c),tr(lg,f'示意记录：{c}次',f'Record: {c} arrivals')) for c in [0,2,3]],'2')
 body+=pair([panel(tr(lg,'事前：全程取1','Before: choose 1 throughout'),image(f'E30-{lg}-pre-2.svg','A predictable constant choice fills the whole time band','data-pre-scene'),tr(lg,'总体期望：0','Population expectation: 0')),panel(tr(lg,'事后：只选刚发生的跳点','After: select observed jump instants'),image(f'E30-{lg}-after-2.svg','Jump-only choices are isolated instants of zero time length','data-after-scene'),tr(lg,'总体期望：3','Population expectation: 3'))])
 body+='<output data-reading>'+tr(lg,'这条记录的补偿收益：事前2−3=−1；事后2−0=2。','Compensated payoff on this record: before 2−3=−1; after 2−0=2.')+'</output>'
 body+=p(tr(lg,'右侧是事后选择跳点的路径 Stieltjes 计算，不是合法的可预测事前策略，不能据此套用可预测鞅积分的公平性。','The right-hand payoff is a pathwise Stieltjes calculation selected after jumps occur, not a legitimate predictable strategy chosen beforehand. The predictable martingale integral’s fairness does not apply.'))
 cap=tr(lg,'率1 Poisson过程、通常增广自然滤过、K=3。左规则H≡1在(0,3]可预测，路径收益∫H dN−∫H dt=N₃−3，期望0。右规则Hₜ=ΔNₜ适应且可选，但不可预测，不是合法的可预测事前策略；这里只计算路径Stieltjes收益，未把它定义为可预测随机积分。路径收益N₃−0，期望3。右图圆点是零长度时刻，不是窄的正长度区间；有限跳点对dt零测，对dN却各有质量1。三条手选记录只展示路径计算，未赋等概率、不是模拟、不能用来估计期望。总体期望来自E N₃=3，且自然滤过和无同时重跳的Poisson模型不可省略；未把此结论推广到任意滤过。','Rate-one Poisson process with its usual augmented natural filtration and K=3. The predictable choice H≡1 on (0,3] gives pathwise payoff N3−3, of expectation 0. Ht=ΔNt is adapted and optional but not predictable, so it is not a legitimate strategy chosen beforehand. Only its pathwise Stieltjes payoff is computed here, not a predictable stochastic integral; it gives N3−0, of expectation 3. Dots denote zero-duration instants, not narrow positive-length intervals. Finitely many jumps have zero dt mass but unit dN mass each. The three hand-chosen records illustrate pathwise calculations only; they are not equiprobable or simulated estimates of expectations. Expectations use E N3=3. The natural filtration and simple Poisson jumps matter; no assertion for every filtration is made.')
 return body,cap,[('Predictable rule',arrival_scene(lg)),('Jump-only rule',arrival_scene(lg,True))]

def comparison24(lg,mode='jump',key=4,aligned=True):
 s=Svg(360,360);d=1/key
 s.text(180,24,tr(lg,'原记录' if aligned else '参考与原记录','Original record' if aligned else 'Reference and record'),18,anchor='middle')
 nest(s,path24(lg,d,mode,False),10,35,340,155)
 s.arrow(180,194,180,220,TEAL if mode=='jump' else WARM)
 s.text(180,246,tr(lg,'同一时钟对齐后' if aligned else '尚未对齐','After the same clock' if aligned else 'Not yet aligned'),18,anchor='middle')
 # Tighten the lower viewport to omit repeated legend but preserve every endpoint.
 t=path24(lg,d,mode,aligned);nest(s,t,10,255,340,155);s.h=418
 return s

def e24(lg):
 for k in [4,8,16]:
  save(clock24(lg,1/k),f'E24-{lg}-clock-{k}.svg','Reference t maps to original time lambda(t)')
  for m in ['jump','pulse']:
   for a in [0,1]:save(comparison24(lg,m,k,bool(a)),f'E24-{lg}-{k}-{m}-{a}.svg','Compare a shifted jump with a non-removable pulse')
 body=p(tr(lg,'两种变化都只发生在很短的时间里。左边只需移动发生时刻；右边却真的走到了高度1，再返回。','Both changes occupy little time. The left only shifts when a jump occurs. The right actually visits height 1 and returns.'))
 body+=buttons('data-clock-key',[(str(k),f'δ=1/{k}') for k in [4,8,16]],'4')
 body+=pair([panel(tr(lg,'时间错位，可以对齐','A time shift can be aligned'),image(f'E24-{lg}-4-jump-1.svg','Before and after a shifted step is aligned','data-jump-scene'),tr(lg,'取值误差 0','Value error 0'),'data-jump-result'),panel(tr(lg,'短暂往返，不能删除','A brief pulse cannot be erased'),image(f'E24-{lg}-4-pulse-1.svg','Before and after a pulse still has height one','data-pulse-scene'),tr(lg,'取值误差 1','Value error 1'))])
 body+=buttons('data-clock-apply',[('1',tr(lg,'使用同一时钟','Apply the same clock')),('0',tr(lg,'撤去时钟','Remove clock'))],'1')
 body+='<details class="b2-tech"><summary>'+tr(lg,'第二层：时钟方向与J₁条件','Technical layer: clock direction and J₁')+'</summary><div class="b2-single">'+image(f'E24-{lg}-clock-4.svg','The increasing homeomorphism fixes 0 and 1 and maps a to a plus delta','data-clock-scene')+'</div>'+p(tr(lg,'上方参考时刻t → 下方原记录λ(t)。比较的是xδ∘λ与x；同一λ用于右侧往返与零函数的比较。','Reference time t (top) → original time λ(t) (bottom). Compare xδ∘λ with x; use the same λ to compare the pulse with zero.'))+'</details>'
 cap=tr(lg,'a=1/2，0<δ≤1/4。左x=1_[a,1]、xδ=1_[a+δ,1]；λ是经过(0,0),(a,a+δ),(1,1)的递增分段线性连续同胚。‖λ−id‖∞=δ，xδ∘λ=x。右zδ=1_[a+δ,a+δ+δ²)，参考是零函数；同一λ将其支撑变为[a,a+δ²(1−a)/(1−a−δ))。任何满射时间同胚都保留其上确界1，故不仅这幅图中的λ不能删除它。所有端点用实心/空心区别右连续取值；灰虚线是参考，实线是当前，不画竖直插值。δ→0时，左在J₁收敛，右不在J₁趋零。把发生时刻接近与振幅小分开，才是两场景的差别。','Let a=1/2, 0<δ≤1/4. Left: x=1_[a,1], xδ=1_[a+δ,1]. The piecewise-linear increasing continuous homeomorphism λ passes through (0,0),(a,a+δ),(1,1). Thus ‖λ−id‖∞=δ and xδ∘λ=x. Right: zδ=1_[a+δ,a+δ+δ²), compared with zero. The same λ moves its support to [a,a+δ²(1−a)/(1−a−δ)). Every onto time homeomorphism preserves supremum 1; the impossibility is not inferred from one chosen clock. Filled/open endpoints specify right-continuous values; gray dashes are the reference, solid lines the record; no vertical interpolation is drawn. As δ→0 the left converges in J1, while the right cannot tend to zero in J1. Small timing error and small amplitude error are different requirements.')
 return body,cap,[('Shifted jump: error 0',comparison24(lg,'jump')),('Pulse: error 1',comparison24(lg,'pulse')),('Clock: reference to record',clock24(lg,.25))]

FUNCS={'E12':e12,'E13':e13,'E14':e14,'E17':e17,'E30':e30,'E24':e24}

def static(code,lg,title,cap,panes):
 # Native two-column math plates; no screenshots of interactive controls.
 cols=2;cellw=420;top=110;y=top;s=Svg(900,1800);s.rect(0,0,900,1800,'white');s.text(30,45,title,26,weight='bold')
 for row in range((len(panes)+1)//2):
  group=panes[2*row:2*row+2];height=max(t.h*min(1,cellw/t.w) for _,t in group)
  for j,(label,t) in enumerate(group):
   x=25+450*j;s.text(x, y-16,tr(lg,{'16 records':'16条记录','One prefix, four futures':'一个前缀，四种未来','Even n=4':'偶数n=4','Odd n=5':'奇数n=5','Actual standardized width':'正确的标准化格宽','Fixed-size rare jumps':'大小不缩的稀有跳跃','Small increments':'真正变小的增量','Last bit: information lost':'只留末位：信息丢失','Posterior: prediction retained':'保留后验：预测完整','Predictable rule':'可预测规则','Jump-only rule':'只选已发生的跳点','Shifted jump: error 0':'错位单跳：误差0','Pulse: error 1':'短暂往返：误差1','Clock: reference to record':'时钟：从参考到原记录'}.get(label,label),label),19,weight='bold');nest(s,t,x,y,cellw,t.h*min(1,cellw/t.w))
  y+=height+65
 s.line(25,y,875,y,RULE,1);lines=wrap_caption(cap,lg)
 for i,line in enumerate(lines):s.text(25,y+30+24*i,line,17,GRAY)
 s.h=y+65+24*len(lines);s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>'
 save(s,f'{code}.{lg}.svg',title)

CSS='''
.batch2{color:#173f39;background:#fffefa;border:1px solid #ccd9d1;padding:28px;margin:2rem 0;font:18px/1.75 "Microsoft YaHei","Noto Sans SC",sans-serif;box-sizing:border-box}.batch2 *{box-sizing:border-box}.batch2 header{display:flex;gap:16px;align-items:baseline}.batch2 header>span{font-size:13px;color:#65756e}.batch2 h3{font-size:26px;margin:0 0 18px;line-height:1.4}.batch2 p{font-size:18px;line-height:1.75;color:inherit}.batch2 .b2-pair{display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:start;margin:20px 0}.batch2 h4{font-size:20px;font-weight:500;line-height:1.5;text-align:center;margin:0 0 12px}.batch2 img.ex-svg{display:block;width:100%;height:auto;max-height:none!important;box-shadow:none;border:0;margin:0;object-fit:contain}.batch2 .b2-single{max-width:370px;margin:18px auto}.batch2 .b2-single.wide{max-width:510px}.batch2 .b2-result{font-size:22px;color:#16776d;text-align:center;border-top:1px solid #ccd9d1;padding:15px 0;margin:8px 0}.batch2 .b2-panel:nth-child(2) .b2-result{color:#a45b30}.batch2 .v5-controls{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:18px 0}.batch2 button{font:17px/1.4 inherit;color:#173f39;background:#fffefa;padding:9px 12px;border:1px solid #bdcbc2;border-radius:4px;cursor:pointer}.batch2 button[aria-pressed=true]{background:#eaf2ee;border:2px solid #16776d;padding:8px 11px}.batch2 output{display:block;border-top:1px solid #ccd9d1;padding:18px 0;font-size:18px}.batch2 figcaption{border-top:1px solid #ccd9d1;padding-top:18px;font-size:15px;line-height:1.85;color:#52665b;overflow-wrap:anywhere}.batch2 nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;margin-top:16px}.batch2 a{color:#146d61}.batch2 .b2-tech{border-top:1px solid #ccd9d1;padding:18px 0}.batch2 summary{cursor:pointer}.batch2 .b2-note{font-size:16px;color:#65756e}
@media(max-width:700px){.batch2{padding:16px;margin:1.2rem 0}.batch2 header{display:block}.batch2 h3{font-size:22px;margin-top:5px}.batch2 .b2-pair{grid-template-columns:1fr;gap:24px}.batch2 h4{font-size:18px}.batch2 p,.batch2 output{font-size:17px}.batch2 button{font-size:16px}.batch2 .b2-result{font-size:20px}.batch2[data-batch2=E24] .b2-pair{grid-template-columns:1fr 1fr;gap:12px}.batch2[data-batch2=E24] .b2-pair img{display:none}.batch2[data-batch2=E24] .b2-pair h4{font-size:17px}.batch2[data-batch2=E24] .b2-result{font-size:18px}.batch2 .e24-mobile{display:block}.batch2[data-batch2=E24] .e24-mobile img{width:100%}}
@media(min-width:701px){.batch2 .e24-mobile{display:none}}
@media print{.batch2{border:0;padding:0;background:white}.batch2 button,.batch2 nav{display:none}}
'''

def mobile24(lg,key=4,aligned=True):
 # Two scenes remain beside each other, but redraw directly for narrow screens.
 s=Svg(340,255);d=1/key;a=.5;b=a+d
 for col,mode in enumerate(['jump','pulse']):
  ox=12+col*174;w=142;x=lambda t:ox+w*t;y0=154;y1=65
  s.line(ox,y0,ox+w,y0,GRAY,1,'4 4')
  if mode=='jump':s.line(x(a),y1,ox+w,y1,'#aabbb2',2,'4 4')
  start=a if aligned else b;end=None if mode=='jump' else (a+d*d*(1-a)/(1-b) if aligned else b+d*d)
  s.line(ox,y0,x(start),y0,TEAL if not end else WARM,2);s.circle(x(start),y0,4,TEAL if not end else WARM,'white');s.circle(x(start),y1,4,TEAL if not end else WARM)
  s.line(x(start),y1,x(end) if end else ox+w,y1,TEAL if not end else WARM,2)
  if end:s.circle(x(end),y1,4,WARM,'white');s.circle(x(end),y0,4,WARM);s.line(x(end),y0,ox+w,y0,WARM,2)
  s.text(ox+w/2,28,tr(lg,'对齐后' if aligned else '未对齐','Aligned' if aligned else 'Unaligned'),17,anchor='middle');s.text(ox+w/2,204,'0' if not end and aligned else '1',36,TEAL if not end else WARM,anchor='middle')
 s.text(170,246,tr(lg,'取值误差：左0，右仍1' if aligned else '取值误差：左右都是1','Value error: left 0, right 1' if aligned else 'Value error: both 1'),18,anchor='middle');return s

def main():
 A.mkdir(parents=True,exist_ok=True);rows=[]
 for code,meta in META.items():
  for lg in ['zh','en']:
   body,cap,panes=FUNCS[code](lg);title=meta[2 if lg=='zh' else 3]
   if code=='E24':
    for k in [4,8,16]:
     for a in [0,1]:save(mobile24(lg,k,bool(a)),f'E24-{lg}-mobile-{k}-{a}.svg','Jump and pulse compared on a compact redraw')
    body=body.replace(buttons('data-clock-apply',[('1',tr(lg,'使用同一时钟','Apply the same clock')),('0',tr(lg,'撤去时钟','Remove clock'))],'1'),'<div class="e24-mobile">'+image(f'E24-{lg}-mobile-4-1.svg','Compact comparison with actual value errors','data-compact-scene')+'</div>'+buttons('data-clock-apply',[('1',tr(lg,'使用同一时钟','Apply the same clock')),('0',tr(lg,'撤去时钟','Remove clock'))],'1'))
   static(code,lg,title,cap,panes)
   html=f'<figure class="batch2" id="visual-{code}" data-batch2="{code}" lang="{lg}"><header><span>{code}</span><h3>{E(title)}</h3></header>{body}<figcaption id="visual-{code}-end">{E(cap)}</figcaption><nav><a href="{BASE}{code}.{lg}.svg">{tr(lg,"完整静态SVG","Complete static SVG")}</a><a href="/print/{code}.{lg}.html">{tr(lg,"打印页","Print view")}</a></nav></figure>'
   rows.append(dict(id=code,chapter=int(meta[0][:2]),slug=meta[0],section=meta[1],title=title,lang=lg,html=html,condition=cap,status='author visual review pending',kind='structural revision' if code=='E24' else 'new explanation'))
 (A/'figures.css').write_text(CSS.replace('font:17px/1.4 inherit;','font-family:inherit;font-size:17px;line-height:1.4;')+'\n.batch2[data-batch2=E14] .b2-panel:first-child .b2-result{color:#a45b30}.batch2[data-batch2=E14] .b2-panel:nth-child(2) .b2-result{color:#16776d}\n',encoding='utf-8',newline='\n')
 (A/'interactions.js').write_text((Path(__file__).parent/'early_batch2_interactions.js').read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
 (R/'publication/explanatory-early-batch2-working.json').write_text(json.dumps(dict(canonical_manuscript_changes=False,automatic_formal_site_injection=False,figures=rows),ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
 print('Five new bilingual models and one E24 structural revision generated.')

if __name__=='__main__':main()
