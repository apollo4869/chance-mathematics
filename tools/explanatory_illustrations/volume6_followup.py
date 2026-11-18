"""Two further exact structural models and a mobile-only V44 clarification."""
from pathlib import Path
import json,re,math
from .pilot_shapes import Svg,tr,E,INK,TEAL,WARM,GRAY,PALE,RULE
from .volume5 import buttons,wrap_caption
R=Path(__file__).resolve().parents[2];A=R/'assets/visuals/explanatory-volume6-v2';BASE='/assets/visuals/explanatory-volume6-v2/'
O=R/'reports/volume6-visual-batch2-2026-11-05';P=A/'local-preview';PREFIX=BASE+'local-preview/'
META={'V42':('42-harris-coupling','42.7','成功的是这一步，重新开始在下一点','Success on this step; a fresh start at its endpoint'),'V47C':('47-partitions','47.16','合并发生了，样本未必看得见','A merger can be invisible to the sample')}
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def save(s,name,title):write(A/name,s.document(title))
def img(name,alt,attr=''):return f'<img src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def nest(s,t,x,y,w,h):s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {t.w} {t.h}">{t.fragment()}</svg>')
def kernel(lg,x,focus):
 s=Svg(350,315);s.circle(175,35,25,TEAL,'white');s.text(175,43,'Xₙ='+x,20,anchor='middle')
 for j,(c,name) in enumerate([(TEAL,'ν'),(WARM,'δ'+x)]):
  u=86+178*j;active=focus==('common' if j==0 else 'residual');s.arrow(155 if j==0 else 195,55,u,106,c);s.text(117+116*j,88,'1/2',18,c,anchor='middle');s.rect(u-68,116,136,89,PALE if active else 'white',c);s.text(u,146,name,23,c,anchor='middle')
  if j==0:
   for k,v in enumerate(['a','b']):s.rect(u-53+53*k,162,53,28,TEAL if k==0 else WARM);s.text(u-26+53*k,182,v,18,'white',anchor='middle')
  else:s.rect(u-53,162,106,28,TEAL if x=='a' else WARM);s.text(u,182,x,18,'white',anchor='middle')
 s.text(86,229,tr(lg,'新抽，与x无关','Fresh, not from x'),16,TEAL,anchor='middle');s.text(264,229,tr(lg,'保留当前x','Stay at the current x'),16,WARM,anchor='middle')
 q=.75 if x=='a' else .25;s.rect(25,265,300*q,30,TEAL);s.rect(25+300*q,265,300*(1-q),30,WARM);s.text(25+150*q,286,'a: '+('3/4' if x=='a' else '1/4'),18,'white',anchor='middle');s.text(25+300*q+150*(1-q),286,'b: '+('1/4' if x=='a' else '3/4'),18,'white',anchor='middle');s.text(175,312,'P('+x+', ·)',17,GRAY,anchor='middle');return s

def record(x,r):
 coins=[int(j in [r,4,7]) for j in range(8)];states=[x]
 for j,v in enumerate(coins):states.append(('b' if j<=2 or j==7 else 'a') if v else states[-1])
 return coins,states,[r+1,5,8]
def cycles(lg,x,r,mobile=False):
 coins,states,ends=record(x,r)
 if mobile:
  s=Svg(350,428);s.text(175,23,tr(lg,'成功边 → 下一个端点','Successful edge → next endpoint'),18,anchor='middle')
  for k,(a,b) in enumerate(zip(ends[:-1],ends[1:])):
   s.rect(234,42+39*a,98,39*(b-a),PALE if k==0 else '#fbf0df',TEAL if k==0 else WARM);s.text(283,42+39*(a+b)/2+5,f'[{a},{b})',20,TEAL if k==0 else WARM,anchor='middle')
  for n,z in enumerate(states):
   y=42+39*n;s.text(15,y+6,str(n),16,GRAY);s.circle(91,y,14,TEAL if n in ends else GRAY,'white');s.text(91,y+6,z,18,anchor='middle')
   if n<8:s.line(91,y+15,91,y+24,TEAL if coins[n] else RULE,2);s.text(134,y+25,'δ'+str(n)+'='+str(coins[n]),16,TEAL if coins[n] else GRAY)
  s.text(175,406,tr(lg,'右端点属于下一周期','The right endpoint starts the next cycle'),17,WARM,anchor='middle');return s
 s=Svg(790,255);s.text(395,25,tr(lg,'同一条记录：硬币在边上，重启在端点','One record: the coin is on an edge; the fresh start is its endpoint'),19,anchor='middle')
 for k,(a,b) in enumerate(zip(ends[:-1],ends[1:])):
  s.rect(45+82*a-19,112,82*(b-a),48,PALE if k==0 else '#fbf0df');s.text(45+82*(a+b)/2-10,210,f'[{a},{b})',22,TEAL if k==0 else WARM,anchor='middle')
 for n,z in enumerate(states):
  u=45+82*n;s.circle(u,136,16,TEAL if n in ends else GRAY,'white');s.text(u,142,z,19,anchor='middle');s.text(u,180,str(n),15,GRAY,anchor='middle')
  if n<8:
   s.line(u+18,136,u+64,136,RULE,2);s.circle(u+41,80,5,TEAL if coins[n] else RULE);s.text(u+41,62,'δ='+str(coins[n]),15,TEAL if coins[n] else GRAY,anchor='middle')
   if coins[n]:s.arrow(u+41,89,u+72,116,TEAL)
 s.text(395,248,tr(lg,'初始延迟不算iid周期；每段不重复计入右端点','The initial delay is not an iid cycle; right endpoints are not counted twice'),17,WARM,anchor='middle');return s

FULL=[((1,),(2,),(3,),(4,)),((1,),(2,),(3,4)),((1,3,4),(2,)),((1,2,3,4),)]
def restrict(p,n):return tuple(sorted([tuple(x for x in b if x<=n) for b in p if any(x<=n for x in b)],key=lambda x:x[0]))
def partition_row(s,p,n,y):
 b=len(p)
 for i,block in enumerate(p):
  cx=350*(i+.5)/b;w=max(53,28*len(block)+14);s.rect(cx-w/2,y-29,w,58,'white',RULE)
  for j,v in enumerate(block):u=cx+28*(j-(len(block)-1)/2);c=TEAL if v<=n else GRAY;s.circle(u,y,11,c,'white' if v>n else c);s.text(u,y+6,str(v),16,INK if v>n else 'white',anchor='middle')
def projection(lg,n,step):
 s=Svg(350,330);full=FULL[step];small=restrict(full,n);s.text(175,25,tr(lg,'完整四人记录','Full four-person record'),20,anchor='middle');partition_row(s,full,n,83)
 s.arrow(175,121,175,180,TEAL);s.text(193,153,tr(lg,'只留','Keep')+' ['+str(n)+']',17)
 s.text(175,209,tr(lg,'有限样本看见的划分','Partition visible to the sample'),18,anchor='middle');partition_row(s,small,n,252)
 changed=step>0 and restrict(FULL[step-1],n)!=small
 s.text(175,321,tr(lg,'可见的合并' if changed else '限制划分没有改变','A visible merger' if changed else 'The restriction has not changed'),19,TEAL if changed else WARM,anchor='middle');return s

def rate_clock(lg,n,step):
 s=Svg(350,330);full=FULL[step];small=restrict(full,n);q=len(full)*(len(full)-1)//2;v=len(small)*(len(small)-1)//2
 s.text(175,25,tr(lg,'每个完整块对，速率1','Each pair of full blocks has rate 1'),18,anchor='middle')
 for k in range(6):
  s.rect(24+51*k,52,43,31,TEAL if k<v else '#e6e8e4' if k<q else 'white',RULE)
  if k<q:s.text(45+51*k,74,'1',17,'white' if k<v else GRAY,anchor='middle')
 s.text(175,111,tr(lg,f'完整总率 {q} = 可见 {v} + 不可见 {q-v}',f'Full rate {q} = visible {v} + invisible {q-v}'),18,anchor='middle')
 for row,y in enumerate([185,265]):
  s.text(22,y-30,tr(lg,'完整事件' if row==0 else '限制事件','Full events' if row==0 else 'Restricted events'),17);s.line(25,y,325,y,RULE,2)
  for j,t in enumerate([.25,.7,1.4],1):
   xx=25+300*t/1.6;visible=restrict(FULL[j-1],n)!=restrict(FULL[j],n)
   if row==0 or visible:
    c=TEAL if visible else GRAY;s.circle(xx,y,6,c,c if j<=step else 'white');s.text(xx,y+23,str(t),14,c,anchor='middle')
  s.text(25,y+23,'0',14,GRAY);s.text(325,y+23,'t',14,GRAY)
 s.text(175,326,tr(lg,'隐藏事件，不能删掉经过的时间','Hide an event; do not delete elapsed time'),17,WARM,anchor='middle');return s

CAP42=('精确有限模型：E=C={a,b}，ε=1/2，ν=(δa+δb)/2，Rₓ=δₓ。因此P的两行为(3/4,1/4)、(1/4,3/4)。先抽独立硬币δₙ，再按ν或Rₓ抽Xₙ₊₁，不能在看完下一状态后补一枚未经校正的独立硬币。图示三次成功发生在n=r、4、7，重启端点为r+1、5、8；所示记录是一个合法的正概率有限配置，不是模拟频率。ν终点独立于此前信息；从ν开始的半开周期标记(L,X₀,…,X_{L−1})为iid，右端点属于下一周期，初始延迟另计。这里L~Geom(1/2)取值1,2,…且均值2；一般小集还需返回条件，有限周期不自动有有限均值，再生也不自动给同刻耦合。',
'Exact finite model: E=C={a,b}, epsilon=1/2, nu=(delta_a+delta_b)/2 and R_x=delta_x. P has rows (3/4,1/4) and (1/4,3/4). Toss an independent coin delta_n first, then draw X_(n+1) from nu or R_x; do not observe the next state and retroactively add an uncorrected independent coin. The displayed successes at n=r,4,7 yield fresh starts at r+1,5,8. This is one valid positive-probability finite configuration, not simulated frequencies. A fresh nu endpoint is independent of the preceding information. From nu, half-open marks (L,X0,...,X_(L-1)) are iid; the right endpoint starts the next cycle, and the initial delay is separate. Here L is geometric(1/2) on positive integers with mean 2. A general small set needs return assumptions; finite cycles need not have finite mean, and regeneration alone does not align two clocks.')
CAP47=('每对当前完整块的Kingman合并率为1，不按块质量加权。四人路径示意依次合并{3}+{4}、{1}+{3,4}、{1,3,4}+{2}；灰色人不在保留样本[n]中。每个可见块对应唯一完整块，因此当前可见块对的速率仍各为1，含空投影块的合并不改变限制。图上速率条每格为一对的速率1，不是概率质量。两条时间轴共用原时间，示意事件时刻0.25、0.7、1.4不因隐藏事件而压缩；这些时刻是一条说明性路径，不是等待时间期望。有限生成矩阵满足L₄(f∘rₙ)=(Lₙf)∘rₙ，逐幂再求指数级数给半群一致性，条件期望塔式再给限制过程的Markov性。不能只匹配边缘或块数就宣布路径一致，也不从无穷总率安装一个首跳时钟。',
'Kingman gives every pair of current full blocks rate 1, without mass weighting. The illustrative four-person path merges {3}+{4}, then {1}+{3,4}, then {1,3,4}+{2}. Gray individuals are not in the retained sample [n]. Each visible block has one full-block preimage; each visible pair still merges at rate 1. A merger with an empty projection leaves the restriction unchanged. Each rate-bar cell is one unit-rate pair, not probability mass. Both axes retain the same elapsed time: the illustrative event times 0.25,0.7,1.4 are neither expected waits nor compressed after hiding events. The finite generators satisfy L4(f o r_n)=(Ln f) o r_n. Powers and the exponential series yield semigroup consistency; conditioning and the tower property give the restricted Markov law. Matching margins or block counts alone is insufficient. No first-jump clock with infinite total rate is assumed.')

def static(code,lg,panes,cap):
 title=META[code][2 if lg=='zh' else 3];s=Svg(900,1100);s.rect(0,0,900,1100,'white')
 lines=wrap_caption(title,lg)
 for j,line in enumerate(lines):s.text(30,40+28*j,line,25,weight='bold')
 y=80+28*(len(lines)-1)
 for i,t in enumerate(panes):nest(s,t,35+440*i,y,390,390*t.h/t.w)
 end=y+max(t.h/t.w*390 for t in panes)+25
 if code=='V47C':
  s.text(30,end,tr(lg,'若只保留前2人：可见合并率仍为1；前两次事件不改变限制。','Keeping [2]: visible rate stays 1; the first two events leave the restriction unchanged.'),17);end+=32
 else:
  s.text(30,end,tr(lg,'成功在n；重启在n+1。两段共用的端点只归下一段。','Success at n; fresh start at n+1. A shared endpoint belongs only to the next cycle.'),17);end+=32
 s.line(30,end,870,end,RULE,1)
 for j,line in enumerate(wrap_caption(cap,lg)):s.text(30,end+30+24*j,line,17,GRAY)
 s.h=end+60+24*len(wrap_caption(cap,lg));s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';save(s,f'{code}.{lg}.svg',title)

def generate():
 rows=[]
 for code in META:
  for lg in ['zh','en']:
   slug,sec,zh,en=META[code];title=tr(lg,zh,en)
   if code=='V42':
    for x in ['a','b']:
     for focus in ['common','residual']:save(kernel(lg,x,focus),f'V42-{lg}-{x}-{focus}-kernel.svg',title)
     for r in [0,1,2]:
      for mobile in [False,True]:save(cycles(lg,x,r,mobile),f'V42-{lg}-{x}-{r}-'+('mobile' if mobile else 'timeline')+'.svg',title)
    body='<p>'+tr(lg,'进入同一个小集，仍不表示下一状态已经独立。先看一份转移怎样被拆开，再在记录中找真正的重启点。','Reaching a small set does not yet make the next state independent. Split one transition, then locate its genuine fresh start.')+'</p>'
    body+=buttons('data-x',[('a','Xₙ=a'),('b','Xₙ=b')],'a')+buttons('data-source',[('common',tr(lg,'成功：抽共同ν','Success: draw from nu')),('residual',tr(lg,'失败：抽残差Rₓ','Failure: draw from R_x'))],'common')
    body+='<div class="v6n-kernel">'+img(f'V42-{lg}-a-common-kernel.svg',tr(lg,'先抽硬币，再抽状态','Coin first, state second'),'data-kernel')+'</div><h4>'+tr(lg,'沿同一时间轴切出周期','Cut cycles along the same time axis')+'</h4>'+buttons('data-first',[(str(i),tr(lg,f'首成功在n={i}',f'First success at n={i}')) for i in [0,1,2]],'1')
    body+='<div class="v6n-timeline">'+img(f'V42-{lg}-a-1-timeline.svg',tr(lg,'半开周期不重计右端点','Half-open cycles do not double-count endpoints'),'data-timeline')+'</div><div class="v6n-mobile-time">'+img(f'V42-{lg}-a-1-mobile.svg',tr(lg,'手机竖向时钟','Vertical mobile clock'),'data-mobile-time')+'</div>'
    body+='<output data-v6n-result>'+tr(lg,'成功边1→重启点2；独立完整段为[2,5)、[5,8)。','Success on edge 1 gives fresh start 2; full independent cycles are [2,5),[5,8).')+'</output>';cap=tr(lg,*CAP42);panes=[kernel(lg,'a','common'),cycles(lg,'a',1,True)]
   else:
    for n in [2,3]:
     for step in range(4):
      save(projection(lg,n,step),f'V47C-{lg}-{n}-{step}-projection.svg',title);save(rate_clock(lg,n,step),f'V47C-{lg}-{n}-{step}-clock.svg',title)
    body='<p>'+tr(lg,'删去观察名单外的人，可以隐藏一些合并；能否因此把经过的等待也删掉？','Removing unobserved individuals hides some mergers. Does it also remove the time that elapsed?')+'</p>'+buttons('data-keep',[('2',tr(lg,'只留1、2','Keep 1,2')),('3',tr(lg,'只留1、2、3','Keep 1,2,3'))],'2')+buttons('data-step',[(str(i),tr(lg,['初始','3与4合并','1与{3,4}合并','最后合并'][i],['Initial','Merge 3 and 4','Merge 1 with {3,4}','Final merger'][i])) for i in range(4)],'0')
    body+='<div class="v6-pair">'+img(f'V47C-{lg}-2-0-projection.svg',tr(lg,'完整记录到有限限制','Full record to finite restriction'),'data-projection')+img(f'V47C-{lg}-2-0-clock.svg',tr(lg,'总跳率与可见跳率的区别','Total and visible rates differ'),'data-clock')+'</div><output data-v6n-result>'+tr(lg,'完整总率6；可见块对速率1。不可见事件不是限制过程的新跳。','Full total rate 6; visible pair rate 1. Invisible events are not jumps of the restriction.')+'</output>';cap=tr(lg,*CAP47);panes=[projection(lg,2,2),rate_clock(lg,2,2)]
   frag=f'<figure class="volume6 v6-next" data-v6-next="{code}" id="visual-{code}" lang="{lg}"><header><span>{code}</span><h3>{title}</h3></header>{body}<details><summary>'+tr(lg,'模型条件与证明边界','Model assumptions and proof limits')+f'</summary><p>{cap}</p></details><figcaption id="visual-{code}-end">'+tr(lg,'本图解释有限模型中的机制，完整一般条件仍见本节与配套证明。','This diagram explains the finite-model mechanism; general assumptions and proofs remain in the chapter.')+f'</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
   static(code,lg,panes,cap);rows.append(dict(id=code,lang=lg,slug=slug,section=sec,coverage_sections=['42.6','42.7','42.8','42.12'] if code=='V42' else ['47.15','47.16','47.17'],title=title,html=frag,condition=cap,asset_base=BASE,status='new candidate; author visual review pending',kind='new explanatory candidate'))
 # Preserve the adopted constructions, CSS and runtime. Only V44 receives a mobile-only insertion.
 previous=json.loads((R/'publication/explanatory-volume6-batch1-working.json').read_text('utf-8'))['figures']
 for r in previous:
  r=r.copy();r['selected_original_registry']='explanatory-volume6-batch1-working.json';r['status']='visual working draft adopted; final/device/PDF review open'
  if r['id']=='V44':
   lg=r['lang'];summary='<div class="v44-mobile-summary"><strong>'+tr(lg,'新桌不一定产生新值','A new table need not give a new value')+'</strong><div class="v44-prob-pair"><span>'+tr(lg,'新桌','New table')+'<b>1/4</b></span><span>'+tr(lg,'新值','New value')+'<b data-newvalue>1/8</b></span></div><small data-v44-condition>'+tr(lg,'第4人抽样前：α=1；前三人的桌与标签已给定，均只见z。','Before draw 4: alpha=1; the first three seats and labels are given, with only z observed.')+'</small></div>'
   r['html']=r['html'].replace('</header>','</header>'+summary,1);r['status']='adopted subject to requested mobile adjustment; author spot-check pending';r['kind']='mobile-only layout refinement'
  rows.append(r)
 jsave(R/'publication/explanatory-volume6-batch2-working.json',dict(source_commit='1dc71f66',automatic_formal_site_injection=False,canonical_manuscript_changes=False,new_groups=['V42','V47C'],protected_adopted=['P02','V41','V45','V46','V47'],figures=rows))
 write(A/'figures.css',CSS);write(A/'interactions.js',JS)
 print('Two bilingual new candidates; V44 mobile-only summary; five earlier structures preserved')
CSS='''.v44-mobile-summary{display:none}.v6-next .v6n-kernel{max-width:440px;margin:auto}.v6-next .v6n-mobile-time{display:none}.v6-next h4{text-align:center}.v6-next img{width:100%}.v6-next .v6n-timeline{margin:20px 0}@media(max-width:700px){[data-v6=V44] .v44-mobile-summary{display:block;padding:12px 0 14px;border-bottom:1px solid #ccd9d1;margin-bottom:15px}[data-v6=V44] .v44-mobile-summary strong{display:block;font-size:18px;text-align:center}.v44-prob-pair{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:12px 0}.v44-prob-pair span{text-align:center;color:#65756e;font-size:15px}.v44-prob-pair b{display:block;color:#16776d;font-size:29px;line-height:1.4}.v44-mobile-summary small{display:block;font-size:13px;line-height:1.65;color:#65756e}.v6-next .v6n-timeline{display:none}.v6-next .v6n-mobile-time{display:block;max-width:350px;margin:auto}.v6-next .v6n-kernel{max-width:350px}}'''
JS='''document.querySelectorAll('[data-v6=V44]').forEach(root=>root.querySelectorAll('[data-newvalue]').length&&root.querySelectorAll('[data-label]').forEach(b=>b.addEventListener('click',()=>{const atomic=b.dataset.label==='atomic',en=root.lang==='en';root.querySelector('[data-newvalue]').textContent=atomic?'1/8':'1/4';root.querySelector('[data-v44-condition]').textContent=en?(atomic?'Before draw 4: alpha=1; given past seats and tied labels, only z has been observed.':'Before draw 4: alpha=1; nonatomic H, given the past labels a,b.'):(atomic?'第4人抽样前：α=1；给定前三人座次与同名标签，已见仅z。':'第4人抽样前：α=1；H无原子，给定前三人已见标签a、b。');})));document.querySelectorAll('[data-v6-next]').forEach(root=>{const code=root.dataset.v6Next,lg=root.lang,B='/assets/visuals/explanatory-volume6-v2/';let x='a',focus='common',first='1',keep='2',step='0';const press=(a,v)=>root.querySelectorAll('['+a+']').forEach(b=>b.setAttribute('aria-pressed',String(b.getAttribute(a)===v)));function draw(){if(code==='V42'){root.dataset.state=x+'-'+focus+'-'+first;root.querySelector('[data-kernel]').src=B+`V42-${lg}-${x}-${focus}-kernel.svg`;root.querySelector('[data-timeline]').src=B+`V42-${lg}-${x}-${first}-timeline.svg`;root.querySelector('[data-mobile-time]').src=B+`V42-${lg}-${x}-${first}-mobile.svg`;let r=+first+1;root.querySelector('[data-v6n-result]').textContent=lg==='zh'?`成功在n=${first}，重启在${r}；半开完整段为[${r},5)、[5,8)。`:`Success at n=${first}, fresh start at ${r}; full half-open cycles [${r},5),[5,8).`;}else{root.dataset.state=keep+'-'+step;root.querySelector('[data-projection]').src=B+`V47C-${lg}-${keep}-${step}-projection.svg`;root.querySelector('[data-clock]').src=B+`V47C-${lg}-${keep}-${step}-clock.svg`;const q=[6,3,1,0][+step],b=keep==='2'?[2,2,2,1][+step]:[3,3,2,1][+step],v=b*(b-1)/2;root.querySelector('[data-v6n-result]').textContent=lg==='zh'?`完整总跳率${q} = 可见${v} + 不可见${q-v}；两条时间轴不压缩。`:`Full total rate ${q} = visible ${v} + invisible ${q-v}; both axes keep elapsed time.`;}}root.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{for(const attr of ['data-x','data-source','data-first','data-keep','data-step'])if(b.hasAttribute(attr)){const v=b.getAttribute(attr);press(attr,v);if(attr==='data-x')x=v;if(attr==='data-source')focus=v;if(attr==='data-first')first=v;if(attr==='data-keep')keep=v;if(attr==='data-step')step=v;}draw();}));draw();});'''
if __name__=='__main__':generate()
