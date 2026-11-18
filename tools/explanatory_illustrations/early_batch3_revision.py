"""E22 annotation-only revision and a single-kernel duality layout for E28."""
from pathlib import Path
from math import sqrt
import json
from .pilot_shapes import Svg,tr,E,INK,TEAL,PALE,WARM,GRAY,RULE
from .volume5 import buttons,wrap_caption
from . import early_batch3 as previous
R=Path(__file__).resolve().parents[2];A=R/'assets/visuals/explanatory-early-v3r2';BASE='/assets/visuals/explanatory-early-v3r2/'
SOURCE='e5ab29b2654baa2df2c4e22f0b880fe051c40c52'
prior=json.loads((R/'publication/explanatory-early-batch3-working.json').read_text(encoding='utf-8'))['figures']
def save(s,name,title):(A/name).write_text(s.document(title),encoding='utf-8',newline='\n')
def image(name,alt,attr='',cls=''):return f'<img class="rev-svg {cls}" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def nest(s,t,x,y,w,h):s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {t.w} {t.h}">{t.fragment()}</svg>')
def clock(lg,n,fast):
 # Preserve the actual original node and waiting-segment fragment, without alteration.
 old=previous.clock(lg,n,fast);s=Svg(370,400)
 s.text(185,31,'ζ < ∞  a.s.' if fast else 'ζ = ∞  a.s.',28,WARM if fast else TEAL,anchor='middle',weight='bold')
 nest(s,old,0,50,370,350);return s

def matrix(s,cx,top,scale=1):
 t=Svg(240,235)
 t.text(120,22,tr('zh' if s.lg=='zh' else 'en','同一转移核 P','The same kernel P'),20,anchor='middle',weight='bold')
 for x,l in [(86,'A'),(154,'B')]:t.text(x,61,l,19,GRAY,anchor='middle')
 for y,l in [(105,'A'),(150,'B')]:t.text(24,y,l,19,GRAY,anchor='middle')
 # Formal 2×2 matrix: exactly four labelled (departure row, arrival column) entries.
 for x,y,text in [(86,105,'3/4'),(154,105,'1/4'),(86,150,'1/4'),(154,150,'3/4')]:t.text(x,y,text,25,anchor='middle')
 for x,sgn in [(48,1),(192,-1)]:
  t.line(x,77,x,164,INK,2);t.line(x,77,x+sgn*12,77,INK,2);t.line(x,164,x+sgn*12,164,INK,2)
 t.text(120,199,tr(s.lg,'行 = 出发状态','Rows = departure states'),16,GRAY,anchor='middle')
 t.text(120,223,tr(s.lg,'列 = 到达状态','Columns = arrival states'),16,GRAY,anchor='middle')
 nest(s,t,cx-120*scale,top,240*scale,235*scale)

def probability(s,cx,cy,values,compact=False):
 gap,r=(35,17) if compact else (52,27)
 for j,(value,label) in enumerate(zip(values,['A','B'])):
  x=cx+(-gap if j==0 else gap)
  s.circle(x,cy,r,RULE,'white')
  if value>0:s.circle(x,cy,r*sqrt(value),TEAL)
  s.text(x,cy-r-10,label,16 if compact else 19,GRAY,anchor='middle')
  s.text(x,cy+r+21,f'{value:g}',16 if compact else 21,TEAL,anchor='middle')

def payoff(s,cx,cy,values,compact=False):
 gap,r=(35,19) if compact else (52,27)
 for j,(value,label) in enumerate(zip(values,['A','B'])):
  x=cx+(-gap if j==0 else gap)
  s.rect(x-r,cy-r,2*r,2*r,'#fbf3e9',WARM)
  s.text(x,cy+7,f'{value:g}',21 if compact else 27,WARM,anchor='middle')
  s.text(x,cy-r-10,label,16 if compact else 19,GRAY,anchor='middle')

def values(u,flip):
 p=u/2;mu=[p,1-p];f=[4,0] if flip else [0,4]
 return mu,[.25+.5*p,.75-.5*p],f,[.75*f[0]+.25*f[1],.25*f[0]+.75*f[1]],1+2*p if flip else 3-2*p

def dual(lg,u=2,flip=0,compact=False):
 mu,muP,f,Tf,total=values(u,flip)
 s=Svg(370,450) if compact else Svg(940,540);s.lg=lg
 if compact:
  matrix(s,185,0,.75)
  for x,title,subtitle in [(92,'μ → μP',tr(lg,'出发 → 未来','Start → future')),(278,'f → Tf',tr(lg,'未来 → 出发','Future → start'))]:
   s.text(x,204,title,23,TEAL if x==92 else WARM,anchor='middle',weight='bold');s.text(x,229,subtitle,16,GRAY,anchor='middle')
  probability(s,92,277,mu,True);payoff(s,278,277,f,True)
  for x,c in [(92,TEAL),(278,WARM)]:s.arrow(x,325,x,343,c)
  probability(s,92,386,muP,True);payoff(s,278,386,Tf,True)
  s.text(185,445,tr(lg,'实色圆面积：概率；方框数值：收益','Disk area = probability; box value = payoff'),13,GRAY,anchor='middle')
 else:
  for x,title in [(160,tr(lg,'分布前推','Push the distribution')),(780,tr(lg,'收益回拉','Pull back the payoff'))]:s.text(x,31,title,26,TEAL if x==160 else WARM,anchor='middle',weight='bold')
  for x,title in [(160,tr(lg,'出发分布 μ','Starting law μ')),(780,tr(lg,'未来收益 f','Future payoff f'))]:s.text(x,82,title,21,anchor='middle')
  probability(s,160,147,mu);payoff(s,780,147,f)
  for x,c,lab in [(160,TEAL,tr(lg,'出发 → 未来','Start → future')),(780,WARM,tr(lg,'未来 → 出发','Future → start'))]:
   s.arrow(x,214,x,282,c);s.text(x,315,lab,19,c,anchor='middle')
  matrix(s,470,102)
  s.arrow(350,248,221,248,TEAL);s.arrow(590,248,719,248,WARM)
  for x,title in [(160,tr(lg,'到达分布 μP','Arrival law μP')),(780,tr(lg,'出发点平均 Tf','Mean at each start Tf'))]:s.text(x,351,title,21,anchor='middle')
  probability(s,160,411,muP);payoff(s,780,411,Tf)
  s.text(470,500,f'(μP)f = μ(Tf) = {total:g}',29,TEAL,anchor='middle',weight='bold')
  s.text(470,534,tr(lg,'圆面积表示概率；方框中的数是收益。P的每个条目按出发行、到达列精确标记。','Disk areas encode probabilities; boxed numbers are payoffs. Each P entry has a departure row and arrival column.'),16,GRAY,anchor='middle')
 return s

def static_e28(lg,title,cap):
 scene=dual(lg);lines=wrap_caption(cap,lg);s=Svg(940,640+24*len(lines))
 s.rect(0,0,s.w,s.h,'white');s.text(26,42,title,27,weight='bold');nest(s,scene,0,75,940,540)
 s.line(26,630,914,630,RULE,1)
 for i,line in enumerate(lines):s.text(26,660+i*24,line,17,GRAY)
 s.h=690+24*len(lines);s.nodes[0]=f'<rect width="940" height="{s.h}" fill="white"/>'
 save(s,f'E28.{lg}.svg',title)

def e22(lg):
 row=next(r for r in prior if r['id']=='E22' and r['lang']==lg);title=row['title'];cap=row['condition']
 for n in [4,6]:
  for fast in [0,1]:save(clock(lg,n,fast),f'E22-{lg}-{n}-{fast}.svg','Original clock structure, explicit lifetime conclusion and nonshared mean scale')
 body='<div class="rev-lifetimes"><div>λⱼ = 1<br><strong>ζ = ∞ a.s.</strong></div><div>λⱼ = 2ʲ<br><strong>ζ &lt; ∞ a.s.</strong></div></div>'
 body+='<div class="rev-scale">'+tr(lg,'<strong>长度 = 平均等待</strong>；左右不共用时间刻度。不是实际样本等待，Eζ=1也不表示ζ≤1。','<strong>Length = mean holding time.</strong> The panels do not share a time scale. These are not sampled waits, and Eζ=1 does not mean ζ≤1.')+'</div>'
 body+=buttons('data-clock-n',[(str(n),tr(lg,f'展开前{n}站',f'Expand first {n} states')) for n in [4,6]],'4')
 body+='<div class="rev-pair">'
 for fast in [0,1]:
  body+='<section><h4>'+tr(lg,'倍增速率 λⱼ=2ʲ' if fast else '恒定速率 λⱼ=1','Doubling rates λⱼ=2ʲ' if fast else 'Constant rates λⱼ=1')+'</h4>'+image(f'E22-{lg}-4-{fast}.svg','Mean holding times, explicit almost-sure lifetime, and no shared scale',f'data-clock-{"fast" if fast else "constant"}')+'</section>'
 body+='</div>'
 lines=wrap_caption(cap,lg);s=Svg(900,670+24*len(lines));s.rect(0,0,s.w,s.h,'white');s.text(25,42,title,27,weight='bold')
 s.text(450,87,tr(lg,'长度 = 平均等待；左右不共用时间刻度。','Length = mean wait; the panels do not share a time scale.'),20,WARM,anchor='middle',weight='bold')
 for x,fast in [(25,False),(475,True)]:
  s.text(x+185,133,'λⱼ = 2ʲ' if fast else 'λⱼ = 1',21,anchor='middle');nest(s,clock(lg,4,fast),x,153,370,400)
 s.line(25,582,875,582,RULE,1)
 for i,line in enumerate(lines):s.text(25,614+24*i,line,17,GRAY)
 s.h=650+24*len(lines);s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';save(s,f'E22.{lg}.svg',title)
 return row,body,cap

def e28(lg):
 row=next(r for r in prior if r['id']=='E28' and r['lang']==lg);title=row['title']
 for u in [0,1,2]:
  for flip in [0,1]:
   for compact in [0,1]:save(dual(lg,u,flip,compact),f'E28-{lg}-{u}-{flip}-{compact}.svg','One formal matrix; forward probability and backward payoff side by side')
 # The identity is first in the mobile reading order, above controls and optional detail.
 body='<output class="rev-identity" data-pairing>(μP)f = μ(Tf) = 1</output>'
 body+='<p class="rev-intro">'+tr(lg,'同一个P，把出发分布推向未来，也把未来收益拉回出发点。两边的总平均相同。','The same P sends laws forward and payoffs back. Both routes give the same mean.')+'</p>'
 body+=buttons('data-mu',[(str(u),'μ(A)='+str(u/2)) for u in [0,1,2]],'2')+buttons('data-payoff',[('0','f(A)=0, f(B)=4'),('1','f(A)=4, f(B)=0')],'0')
 body+=image(f'E28-{lg}-2-0-0.svg','One central two by two kernel with forward mass and backward payoff on opposite sides','data-kernel-desktop','rev-desktop')
 body+=image(f'E28-{lg}-2-0-1.svg','Mobile: one formal kernel and two compact operations compared together','data-kernel-mobile','rev-mobile')
 body+='<details><summary>'+tr(lg,'第二层：读数、索引与固定时刻的范围','Second layer: readings, indices and the fixed-time scope')+'</summary><p>'+tr(lg,'每组左边是A、右边是B。实色圆面积表示概率，浅轮廓为单位参照；方框数值是收益，不是概率。矩阵的行是出发状态，列是到达状态：P(A,A)=P(B,B)=3/4，P(A,B)=P(B,A)=1/4。两条中心连接线只表示共用P，不编码转移流量。','Each pair reads A on the left, B on the right. Filled disk areas encode probabilities, with pale unit outlines for reference; boxed values are payoffs, not probabilities. Matrix rows are departure states and columns arrival states: P(A,A)=P(B,B)=3/4 and P(A,B)=P(B,A)=1/4. The two central connectors mean that both operations use P, not transition flows.')+'</p><p>'+tr(lg,'有限求和交换给出 Σᵧ(ΣₓμₓPₓᵧ)fᵧ = Σₓμₓ(ΣᵧPₓᵧfᵧ)。这里只展示一个固定时刻的转移核，不宣称一份矩阵已经给出整个强连续半群。','Interchanging finite sums gives Σy(Σx μxPxy)fy = Σx μx(Σy Pxyfy). This is one fixed-time transition kernel, not a construction of an entire strongly continuous semigroup.')+'</p></details>'
 cap=tr(lg,'准确模型保持：P各行和为1，对角3/4、非对角1/4，μ=(p,1−p)，p∈{0,1/2,1}，f=(0,4)或(4,0)。μP=(1/4+p/2,3/4−p/2)。前者Tf=(1,3)、共同平均3−2p；后者Tf=(3,1)、共同平均1+2p。实色圆面积为概率，浅轮廓是单位参照；方框数为收益。P的四个条目通过出发行与到达列逐一标明，无重复交叉转移箭头。图只解释固定时刻的核与对偶平均，不以它代替半群、生成元定义域或Feller条件的证明。',
 'Unchanged exact model: P is row-stochastic, with diagonal 3/4 and off-diagonal 1/4; μ=(p,1−p), p∈{0,1/2,1}, and f=(0,4) or (4,0). Then μP=(1/4+p/2,3/4−p/2). For the first payoff Tf=(1,3), with common mean 3−2p; for the second Tf=(3,1), with mean 1+2p. Filled disk areas are probabilities, pale outlines unit references, and boxed numbers payoffs. Each of the four P entries has its departure row and arrival column, without duplicated crossing transition arrows. This illustrates a fixed-time kernel and dual averaging, not a proof of semigroup generation, generator domains or Feller conditions.')
 static_e28(lg,title,cap);return row,body,cap

CSS='''.rev-figure{background:#fffefa;color:#173f39;padding:28px;border:1px solid #ccd9d1;margin:2rem 0;font-family:"Microsoft YaHei",sans-serif;box-sizing:border-box}.rev-figure *{box-sizing:border-box}.rev-figure h3{font-size:26px;margin:0 0 20px;line-height:1.4}.rev-figure header span{font-size:13px;color:#65756e}.rev-figure p{font-size:18px;line-height:1.8}.rev-figure .rev-lifetimes{display:none;grid-template-columns:1fr 1fr;text-align:center;font-size:22px;line-height:1.6;margin:14px 0 22px;color:#16776d}.rev-figure .rev-lifetimes>div:last-child{color:#a45b30}.rev-figure .rev-scale{padding:18px;background:#f4efe3;border-left:4px solid #a45b30;font-size:18px;line-height:1.8}.rev-figure .rev-pair{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin:22px 0}.rev-figure h4{font-size:20px;text-align:center;font-weight:500;margin:0 0 10px}.rev-figure img.rev-svg{display:block;width:100%;height:auto;max-height:none!important;border:0;box-shadow:none;margin:0;object-fit:contain}.rev-figure img.rev-mobile{display:none}.rev-figure .rev-identity{display:block;font-size:30px;text-align:center;color:#16776d;background:#eaf2ee;padding:18px;margin:16px 0;line-height:1.5}.rev-figure .v5-controls{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:18px 0}.rev-figure button{font:inherit;font-size:16px;padding:9px 12px;border:1px solid #ccd9d1;border-radius:4px;background:#fffefa;color:#173f39;cursor:pointer}.rev-figure button[aria-pressed=true]{border:2px solid #16776d;background:#eaf2ee;padding:8px 11px}.rev-figure details{margin:18px 0;border-top:1px solid #ccd9d1;padding:18px 0}.rev-figure summary{font-size:17px;cursor:pointer}.rev-figure figcaption{border-top:1px solid #ccd9d1;padding-top:18px;font-size:15px;line-height:1.9;overflow-wrap:anywhere}.rev-figure nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;margin-top:18px}.rev-figure a{color:#146d61}@media(max-width:700px){.rev-figure{padding:16px}.rev-figure h3{font-size:22px}.rev-figure .rev-lifetimes{display:grid}.rev-figure .rev-pair{grid-template-columns:1fr;gap:25px}.rev-figure p,.rev-figure .rev-scale{font-size:17px}.rev-figure img.rev-desktop{display:none}.rev-figure img.rev-mobile{display:block}.rev-figure .rev-identity{font-size:23px;padding:12px}.rev-figure[data-revision=E28]{display:flex;flex-direction:column}.rev-figure[data-revision=E28] header{order:0}.rev-figure[data-revision=E28] .rev-identity{order:1}.rev-figure[data-revision=E28] .rev-intro{order:2}.rev-figure[data-revision=E28] .rev-mobile{order:3}.rev-figure[data-revision=E28] .v5-controls{order:4}.rev-figure[data-revision=E28] details{order:5}.rev-figure[data-revision=E28] figcaption{order:6}.rev-figure[data-revision=E28] nav{order:7}}@media print{.rev-figure button{display:none}}'''
JS='''document.querySelectorAll('[data-revision]').forEach(root=>{const code=root.dataset.revision,lg=root.lang,B='/assets/visuals/explanatory-early-v3r2/';let u=2,f=0;const press=(a,b)=>root.querySelectorAll('['+a+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const img=(a,name)=>root.querySelector(a).src=B+name;root.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{if(code==='E22'){const n=b.dataset.clockN;press('data-clock-n',b);img('[data-clock-constant]',`E22-${lg}-${n}-0.svg`);img('[data-clock-fast]',`E22-${lg}-${n}-1.svg`);}else{if(b.hasAttribute('data-mu')){u=Number(b.dataset.mu);press('data-mu',b);}else{f=Number(b.dataset.payoff);press('data-payoff',b);}img('[data-kernel-desktop]',`E28-${lg}-${u}-${f}-0.svg`);img('[data-kernel-mobile]',`E28-${lg}-${u}-${f}-1.svg`);const p=u/2,v=f?1+2*p:3-2*p;root.querySelector('[data-pairing]').textContent=`(μP)f = μ(Tf) = ${v}`;}}));});'''

def main():
 A.mkdir(parents=True,exist_ok=True);rows=[]
 for code,fn in [('E22',e22),('E28',e28)]:
  for lg in ['zh','en']:
   row,body,cap=fn(lg);title=row['title'];fragment=f'<figure class="rev-figure" id="visual-{code}" data-revision="{code}" lang="{lg}"><header><span>{code}</span><h3>{title}</h3></header>{body}<figcaption id="visual-{code}-end">{cap}</figcaption><nav><a href="{BASE}{code}.{lg}.svg">SVG</a><a href="/print/{code}.{lg}.html">'+tr(lg,'静态打印','Static print')+'</a></nav></figure>'
   rows.append(row|dict(html=fragment,condition=cap,asset_base=BASE,status=('adopted with requested annotation, author spot-check pending' if code=='E22' else 'revised visual working draft, author review pending'),kind='annotation only' if code=='E22' else 'single-kernel duality redesign'))
 (A/'figures.css').write_text(CSS,encoding='utf-8',newline='\n');(A/'interactions.js').write_text(JS,encoding='utf-8',newline='\n')
 (R/'publication/explanatory-batch3-revision-working.json').write_text(json.dumps(dict(source_commit=SOURCE,automatic_formal_site_injection=False,canonical_manuscript_changes=False,adopted_and_protected=['E14','E30','E39'],figures=rows),ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
 print('Only E22/E28 revision assets created; all previous files untouched')
if __name__=='__main__':main()
