"""Volume VIII explanatory candidates. Public book models only; no manuscript writes."""
from pathlib import Path
from fractions import Fraction as F
import json,math,textwrap
from .pilot_shapes import Svg,tr,E,INK,TEAL,WARM,GRAY,PALE,RULE
from .volume5 import wrap_caption

R=Path(__file__).resolve().parents[2];A=R/'assets/visuals/explanatory-volume8-v1';O=R/'reports/volume8-visual-batch1-2026-11-06'
BASE='/assets/visuals/explanatory-volume8-v1/'
META={
 'V54':('54-brownian-crt','54.9','树没有变，抽样质量变了','The tree stays; its sampling mass changes'),
 'V55':('55-metric-measure-limits','55.12','分别对齐，未必能一起对齐','Separate alignments need not agree'),
 'V56':('56-fragmentation-hierarchies','56.1','藏起第三人，不该改变前两人的规律','Hiding a third label must preserve the pair law'),
 'V57':('57-regenerative-growth','57.7','新枝接在哪里，由长度决定','Length decides where a new branch attaches'),
 'V58':('58-multifurcation','58.5','同为k叉，比较两种公开模型','Compare two public k-ary models')}
SOURCES={
 'V54':[('Le Gall (2005), §2.2, §2.5','https://arxiv.org/pdf/math/0511515')],
 'V55':[('Book §55.12–13; explicit interval calculation','/chapters/55-metric-measure-limits.html')],
 'V56':[('Book §56.1, §56.8–9; finite generator check','/chapters/56-fragmentation-hierarchies.html')],
 'V57':[('Aldous (1993), §4.3, pp.275–276','https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf')],
 'V58':[('Haas–Stephenson (2015), model p.1314; Theorem 1.1','https://www.math.univ-paris13.fr/~haas/AIHPB2015514.pdf'),('Le Gall (2005), §1, conditioned plane trees','https://arxiv.org/pdf/math/0511515')]}
CAP={
 'V54':('确定性编码hₐ从0线性上升到1，在1停留a，再线性回0；上升、下降各用(1−a)/2时间，a∈{0,1/4,1/2}。商树始终保根等距于[0,1]，但均匀时间的推前为μₐ=(1−a)Unif[0,1]+aδ₁。几何细线不变，宽带只表示连续质量密度，顶端圆面积表示原子质量。U滑块指定一次示意输入，U不是树上位置。一般连续编码允许原子；这不是Brownian样本，Brownian CRT的无原子性仍依正文定理。',
 'The deterministic code rises linearly from 0 to 1, pauses for a, then returns linearly to 0, with a in {0,1/4,1/2}. Each sloping part lasts (1-a)/2. Its rooted quotient tree is always [0,1], but uniform time pushes forward to (1-a)Unif[0,1]+a delta_1. The thin line is geometry; band width is diffuse mass density; the top disk area is atomic mass. The slider chooses an illustrative U, not a new probability law. This is not a Brownian sample; atomlessness of Brownian CRT mass is a separate theorem.'),
 'V55':('X=Y=[−1,2]，两根均为0，μX=δ₁、μY=δ₋₁。图示三种等距嵌入：恒等、反射、反射再平移1/2；只改变共同背景中的位置，不改变内部距离。当前见证的(Hausdorff,根,Prokhorov)误差依次为(0,0,1)、(1,0,0)、(1/2,1/2,1/2)。dP采用概率测度规范，距离2的两原子dP=1。分别优化可给rGH=rGP=0，rGHP却为1/2：两质量点在各自全空间中的最远距离是2与3，任一误差r<1的共同见证必须有3≤2+2r；第三种摆放取到上界。这是正文区间反例的有限几何计算，不将某种摆放当作一般最优嵌入。',
 'X=Y=[-1,2], with root 0 and masses delta_1 and delta_-1. Three isometric placements of Y are identity, reflection, and reflection followed by translation by 1/2. Their current (Hausdorff,root,Prokhorov) errors are (0,0,1), (1,0,0), and (1/2,1/2,1/2). Two Dirac masses separated by 2 have Prokhorov distance 1 in the probability convention. Separately rGH=rGP=0, but rGHP=1/2: eccentricities of the mass points are 2 and 3, so any common witness with error r<1 requires 3<=2+2r. The third placement attains the bound. These are explicit witnesses for this interval example, not a general embedding algorithm.'),
 'V56':('只比较一块的有限样本生成机制，候选分裂事件率均为1。按样本数尽量均分时，两人必分开，三人有三种等概率单人侧，指定两人仅以2/3分开。正确对照为各标签独立投公平位：二人及三人投影的指定对分离概率都为1/2；八份三位输入等概率，000和111不是有效分裂。图中删除3只删除观察，不重抽1、2的颜色。所列速率=事件率×可见分离概率；不是单凭图片证明一般无限碎裂。每块未来独立、可测构造及可积条件仍依正文。',
 'Only the finite generator of one block is compared, with raw candidate-event rate 1. Balancing the observed sample always separates two labels; among the three equiprobable singleton sides for three labels, a fixed pair separates with probability 2/3. In the independent fair-bit model the pair separates with probability 1/2 both directly and after restricting three labels. The eight bit words are equiprobable; 000 and 111 cause no effective split. Hiding label 3 removes an observation, not the colors of labels 1 and 2. Visible rates are raw rate times separation probability. General infinite fragmentation, independent block futures and integrability still require the text.'),
 'V57':('给定一棵两叶约化度量树，三边长度1/2、1、1/2，总长s=2。接点按骨架长度均匀，因此选边概率为1/4、1/2、1/4，不能在已知这些边长时改成每边1/3。独立示意输入U、E给接点累计长度sU及L新=√(s²+E/2)，新枝b=L新−s；E按Exp(1)分布时对应标准e的4r dr时钟，按钮中的固定数值仅为示意输入。新增边不改变旧距离。出生叶经验质量不是归一化骨架长度；有限接枝本身也不证明无限紧性或质量存在。Aldous原文使用r dr及2e，故本图明确换算因子2。',
 'Condition on a two-leaf metric tree with edge lengths 1/2,1,1/2 and total s=2. A length-uniform attachment selects edges with probabilities 1/4,1/2,1/4, not 1/3 when those lengths are known. Independent illustrative inputs U,E give arclength sU, new total L=sqrt(s²+E/2), and branch length L-s. With E exponential of rate 1 this is the standard-e clock 4r dr; buttons merely specify inputs. Grafting preserves old distances. Empirical birth-leaf mass is not normalized skeleton length; finite grafting does not prove infinite compactness or existence of mass. Aldous uses r dr and the 2e scale, so lengths are halved here.'),
 'V58':('只用公开模型：固定k∈{2,3,4}的临界GW后代律P(0)=1−1/k、P(k)=1/k，条件内部节点I=3，即总节点N=3k+1，平面树等概率；另一模型严格依Haas–Stephenson(2015)均匀选边、插点并加k−1枝，所有新组合边长1。图比较内部根有两个内部孩子的事件B；k=2时两边均为1/5，仅凭这一个事件相等不能识别全部概率律。k=3、4时本事件的概率不同。GW有C(k,2)个合法平面形状、总数k(3k−1)/2；增长在第3步前有2k+1条等概率边，其中k−1条导致该事件。只检查这个无标号根分裂事件，不混同出生标签、均匀节点与均匀叶。增长图包含辅助根干；GW根不加干。此有限计算直接由公开规则枚举，不使用作者未发表公式或质量密度。有限阶段不冒充CRT极限证明；不同缩放及理论状态见正文与公开文献。',
 'Public models only: fixed k in {2,3,4}, critical GW offspring P(0)=1-1/k, P(k)=1/k, conditioned on I=3 internal vertices (N=3k+1), uniform over plane trees; versus the Haas–Stephenson (2015) uniform-edge growth rule, inserting a vertex and k-1 branches with unit combinatorial edges. Event B is that the internal root has two internal children. For k=2 both probabilities are 1/5; equality of this one event alone does not identify the complete laws. For k=3,4 the event probabilities differ. GW has C(k,2) such plane shapes out of k(3k-1)/2; at growth step 3 there are 2k+1 equiprobable edges, of which k-1 give that event. Only this unlabeled root event is compared. Birth labels, vertex mass and leaf mass are distinct. Growth has a planted root edge; GW does not. Counts are independently enumerated from public rules, with no unpublished formula or density. Finite counts are not a continuum-limit proof.')}

def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf8',newline='\n')
def ratio(x):return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def title(s,t):
    lines=textwrap.wrap(t,width=35) if s.w<400 and len(t)>35 else [t]
    for i,line in enumerate(lines):s.text(s.w/2,23+21*i,line,17 if s.w<400 else 20,anchor='middle',weight='bold')
def foot(s,t,c=GRAY):s.text(s.w/2,s.h-12,t,13 if s.w<400 else 16,c,anchor='middle')
def nested(s,p,x,y):s.nodes.append(f'<svg x="{x}" y="{y}" width="{p.w}" height="{p.h}" viewBox="0 0 {p.w} {p.h}">{p.fragment()}</svg>')
def save(s,name,t):write(A/name,s.document(t))
def line(s,x,y,u,v,c=INK,w=2):s.line(x,y,u,v,c,w)
def bar(s,x,y,w,parts,colors):
    start=x
    for a,c in zip(parts,colors):s.rect(start,y,w*float(a),20,c);start+=w*float(a)
    s.rect(x,y,w,20,'none',RULE)

def h_value(a,u):
    b=(1-a)/2
    return u/b if u<b else (1-u)/b if u>1-b else F(1)

def mass_scene(lg,ai,ui,mobile=False):
    a=[F(0),F(1,4),F(1,2)][ai];u=F(ui,8);z=h_value(a,u);w=360 if mobile else 850;s=Svg(w,735 if mobile else 425)
    title(s,tr(lg,'同一条长1的树，时间分配可以改变','One unit tree, different time allocations'))
    tx,ty,tw=(25,98,310) if mobile else (35,105,390);b=(1-a)/2
    for j,(start,length,c) in enumerate([(F(0),b,TEAL),(b,a,WARM),(1-b,b,TEAL)]):
        if length:s.rect(tx+tw*float(start),ty,tw*float(length),45,c)
    s.text(tx,ty-14,'U ~ Unif[0,1]',18,GRAY);s.text(tx,ty+72,'0',14,GRAY);s.text(tx+tw,ty+72,'1',14,GRAY,anchor='end')
    xx=tx+tw*float(u);s.arrow(xx,ty+93,xx,ty+48,WARM)
    s.text(tx+tw/2,ty+126,'U = '+ratio(u),20,WARM,anchor='middle')
    s.text(tx+tw/2,ty+157,tr(lg,'顶端停顿时间 a = ','Top pause a = ')+ratio(a),18,WARM,anchor='middle')
    x,y,height=(180,346,238) if mobile else (650,90,220)
    # Density width and endpoint mass are distinct from the fixed geometric line.
    s.rect(x-21*float(1-a),y,42*float(1-a),height,'#c8ded3')
    s.line(x,y,x,y+height,INK,2)
    if a:s.circle(x,y,29*math.sqrt(float(a)),WARM,WARM)
    else:s.circle(x,y,4,INK,'white')
    s.circle(x,y+height,6,INK,'white');s.text(x+42,y+8,'1',16,GRAY);s.text(x+42,y+height+6,'ρ = 0',16,GRAY)
    sy=y+height*(1-float(z));s.circle(x,sy,7,TEAL,'white');s.text(x-28,sy+5,'p(U)',16,TEAL,anchor='end')
    s.text(x,y+height+39,tr(lg,'几何长度恒为1','Geometric length stays 1'),16,anchor='middle')
    bx,by,bw=(40,651,280) if mobile else (40,340,360)
    bar(s,bx,by,bw,[a,1-a],[WARM,PALE]);s.text(bx,by-12,tr(lg,'顶端原子质量 ','Top atom mass ')+ratio(a),18,WARM)
    foot(s,tr(lg,'细线是距离；宽带与圆面积是质量','Thin line: geometry; band and disk: mass'));return s

PLACEMENTS=[(F(-1),F(2),F(0),F(-1)),(F(-2),F(1),F(0),F(1)),(F(-3,2),F(3,2),F(1,2),F(3,2))]
def witness_values(mode):return [(F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(1,2),)*3][mode]
def witness_scene(lg,mode,mobile=False):
    w=360 if mobile else 850;s=Svg(w,565 if mobile else 410)
    title(s,tr(lg,['先把全部几何重合','先把质量点重合','在一次比较中折中'][mode],['Align the full geometry','Align the mass points','One joint compromise'][mode]))
    x0=30 if mobile else 75;ww=w-2*x0;axis=lambda x:x0+(float(x)+2.5)/5*ww
    ys=[130,274] if mobile else [135,265];data=[(F(-1),F(2),F(0),F(1)),PLACEMENTS[mode]]
    for i,((lo,hi,root,mass),y) in enumerate(zip(data,ys)):
        s.text(18 if mobile else 35,y-34,['X','Y'][i],24,INK,weight='bold')
        s.line(axis(lo),y,axis(hi),y,INK,3)
        for e in [lo,hi]:s.line(axis(e),y-9,axis(e),y+9,GRAY,1);s.text(axis(e),y+33,ratio(e),14,GRAY,anchor='middle')
        s.circle(axis(root),y,6,TEAL,'white');s.text(axis(root),y-16,'ρ',18,TEAL,anchor='middle')
        s.circle(axis(mass),y,15,WARM,WARM);s.text(axis(mass),y+6,'1',17,'white',anchor='middle');s.text(axis(mass),y-26,tr(lg,'全部质量','all mass'),14,WARM,anchor='middle')
    s.line(axis(data[0][2]),ys[0]+8,axis(data[1][2]),ys[1]-8,TEAL,1,'4 4')
    s.line(axis(data[0][3]),ys[0]+17,axis(data[1][3]),ys[1]-17,WARM,1,'4 4')
    vals=witness_values(mode);labels=tr(lg,['全空间','根','质量'],['Shape','Root','Mass'])
    for i,(label,v) in enumerate(zip(labels,vals)):
        x=w*(i+1)/4;y=412 if mobile else 340;s.text(x,y,label,16,GRAY,anchor='middle');s.text(x,y+35,ratio(v),27,TEAL if v==0 else WARM,anchor='middle',weight='bold')
    foot(s,tr(lg,'这是当前共同摆放的三项误差','Errors in this common placement'));return s

def split_bits(mode,j):
    return tuple(1 if i==j else 0 for i in range(3)) if mode=='balanced' else tuple(int(c) for c in f'{j:03b}')
def people_panel(lg,bits,hide=False):
    s=Svg(350,245);s.text(175,22,tr(lg,'只隐藏3，不重抽1、2' if hide else '同一份三人记录','Hide 3; keep 1 and 2' if hide else 'One three-label observation'),17,anchor='middle')
    for side,x in enumerate([88,262]):
        s.rect(x-60,65,120,128,PALE if side==0 else '#f6eadd',RULE)
        ids=[i for i in range(3) if bits[i]==side]
        for j,i in enumerate(ids):
            yy=90+j*37;color=RULE if hide and i==2 else TEAL if side==0 else WARM
            s.circle(x,yy,13,color,'white');s.text(x,yy+5,str(i+1),17,color,anchor='middle')
            if hide and i==2:s.line(x-17,yy-17,x+17,yy+17,GRAY,1)
    separated=bits[0]!=bits[1]
    s.text(175,233,tr(lg,'1、2分开' if separated else '1、2仍同块','1 and 2 separate' if separated else '1 and 2 stay together'),18,TEAL if separated else WARM,anchor='middle');return s

def split_scene(lg,mode,j,mobile=False):
    w=360 if mobile else 850;s=Svg(w,875 if mobile else 570);bits=split_bits(mode,j)
    title(s,tr(lg,'按样本均分' if mode=='balanced' else '各标签独立投公平位','Balance the sample' if mode=='balanced' else 'Independent fair bits'))
    nested(s,people_panel(lg,bits),5 if mobile else 30,55);nested(s,people_panel(lg,bits,True),5 if mobile else 465,320 if mobile else 55)
    if not mobile:s.arrow(390,170,445,170,GRAY)
    y=615 if mobile else 345;count=3 if mode=='balanced' else 8;cols=3 if mode=='balanced' else 4;bw=84 if mobile else 94;left=(w-cols*bw)/2
    s.text(w/2,y-24,tr(lg,'枚举全部等概率输入','All equiprobable inputs'),18,anchor='middle')
    for k in range(count):
        b=split_bits(mode,k);x=left+(k%cols)*bw;yy=y+(k//cols)*58;good=b[0]!=b[1]
        s.rect(x+4,yy,bw-8,44,PALE if good else '#f6eadd',TEAL if k==j else RULE)
        for i,bit in enumerate(b):s.circle(x+18+i*23,yy+21,7,TEAL if bit==0 else WARM)
    low=y+65 if mode=='balanced' else y+135
    s.text(w/2,low+20,tr(lg,'直接看2人：1；先看3人再限制：2/3','Direct pair: 1; restricted triple: 2/3') if mode=='balanced' else tr(lg,'直接看2人 = 三人限制 = 1/2','Direct pair = restricted triple = 1/2'),16 if mobile else 20,WARM if mode=='balanced' else TEAL,anchor='middle',weight='bold')
    foot(s,tr(lg,'上列数值是分离率；候选事件率均为1','Visible separation rates; raw event rate is 1'));return s

EDGE_LENGTHS=[F(1,2),F(1),F(1,2)];US=[F(1,8),F(1,2),F(7,8)];ES=[1,4,8]
def graft_data(ui,ei):
    u=US[ui];distance=2*u;cum=F(0)
    for edge,length in enumerate(EDGE_LENGTHS):
        if distance<cum+length:break
        cum+=length
    pos=(distance-cum)/length;b=math.sqrt(4+ES[ei]/2)-2
    return dict(edge=edge,pos=float(pos),L=2,b=b,next=2+b,U=str(u),E=ES[ei])

def graft_tree(lg,ui,ei,after):
    s=Svg(360,390);d=graft_data(ui,ei);xy=[(180,320),(180,250),(96,138),(236,208)];edges=[(0,1),(1,2),(1,3)];colors=[TEAL,'#496c8e','#70846c']
    for j,(a,b) in enumerate(edges):
        s.line(*xy[a],*xy[b],colors[j],3);mx=(xy[a][0]+xy[b][0])/2;my=(xy[a][1]+xy[b][1])/2;s.text(mx-13,my,str(EDGE_LENGTHS[j]),16,colors[j],anchor='end')
    a,b=edges[d['edge']];p=tuple(xy[a][k]+d['pos']*(xy[b][k]-xy[a][k]) for k in [0,1]);s.circle(*p,6,WARM,'white')
    if after:
        vx,vy=[(1,0),(-.8,.6),(.6,.8)][d['edge']];tip=(p[0]+140*d['b']*vx,p[1]+140*d['b']*vy);s.line(*p,*tip,WARM,3);s.circle(*tip,6,WARM,WARM);s.text(tip[0],tip[1]-12,'3',18,WARM,anchor='middle')
    for i,(x,y) in enumerate(xy):s.circle(x,y,4,INK,'white');s.text(x+12,y+4,['ρ','','1','2'][i],17,GRAY)
    s.text(180,30,tr(lg,'添枝后，旧距离不变' if after else '先给定旧度量树','Old distances stay' if after else 'Condition on this metric tree'),18,anchor='middle')
    s.text(180,370,tr(lg,'新枝 b = ','New branch b = ')+f'{d["b"]:.4f}',19,WARM,anchor='middle');return s

def graft_scene(lg,ui,ei,after,mobile=False):
    w=360 if mobile else 850;s=Svg(w,790 if mobile else 455);d=graft_data(ui,ei)
    title(s,tr(lg,'同一个U，沿累计长度定位','Locate U along accumulated length'))
    nested(s,graft_tree(lg,ui,ei,after),0 if mobile else 20,50)
    x,y,bw=(30,493,300) if mobile else (438,105,370)
    bar(s,x,y,bw,[F(1,4),F(1,2),F(1,4)],[TEAL,'#496c8e','#70846c'])
    for mid,label in [(F(1,8),'1/4'),(F(1,2),'1/2'),(F(7,8),'1/4')]:s.text(x+bw*float(mid),y+46,label,18,anchor='middle')
    s.arrow(x+bw*float(US[ui]),y-35,x+bw*float(US[ui]),y-3,WARM)
    s.text(x+bw/2,y+85,'U = '+str(US[ui])+' · E = '+str(ES[ei]),20,anchor='middle')
    s.text(x+bw/2,y+123,'L: 2 → '+f'{d["next"]:.4f}',21,TEAL,anchor='middle')
    s.text(x+bw/2,y+164,tr(lg,'已知边长时，不是每边1/3','With known lengths: not 1/3 per edge'),14 if mobile else 17,WARM,anchor='middle')
    s.text(x+bw/2,y+202,tr(lg,'标准e：累计强度 2r²','Standard e: cumulative intensity 2r²'),16,GRAY,anchor='middle')
    foot(s,tr(lg,'接枝位置按长度；概率质量另需构造','Length selects attachment; mass needs construction'));return s

def kary_values(k):return dict(gw_total=k*(3*k-1)//2,gw_balanced=k*(k-1)//2,growth_total=2*k+1,growth_balanced=k-1)
def kary_title(lg,k):
    return tr(lg,f'k={k}：事件B的概率'+('相同' if k==2 else '不同'),f'k={k}: event B has '+('equal' if k==2 else 'different')+' probabilities')
def growth_edges(k):
    pts=[(180,330),(180,242),(68,155)]+[(150+(160*i/(k-2) if k>2 else 80),155) for i in range(k-1)]+[(18+100*i/(k-1),65) for i in range(k)]
    edges=[(0,1),(1,2)]+[(1,3+i) for i in range(k-1)]+[(2,k+2+i) for i in range(k)]
    return pts,edges
def growth_panel(lg,k,j):
    s=Svg(360,390);pts,edges=growth_edges(k)
    for i,(a,b) in enumerate(edges):
        good=2<=i<=k;c=TEAL if good else GRAY;s.line(*pts[a],*pts[b],WARM if i==j else c,4 if i==j else 1.8)
        xx=(pts[a][0]+pts[b][0])/2;yy=(pts[a][1]+pts[b][1])/2;s.text(xx+10,yy,str(i),14,WARM if i==j else c)
        if i==j:s.circle(xx,yy,7,WARM,'white')
    for i,(x,y) in enumerate(pts):s.circle(x,y,4,INK,'white')
    s.text(194,334,'ρ',16,GRAY);s.text(194,244,'v',16,GRAY)
    s.text(180,28,tr(lg,'增长第3步前：'+str(2*k+1)+'条边','Before growth step 3: '+str(2*k+1)+' edges'),17,anchor='middle')
    s.text(180,366,tr(lg,'绿边才产生两个内部孩子','Green edges create two internal children'),15,TEAL,anchor='middle');return s

def kary_scene(lg,k,j,mobile=False):
    w=360 if mobile else 850;s=Svg(w,954 if mobile else 659);d=kary_values(k)
    title(s,kary_title(lg,k))
    # This compares only event B, not equality of the complete model laws.
    ly,vy=(80,112) if mobile else (58,88)
    for x,label,n,den in [(w/4,'GW',d['gw_balanced'],d['gw_total']),(3*w/4,tr(lg,'公开增长','Public growth'),d['growth_balanced'],d['growth_total'])]:
        s.text(x,ly,label,15,GRAY,anchor='middle')
        s.text(x,vy,f'{n}/{den}',27,TEAL,anchor='middle',weight='bold')
    s.text(w/2,vy,'=' if k==2 else '≠',26,GRAY if k==2 else WARM,anchor='middle',weight='bold')
    s.line(25,vy+16,w-25,vy+16,RULE,1)
    # Exact finite configuration counts, not a simulated continuum limit.
    x,y=(25,153) if mobile else (45,164);cols=6 if k==4 else 5 if k==2 else 6;step=49
    s.text(x,y,tr(lg,'GW：条件内部节点 I=3','GW: condition on I=3 internal vertices'),17,anchor='start')
    s.text(x,y+29,'N = '+str(3*k+1),16,GRAY)
    for i in range(d['gw_total']):
        xx=x+(i%cols)*step;yy=y+55+(i//cols)*40;good=i<d['gw_balanced'];s.rect(xx,yy,38,29,PALE if good else '#f0f0e9',TEAL if good else RULE);s.text(xx+19,yy+21,'B' if good else 'C',16,TEAL if good else GRAY,anchor='middle')
    bottom=y+55+math.ceil(d['gw_total']/cols)*40
    s.text(x+145,bottom+26,f'{d["gw_balanced"]}/{d["gw_total"]} = '+ratio(F(d['gw_balanced'],d['gw_total'])),23,TEAL,anchor='middle',weight='bold')
    s.text(x+145,bottom+54,tr(lg,'B：根有两个内部孩子','B: root has two internal children'),14,GRAY,anchor='middle')
    # B/C are concrete ancestor patterns; leaves are omitted in this tiny key.
    for tag,points in [('B',[(x+70,bottom+79),(x+46,bottom+111),(x+94,bottom+111)]),('C',[(x+206,bottom+79),(x+224,bottom+96),(x+242,bottom+113)])]:
        pairs=[(0,1),(0,2)] if tag=='B' else [(0,1),(1,2)]
        for aa,bb in pairs:s.line(*points[aa],*points[bb],TEAL if tag=='B' else GRAY,1.5)
        for px,py in points:s.circle(px,py,4,TEAL if tag=='B' else GRAY,'white')
        s.text(x+(70 if tag=='B' else 224),bottom+137,tag,15,TEAL if tag=='B' else GRAY,anchor='middle')
    s.text(x+145,bottom+160,tr(lg,'小图仅画三个内部节点','Key shows internal vertices only'),13,GRAY,anchor='middle')
    gy=bottom+195 if mobile else 124
    nested(s,growth_panel(lg,k,j),0 if mobile else 465,gy)
    yy=gy+415 if mobile else 599
    if mobile:s.h=gy+465
    s.text(w/2,yy,tr(lg,'增长：','Growth: ')+f'{d["growth_balanced"]}/{d["growth_total"]}'+tr(lg,'；所选边 ','; selected edge ')+str(j)+tr(lg,' → B' if 2<=j<=k else ' → C',' → B' if 2<=j<=k else ' → C'),19,TEAL if 2<=j<=k else WARM,anchor='middle',weight='bold')
    foot(s,tr(lg,'有限精确计算；不是CRT收敛图','Exact finite counts, not a CRT limit picture'));return s

def controls(attr,items,active,extra=''):
    return '<div class="v8-controls" '+extra+'>'+''.join(f'<button type="button" data-{attr}="{k}" aria-pressed="{str(str(k)==str(active)).lower()}">{v}</button>' for k,v in items)+'</div>'
def responsive(code,lg,key):return f'<picture data-v8-picture><source media="(max-width:700px)" srcset="{BASE}{code}-{lg}-{key}-mobile.svg"><img class="v8-scene" src="{BASE}{code}-{lg}-{key}-desktop.svg" alt="{E(tr(lg,*META[code][2:]))}"></picture>'
def static(code,lg,panes):
    cap=tr(lg,*CAP[code]);lines=wrap_caption(cap,lg);s=Svg(900,100+sum(p.h+25 for p in panes)+25*len(lines));title(s,tr(lg,*META[code][2:]));y=55
    for i,p in enumerate(panes):save(p,f'{code}.{lg}.page{i+1}.svg',tr(lg,*META[code][2:]));nested(s,p,(900-p.w)/2,y);y+=p.h+25
    for line_ in lines:s.text(25,y+22,line_,16,GRAY);y+=25
    save(s,f'{code}.{lg}.svg',tr(lg,*META[code][2:]))

def generate():
    A.mkdir(parents=True,exist_ok=True);rows=[]
    for lg in ['zh','en']:
      for code,(slug,section,zh,en) in META.items():
        heading=tr(lg,zh,en);cap=tr(lg,*CAP[code]);coverage=[section]
        def emit(scene,key):
            for mobile in [False,True]:save(scene(mobile),f'{code}-{lg}-{key}-'+('mobile' if mobile else 'desktop')+'.svg',kary_title(lg,int(key.split('-')[0])) if code=='V58' else heading)
        if code=='V54':
            for ai in range(3):
                for ui in range(9):emit(lambda mobile:mass_scene(lg,ai,ui,mobile),f'{ai}-{ui}')
            body=controls('pause',[(str(i),'a = '+str(v)) for i,v in enumerate([F(0),F(1,4),F(1,2)])],'1')+'<label class="v8-range">U <input type="range" min="0" max="8" step="1" value="4" data-time aria-label="'+tr(lg,'示意均匀时间','Illustrative uniform time')+'"><span data-time-label>1/2</span></label>'+responsive(code,lg,'1-4')
            result=tr(lg,'距离树相同；顶端质量1/4，连续质量3/4。','Same metric tree; top mass 1/4, diffuse mass 3/4.');panes=[mass_scene(lg,i,4) for i in [0,2]];coverage=['54.9','54.19','54.21']
        elif code=='V55':
            for mode in range(3):emit(lambda mobile:witness_scene(lg,mode,mobile),str(mode))
            body=controls('witness',[(str(i),tr(lg,['几何对齐','质量对齐','共同折中'][i],['Geometry','Mass','Joint compromise'][i])) for i in range(3)],'0')+responsive(code,lg,'0')
            result=tr(lg,'分别rGH=rGP=0；共同rGHP=1/2。图内数值是当前摆放误差。','Separately rGH=rGP=0; jointly rGHP=1/2. Diagram values describe the current placement.');panes=[witness_scene(lg,i) for i in range(3)];coverage=['55.12','55.13']
        elif code=='V56':
            for mode,count in [('balanced',3),('iid',8)]:
                for j in range(count):emit(lambda mobile:split_scene(lg,mode,j,mobile),f'{mode}-{j}')
            body=controls('splitmode',[('balanced',tr(lg,'按可见人数均分','Balance visible sample')),('iid',tr(lg,'独立投公平位','Independent fair bits'))],'balanced')
            body+=controls('splitinput',[(str(i),tr(lg,'单独'+str(i+1),'Isolate '+str(i+1))) for i in range(3)],'2','data-input-group="balanced"')
            body+=controls('splitinput',[(str(i),f'{i:03b}') for i in range(8)],'1','data-input-group="iid" hidden')+responsive(code,lg,'balanced-2')
            result=tr(lg,'先检验按人数均分：直接分离率1，三人限制后2/3，不一致。切换到独立投位后，两者都是1/2。','First test sample balancing: direct rate 1, restricted rate 2/3—inconsistent. Switch to independent bits: both rates are 1/2.');panes=[split_scene(lg,'balanced',2),split_scene(lg,'iid',1)];coverage=['56.1','56.8','56.9']
        elif code=='V57':
            for ui in range(3):
                for ei in range(3):
                    for after in [0,1]:emit(lambda mobile:graft_scene(lg,ui,ei,after,mobile),f'{ui}-{ei}-{after}')
            body=controls('graftu',[(str(i),'U = '+str(v)) for i,v in enumerate(US)],'1')+controls('exponential',[(str(i),'E = '+str(v)) for i,v in enumerate(ES)],'1')+controls('after',[('0',tr(lg,'接枝前','Before')),('1',tr(lg,'接枝后','After'))],'1')+responsive(code,lg,'1-1-1')
            result=tr(lg,'按长度选边：1/4、1/2、1/4。标准e的4r dr时钟。','Length weights: 1/4,1/2,1/4. Clock 4r dr for standard e.');panes=[graft_scene(lg,1,1,a) for a in [0,1]];coverage=['57.6','57.7','57.8','57.12']
        else:
            for k in [2,3,4]:
                for j in range(2*k+1):emit(lambda mobile:kary_scene(lg,k,j,mobile),f'{k}-{j}')
            body=controls('arity',[(str(k),'k = '+str(k)) for k in [2,3,4]],'3')+controls('growedge',[(str(j),tr(lg,'边'+str(j),'Edge '+str(j))) for j in range(9)],'2')+responsive(code,lg,'3-2')
            result=tr(lg,'k=3：GW为3/12，公开增长为2/7。分叉数没有唯一确定概率律。','k=3: GW gives 3/12; public growth gives 2/7. Arity does not determine the law.')
            body+='<details><summary>'+tr(lg,'公开模型与连续极限的边界','Public models and continuum-limit boundaries')+'</summary><p>'+tr(lg,'固定k的条件有限方差GW采用均匀节点质量与平方根尺度。Haas–Stephenson增长采用均匀叶质量与I^(-1/k)尺度；本书未完整重证其一般整树紧性。图中的有限计算既不证明该定理，也不识别任何作者未发表的CRT。稳定Lévy树和ICRT是其他模型，本图不添加它们的分类或质量公式。','Fixed-k conditioned finite-variance GW uses vertex mass and square-root scaling. Haas–Stephenson growth uses leaf mass and I^(-1/k) scaling; the book has not fully reproved its general whole-tree tightness theorem. Finite counts do not prove that theorem or identify any unpublished CRT. Stable Lévy trees and ICRT are other models, and no classification or mass formula for them is added here.')+'</p></details>'
            panes=[kary_scene(lg,k,2) for k in [2,3,4]];coverage=['58.1','58.2','58.3','58.5','58.19']
        static(code,lg,panes)
        printbody='<div class="v8-print">'+''.join(f'<section><h4>{E(heading)} · {i+1}/{len(panes)}</h4><img src="{BASE}{code}.{lg}.page{i+1}.svg" alt="{E(heading)}"><p>{E(cap)}</p></section>' for i in range(len(panes)))+'</div>'
        refs=' · '.join(f'<a href="{url}">{E(label)}</a>' for label,url in SOURCES[code])
        displayheading=kary_title(lg,3) if code=='V58' else heading
        headingattr=' data-v8-heading' if code=='V58' else ''
        fragment=f'<figure class="volume8-explain" id="visual-{code}" data-v8="{code}" lang="{lg}"><header><span>{code}</span><h3{headingattr}>{E(displayheading)}</h3></header>{body}{printbody}<output data-v8-result aria-live="polite">{result}</output><details><summary>'+tr(lg,'条件、计算与边界','Conditions, calculations and limits')+f'</summary><p>{E(cap)}</p><p>{refs}</p></details><figcaption>'+tr(lg,'准确有限模型或确定性构造；不以图像替代证明。','Exact finite models or deterministic constructions; diagrams do not replace proofs.')+f'</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/figures/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
        rows.append(dict(id=code,lang=lg,slug=slug,section=section,coverage_sections=coverage,title=heading,html=fragment,condition=cap,sources=SOURCES[code],status='adopted visual working draft; targeted revision awaiting author spot-check' if code in ['V56','V58'] else 'adopted visual working draft; final device, PDF and aesthetic acceptance open'))
    write(R/'publication/explanatory-volume8-batch1-working.json',json.dumps(dict(automatic_formal_site_injection=False,canonical_manuscript_changes=False,reused_adopted=['P04','P05'],unpublished_author_research_used=False,figures=rows),ensure_ascii=False,indent=2)+'\n')
    print('Five bilingual volume VIII candidates generated; no old manuscript or asset overwritten.')

if __name__=='__main__':generate()
