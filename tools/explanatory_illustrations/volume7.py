"""Exact, bilingual explanatory models for volume VII. Never writes manuscripts."""
from pathlib import Path
from fractions import Fraction as F
import json, math, re, hashlib
from .pilot_shapes import Svg, tr, E, INK, TEAL, WARM, GRAY, PALE, RULE
from .volume5 import wrap_caption

R=Path(__file__).resolve().parents[2]
A=R/'assets/visuals/explanatory-volume7-v1'
O=R/'reports/volume7-visual-batch1-2026-11-06'
BASE='/assets/visuals/explanatory-volume7-v1/'
META={
 'V48':('48-point-processes','48.9','两扇窗各自Poisson，还没有独立','Poisson in each window is not yet independence'),
 'V49':('49-random-measures','49.7','无穷多个位置，未必有无穷质量','Infinitely many locations need not mean infinite mass'),
 'V51':('51-random-closed-sets','51.8','窗口不相交，命中却可以是同一次','Disjoint windows can be hit by the same event'),
 'V52':('52-discrete-trees','52.12','同一棵树，三种记录与两个时钟','One tree, three records and two clocks'),
 'V53':('53-tree-scaling','53.9','切口合法，还没有控制树高','A legal cut does not yet control height')}
CAP={
'V48':('空间只有a、b两点，允许重数。独立模型取Kₐ、Kᵦ独立Poisson(1)，复制模型取单个K∼Poisson(1)并令两区计数都等于K。两模型有相同Poisson边缘和平均计数，但两区全空概率分别为e⁻²、e⁻¹。以独立U、V均匀于[0,1)作共同底层输入：独立模型各取Poisson逆CDF，复制模型只使用U。概率面积是连续均匀输入下的精确面积；按钮只指定说明性输入，不进行模拟。有限两点模型解释联合信息的必要性，不代替正文一般PRM的构造与独立散布证明。',
'The space has two locations a,b and permits multiplicities. Independent counts K_a,K_b are Poisson(1); the copied model sets both counts equal to one Poisson(1) variable K. Marginals and mean measures agree, but the probability of two empty windows is exp(-2) versus exp(-1). Independent uniforms U,V in [0,1) form a common input: two inverse CDFs in the first model, U alone in the second. Shaded probabilities are exact continuous-input areas. Buttons specify illustrative inputs, not simulations. This two-location example does not replace the general PRM construction or scattering proof.'),
'V49':('xₖ=1/(k+1)，k≥1。比较μ=Σ2⁻ᵏδₓₖ、η=Σδₓₖ及Lebesgue测度。前两者有相同无限支撑点，μ总质量1，η总质量∞。在R中，含0的紧窗口使η局部无限，而μ仍为Radon；在E=(0,1)中η是Radon，因为每个紧集远离0。图中包含0的闭区间不是E=(0,1)的紧子集，显示“—”而非质量0。闭窗口[1/4,3/4]含3个原子，μ质量7/8；[1/16,3/4]含15个，μ质量1−2⁻¹⁵。点圆面积按前若干权重表示，省略号代表未画完的尾部；无限结论由完整级数和紧集距离证明，不由有限图点数推出。',
'Let x_k=1/(k+1), k>=1. Compare mu=sum 2^(-k) delta_(x_k), eta=sum delta_(x_k), and Lebesgue measure. The first two have the same infinitely many locations, but total masses 1 and infinity. On R, a compact window containing 0 makes eta locally infinite; mu remains Radon. On E=(0,1), eta is Radon because compact subsets stay away from 0. The displayed closed interval containing 0 is not a compact subset of E: a dash does not mean zero mass. [1/4,3/4] contains 3 atoms with mu mass 7/8; [1/16,3/4] contains 15 with mass 1-2^(-15). Circle areas encode initial weights; the ellipsis stands for the unpictured tail. Infinite claims follow from the full series and compact-set argument, not from drawn point counts.'),
'V51':('U为[0,1]上的连续均匀变量，Fᵤ=[0,1]×{U}。Kₐ、Kᵦ是两个横坐标不同的紧竖线段，空间中始终不交；各自命中当且仅当U落在相应闭高度区间。T(K)等于高度投影的长度，P(两区共同命中)=T(Kₐ)+T(Kᵦ)−T(Kₐ∪Kᵦ)。面积／长度读数来自连续U的Lebesgue概率，滑块的有限示意位置不被当作离散均匀模型。端点属于窗口，单个端点对概率没有贡献。这里只演示容量非可加和由并集恢复联合读数；一般LCSC空间的Choquet存在唯一性与完全交替性仍由正文证明。',
'U is continuously uniform on [0,1], and F_U=[0,1] x {U}. The two compact vertical segments have different horizontal coordinates, so they are disjoint in space. Each is hit exactly when U is in its closed height interval. T(K) is the length of the height projection; the probability of hitting both is T(K_a)+T(K_b)-T(K_a union K_b). Readings use continuous Lebesgue probability, not a discrete uniform law on slider positions. Endpoints are included but have probability zero individually. This shows nonadditivity and recovery of joint readings from unions; the general LCSC Choquet theorem and complete alternation remain the responsibility of the text.'),
'V52':('只使用52.1的两棵五节点有根平面树。访问顺序为深度优先先序，队列先放新孩子，Qⱼ=1+Sⱼ是访问节点j之前的待访问位置数，Hⱼ是其深度。S有5个增量、6个端点，H有5个首次访问读数，C每条边往返一次，时长2(n−1)=8；首次轮廓访问时刻bⱼ=2j−Hⱼ。图不将三者纵值或时钟等同。两棵树每代人口均为1、2、2，却有不同编码。终点S₅=−1表示队列清空，不表示负人口；高度未额外补造第六个节点。有限双射不等于随机树极限，也不自动适用于普通先序无法列完的无限树。',
'These are exactly the two rooted plane trees of five vertices in section 52.1. Order is depth-first preorder; new children enter the front of the task list. Q_j=1+S_j counts pending positions before vertex j, while H_j is its depth. S has 5 increments and 6 endpoints; H has 5 first-visit readings; C traverses each edge twice and lasts 2(n-1)=8. Its first visit to vertex j is b_j=2j-H_j. Neither values nor clocks are identified. Both generation profiles are 1,2,2, but encodings differ. S_5=-1 means an empty task list, not negative population. No sixth vertex is added to H. A finite bijection is not a tree limit theorem or an enumeration theorem for arbitrary infinite trees.'),
'V53':('有限增量串(-1,+1,-1,+1,-1)，总和−1，各增量≥−1。在0≤j<5上最小值−1第一次出现在r=1，最后一次在r=3；前者旋转后只在末步到−1，后者在第3步已到−1而失败。每个有编号切口均实际计算，不将重复最低点忽略。它是离散桥到合法树词的有限操作，不是标准Brownian游程本身。连续Vervaat极限还需要条件桥收敛、唯一最低点的切口稳定与游程律识别。附加单孩子链产生零增量前缀，却使所有旧节点深度增加链长；一般取ℓₘ=⌊m³⁄⁴⌋时ℓₘ/m→0而ℓₘ/√m→∞。这是确定性高度失稳机制，不宣称加链后仍服从固定条件GW律，也不宣称已得到CRT或GHP收敛。',
'The finite increments are (-1,+1,-1,+1,-1), each at least -1 and summing to -1. On 0<=j<5, the minimum -1 is first reached at r=1 and last at r=3. The first cut reaches -1 only at the end; the last cut reaches it at step 3 and fails. Every indexed cut is computed. This is a finite bridge-to-tree-word operation, not itself a standard Brownian excursion. The continuous Vervaat limit also needs a conditioned bridge theorem, cut stability at a unique minimum, and identification of the excursion law. A unary ancestral chain adds a zero-increment prefix but increases all old depths by its length. For l_m=floor(m^(3/4)), l_m/m tends to 0 while l_m/sqrt(m) diverges. This is a deterministic instability example, not a claim that modified trees retain the fixed conditioned GW law or that CRT/GHP convergence is proved.')}

def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def save(s,name,title):write(A/name,s.document(title));return s
def nested(s,t,x,y,w,h):s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {t.w} {t.h}">{t.fragment()}</svg>')
def title(s,text,y=28):
    if s.w<=350 and len(text)>35:
        import textwrap
        lines=textwrap.wrap(text,width=34)
        for i,line in enumerate(lines):s.text(s.w/2,22+21*i,line,17,anchor='middle',weight='bold')
    else:s.text(s.w/2,y,text,18 if s.w<=350 else 20,anchor='middle',weight='bold')
def ratio(x):return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def poisson_quantile(u):
    p=math.exp(-1);s=p;k=0
    while u>s:k+=1;p/=k;s+=p
    return k

def count_scene(lg,mode,preset,mobile=False):
    w=350 if mobile else 830;s=Svg(w,620 if mobile else 410)
    u,v=[(.12,.8),(.64,.08),(.84,.84)][preset];q=math.exp(-1)
    counts=[poisson_quantile(u),poisson_quantile(v if mode=='independent' else u)]
    title(s,tr(lg,'独立的两个输入' if mode=='independent' else '复制同一个输入','Two independent inputs' if mode=='independent' else 'Copy one input'))
    xs=[78,272] if mobile else [115,315]
    if mode=='independent':
        for x,l in zip(xs,['U','V']):s.circle(x,75,22,TEAL,'white');s.text(x,82,l,22,anchor='middle');s.arrow(x,100,x,140)
    else:
        cx=sum(xs)/2;s.circle(cx,75,22,TEAL,'white');s.text(cx,82,'U',22,anchor='middle');s.line(cx,97,cx,115,TEAL);s.line(xs[0],115,xs[1],115,TEAL)
        for x in xs:s.arrow(x,115,x,140)
    for i,x in enumerate(xs):
        s.rect(x-64,148,128,94,'white',TEAL)
        s.text(x,170,['a','b'][i],19,GRAY,anchor='middle')
        for k in range(counts[i]):s.circle(x-15+30*k,197,8,TEAL)
        s.text(x,230,'N = '+str(counts[i]),22,anchor='middle')
    s.text(sum(xs)/2,280,f'U={u:.2f}, V={v:.2f}',17,GRAY,anchor='middle')
    if mode=='copied':s.text(sum(xs)/2,306,tr(lg,'V未使用；两区计数都只由U生成','V unused; both counts use U'),15,WARM,anchor='middle')
    x,y,side=(67,343,216) if mobile else (540,72,216)
    s.rect(x,y,side,side,'#f0f1eb',RULE)
    s.rect(x,y+side*(1-(q if mode=='independent' else 1)),side*q,side*(q if mode=='independent' else 1),'#b9d9ca',TEAL)
    s.line(x+q*side,y,x+q*side,y+side,TEAL,1,'4 4')
    s.circle(x+u*side,y+(1-v)*side,5,WARM)
    if mode=='independent':s.line(x,y+side*(1-q),x+side,y+side*(1-q),TEAL,1,'4 4')
    s.text(x+side/2,y-15,tr(lg,'两扇窗同时空：输入区域','Input region: both windows empty'),16,anchor='middle')
    s.text(x+side+8,y+side+4,'U',17,GRAY);s.text(x-18,y+5,'V',17,GRAY)
    label=('e⁻² = '+f'{q*q:.4f}') if mode=='independent' else ('e⁻¹ = '+f'{q:.4f}')
    s.text(x+side/2,y+side+36,label,25,TEAL,anchor='middle',weight='bold')
    s.text(w/2,s.h-12,tr(lg,'边缘都Poisson(1)，联合律不同','Same Poisson marginals; different joint law'),13 if mobile else 15,GRAY,anchor='middle')
    return s

def mass_values(space,window):
    lo=[F(1,4),F(1,16),F(0)][window];valid=not(space=='open' and lo==0)
    if not valid:return dict(valid=False,counts=None,mass=None,length=None)
    n=None if lo==0 else int(1/lo)-1
    return dict(valid=True,counts=n,mass=F(1) if n is None else F(1)-F(1,2**n),length=F(3,4)-lo)

def mass_scene(lg,space,window,mobile=False):
    w=350 if mobile else 840;s=Svg(w,610 if mobile else 460);vals=mass_values(space,window);lo=[0.25,.0625,0][window]
    title(s,'E = '+('(0,1)' if space=='open' else 'R'))
    a,b=(40,w-36) if mobile else (210,790);Y=[132,300,468] if mobile else [135,260,385]
    labels=[tr(lg,'加权原子 μ','Weighted atoms: mu'),tr(lg,'单位点计数 η','Unit counting: eta'),tr(lg,'长度质量 dx','Length: dx')]
    for i,y in enumerate(Y):
        s.text(20,y-58,labels[i],17,TEAL if i==0 else WARM if i==1 else GRAY)
        left=a+lo*(b-a);right=a+.75*(b-a)
        s.rect(left,y-36,right-left,67,PALE if vals['valid'] else '#fbf0df',TEAL if vals['valid'] else WARM)
        s.line(a,y,b,y,GRAY,1)
        if i==2:
            s.rect(a,y-5,b-a,10,'#bdd3ca');s.line(a-9,y,a-2,y,GRAY,1);s.line(b+2,y,b+9,y,GRAY,1)
        else:
            for k in range(1,10):
                x=a+(b-a)/(k+1);radius=math.sqrt(2**(-k))*17 if i==0 else 4
                s.circle(x,y,radius,TEAL if i==0 else WARM,'white' if i==1 else None)
            s.text(a+3,y-12,'…',22,GRAY)
        # Zero is a boundary/accumulation location, never an extra atom.
        s.line(a,y-8,a,y+8,GRAY,1)
        s.text(a,y+52,'0',14,GRAY,anchor='middle');s.text(b,y+52,'1',14,GRAY,anchor='middle')
        value='—' if not vals['valid'] else (ratio(vals['mass']) if i==0 else ('∞' if vals['counts'] is None else str(vals['counts'])) if i==1 else ratio(vals['length']))
        posx=w-24 if mobile else 126;posy=y-58 if mobile else y+6
        s.text(posx,posy,value,23,TEAL if i==0 else WARM if i==1 else GRAY,anchor='end' if mobile else 'middle',weight='bold')
    foot=tr(lg,'K不是E内的紧集；—不是质量0','K is not compact in E; a dash is not zero') if not vals['valid'] else tr(lg,'同一个紧窗口：读质量，不只数位置','One compact window: read mass, not only locations')
    s.text(w/2,s.h-10,foot,12 if mobile and lg=='en' else 15,WARM if not vals['valid'] else GRAY,anchor='middle');return s

INTERVALS=[(F(1,5),F(3,5),F(1,5),F(3,5)),(F(1,10),F(7,20),F(13,20),F(9,10)),(F(3,20),F(13,20),F(2,5),F(17,20))]
def hit_values(case):
    a,b,c,d=INTERVALS[case];joint=max(F(0),min(b,d)-max(a,c));return b-a,d-c,(b-a)+(d-c)-joint,joint

def hit_conclusion(lg,case):
    relation=tr(lg,['高度相同','高度分离','高度重叠'][case],['Same heights','Separated heights','Overlapping heights'][case])
    return relation+tr(lg,'：共同命中概率',': P(both)=')+ratio(hit_values(case)[3])

def hit_scene(lg,case,u_step,mobile=False):
    w=350 if mobile else 850;s=Svg(w,705 if mobile else 440);a,b,c,d=INTERVALS[case];u=F(u_step,20)
    title(s,tr(lg,'一条横线，同时回答两次命中','One horizontal line answers both hit questions'))
    x0,y0,side=(30,80,285) if mobile else (38,75,288)
    s.rect(x0,y0,side,side,'white',RULE)
    for x,lo,hi,label,color in [(x0+.3*side,a,b,'Kₐ',TEAL),(x0+.7*side,c,d,'Kᵦ',WARM)]:
        s.line(x,y0+side*(1-float(hi)),x,y0+side*(1-float(lo)),color,7);s.text(x,y0+side+25,label,19,color,anchor='middle')
        if lo<=u<=hi:s.circle(x,y0+side*(1-float(u)),7,color,'white')
    s.line(x0,y0+side*(1-float(u)),x0+side,y0+side*(1-float(u)),INK,2)
    s.text(x0+side,y0-12,'U = '+ratio(u),17,GRAY,anchor='end')
    bx,by,bs=(57,440,180) if mobile else (470,100,240)
    s.text(bx+55,by-25,tr(lg,'同一高度U的事件','Events on the same U'),18,anchor='middle')
    for j,(lo,hi,c0,label) in enumerate([(a,b,TEAL,'A'),(c,d,WARM,'B')]):
        x=bx+70*j;s.rect(x,by,28,bs,'#f1f0e9',RULE);s.rect(x,by+bs*(1-float(hi)),28,bs*float(hi-lo),c0)
        s.text(x+14,by+bs+25,label,17,c0,anchor='middle')
    s.line(bx-10,by+bs*(1-float(u)),bx+110,by+bs*(1-float(u)),INK,1.5)
    s.text(bx+145,by+bs/2,'∩',24,TEAL,anchor='middle')
    joint=hit_values(case)[3]
    s.text(bx+145,by+bs/2+36,ratio(joint),24,TEAL,anchor='middle',weight='bold')
    s.text(w/2,s.h-14,hit_conclusion(lg,case),15,WARM if joint==0 else GRAY,anchor='middle')
    return s

TREES={
 'A':{'nodes':['','1','11','12','2'],'xy':[(175,35),(95,125),(50,215),(140,215),(275,125)]},
 'B':{'nodes':['','1','11','2','21'],'xy':[(175,35),(90,125),(90,215),(270,125),(270,215)]}}
def tree_data(name):
    nodes=TREES[name]['nodes'];k=[sum(v[:-1]==u for v in nodes[1:]) for u in nodes]
    W=[0]
    for z in k:W.append(W[-1]+z-1)
    H=list(map(len,nodes));C=[];walk=[]
    def visit(u):
        walk.append(u);C.append(len(u))
        for v in nodes:
            if v and v[:-1]==u:visit(v);walk.append(u);C.append(len(u))
    visit('');queue=[''];qs=[]
    for u in nodes:
        assert queue[0]==u;qs.append(queue[:]);queue=queue[1:];queue=[v for v in nodes if v and v[:-1]==u]+queue
    return dict(nodes=nodes,k=k,W=W,H=H,C=C,walk=walk,queue=qs,b=[2*j-h for j,h in enumerate(H)])

def tree_panel(lg,name,j):
    data=tree_data(name);s=Svg(350,295);xy=TREES[name]['xy'];nodes=data['nodes'];active=nodes[j]
    for i,u in enumerate(nodes):
        if u:
            pi=nodes.index(u[:-1]);s.line(*xy[pi],*xy[i],WARM if active.startswith(u) else RULE,2)
    for i,(u,(x,y)) in enumerate(zip(nodes,xy)):
        color=TEAL if i==j else WARM if active.startswith(u) else GRAY
        s.circle(x,y,18,color,color if i==j else 'white');s.text(x,y+6,'ρ' if not u else u,17,'white' if i==j else color,anchor='middle')
        s.text(x+24,y-14,'v'+str(i),13,GRAY)
    s.text(175,278,tr(lg,'每代人口仍是1、2、2','Generation sizes remain 1,2,2'),16,GRAY,anchor='middle');return s

def task_panel(lg,name,j):
    d=tree_data(name);s=Svg(350,245);title(s,tr(lg,'访问前，列表还剩哪些地址？','Which addresses are pending before this visit?'))
    for i,u in enumerate(d['queue'][j]):
        x=18+i*104;s.rect(x,65,90,52,PALE if i==0 else 'white',TEAL if i==0 else RULE);s.text(x+45,99,u or 'ρ',22,TEAL if i==0 else GRAY,anchor='middle')
    s.text(175,159,'Q'+str(j)+' = '+str(1+d['W'][j]),27,TEAL,anchor='middle',weight='bold')
    s.text(175,201,tr(lg,'先用掉当前位置，再把孩子插到最前','Use slot; put children at the front'),16,anchor='middle')
    s.text(175,234,tr(lg,'不是本代人口，也不是深度','Neither generation size nor depth'),16,WARM,anchor='middle');return s

def strip(s,values,label,x,y,width,height,selected,clock_label):
    lo=min(values);hi=max(max(values),1);xstep=width/(len(values)-1);scale=height/(hi-lo+1)
    yy=lambda v:y+(hi-v)*scale+10
    s.text(x,y-28,label,17,TEAL);s.line(x,yy(0),x+width,yy(0),RULE,1)
    for i in range(len(values)-1):s.line(x+i*xstep,yy(values[i]),x+(i+1)*xstep,yy(values[i+1]),GRAY,1.7)
    for i,v in enumerate(values):s.circle(x+i*xstep,yy(v),4,TEAL if i==selected else GRAY,'white');s.text(x+i*xstep,y+height+30,str(i),13,GRAY,anchor='middle')
    s.circle(x+selected*xstep,yy(values[selected]),7,TEAL,TEAL)
    s.text(x+width,y-11,clock_label,14,GRAY,anchor='end')

def coding_scene(lg,name,j,mobile=False):
    s=Svg(350 if mobile else 850,1065 if mobile else 710);d=tree_data(name)
    title(s,tr(lg,'树'+name+'：选择一次首次访问','Tree '+name+': select one first visit'))
    nested(s,tree_panel(lg,name,j),0 if mobile else 25,50,350,295)
    nested(s,task_panel(lg,name,j),0 if mobile else 470,355 if mobile else 70,350,245)
    y=665 if mobile else 405;w=296 if mobile else 750;x=27 if mobile else 50
    strip(s,d['W'],'S: '+tr(lg,'待访问数减1','pending minus one'),x,y,w,55,j,tr(lg,'节点步 j','vertex step j'))
    strip(s,d['H'],'H: '+tr(lg,'首次访问深度','first-visit depth'),x,y+132,w,55,j,tr(lg,'节点步 j','vertex step j'))
    strip(s,d['C'],'C: '+tr(lg,'逐边往返深度','edge-walk depth'),x,y+264,w,55,d['b'][j],tr(lg,'边步 ℓ','edge step l'))
    # Desktop needs more room for three complete strips.
    if not mobile:s.h=815
    text=f'j={j}  ·  H={d["H"][j]}  ·  b={d["b"][j]}'
    s.text(s.w/2,s.h-12,text,20,TEAL,anchor='middle',weight='bold');return s

INCREMENTS=[-1,1,-1,1,-1]
def cut_data(r):
    inc=INCREMENTS[r:]+INCREMENTS[:r];w=[0]
    for a in inc:w.append(w[-1]+a)
    return dict(increments=inc,W=w,legal=min(w[:-1])>=0,first_hit=next(i for i,x in enumerate(w) if x==-1))

def necklace(lg,r):
    s=Svg(350,235);cx,cy=175,105;rad=74
    xy=[]
    for i,z in enumerate(INCREMENTS):
        a=-math.pi/2+i*2*math.pi/5;x=cx+rad*math.cos(a);y=cy+rad*math.sin(a);xy.append((x,y))
    for i,(x,y) in enumerate(xy):
        xx,yy=xy[(i+1)%5];s.line(x,y,xx,yy,RULE,1.5)
        s.arrow(x+(xx-x)*.43,y+(yy-y)*.43,x+(xx-x)*.64,y+(yy-y)*.64,GRAY)
    for i,((x,y),z) in enumerate(zip(xy,INCREMENTS)):
        c=TEAL if i==r else GRAY;s.rect(x-27,y-19,54,38,PALE if i==r else 'white',c);s.text(x,y+7,'+1' if z==1 else '−1',21,c,anchor='middle');s.text(x,y-27,chr(97+i),14,GRAY,anchor='middle')
    s.text(cx,cy+5,'r = '+str(r),24,TEAL,anchor='middle');s.text(175,225,tr(lg,'字母保留原来每一个增量的身份','Letters retain the identity of each increment'),15,GRAY,anchor='middle');return s

def cut_scene(lg,r,mobile=False):
    d=cut_data(r);s=Svg(350 if mobile else 850,685 if mobile else 440);title(s,tr(lg,'在第'+str(r)+'个端点前切开','Cut before endpoint '+str(r)))
    nested(s,necklace(lg,r),0 if mobile else 15,42,350,235)
    x,y,width=(27,390,296) if mobile else (470,125,315)
    s.text(x+width/2,y-50,tr(lg,'移到开头的增量次序','Rotated order'),18,anchor='middle')
    for j,z in enumerate(d['increments']):
        xx=x+j*width/5;s.rect(xx,y-25,width/5-4,34,PALE if j==0 else 'white',RULE);s.text(xx+width/10,y-2,chr(97+(r+j)%5),18,TEAL,anchor='middle')
    # A connected path explains first arrival; red marks any premature -1.
    yy=lambda v:y+90-44*v
    s.line(x,yy(0),x+width,yy(0),RULE,1);s.line(x,yy(-1),x+width,yy(-1),WARM,1,'4 4')
    s.text(x-9,yy(0)+5,'0',13,GRAY,anchor='end');s.text(x-9,yy(-1)+5,'−1',13,WARM,anchor='end')
    for j in range(5):s.line(x+j*width/5,yy(d['W'][j]),x+(j+1)*width/5,yy(d['W'][j+1]),TEAL if d['legal'] else WARM,2)
    for j,v in enumerate(d['W']):s.circle(x+j*width/5,yy(v),4,WARM if v<0 else TEAL,'white');s.text(x+j*width/5,y+200,str(j),14,GRAY,anchor='middle')
    if not d['legal']:s.circle(x+d['first_hit']*width/5,yy(-1),9,WARM,'white')
    msg=tr(lg,'只在末步到−1：合法树词','First reaches -1 at the end: legal') if d['legal'] else tr(lg,'第'+str(d['first_hit'])+'步已到−1：提前结束','Already at -1 at step '+str(d['first_hit'])+': too early')
    s.text(s.w/2,s.h-15,msg,19,TEAL if d['legal'] else WARM,anchor='middle',weight='bold');return s

def chain_scene(lg,length):
    s=Svg(350,290);title(s,tr(lg,'再加'+str(length)+'层单孩子祖先','Add '+str(length)+' unary ancestors'))
    y0=60
    if length:
        for i in range(length):
            y=y0+i*22
            if i:s.line(175,y-16,175,y-3,WARM,2)
            s.circle(175,y,4,WARM,'white')
        s.line(175,y0+(length-1)*22+4,175,y0+length*22+15,WARM,2)
    top=y0+length*22+16;s.nodes.append(f'<path d="M175 {top}l-42 55h84z" fill="{PALE}" stroke="{TEAL}"/>');s.text(175,top+43,'T',23,TEAL,anchor='middle')
    s.text(175,260,tr(lg,'任务前缀全0；旧节点深度 +'+str(length),'Zero task prefix; old depths +'+str(length)),16,anchor='middle');return s

def controls(attr,items,active):
    return '<div class="v7-controls" role="group">'+''.join(f'<button type="button" {attr}="{key}" aria-pressed="{str(str(key)==str(active)).lower()}">{label}</button>' for key,label in items)+'</div>'
def responsive(code,lg,state):
    return f'<picture data-v7-picture><source media="(max-width:700px)" srcset="{BASE}{code}-{lg}-{state}-mobile.svg"><img class="v7-scene" src="{BASE}{code}-{lg}-{state}-desktop.svg" alt="{E(tr(lg,*META[code][2:]))}" loading="eager"></picture>'

def static(code,lg,panes,cap):
    lines=wrap_caption(cap,lg);scale=1;heights=[p.h for p in panes];height=75+sum(heights)+len(panes)*25+len(lines)*25+45;s=Svg(900,height)
    title(s,tr(lg,*META[code][2:]),38);y=65
    for p in panes:
        h=p.h; nested(s,p,(900-p.w)/2,y,p.w,h);y+=h+25
    for i,p in enumerate(panes):save(p,f'{code}.{lg}.page{i+1}.svg',tr(lg,*META[code][2:]))
    s.line(30,y,870,y,RULE,1);y+=28
    for line in lines:s.text(30,y,line,16,GRAY);y+=25
    save(s,code+'.'+lg+'.svg',tr(lg,*META[code][2:]))

def generate(codes=None):
    A.mkdir(parents=True,exist_ok=True);rows=[];states={};contexts=[]
    registry=R/'publication/explanatory-volume7-batch1-working.json'
    previous=json.loads(registry.read_text('utf-8')) if registry.exists() else {}
    for lg in ['zh','en']:
        for code,(slug,section,zh,en) in META.items():
            if codes is not None and code not in codes:continue
            cap=tr(lg,*CAP[code]);heading=tr(lg,zh,en)
            if code=='V48':
                for mode in ['independent','copied']:
                    for p in range(3):
                        for mobile in [False,True]:save(count_scene(lg,mode,p,mobile),f'{code}-{lg}-{mode}-{p}-'+('mobile' if mobile else 'desktop')+'.svg',heading)
                body='<p>'+tr(lg,'两扇窗的单独计数都一样。把生成输入连起来以后，哪些联合事件改变了？','Each window has the same count law. Which joint events change when we connect the inputs?')+'</p>'
                body+=controls('data-mode',[('independent',tr(lg,'分别抽两个Poisson数','Two independent Poisson counts')),('copied',tr(lg,'一个Poisson数，复制两次','One Poisson count, copied twice'))],'independent')
                body+=controls('data-preset',[(str(i),f'U={u}, V={v}') for i,(u,v) in enumerate([('.12','.80'),('.64','.08'),('.84','.84')])],'0')+responsive(code,lg,'independent-0')
                result=tr(lg,'两区都空：e⁻²≈0.1353；边缘各自为空：e⁻¹。','Both empty: exp(-2)≈0.1353; each empty marginal: exp(-1).')
                panes=[count_scene(lg,m,0) for m in ['independent','copied']];coverage=['48.1','48.8','48.9','48.11']
            elif code=='V49':
                for space in ['real','open']:
                    for window in range(3):
                        for mobile in [False,True]:save(mass_scene(lg,space,window,mobile),f'{code}-{lg}-{space}-{window}-'+('mobile' if mobile else 'desktop')+'.svg',heading)
                body='<p>'+tr(lg,'同样无限多个位置，可以承载有限质量，也可以让一个紧窗口装下无限质量。先选空间，再选窗口。','The same infinite set of locations can carry finite mass or overload one compact window. Choose the space before the window.')+'</p>'
                body+=controls('data-space',[('real','E = R'),('open','E = (0,1)')],'real')+controls('data-window',[(str(i),'K = '+v) for i,v in enumerate(['[1/4,3/4]','[1/16,3/4]','[0,3/4]'])],'0')+responsive(code,lg,'real-0')
                result=tr(lg,'窗口内：加权质量7/8、单位计数3、长度1/2。','In the window: weighted mass 7/8, unit count 3, length 1/2.')
                body+='<p class="v7-boundary">'+tr(lg,'总质量：μ为1，η为∞；dx在R上为∞，在(0,1)上为1。','Total mass: mu=1, eta=infinity; dx is infinite on R and 1 on (0,1).')+'</p>'
                panes=[mass_scene(lg,'real',2),mass_scene(lg,'open',0)];coverage=['49.1','49.5','49.7','49.24']
            elif code=='V51':
                for case in range(3):
                    for u in range(21):
                        for mobile in [False,True]:save(hit_scene(lg,case,u,mobile),f'{code}-{lg}-{case}-{u}-'+('mobile' if mobile else 'desktop')+'.svg',heading)
                body='<p>'+tr(lg,'两个竖窗口始终不接触。它们会不会同时被同一条随机横线命中？','The two vertical windows never touch. Can one random horizontal line hit both?')+'</p>'
                body+=controls('data-case',[(str(i),tr(lg,['同一高度区间','高度区间分离','高度部分重叠'][i],['Same height interval','Separated heights','Partly overlapping heights'][i])) for i in range(3)],'0')
                body+='<label class="v7-range">U <input type="range" min="0" max="20" step="1" value="10" data-height aria-label="'+tr(lg,'示意横线高度','Illustrative line height')+'"><span data-height-label>1/2</span></label>'+responsive(code,lg,'0-10')
                result=tr(lg,'T(Kₐ)=2/5；T(Kᵦ)=2/5；T(并)=2/5；共同命中=2/5。','T(K_a)=2/5; T(K_b)=2/5; T(union)=2/5; both hit=2/5.')
                panes=[hit_scene(lg,i,10) for i in [0,1,2]];coverage=['51.1','51.7','51.8','51.9']
            elif code=='V52':
                for name in ['A','B']:
                    for j in range(5):
                        for mobile in [False,True]:save(coding_scene(lg,name,j,mobile),f'{code}-{lg}-{name}-{j}-'+('mobile' if mobile else 'desktop')+'.svg',heading)
                body='<p>'+tr(lg,'先点一名节点，再看它在任务列表、先序高度和逐边轮廓中分别出现在哪里。','Choose a vertex, then locate it in the pending list, preorder height and edge contour.')+'</p>'
                body+=controls('data-tree',[('A',tr(lg,'树A：两个末代成员是兄弟','Tree A: the last generation are siblings')),('B',tr(lg,'树B：来自不同家庭','Tree B: different parents'))],'A')+controls('data-vertex',[(str(j),'j = '+str(j)) for j in range(5)],'3')+responsive(code,lg,'A-3')
                result='j=3: S=1, Q=2, H=2, b=4; C(4)=2.'
                panes=[coding_scene(lg,n,3) for n in ['A','B']];coverage=['52.1','52.5','52.6','52.9','52.11','52.12','52.13']
            else:
                for r in range(5):
                    for mobile in [False,True]:save(cut_scene(lg,r,mobile),f'{code}-{lg}-{r}-'+('mobile' if mobile else 'desktop')+'.svg',heading)
                for length in [0,2,5]:save(chain_scene(lg,length),f'{code}-{lg}-chain-{length}.svg',heading)
                body='<p>'+tr(lg,'同一串增量，第一次最低点与最后一次最低点会给出相同的合法树词吗？','Do the first and last minima of the same increment word give equally legal tree words?')+'</p>'
                body+=controls('data-cut',[(str(j),tr(lg,'r='+str(j)+(' 首次最低' if j==1 else ' 最后最低' if j==3 else ''),'r='+str(j)+(' first min' if j==1 else ' last min' if j==3 else ''))) for j in range(5)],'1')+responsive(code,lg,'1')
                result=tr(lg,'r=1合法；桥的终点条件没有自行给出首次到达条件。','r=1 is legal; the bridge endpoint alone does not impose first arrival.')
                body+='<details class="v7-deeper"><summary>'+tr(lg,'为什么接下来仍要单独控制高度？','Why does height still need a separate argument?')+'</summary><p>'+tr(lg,'在一棵固定树之前接一条单孩子链：每层新增0任务增量，却增加一层祖先。','Prepend a unary ancestral chain: each new layer adds a zero task increment but one level of ancestry.')+'</p>'+controls('data-chain',[(str(n),'ℓ = '+str(n)) for n in [0,2,5]],'2')+f'<img class="v7-chain" data-chain-scene src="{BASE}{code}-{lg}-chain-2.svg" alt="'+tr(lg,'单孩子链的高度与任务记录','Height and task readings of a unary chain')+'"><p>'+tr(lg,'ℓₘ=⌊m³⁄⁴⌋：相对时长趋0，平方根尺度的高度却发散。这是确定性反例，不是固定条件GW样本。','l_m=floor(m^(3/4)): relative time vanishes, but the height on a square-root scale diverges. This is a deterministic counterexample, not a fixed conditioned-GW sample.')+'</p></details>'
                panes=[cut_scene(lg,r) for r in [1,3]]+[chain_scene(lg,2)];coverage=['53.7','53.8','53.9','53.12','53.13','53.14']
            printbody='<div class="v7-print">'+''.join(f'<section><h4>{E(heading)} · {i+1}/{len(panes)}</h4><img src="{BASE}{code}.{lg}.page{i+1}.svg" alt="{E(heading)}"><p class="v7-print-caption">{E(cap)}</p></section>' for i in range(len(panes)))+'</div>'
            fragment=f'<figure class="volume7-explain" id="visual-{code}" data-v7="{code}" lang="{lg}"><header><span>{code}</span><h3>{E(heading)}</h3></header>{body}{printbody}<output data-v7-result aria-live="polite">{result}</output><details><summary>'+tr(lg,'数学条件与图示边界','Assumptions and diagram limits')+f'</summary><p>{E(cap)}</p></details><figcaption>'+tr(lg,'有限精确模型帮助看见机制；完整定理与证明仍在正文。','An exact finite model reveals the mechanism; full theorems and proofs remain in the text.')+f'</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/figures/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
            rows.append(dict(id=code,lang=lg,slug=slug,section=section,coverage_sections=coverage,title=heading,html=fragment,condition=cap,asset_base=BASE,status='candidate; author visual review pending'))
            static(code,lg,panes,cap)
    if codes is not None:
        old=previous['figures']
        replacements={(r['id'],r['lang']):r for r in rows}
        rows=[replacements.get((r['id'],r['lang']),r) for r in old]
    statuses={(r['id'],r['lang']):r['status'] for r in previous.get('figures',[]) if r.get('status','').startswith('adopted')}
    for row in rows:
        if (row['id'],row['lang']) in statuses:row['status']=statuses[(row['id'],row['lang'])]
    write(registry,json.dumps(dict(previous,automatic_formal_site_injection=False,canonical_manuscript_changes=False,reused_adopted=['P03'],figures=rows),ensure_ascii=False,indent=2)+'\n')
    write(A/'models.json',json.dumps(dict(trees={k:tree_data(k) for k in TREES},cuts={str(r):cut_data(r) for r in range(5)},hit_intervals=[[str(x) for x in row] for row in INTERVALS],hit_values=[[str(x) for x in hit_values(i)] for i in range(3)]),ensure_ascii=False,indent=2))
    print(f'{len(codes) if codes is not None else len(META)} bilingual figure groups updated; protected artwork retained')

if __name__=='__main__':generate()
