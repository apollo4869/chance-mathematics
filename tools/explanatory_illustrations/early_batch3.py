"""Three new structural models, and only the two author-requested batch2 corrections."""
from pathlib import Path
from math import sqrt
import json
from .pilot_shapes import Svg,tr,E,INK,TEAL,PALE,WARM,GRAY,RULE
from .volume5 import buttons,wrap_caption
from . import early_batch2 as old
R=Path(__file__).resolve().parents[2]; A=R/'assets/visuals/explanatory-early-v3'; BASE='/assets/visuals/explanatory-early-v3/'
META={
'E22':('22-continuous-time-chains','22.9','跳链相同，寿命仍可不同','Same jump chain, different lifetimes'),
'E28':('28-semigroups','28.1','同一个核，两个方向的平均','One kernel, two directions of averaging'),
'E39':('39-malliavin','39.14','两个坐标，不一定有两个方向','Two coordinates need not give two directions')}
def save(s,name,title): (A/name).write_text(s.document(title),encoding='utf-8',newline='\n')
def img(name,alt,attr):return f'<img class="ex-svg" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def panel(title,graphic):return f'<section><h4>{title}</h4>{graphic}</section>'
def pair(*parts):return '<div class="b3-pair">'+''.join(parts)+'</div>'
def paragraph(t):return '<p>'+t+'</p>'

def clock(lg,n,fast):
 s=Svg(370,350);c=WARM if fast else TEAL
 s.text(185,25,tr(lg,'每个箭头都只走向下一个状态','Each jump goes to the next state'),16,GRAY,anchor='middle')
 # Exactly n displayed states; an ellipsis explicitly denotes the undisplayed continuation.
 step=300/(n-1)
 for j in range(n):
  x=25+j*step;s.circle(x,64,11,c,'white');s.text(x,69,str(j+1),13,anchor='middle')
  if j<n-1:s.arrow(x+13,64,x+step-13,64,c)
 s.text(351,69,'…',20,c)
 s.text(185,111,tr(lg,'下面的长度 = 平均等待','Lengths below = mean holding times'),17,anchor='middle')
 if fast:
  # Common unit 280px; these are expectations, never asserted sample holding times.
  x=35
  for j in range(1,n+1):
   w=280*2**(-j);s.rect(x,143,w,47,PALE,c)
   if w>25:s.text(x+w/2,173,'1/'+str(2**j),15,c,anchor='middle')
   x+=w
  s.rect(x,143,280*2**(-n),47,'white',GRAY)
  s.text(185,221,tr(lg,'实色：前n段均值','Filled: first n means'),16,c,anchor='middle')
  s.text(185,248,tr(lg,'留白：所有后段均值的和','Unfilled: sum of all later means'),16,GRAY,anchor='middle')
  s.line(35,277,315,277,GRAY,1);s.line(35,270,35,284,GRAY);s.line(315,270,315,284,GRAY)
  s.text(185,309,'Eζ = 1',29,c,anchor='middle')
  s.text(185,339,'λⱼ = 2ʲ     Eτⱼ = 2⁻ʲ',18,anchor='middle')
 else:
  # A run of equal slots has no finite endpoint. Do not fit it to the fast row's calendar.
  for j in range(n):s.rect(23+j*40,143,40,47,PALE,c)
  s.arrow(23+n*40,166,350,166,c)
  s.text(185,221,tr(lg,'每段均值都是1','Each mean is 1'),18,c,anchor='middle')
  s.text(185,248,tr(lg,'箭头表示仍有后续，不是有限终点','The arrow continues, with no finite endpoint'),15,GRAY,anchor='middle')
  s.text(185,309,'ζ = ∞  a.s.',29,c,anchor='middle')
  s.text(185,339,'λⱼ = 1     Eτⱼ = 1',18,anchor='middle')
 return s

def e22(lg):
 for n in [4,6]:
  for fast in [False,True]:save(clock(lg,n,fast),f'E22-{lg}-{n}-{int(fast)}.svg','Same embedded chain; mean holding times, not a sampled clock')
 body=paragraph(tr(lg,'状态顺序完全一样。改变的只是每一站的等待规律；下方长度画的是均值，不能读成一条真实轨迹的时间上界。','The state sequence is identical. Only the holding laws change. The lengths below are expectations, not a time bound on a sample path.'))
 body+=buttons('data-clock-n',[(str(n),tr(lg,f'展开前{n}站',f'Expand first {n} states')) for n in [4,6]],'4')
 body+=pair(panel(tr(lg,'恒定速率：不断延续','Constant rates: no finite endpoint'),img(f'E22-{lg}-4-0.svg','Equal mean holding times continue without a finite endpoint','data-constant')),
 panel(tr(lg,'倍增速率：均值可相加到1','Doubling rates: means sum to one'),img(f'E22-{lg}-4-1.svg','Geometric mean waits with an explicitly marked remaining tail','data-fast')))
 cap=tr(lg,'精确模型：从状态1出发的纯生链j→j+1。令Eⱼ独立且为Exp(1)，等待τⱼ=Eⱼ/λⱼ，寿命ζ=Στⱼ。左λⱼ=1，由独立同分布强大数律ζ=∞几乎必然；不是仅凭Eζ=∞推断。右λⱼ=2ʲ，由Tonelli得Eζ=Σ2⁻ʲ=1，非负性遂给ζ<∞几乎必然。所有单段等待都严格正且速率有限。右图白色尾段均值恰为2⁻ⁿ；不声称ζ≤1，也不声称图中均值长度是实际等待。左右平均时钟示意不是共同数轴，不能比较其像素单位。爆炸后规则仍须另定，图不构造重启。',
 'Exact model: a pure-birth chain j→j+1 started at 1, with independent unit exponentials Ej, waits τj=Ej/λj and lifetime ζ=Στj. For λj=1, the iid strong law gives ζ=∞ almost surely; infinite expectation alone would not prove this. For λj=2^j, Tonelli gives Eζ=Σ2^(-j)=1, hence ζ<∞ almost surely by nonnegativity. Each wait is strictly positive and each rate finite. The unfilled tail has mean 2^(-n); this asserts neither ζ≤1 nor that displayed mean lengths are sample waits. The two diagrams use different display units, not a shared calendar axis. No post-explosion restart is constructed.')
 return body,cap,[('λⱼ = 1',clock(lg,4,False)),('λⱼ = 2ʲ',clock(lg,4,True))]

def kernel(lg,u,reverse,flip):
 s=Svg(370,330);p=u/2;f=[4,0] if flip else [0,4];mu=[p,1-p];out=[.75*p+.25*(1-p),.25*p+.75*(1-p)];tf=[.75*f[0]+.25*f[1],.25*f[0]+.75*f[1]]
 for i,y in enumerate([86,226]):
  for j,z in enumerate([86,226]):
   if reverse:s.arrow(290,z+(-14 if j==0 else 14),80,y+(-14 if i==0 else 14),TEAL)
   else:s.arrow(80,y+(-14 if i==0 else 14),290,z+(-14 if j==0 else 14),TEAL)
 for x in [53,317]:
  for j,y in enumerate([86,226]):s.circle(x,y,25,INK,'white');s.text(x,y+7,'AB'[j],21,anchor='middle')
 s.text(185,47,'P = [ 3/4  1/4 ; 1/4  3/4 ]',17,anchor='middle')
 # Overlaid labels avoid ambiguous line widths; arrows only denote the direction of the operation.
 s.rect(139,118,92,67,'white');s.text(185,143,'3/4',20,TEAL,anchor='middle');s.text(185,172,'1/4',20,TEAL,anchor='middle')
 if reverse:
  for j,y in enumerate([86,226]):
   s.text(53,y+49,f'{tf[j]:g}',26,WARM,anchor='middle');s.text(317,y+49,str(f[j]),26,WARM,anchor='middle')
  s.text(53,305,'Tf',24,WARM,anchor='middle');s.text(317,305,'f',24,WARM,anchor='middle')
 else:
  for x,v in [(53,mu),(317,out)]:
   # Areas of the two strips at each side sum to the same fixed total width.
   for j,y in enumerate([86,226]):
    s.rect(x-30,y+35,60,13,'#f1f0e9');s.rect(x-30,y+35,60*v[j],13,PALE,TEAL);s.text(x,y+72,f'{v[j]:g}',20,TEAL,anchor='middle')
  s.text(53,320,'μ',24,TEAL,anchor='middle');s.text(317,320,'μP',24,TEAL,anchor='middle')
 return s

def e28(lg):
 for u in [0,1,2]:
  for flip in [0,1]:
   for rev in [0,1]:save(kernel(lg,u,rev,flip),f'E28-{lg}-{u}-{flip}-{rev}.svg','Forward distribution and backward observable for the same stochastic kernel')
 body=paragraph(tr(lg,'左边把出发质量送到未来；右边把未来收益拉回每个出发点。箭头方向不同，转移概率始终是同一个P。','The left view pushes starting mass into the future. The right view pulls future payoffs back to each starting point. The directions differ; the transition probabilities are the same P.'))
 body+=buttons('data-mu',[(str(u),'μ(A)='+str(u/2)) for u in [0,1,2]],'2')+buttons('data-payoff',[('0','f(A)=0, f(B)=4'),('1','f(A)=4, f(B)=0')],'0')
 body+=pair(panel(tr(lg,'推动分布','Push the distribution'),img(f'E28-{lg}-2-0-0.svg','Starting and final probability strips, forward arrows','data-push')),
 panel(tr(lg,'拉回收益','Pull back the payoff'),img(f'E28-{lg}-2-0-1.svg','Future payoffs and conditional expected payoffs, backward arrows','data-pull')))
 body+='<output data-pairing>'+tr(lg,'两边得到同一总平均：(μP)f = μ(Tf) = 1','Both give the same total mean: (μP)f = μ(Tf) = 1')+'</output>'
 cap=tr(lg,'有限状态精确核：行是出发状态、列是到达状态，对角3/4、非对角1/4。左下色条长度表示质量，右图数值是收益，不是概率；所有箭头只是运算方向，不以线宽编码流量。Tf=(3f(A)/4+f(B)/4, f(A)/4+3f(B)/4)。独立选择μ与f，有限求和交换给Σᵧ(ΣₓμₓPₓᵧ)fᵧ=Σₓμₓ(ΣᵧPₓᵧfᵧ)。本图只解释一个固定时刻的核及其对偶作用，不以单个矩阵证明连续时间半群、生成元或Feller条件。',
 'Exact two-state kernel: rows are departure states, columns arrival states, diagonal 3/4 and off-diagonal 1/4. Strip lengths encode probabilities; the right-hand numbers are payoffs, not probabilities. Arrows indicate operation direction, never flow magnitude. Tf=(3f(A)/4+f(B)/4, f(A)/4+3f(B)/4). For independently selected μ and f, interchanging finite sums gives Σy(Σx μx Pxy)fy=Σx μx(Σy Pxy fy). One fixed-time kernel illustrates dual actions; it does not establish a continuous-time semigroup, a generator or the Feller property.')
 return body,cap,[('μ → μP',kernel(lg,2,False,False)),('Tf ← f',kernel(lg,2,True,False))]

def directions(lg,full,change=False):
 s=Svg(370,390);s.text(185,24,tr(lg,'同一路径，两个正交读数','Two orthogonal readings, one path'),15,GRAY,anchor='middle')
 s.text(185,56,'F = (Z₁, Z₁+Z₂)' if full else 'F = (Z₁, 2Z₁)',23,anchor='middle')
 ox,oy=185,224;scale=57
 def xy(x,y):return (ox+x*scale,oy-y*scale)
 s.line(*xy(-1.7,0),*xy(1.8,0),RULE,1);s.line(*xy(0,-2.1),*xy(0,2.1),RULE,1)
 s.text(*xy(1.9,0),'F₁',16,GRAY);s.text(ox+10,91,'F₂',16,GRAY)
 if full:
  coords=[xy(-1,-2),xy(1,0),xy(1,2),xy(-1,0)]
  s.nodes.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in coords)+'" fill="'+PALE+'" stroke="'+TEAL+'" stroke-width="2"/>')
  for a in [-.5,0,.5]:
   s.line(*xy(a,a-1),*xy(a,a+1),RULE,1);s.line(*xy(-1,-1+a),*xy(1,1+a),RULE,1)
 else:s.line(*xy(-1,-2),*xy(1,2),WARM,4)
 # Unit noise perturbations, not output coordinates or time increments.
 v=(0,1) if full else (0,0)
 s.arrow(ox,oy,*xy(1,1 if full else 2),TEAL);s.text(ox+65,oy-59 if full else oy-116,'ΔZ₁',16,TEAL)
 if full:s.arrow(ox,oy,*xy(*v),WARM);s.text(ox-53,oy-62,'ΔZ₂',16,WARM)
 else:s.circle(ox,oy,6,WARM,'white');s.text(ox+13,oy+29,'ΔZ₂ ↦ 0',17,WARM)
 if change:
  # Changing only Z2 has a visibly different effect between the two maps.
  s.circle(*xy(*v),8,WARM);s.text(185,374,tr(lg,'只将Z₂增加1：输出移动' if full else '只将Z₂增加1：输出不动','Z₂ alone +1: output moves' if full else 'Z₂ alone +1: output unchanged'),17,WARM,anchor='middle')
 else:s.text(185,374,tr(lg,'扰动方块的像有面积' if full else '扰动方块的像仍是一条线','Perturbation square → area' if full else 'Perturbation square → line'),17,anchor='middle')
 return s

def e39(lg):
 for full in [0,1]:
  for change in [0,1]:save(directions(lg,full,change),f'E39-{lg}-{full}-{change}.svg','Rank of the response to orthogonal noise directions')
 for change in [0,1]:
  small=Svg(370,260)
  for full,ox in [(False,90),(True,280)]:
   small.text(ox,25,tr(lg,'秩2：面积' if full else '秩1：直线','Rank 2: area' if full else 'Rank 1: line'),18,TEAL if full else WARM,anchor='middle')
   small.text(ox,53,'(Z₁, Z₁+Z₂)' if full else '(Z₁, 2Z₁)',16,anchor='middle')
   xy=lambda x,y:(ox+32*x,149-32*y)
   small.line(*xy(-1.5,0),*xy(1.5,0),RULE,1);small.line(*xy(0,-2.1),*xy(0,2.1),RULE,1)
   if full:
    coords=[xy(-1,-2),xy(1,0),xy(1,2),xy(-1,0)]
    small.nodes.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in coords)+'" fill="'+PALE+'" stroke="'+TEAL+'" stroke-width="2"/>')
    small.arrow(*xy(0,0),*xy(0,1),WARM)
   else:small.line(*xy(-1,-2),*xy(1,2),WARM,3)
   if change:small.circle(*xy(0,1 if full else 0),7,WARM)
   small.text(ox,245,'ΔZ₂ ↦ (0,1)' if full else 'ΔZ₂ ↦ (0,0)',15,WARM,anchor='middle')
  save(small,f'E39-{lg}-compact-{change}.svg','Mobile comparison: the same second-noise perturbation moves one output and not the other')
 body=paragraph(tr(lg,'轻推同一路径中的两个正交噪声读数，检查输出能否独立移动。这是噪声方向的微分，不是路径的时间导数。','Perturb two orthogonal readings of one path. Can the outputs move independently? These are noise directions, not time derivatives.'))
 body+=buttons('data-noise',[('0',tr(lg,'看两个方向','Show both directions')),('1',tr(lg,'只推动Z₂','Perturb Z₂ only'))],'0')
 body+=pair(panel(tr(lg,'重复信息：秩1','Repeated information: rank one'),img(f'E39-{lg}-0-0.svg','A noise perturbation square maps to a line','data-rank-one')),
 panel(tr(lg,'不同响应：秩2','Independent responses: rank two'),img(f'E39-{lg}-1-0.svg','The same perturbation square maps to a parallelogram','data-rank-two')))
 body+='<div class="b3-mobile">'+img(f'E39-{lg}-compact-0.svg','Both rank structures in a dedicated compact layout','data-rank-compact')+'</div>'
 body+='<output>'+tr(lg,'左 det γ = 0；右 det γ = 1。差别来自响应方向，不是Brownian路径的条数。','Left det γ = 0; right det γ = 1. The difference is in response directions, not the number of Brownian paths.')+'</output>'
 cap=tr(lg,'取同一Brownian运动上Z₁=B₁、Z₂=√12(∫₀¹Bₛds−B₁/2)=∫₀¹√12(1/2−s)dBₛ。两个核在L²[0,1]中正交且范数1，故(Z₁,Z₂)为独立标准正态。左响应矩阵[[1,0],[2,0]]，γ=[[1,2],[2,4]]；右[[1,0],[1,1]]，γ=[[1,1],[1,2]]。图画[-1,1]²噪声扰动方块的线性像，不是密度热图，也不把方块当作Gaussian支撑。这里的线性Gaussian例子右侧有光滑密度，不能据此宣称任意可Malliavin微分输出都有光滑密度；一般结论还需正文的非退化与可积性条件。',
 'On one Brownian path set Z1=B1 and Z2=√12(∫0^1 Bs ds−B1/2)=∫0^1 √12(1/2−s)dBs. Their L²[0,1] kernels are orthogonal unit vectors, hence Z1,Z2 are independent standard normals. Left response matrix [[1,0],[2,0]] gives γ=[[1,2],[2,4]]; right [[1,0],[1,1]] gives γ=[[1,1],[1,2]]. The drawings are linear images of the noise perturbation square [-1,1]^2, not density heat maps or bounded Gaussian supports. The full-rank linear Gaussian example has a smooth density; arbitrary Malliavin differentiability does not imply this. General results require the nondegeneracy and integrability conditions established in the text.')
 return body,cap,[('rank 1',directions(lg,False)),('rank 2',directions(lg,True))]

CSS='''
.batch3 .b3-mobile{display:none}.batch3{background:#fffefa;color:#173f39;border:1px solid #ccd9d1;padding:28px;margin:2rem 0;font-family:"Microsoft YaHei",sans-serif;box-sizing:border-box}.batch3 *{box-sizing:border-box}.batch3 h3{font-size:26px;line-height:1.4;margin:0 0 18px}.batch3 header span{font-size:13px;color:#65756e}.batch3 p{font-size:18px;line-height:1.8}.batch3 .b3-pair{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin:22px 0}.batch3 h4{text-align:center;font-size:20px;font-weight:500;line-height:1.5;margin:0 0 12px}.batch3 img.ex-svg{display:block!important;width:100%;height:auto;max-height:none!important;margin:0;border:0;box-shadow:none}.batch3 .v5-controls{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin:16px 0}.batch3 button{font:inherit;font-size:16px;color:#173f39;padding:9px 12px;background:#fffefa;border:1px solid #ccd9d1;border-radius:4px;cursor:pointer}.batch3 button[aria-pressed=true]{background:#eaf2ee;border:2px solid #16776d;padding:8px 11px}.batch3 output{display:block;border-top:1px solid #ccd9d1;padding:18px 0;font-size:21px;line-height:1.65;color:#16776d}.batch3 figcaption{font-size:15px;line-height:1.9;border-top:1px solid #ccd9d1;padding-top:18px;overflow-wrap:anywhere}.batch3 nav{display:flex;gap:16px;flex-wrap:wrap;margin-top:18px;font-size:14px}.batch3 a{color:#146d61}@media(max-width:700px){.batch3{padding:16px;margin:1rem 0}.batch3 .b3-pair{grid-template-columns:1fr;gap:24px}.batch3 h3{font-size:22px}.batch3[data-batch3=E39] .b3-pair{display:none}.batch3 .b3-mobile{display:block}.batch3 h4{font-size:18px}.batch3 p{font-size:17px}}@media print{.batch3 button{display:none}}
'''
JS='''document.querySelectorAll('[data-batch3]').forEach(root=>{const id=root.dataset.batch3,lg=root.lang,B='/assets/visuals/explanatory-early-v3/';const image=(s,f)=>root.querySelector(s).src=B+f;const press=(a,b)=>root.querySelectorAll('['+a+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));let u=2,flip=0;root.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{if(id==='E22'){const n=b.dataset.clockN;press('data-clock-n',b);image('[data-constant]',`E22-${lg}-${n}-0.svg`);image('[data-fast]',`E22-${lg}-${n}-1.svg`);}if(id==='E28'){if(b.hasAttribute('data-mu')){u=Number(b.dataset.mu);press('data-mu',b);}else{flip=Number(b.dataset.payoff);press('data-payoff',b);}image('[data-push]',`E28-${lg}-${u}-${flip}-0.svg`);image('[data-pull]',`E28-${lg}-${u}-${flip}-1.svg`);const p=u/2,v=flip?1+2*p:3-2*p;root.querySelector('[data-pairing]').textContent=(lg==='zh'?'两边得到同一总平均：':'Both give the same total mean: ')+`(μP)f = μ(Tf) = ${v}`;}if(id==='E39'){press('data-noise',b);const k=b.dataset.noise;image('[data-rank-one]',`E39-${lg}-0-${k}.svg`);image('[data-rank-two]',`E39-${lg}-1-${k}.svg`);image('[data-rank-compact]',`E39-${lg}-compact-${k}.svg`);}}));});'''

def main():
 A.mkdir(parents=True,exist_ok=True);rows=[]
 for code,fn in [('E22',e22),('E28',e28),('E39',e39)]:
  slug,sec,zh,en=META[code]
  for lg in ['zh','en']:
   title=tr(lg,zh,en);body,cap,panes=fn(lg)
   fragment=f'<figure class="batch3" id="visual-{code}" data-batch3="{code}" lang="{lg}"><header><span>{code}</span><h3>{title}</h3></header>{body}<figcaption id="visual-{code}-end">{cap}</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
   # Reuse the static layout mechanism, but save only into the new namespace.
   previous=old.A;old.A=A
   try:old.static(code,lg,title,cap,panes)
   finally:old.A=previous
   rows.append(dict(id=code,chapter=int(slug[:2]),slug=slug,section=sec,lang=lg,title=title,html=fragment,condition=cap,status='author visual review pending',kind='new explanatory figure',asset_base=BASE))
 # Only E14/E30 are regenerated; all other adopted batch2 SVG/CSS/JS and old report pages stay unchanged.
 registry=json.loads((R/'publication/explanatory-early-batch2-working.json').read_text(encoding='utf-8'))
 for row in registry['figures']:
  code,lg=row['id'],row['lang']
  if code not in ['E14','E30']:continue
  body,cap,panes=old.FUNCS[code](lg);title=row['title'];old.static(code,lg,title,cap,panes)
  frag=f'<figure class="batch2" id="visual-{code}" data-batch2="{code}" lang="{lg}"><header><span>{code}</span><h3>{title}</h3></header>{body}<figcaption id="visual-{code}-end">{cap}</figcaption><nav><a href="{old.BASE}{code}.{lg}.svg">SVG</a><a href="/print/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
  row.update(html=frag,condition=cap,status='adopted working visual; local clarification pending author check')
  rows.append(row|{'asset_base':old.BASE,'kind':'minimal author-requested clarification'})
 (A/'figures.css').write_text(CSS,encoding='utf-8',newline='\n');(A/'interactions.js').write_text(JS,encoding='utf-8',newline='\n')
 (R/'publication/explanatory-early-batch3-working.json').write_text(json.dumps(dict(automatic_formal_site_injection=False,canonical_manuscript_changes=False,source_commit='c7d426b52338eb77b7a024fe0da8d1f4c656eb1d',figures=rows),ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
 print('3 new bilingual figures; E14/E30 localized correction assets only; no manuscript edits')
if __name__=='__main__':main()
