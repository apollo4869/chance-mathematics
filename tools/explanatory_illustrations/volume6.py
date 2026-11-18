"""Five finite exact visual models; no mathematical manuscript writes."""
from pathlib import Path
import json,math
from .pilot_shapes import Svg,tr,E,INK,TEAL,WARM,GRAY,PALE,RULE
from .volume5 import buttons,wrap_caption
from .volume6_review import A,BASE,R,write,jsave
META={'V41':('41-ergodic-theory','41.9','移走开头，环境仍然留下','Shift the record; the environment stays'),'V44':('44-dirichlet-process','44.19','新开一桌，未必出现新值','A new table need not mean a new value'),'V45':('45-invariance','45.1','每个旋转保律，不等于任意选法保律','Each rotation preserves law; not every selection does'),'V46':('46-arrays','46.1','每行都一样，三角关系却不同','Same row laws, different triangles'),'V47':('47-partitions','47.7','剩余质量，不是最后一种颜色','Residual mass is not one more color')}
COLORS=[TEAL,WARM,'#6d6697']
def save(s,name,title):write(A/name,s.document(title))
def img(name,alt,attr=''):return f'<img src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def pair(a,b):return '<div class="v6-pair">'+a+b+'</div>'
def panel(title,body):return '<section><h4>'+title+'</h4>'+body+'</section>'
def nested(s,t,x,y,w,h):s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {t.w} {t.h}">{t.fragment()}</svg>')
def ribbon(s,x,y,w,q,label):
 s.rect(x,y,w*q,30,TEAL);s.rect(x+w*q,y,w*(1-q),30,'white',RULE);s.text(x,y-10,label,18);s.text(x+w,y+56,str(q),22,TEAL,anchor='end')
def environment(lg,q,offset):
 s=Svg(350,306);s.rect(94,12,162,44,PALE,TEAL);s.text(175,41,'Θ = '+('1/4' if q==.25 else '3/4'),24,anchor='middle');s.text(175,83,tr(lg,'同一环境，一直参与生成','The same environment keeps generating'),17,anchor='middle')
 s.arrow(175,94,175,115)
 seq=([0,0,1,0,0,1,0,0,1,0,0,0] if q==.25 else [1,1,0,1,1,0,1,1,1,0,1,1]);vals=seq[offset:offset+6]
 for j,v in enumerate(vals):
  x=20+52*j;s.rect(x,135,42,45,TEAL if v else 'white',TEAL);s.text(x+21,165,str(v),24,'white' if v else INK,anchor='middle');s.text(x+21,205,str(offset+j),14,GRAY,anchor='middle')
 s.text(175,246,tr(lg,f'当前窗口起点：{offset}',f'Window starts at index {offset}'),18,anchor='middle');s.text(175,282,tr(lg,'窗口变了，Θ没有变','The window changes; Θ does not'),20,TEAL,anchor='middle',weight='bold');return s

def averages(lg,q,offset):
 s=Svg(350,306);ribbon(s,22,55,306,.5,tr(lg,'把两种环境混在一起','Mix both environments'));s.text(175,144,'E X₀ = 1/2',24,anchor='middle')
 ribbon(s,22,211,306,q,tr(lg,'一条长记录留下的环境','This path retains its environment'));s.text(175,304,'lim AₙX₀ = Θ',25,TEAL,anchor='middle');return s

def tables(lg,mode,choice):
 s=Svg(350,300);labels=['a','b','c'] if mode=='diffuse' else ['z','z','z'];groups=[[1,2],[3],[]]
 if choice=='A':groups[0].append(4)
 elif choice=='B':groups[1].append(4)
 else:groups[2].append(4)
 for j,group in enumerate(groups):
  x=60+114*j;s.circle(x,118,34,COLORS[j],'white');s.text(x,126,['A','B','C'][j],24,COLORS[j],anchor='middle')
  for k,person in enumerate(group):
   dx=[-25,25,0][k];yy=[58,58,179][k];s.circle(x+dx,yy,16,TEAL if person==4 else GRAY,'#eaf2ee' if person==4 else 'white');s.text(x+dx,yy+6,str(person),17,anchor='middle');s.line(x+dx,yy+(17 if yy<118 else -17),x,118+(-34 if yy<118 else 34),RULE,1)
  if group:s.text(x,229,'Z'+str(j+1)+' = '+labels[j],18,COLORS[j],anchor='middle')
  else:s.text(x,229,tr(lg,'尚未开桌','Unopened'),15,GRAY,anchor='middle')
 s.text(175,282,tr(lg,'圆桌记祖先，标签记观测值','Tables track ancestry; labels give values'),17,anchor='middle');return s

def equalvalues(lg,mode,choice):
 s=Svg(350,300);labels=['a','a','b',{'A':'a','B':'b','new':'c'}[choice]] if mode=='diffuse' else ['z']*4
 s.text(175,33,tr(lg,'按观测值重新归类','Regroup by observed value'),20,anchor='middle')
 groups={}
 for i,z in enumerate(labels,1):groups.setdefault(z,[]).append(i)
 for j,(z,people) in enumerate(groups.items()):
  y=90+58*j;s.rect(30,y-25,290,46,PALE,RULE);s.text(50,y+5,z,22,TEAL);s.text(195,y+5,'{ '+', '.join(map(str,people))+' }',22,anchor='middle')
 s.text(175,282,tr(lg,'同名标签可以合并不同餐桌','Equal labels may merge distinct tables'),17,WARM,anchor='middle');return s

def rotation(lg,mode,side):
 s=Svg(350,290);cx,cy,r=175,137,91;s.circle(cx,cy,r,RULE,'white')
 pts=[]
 for i in range(8):
  a=math.pi/2-i*math.pi/4
  if side=='after':a=math.pi/2 if mode=='adaptive' else a-float(mode)*math.pi/180
  pts.append((cx+r*math.cos(a),cy-r*math.sin(a)))
 if side=='after' and mode=='adaptive':
  x,y=pts[0];s.circle(x,y,math.sqrt(8)*6,TEAL,TEAL);s.text(cx,cy+12,'P{0}=1',24,WARM,anchor='middle')
 else:
  for i,(x,y) in enumerate(pts):s.circle(x,y,6,TEAL if i==0 else GRAY,TEAL if i==0 else 'white')
  if side=='after':
   a=math.pi/2-float(mode)*math.pi/180;s.line(cx,cy,cx+75*math.cos(a),cy-75*math.sin(a),TEAL,2)
 s.text(175,25,tr(lg,'输入：8个等可能角度','Input: 8 equiprobable angles') if side=='before' else (tr(lg,'看完角度，再转到0','Read angle, then send it to 0') if mode=='adaptive' else tr(lg,'同转 '+mode+'°','Rotate all by '+mode+'°')),18,anchor='middle')
 s.text(175,276,tr(lg,'每个位置概率1/8','Probability 1/8 at each position') if side=='before' or mode!='adaptive' else tr(lg,'八份质量全部聚到同一点','All eight masses meet at one point'),17,TEAL if mode!='adaptive' else WARM,anchor='middle');return s

def relation(lg,mode,bits):
 s=Svg(350,290);xy=[(175,66),(60,216),(290,216)];edges=[(0,1),(1,2),(2,0)];vs=[int(x) for x in bits];es=vs if mode=='pairs' else [int(vs[i]!=vs[j]) for i,j in edges]
 for k,((i,j),v) in enumerate(zip(edges,es)):
  s.line(*xy[i],*xy[j],TEAL if v else RULE,4 if v else 2,None if v else '5 5')
  x=(xy[i][0]+xy[j][0])/2;y=(xy[i][1]+xy[j][1])/2;s.circle(x,y,13,'white','white');s.text(x,y+6,str(v),19,TEAL if v else GRAY,anchor='middle')
 for j,(x,y) in enumerate(xy):
  c=(TEAL if vs[j] else WARM) if mode=='colors' else GRAY;s.circle(x,y,23,c,'white' if mode=='pairs' else c);s.text(x,y+7,str(j+1),22,'white' if mode=='colors' else INK,anchor='middle')
 s.text(175,26,tr(lg,'每对各自抽一位','One independent bit per pair') if mode=='pairs' else tr(lg,'每人抽颜色，异色才连边','One color per vertex; connect unlike colors'),17,anchor='middle');s.text(175,278,'X₁₂X₂₃X₃₁ = '+''.join(map(str,es)),21,anchor='middle');return s

def patterns(lg,mode):
 s=Svg(350,225);s.text(175,25,tr(lg,'8份等概率输入，各占1/8','Eight equiprobable inputs, each 1/8'),17,anchor='middle')
 for z in range(8):
  bits=[(z>>j)&1 for j in range(3)];es=bits if mode=='pairs' else [int(bits[0]!=bits[1]),int(bits[1]!=bits[2]),int(bits[2]!=bits[0])];x=45+85*(z%4);y=70+80*(z//4);xy=[(x,y-15),(x-23,y+20),(x+23,y+20)]
  for (i,j),v in zip([(0,1),(1,2),(2,0)],es):s.line(*xy[i],*xy[j],TEAL if v else RULE,2,None if v else '3 3')
  for i,(u,v) in enumerate(xy):s.circle(u,v,3,TEAL if mode=='pairs' or bits[i] else WARM)
  if sum(es)==3:s.circle(x,y+3,34,WARM,'none')
 s.text(175,220,'P(111) = '+('1/8' if mode=='pairs' else '0'),24,WARM,anchor='middle');return s

def paint(lg,d):
 s=Svg(350,345);end=.5+(0.5-d);s.text(175,25,tr(lg,'同一色带才属于同一块','A shared positive band defines a block'),18,anchor='middle')
 s.rect(15,51,160,33,PALE,TEAL);s.rect(175,51,320*(.5-d),33,'#fbf0df',WARM)
 if d:s.rect(15+320*end,51,320*d,33,'white',GRAY)
 s.text(95,75,'s₁=1/2',17,TEAL,anchor='middle')
 if d<.5:s.text(175+160*(.5-d),75,'s₂='+('1/2' if d==0 else '1/4'),17,WARM,anchor='middle')
 if d:s.text(15+320*(end+d/2),75,'dust',16,GRAY,anchor='middle')
 us=[.1,.3,.6,.79,.87,.95]
 for i,u in enumerate(us):
  x=15+320*u;dust=u>=end;c=TEAL if u<.5 else WARM if not dust else GRAY;s.circle(x,121,4,c,'white' if dust else c);s.line(x,88,x,115,c,1);yy=180+37*max(0,i-3);xx=x;s.arrow(x,132,xx,yy-16,c);s.circle(xx,yy,14,c,'white');s.text(xx,yy+6,str(i+1),18,c,anchor='middle')
 s.text(175,281,tr(lg,'点的位置固定，改变质量分配','Points held fixed; band masses change'),17,anchor='middle');s.text(175,320,'s₁ + s₂ + d = 1',22,anchor='middle');return s

def blocks(lg,d):
 s=Svg(350,345);s.text(175,25,tr(lg,'只看谁与谁同类','Keep only the equivalence relation'),19,anchor='middle');us=[.1,.3,.6,.79,.87,.95];groups={}
 for i,u in enumerate(us,1):key='A' if u<.5 else 'B' if u<1-d else str(i);groups.setdefault(key,[]).append(i)
 for j,(key,g) in enumerate(groups.items()):
  y=72+47*j;c=TEAL if key=='A' else WARM if key=='B' else GRAY;s.rect(48,y-20,254,37,PALE if key=='A' else '#fbf0df' if key=='B' else 'white',c);s.text(175,y+5,'{ '+', '.join(map(str,g))+' }',22,c,anchor='middle')
 s.text(175,337,tr(lg,'dust中的点各自成块','Each dust point is its own singleton'),18,WARM,anchor='middle');return s

CAP={
'V41':('Θ等概率取1/4或3/4；条件于Θ，各Xₖ为iid Bernoulli(Θ)。记录窗口是确定示意、不是模拟或强律证明；其有限比例不等于极限。给定环境的强律使长期平均趋Θ，整份混合律的均值则为1/2。不变σ域在本例等于σ(Θ)，模零集。按钮只移动有限观察窗口或切换条件环境，不在一条实现中重新抽环境。一般Birkhoff结论须保测与可积；遍历才使条件平均为常数，遍历也不自动推出混合。','Θ is 1/4 or 3/4 with equal probabilities; given Θ, the Xk are iid Bernoulli(Θ). Displayed windows are deterministic examples, not simulations or a proof of the strong law; finite frequencies are not limits. The conditional strong law gives limit Θ, while the mixture mean is 1/2. Here the invariant sigma-field is sigma(Θ), modulo null sets. Controls move a finite window or compare conditional environments; they do not resample Θ along one path. General Birkhoff requires measure preservation and integrability; ergodicity makes the conditional mean constant but does not imply mixing.'),
'V44':('标准一参数CRP，α=1；已有桌A={1,2}、B={3}，第四人坐A、B或新桌的预测概率分别1/2、1/4、1/4。每桌标签独立从H抽取，并独立于餐桌过程。原子示例H=(δz+δw)/2，所显示各已开桌恰同为z是一个正概率条件配置，不是几乎必然结论；无原子H时标签几乎必然互异。图上选择分支是检查条件结果，不宣称三个分支等可能。实际观测值相等划分可以比餐桌划分更粗。P(1∼Π2)=1/2，而本原子H下P(X₁=X₂)=3/4。','Standard one-parameter CRP with alpha=1. Given A={1,2}, B={3}, customer 4 joins A, B or a new table with probabilities 1/2, 1/4, 1/4. Table labels are iid H and independent of seating. For H=(delta_z+delta_w)/2, the displayed all-z labels form a positive-probability configuration, not an almost-sure outcome. Nonatomic H gives distinct labels almost surely. Buttons inspect conditional branches, not equiprobable alternatives. Equality of observed values may coarsen the table partition. P(1~Pi2)=1/2, whereas this atomic H gives P(X1=X2)=3/4.'),
'V45':('图用圆上的8个等可能角度和90°整数倍旋转，构成精确有限群例子，不是用8点近似连续Haar积分。每个固定旋转都置换8份质量；a(θ)=−θ却把它们送到0。圆点面积表示概率，集中后面积为单点的8倍。连续均匀圆周的同类结论由弧长不变证明。并非所有依赖数据的旋转都失效：按轨道半径选择旋转可保律；使用独立新噪声前的可测选择另需§45.16的条件独立假设。','Eight equiprobable circle angles with multiples of 90 degrees give an exact finite-group example, not quadrature for continuous Haar measure. Each fixed rotation permutes the eight masses; a(theta)=-theta sends them all to 0. Circle area denotes probability; the concentrated disk has eight times one input mass. The continuous analogue follows from arc-length invariance. Not every data-dependent rotation fails: a radius-based orbit choice may preserve law. Predictable choices for fresh noise require the independence assumptions of section 45.16.'),
'V46':('无限对称无向数组，对角固定0。模型A每个无序人对取独立公平位；模型B每个顶点取独立公平两色，异色记1。两模型固定一行略去对角后均为iid Bernoulli(1/2)，但三角全1概率分别1/8、0。按钮遍历三个独立输入位：A为三个边位，B为三个顶点色；下方枚举全部8份等概率输入。共享顶点会组织高阶约束，不意味着每对相邻边都相关，本例边两两独立。此为已有表示的具体反例，不代替一般Aldous–Hoover表示证明；全局输入、分别交换与对角机制仍依正文。','Infinite symmetric undirected arrays with zero diagonal. A assigns independent fair bits to unordered pairs. B assigns iid fair vertex colors and puts an edge between unlike colors. Each row off the diagonal is iid Bernoulli(1/2) in both models, but the all-edge triangle probabilities are 1/8 and 0. Buttons enumerate three independent input bits: edges in A, vertex colors in B. The lower panel lists all eight equiprobable inputs. Shared vertices organize higher-order constraints; here individual edge pairs are independent. This counterexample does not prove the general Aldous–Hoover theorem; global inputs, separate exchangeability and diagonal mechanisms remain in the text.'),
'V47':('确定paintbox质量s₁=1/2、s₂=1/2−d，d=0、1/4或1/2；零长度色带删去。条件于质量，每个人独立均匀取[0,1]点；正色带同类，剩余部分各为单点。图中6个点位置为确定示意，不是抽样频率或频率极限的证明。剩余部分不是共享颜色；两次抽到dust的概率d²不计为同块概率。两人同块概率s₁²+s₂²。一般随机质量还需Kingman的混合、共同零集及可测排序定理。静态paintbox不决定合并时钟；每块对速率1是另加的Kingman规则。','Deterministic paintbox masses s1=1/2, s2=1/2-d, with d=0,1/4,1/2; omit zero bands. Given masses, each individual samples an independent uniform point; shared positive bands define a class, while residual points are singletons. Six fixed positions illustrate the rule, not frequencies or their limiting theorem. Residual mass is not a shared color; d squared is not added to the same-block probability s1 squared+s2 squared. Random masses require Kingman mixing, common null sets and measurable ranking. A static paintbox does not specify coalescent clocks: pair rate 1 is an additional Kingman rule.')}

DEFAULT={'V41':('25',0),'V44':('atomic','new'),'V45':('90',),'V46':('colors','011'),'V47':('25',)}
def scenes(code,lg,state):
 if code=='V41':q=int(state[0])/100;o=int(state[1]);return environment(lg,q,o),averages(lg,q,o)
 if code=='V44':return tables(lg,*state),equalvalues(lg,*state)
 if code=='V45':return rotation(lg,state[0],'before'),rotation(lg,state[0],'after')
 if code=='V46':return relation(lg,*state),patterns(lg,state[0])
 return paint(lg,int(state[0])/100),blocks(lg,int(state[0])/100)
def filename(code,lg,state,i):return f'{code}-{lg}-'+ '-'.join(map(str,state))+f'-{i}.svg'
def allstates(code):
 if code=='V41':return [(q,o) for q in ['25','75'] for o in [0,3,6]]
 if code=='V44':return [(m,c) for m in ['atomic','diffuse'] for c in ['A','B','new']]
 if code=='V45':return [(m,) for m in ['0','90','180','adaptive']]
 if code=='V46':return [(m,format(i,'03b')) for m in ['pairs','colors'] for i in range(8)]
 return [(d,) for d in ['0','25','50']]
INTRO={
'V41':('把开头移走以后，哪些随机信息仍会留在同一条记录中？','After shifting the record, what random information can still remain?'),
'V44':('先分桌，再给桌贴标签。这两步会得到同一份划分吗？','Seat first, then label each table. Do these operations define the same partition?'),
'V45':('每个固定旋转都把概率均匀搬过去。先看见点，再挑旋转，还会均匀吗？','Every fixed rotation moves uniform mass uniformly. What if the angle is chosen after seeing the point?'),
'V46':('单看一行，两种无限随机图完全同律。三个人之间，却能出现不同的关系。','One row has exactly the same law in two infinite random graphs. Three vertices reveal the difference.'),
'V47':('没有落进任何正质量色带的人，是属于同一个剩余类别，还是各自单独成类？','Do points outside the positive mass bands share one residual class, or form separate singletons?')}
HEADS={'V41':('移动有限观察窗口','长期留下什么','Move a finite window','What the long run retains'),'V44':('餐桌：按共同复制来源分组','观测：按标签值分组','Tables: copy ancestry','Observations: equal labels'),'V45':('变换之前','变换之后','Before the map','After the map'),'V46':('共享输入怎样决定三条边','全部8份输入，检查三角事件','Shared inputs determine edges','All eight inputs; test a triangle'),'V47':('位置到类别的映射','丢掉位置，只保留分类','Map locations to classes','Forget locations; keep classes')}
def controls(code,lg):
 if code=='V41':return buttons('data-env', [('25','Θ=1/4'),('75','Θ=3/4')],'25')+buttons('data-offset',[(str(n),tr(lg,f'窗口从{n}开始',f'Start at {n}')) for n in [0,3,6]],'0')
 if code=='V44':return buttons('data-label',[('atomic',tr(lg,'原子H：可同名','Atomic H: labels may tie')),('diffuse',tr(lg,'无原子H','Nonatomic H'))],'atomic')+buttons('data-seat',[('A',tr(lg,'坐A：1/2','Join A: 1/2')),('B',tr(lg,'坐B：1/4','Join B: 1/4')),('new',tr(lg,'新桌：1/4','New table: 1/4'))],'new')
 if code=='V45':return buttons('data-rotation',[(x,tr(lg,'固定'+x+'°','Fixed '+x+'°')) for x in ['0','90','180']]+[('adaptive',tr(lg,'看完θ，再选−θ','See θ, then choose −θ'))],'90')
 if code=='V46':return buttons('data-array-model',[('pairs',tr(lg,'独立边输入','Independent pair inputs')),('colors',tr(lg,'共享顶点色','Shared vertex colors'))],'colors')+'<div class="v6-controls">'+''.join(f'<button data-bit="{i}" aria-pressed="{str(v=="1").lower()}">'+tr(lg,f'切换输入{i+1}',f'Toggle input {i+1}')+'</button>' for i,v in enumerate('011'))+'</div>'
 return buttons('data-dust',[('0','d=0'),('25','d=1/4'),('50','d=1/2')],'25')
def result(code,lg,state):
 if code=='V41':return tr(lg,'无条件均值1/2；这一环境下的长期平均为','Mixture mean 1/2; the long-run mean in this environment is ')+('1/4' if state[0]=='25' else '3/4')+'。'
 if code=='V44':return tr(lg,'新桌机会为1/4；新观测值机会还取决于H。图中同名配置只是正概率示例。','New-table chance is 1/4; a new value also depends on H. The tied labels shown are one positive-probability configuration.')
 if code=='V45':return tr(lg,'固定旋转：只置换八份概率；依据当前角度归零：把八份概率合为一份。','Fixed rotations permute eight masses; current-angle recentering combines all eight into one.')
 if code=='V46':return tr(lg,'同一行都是独立公平位；三条边全1的概率却是1/8与0。','Each row is iid fair bits; the all-edge triangle probabilities are 1/8 and 0.')
 d=int(state[0])/100;return tr(lg,'两人同块概率 = s₁²+s₂² = ','Same-block probability = s1²+s2² = ')+str(.25+(.5-d)**2)+tr(lg,'；不能再加d²。','; do not add d².')
def static(code,lg):
 title=META[code][2 if lg=='zh' else 3];state=DEFAULT[code];panes=scenes(code,lg,state);s=Svg(900,1000);s.rect(0,0,900,1000,'white');s.text(30,44,title,26,weight='bold');intro_lines=wrap_caption(tr(lg,*INTRO[code]),lg)
 for j,line in enumerate(intro_lines):s.text(30,84+j*24,line,17)
 y=105+24*(len(intro_lines)-1)
 for i,t in enumerate(panes):nested(s,t,35+440*i,y,390,390*t.h/t.w)
 end=y+max(t.h/t.w*390 for t in panes)+35
 # Static variants make the central contrast readable without clicking.
 compare={'V41':('75',0),'V44':('diffuse','new'),'V45':('adaptive',),'V46':('pairs','111'),'V47':('0',)}[code]
 s.text(30,end,tr(lg,'对照状态','Comparison state'),22,WARM);end+=15
 for i,t in enumerate(scenes(code,lg,compare)):nested(s,t,35+440*i,end,330,330*t.h/t.w)
 end+=max(t.h/t.w*330 for t in scenes(code,lg,compare))+30
 s.line(30,end,870,end,RULE,1)
 lines=wrap_caption(tr(lg,*CAP[code]),lg)
 for j,line in enumerate(lines):s.text(30,end+29+24*j,line,17,GRAY)
 s.h=end+60+24*len(lines);s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';save(s,f'{code}.{lg}.svg',title)

def main():
 rows=[]
 for code in META:
  slug,section,zh,en=META[code]
  for lg in ['zh','en']:
   for state in allstates(code):
    for i,s in enumerate(scenes(code,lg,state)):save(s,filename(code,lg,state,i),tr(lg,zh,en))
   heads=HEADS[code][:2] if lg=='zh' else HEADS[code][2:];state=DEFAULT[code];body='<p class="v6-intro">'+tr(lg,*INTRO[code])+'</p>'+controls(code,lg)
   if code=='V41':body+='<p class="v6-compact-result">'+tr(lg,'整体均值1/2，不是每条长记录的极限','Mixture mean 1/2 is not every path’s limit')+'</p>'
   if code=='V44':body+='<p class="v6-compact-result">'+tr(lg,'新桌≠新值：同名标签会合并餐桌','New table ≠ new value: tied labels merge tables')+'</p>'
   if code=='V46':body+='<p class="v6-compact-result">'+tr(lg,'三角全1概率：独立边1/8，顶点色0','All-edge triangle: independent pairs 1/8, vertex colors 0')+'</p>'
   body+=pair(*(panel(heads[i],img(filename(code,lg,state,i),heads[i],f'data-pane="{i}"')) for i in range(2)))
   body+='<output data-result aria-live="polite">'+result(code,lg,state)+'</output>'
   if code=='V41':body+='<p class="v6-limit">'+tr(lg,'有限窗口是示意；显示的Θ是条件参数，不是从这6项算出的比例。','The finite window is illustrative. Θ is the conditional parameter, not the frequency of these six entries.')+'</p>'
   cap=tr(lg,*CAP[code]);frag=f'<figure class="volume6" data-v6="{code}" id="visual-{code}" lang="{lg}"><header><span>{code}</span><h3>{tr(lg,zh,en)}</h3></header>{body}<details><summary>'+tr(lg,'模型条件与数学边界','Model assumptions and mathematical limits')+f'</summary><p>{cap}</p></details><figcaption id="visual-{code}-end">'+tr(lg,'图解释正文中的具体模型；完整定理与证明仍在正文及配套专题中。','The diagram explains a specific model in the text; full theorems and proofs remain in the chapter and its foundations.')+f'</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
   rows.append(dict(id=code,lang=lg,slug=slug,section=section,coverage_sections={'V41':['41.1','41.4','41.9'],'V44':['44.17','44.18','44.19'],'V45':['45.1','45.16','45.17'],'V46':['46.1','46.3','46.12'],'V47':['47.5','47.6','47.7']}[code],title=tr(lg,zh,en),html=frag,condition=cap,asset_base=BASE,status='author visual review pending',kind='new explanatory candidate'))
   static(code,lg)
 jsave(R/'publication/explanatory-volume6-batch1-working.json',dict(source_commit='aff0d034',automatic_formal_site_injection=False,canonical_manuscript_changes=False,reused_adopted=['P02'],figures=rows))
 write(A/'figures.css',CSS);write(A/'interactions.js',JS)
 print('Five bilingual finite-model candidates generated; old assets untouched')
CSS='''.volume6{background:#fffefa;color:#173f39;border:1px solid #ccd9d1;padding:28px;margin:2rem 0;font-family:"Microsoft YaHei",sans-serif;box-sizing:border-box}.volume6 *{box-sizing:border-box}.volume6 header span{font-size:13px;color:#65756e}.volume6 h3{font-size:26px;line-height:1.5;margin:0 0 18px}.volume6 p{font-size:18px;line-height:1.8}.volume6 h4{font-size:19px;font-weight:500;text-align:center;line-height:1.5;margin:18px 0 10px}.volume6 img{display:block;width:100%;height:auto!important;max-height:none!important;margin:0!important;box-shadow:none!important;border:0!important}.volume6 .v6-pair{display:grid;grid-template-columns:1fr 1fr;gap:30px}.volume6 .v5-controls,.volume6 .v6-controls{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin:14px 0}.volume6 button{font:inherit;font-size:16px;padding:9px 12px;color:#173f39;border:1px solid #ccd9d1;background:#fffefa;border-radius:4px;cursor:pointer}.volume6 button[aria-pressed=true]{border:2px solid #16776d;padding:8px 11px;background:#eaf2ee}.volume6 output{display:block;color:#16776d;font-size:20px;line-height:1.7;border-top:1px solid #ccd9d1;padding:18px 0}.volume6 .v6-limit{font-size:16px;color:#a45b30}.volume6 .v6-compact-result{font-size:20px;color:#16776d;text-align:center}.volume6 details{border-top:1px solid #ccd9d1;padding:16px 0}.volume6 summary{font-size:16px;cursor:pointer}.volume6 details p,.volume6 figcaption{font-size:15px;line-height:1.9;overflow-wrap:anywhere}.volume6 nav{display:flex;gap:18px;font-size:14px;margin-top:16px}@media(max-width:700px){.volume6{padding:15px}.volume6 h3{font-size:22px}.volume6 .v6-pair{grid-template-columns:1fr;gap:6px}.volume6 p{font-size:17px}.volume6 h4{font-size:18px}.volume6 img{max-width:400px;margin:0 auto!important}.volume6 .v6-compact-result{font-size:18px}.volume6 button{font-size:15px}}@media print{.volume6 button{display:none}.volume6 details{display:block}}'''
JS='''document.querySelectorAll('[data-v6]').forEach(root=>{const code=root.dataset.v6,lg=root.lang,B='/assets/visuals/explanatory-volume6-v1/';let env='25',offset='0',label='atomic',seat='new',rotation='90',model='colors',bits='011',dust='25';const press=(a,v)=>root.querySelectorAll('['+a+']').forEach(b=>b.setAttribute('aria-pressed',String(b.getAttribute(a)===v)));function draw(){const st=code==='V41'?[env,offset]:code==='V44'?[label,seat]:code==='V45'?[rotation]:code==='V46'?[model,bits]:[dust];root.dataset.state=st.join('-');root.querySelectorAll('[data-pane]').forEach(i=>i.src=B+`${code}-${lg}-${st.join('-')}-${i.dataset.pane}.svg`);let s='';if(code==='V41')s=(lg==='zh'?'无条件均值1/2；本环境长期平均为':'Mixture mean 1/2; long-run conditional mean: ')+(env==='25'?'1/4':'3/4');if(code==='V44')s=lg==='zh'?(label==='atomic'?'本例已见仅z：新桌概率1/4，新观测值概率1/8。当前图展示同名分支。':'无原子H：各桌标签几乎必然互异；新桌与新值机会均为1/4。'):(label==='atomic'?'Only z has been observed: a new table has chance 1/4, a new value 1/8. The picture shows a tied-label branch.':'Nonatomic H: labels are distinct almost surely; both new-table and new-value chances are 1/4.');if(code==='V45')s=rotation==='adaptive'?(lg==='zh'?'看完当前角度，再选−θ：输出集中在0。':'Read current angle, then choose −θ: output concentrates at 0.'):(lg==='zh'?'固定旋转：8个角度仍各占1/8。':'Fixed rotation: all eight angles retain mass 1/8.');if(code==='V46'){const v=[...bits].map(Number),e=model==='pairs'?v:[+(v[0]!==v[1]),+(v[1]!==v[2]),+(v[2]!==v[0])];s=(lg==='zh'?'当前输入':'Input ')+bits+' → '+e.join('')+(lg==='zh'?'；三角全1概率：':' ; all-edge triangle probability: ')+(model==='pairs'?'1/8':'0');root.querySelectorAll('[data-bit]').forEach(b=>{let i=Number(b.dataset.bit);b.setAttribute('aria-pressed',String(bits[i]==='1'));b.textContent=(lg==='zh'?(model==='pairs'?'边输入':'顶点色'):(model==='pairs'?'Pair bit ':'Vertex color '))+(i+1)+' = '+bits[i];});}if(code==='V47'){let d=Number(dust)/100;s=(lg==='zh'?'两人同块概率 = ':'Same-block probability = ')+(.25+(.5-d)**2)+(lg==='zh'?'；不是再加d²。':'; do not add d².');}root.querySelector('[data-result]').textContent=s;}root.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{if(b.hasAttribute('data-env')){env=b.dataset.env;press('data-env',env);}if(b.hasAttribute('data-offset')){offset=b.dataset.offset;press('data-offset',offset);}if(b.hasAttribute('data-label')){label=b.dataset.label;press('data-label',label);}if(b.hasAttribute('data-seat')){seat=b.dataset.seat;press('data-seat',seat);}if(b.hasAttribute('data-rotation')){rotation=b.dataset.rotation;press('data-rotation',rotation);}if(b.hasAttribute('data-array-model')){model=b.dataset.arrayModel;press('data-array-model',model);}if(b.hasAttribute('data-bit')){let n=+b.dataset.bit;bits=bits.slice(0,n)+(bits[n]==='1'?'0':'1')+bits.slice(n+1);}if(b.hasAttribute('data-dust')){dust=b.dataset.dust;press('data-dust',dust);}draw();}));draw();});'''
if __name__=='__main__':main()
