"""Five exact, bilingual visual models. All writes use a new asset namespace."""
from pathlib import Path
from .pilot_shapes import Svg,tr,E,INK,TEAL,PALE,WARM,GRAY,RULE
from .volume5 import buttons,wrap_caption
from .early_audit import PILOTS
import json,math
R=Path(__file__).resolve().parents[2];A=R/'assets/visuals/explanatory-early-v1';BASE='/assets/visuals/explanatory-early-v1/'
COL={1:TEAL,3:'#96753b',5:'#7257a4'}
def save(s,name,title):
 (A/name).write_text(s.document(title),encoding='utf-8',newline='\n');return name
def img(name,alt,attr=''):return f'<img class="ex-svg" src="{BASE}{name}" alt="{E(alt)}" {attr}>'
def para(txt,cls=''):return f'<p class="{cls}">{txt}</p>'
def scene06(lg,group=False,focus=0):
 s=Svg(340,245);base=192;unit=26;hh=27
 if not group:
  for i,val in enumerate([1,5,1,3,5,1,3,5]):
   x=57+i*unit;top=base-val*hh;on=focus in [0,val];s.rect(x,top,unit,val*hh,COL[val] if on else '#e7ebe6','white');s.text(x+unit/2,top-10,str(val),19,COL[val] if on else GRAY,anchor='middle')
  s.line(57,base+1,265,base+1,GRAY,1);s.text(161,229,tr(lg,'同一条[0,1]，每格宽1/8','Same [0,1], each cell width 1/8'),17,anchor='middle')
 else:
  x=57
  for val,count in [(1,3),(3,2),(5,3)]:
   w=count*unit;top=base-val*hh;on=focus in [0,val];s.rect(x,top,w,val*hh,COL[val] if on else '#e7ebe6','white');s.text(x+w/2,top-10,str(val),20,COL[val] if on else GRAY,anchor='middle');s.text(x+w/2,224,f'{count}/8',18,anchor='middle');x+=w
 return s
def mobile06(lg,focus=0):
 s=Svg(340,300);unit=26;hh=14
 for i,val in enumerate([1,5,1,3,5,1,3,5]):
  x=57+i*unit;top=92-val*hh;on=focus in [0,val];s.rect(x,top,unit,val*hh,COL[val] if on else '#e7ebe6','white');s.text(x+13,top-7,str(val),18,COL[val] if on else GRAY,anchor='middle')
 s.text(170,118,tr(lg,'每格宽1/8','Each cell width 1/8'),17,anchor='middle');s.arrow(170,132,170,151)
 x=57
 for val,count in [(1,3),(3,2),(5,3)]:
  w=count*unit;top=249-val*hh;on=focus in [0,val];s.rect(x,top,w,val*hh,COL[val] if on else '#e7ebe6','white');s.text(x+w/2,top-8,str(val),18,COL[val] if on else GRAY,anchor='middle');s.text(x+w/2,280,f'{count}/8',18,anchor='middle');x+=w
 return s
def scene08(lg,mode,flip=0):
 s=Svg(360,285);bits=[flip,1-flip,flip];pts=[(180,53),(53,211),(307,211)]
 # Edge color reports whether this displayed assignment meets that pair constraint.
 for a,b in [(0,1),(1,2),(0,2)]:
  valid=bits[a]!=bits[b] if (a,b)!=(0,2) or mode=='impossible' else bits[a]==bits[b]
  x,y=pts[a];u,v=pts[b];s.line(x,y,u,v,TEAL if valid else WARM,2,'5 4' if not valid else None)
  tx,ty={(0,1):(80,124),(1,2):(180,245),(0,2):(280,124)}[(a,b)]
  s.text(tx,ty,tr(lg,'相反','opposite') if ((a,b)!=(0,2) or mode=='impossible') else tr(lg,'相同','equal'),18,TEAL if valid else WARM,anchor='middle')
  if not valid:s.text(263,158,'×',29,WARM,anchor='middle')
 for j,(x,y) in enumerate(pts):
  s.circle(x,y,25,TEAL,'#fffefa');s.text(x,y+8,str(bits[j]),26,anchor='middle');s.text(x,y-35,['X₁','X₂','X₃'][j],18,anchor='middle')
 return s
def scene16(lg,reveal=False):
 s=Svg(360,310)
 # The single prefix belongs to both completions. It is drawn only once.
 pts=[(30,146),(92,88),(154,146)]
 for (x,y),(u,v) in zip(pts,pts[1:]):s.line(x,y,u,v,TEAL,2.5)
 for j,(x,y) in enumerate(pts):s.circle(x,y,5,TEAL);s.text(x,y+25,'n='+str(j),15,GRAY,anchor='middle');s.text(x,y-12,str([0,1,0][j]),18,TEAL,anchor='middle')
 s.text(89,40,tr(lg,'已看见的共同前缀','One observed prefix'),18,anchor='middle');s.text(154,191,tr(lg,'现在 n=2','Now n=2'),19,anchor='middle')
 s.line(174,54,174,270,RULE,1,'4 4')
 if reveal:
  s.line(154,146,235,88,TEAL,2);s.line(235,88,324,30,TEAL,2);s.line(235,88,324,146,WARM,2)
  s.circle(324,30,6,TEAL);s.circle(324,146,6,WARM);s.text(307,66,'L=2',19,TEAL,anchor='middle');s.text(307,182,'L=4',19,WARM,anchor='middle');s.text(235,111,'n=3',15,GRAY,anchor='middle');s.text(324,222,'n=4',15,GRAY,anchor='middle')
 else:
  s.rect(190,20,154,218,'#eef0ea');s.text(267,120,'?',48,GRAY,anchor='middle');s.text(267,160,tr(lg,'未来未揭晓','Future hidden'),18,GRAY,anchor='middle')
 s.text(180,292,tr(lg,'首次正时返回 T=2：两条都已知道','First positive return T=2: already known'),17,anchor='middle')
 return s
def scene20(lg,mode='P',chosen=1):
 s=Svg(390,280);leafs=[(62,189),(224,189),(280,189),(336,189)]
 for i,(cx,k) in enumerate([(62,1),(280,3)]):
  rooty=73;s.circle(cx,rooty,7,INK);s.text(cx,29,['A','B'][i],23,anchor='middle');s.text(cx,55,('1/2' if mode=='P' else ['1/4','3/4'][i]),19,WARM,anchor='middle')
  inds=[0] if i==0 else [1,2,3]
  for j in inds:
   x,y=leafs[j];mark=j==chosen;s.line(cx,rooty,x,y,TEAL if mark else '#aab6ae',3 if mark else 1.5)
   prob=([.5,1/6,1/6,1/6][j] if mode=='P' else .25);rad=37*math.sqrt(prob/.5)
   s.circle(x,y,rad,TEAL if mark else '#82968a',PALE if mark else '#f4f5f0');s.text(x,y+7,('1/2' if j==0 else '1/6') if mode=='P' else '1/4',18,anchor='middle');s.text(x,244,['A₁','B₁','B₂','B₃'][j],18,anchor='middle')
 s.text(195,277,tr(lg,'圆面积 ∝ 该“树＋标记个体”的联合概率','Disk area ∝ joint chance of tree + marked child'),15,GRAY,anchor='middle')
 return s
def clock24(lg,delta):
 s=Svg(340,132);a=.5;b=a+delta;x=lambda t:25+290*t
 for y,label in [(25,tr(lg,'参考时间','Reference')),(105,tr(lg,'原记录时间','Original'))]:s.line(25,y,315,y,GRAY,1);s.text(3,y+6,'0',16,GRAY);s.text(328,y+6,'1',16,GRAY,anchor='middle')
 for u,v in [(0,0),(a,b),(1,1)]:s.arrow(x(u),30,x(v),96,TEAL)
 s.text(x(a),18,'a',18,anchor='middle');s.text(x(b),130,'a+δ',18,anchor='middle');s.text(40,72,'λ',25,TEAL);return s
def path24(lg,delta,mode='jump',aligned=False):
 s=Svg(340,196);a=.5;b=a+delta;left=25;right=315;x=lambda t:left+290*t;y0=151;y1=52
 def step(start,end,c,dash=None):
  s.line(left,y0,x(start),y0,c,2,dash);s.circle(x(start),y0,4,c,'white');s.circle(x(start),y1,4,c)
  if end is None:s.line(x(start),y1,right,y1,c,2,dash)
  else:
   s.line(x(start),y1,x(end),y1,c,2,dash);s.circle(x(end),y1,4,c,'white');s.circle(x(end),y0,4,c);s.line(x(end),y0,right,y0,c,2,dash)
 if mode=='jump':
  step(a,None,'#b6c3bb','4 4');step(a if aligned else b,None,TEAL)
 else:
  width=delta**2;start=a if aligned else b;end=a+width*(1-a)/(1-b) if aligned else b+width
  s.line(left,y0,right,y0,'#b6c3bb',1,'4 4');step(start,end,WARM)
 s.text(13,y1+6,'1',17,GRAY);s.text(13,y0+6,'0',17,GRAY);s.text(170,187,tr(lg,'灰虚线：参考；实线：当前记录','Gray dashes: reference; solid: current'),15,anchor='middle')
 return s
def body06(lg):
 for v in [0,1,3,5]:
  for part in ['domain','values']:save(scene06(lg,part=='values',v),f'E06-{lg}-{part}-{v}.svg','Equal-value sets retain their exact measure')
  save(mobile06(lg,v),f'E06-{lg}-mobile-{v}.svg','Compact spatial-to-value grouping with unchanged area ratios')
 body=para(tr(lg,'同一函数，不相邻的位置也可以有相同取值。把它们归组，累计的是“值 × 这组的测度”。','The same value may occur in separated places. Group those places and add value × measure.'))
 body+='<div class="early-flow"><section><h4>'+tr(lg,'位置顺序','Spatial order')+'</h4>'+img(f'E06-{lg}-domain-0.svg','Eight equal cells with three values','data-domain')+'</section><div class="flow-arrow">→</div><section><h4>'+tr(lg,'按数值归组','Group by value')+'</h4>'+img(f'E06-{lg}-values-0.svg','Equal-value regions have measures 3/8,2/8,3/8','data-values')+'</section></div>'
 body+='<div class="e06-mobile"><h4>'+tr(lg,'位置顺序 ↓ 按数值归组','Spatial order ↓ group by value')+'</h4>'+img(f'E06-{lg}-mobile-0.svg','Compact grouped measure diagram','data-mobile-group')+'</div>'
 body+=buttons('data-value',[(str(v),tr(lg,'全部','All') if not v else f'f={v}') for v in [0,1,3,5]],'0')+para(tr(lg,'3/8 ＋ 6/8 ＋ 15/8 ＝ 3','3/8 + 6/8 + 15/8 = 3'),'early-result')+'<output data-reading>'+tr(lg,'三组面积相加，函数没有被改动。','Add the three contributions; the original function is unchanged.')+'</output>'
 cap=tr(lg,'具体模型：Lebesgue空间[0,1]分为8个等宽半开小格，最后一格包含1，取值依次1,5,1,3,5,1,3,5。右图是把等值集合的测度重新排成连续宽带的示意，不是声称原集合连续。三个原像可测，测度为3/8、2/8、3/8，积分为3。点击只突出同一组，不改变函数或测度。它解释简单函数的加权和，不以这幅有限图代替一般Lebesgue积分构造。','Model: eight equal half-open cells in [0,1], with 1 included in the last cell, have values 1,5,1,3,5,1,3,5. The right panel rearranges the measures of equal-value sets into contiguous bands; it does not assert that the original sets are contiguous. Their measurable preimages have measures 3/8,2/8,3/8; the integral is 3. Clicking highlights a group without changing the function or measure. This explains a simple-function sum, not the full construction of Lebesgue integration.')
 cap+=tr(lg,' 此有限阶梯也Riemann可积；失败反例是正文的Dirichlet函数。',' This finite step function is also Riemann integrable; the failure example is the text’s Dirichlet function.')
 return body,cap,[scene06(lg),scene06(lg,True)]
def body08(lg):
 for mode in ['impossible','consistent']:
  for flip in [0,1]:save(scene08(lg,mode,flip),f'E08-{lg}-{mode}-{flip}.svg','Three pair constraints need a joint law')
 body=para(tr(lg,'每一对都能公平地取01或10；三对同时要求相反，却没有一个三元记录能通过。','Each opposite pair can fairly take 01 or 10. But no triple can make all three pairs opposite.'))+buttons('data-pairs', [('impossible',tr(lg,'三对相反','All opposite')),('consistent',tr(lg,'第三对相同','Third pair equal'))],'impossible')+'<div class="early-single">'+img(f'E08-{lg}-impossible-0.svg','A binary triangle violates one of three opposite constraints','data-pair-scene')+'</div>'+buttons('data-flip',[('0','010'),('1','101')],'0')+'<output data-reading>'+tr(lg,'前两条关系成立，第三条必定失败。','The first two relations hold; the third must fail.')+'</output>'
 cap=tr(lg,'X₁,X₂,X₃取0或1，每个单独分布均公平。“相反”的两维律为01、10各1/2，“相同”为00、11各1/2。若三对几乎必然相反，X₁≠X₂且X₂≠X₃就迫使X₁=X₃，矛盾；不是仅凭画出的某一条记录下结论。将第三对改为相同后，联合律P(010)=P(101)=1/2真实实现全部三对。两个记录按钮互换全局0/1，三份一维边际始终相同。图揭示一致性必要性，不取代扩张定理。','Each Xi is a fair bit. An opposite pair has law 01,10 with probability 1/2 each; an equal pair has law 00,11 with probability 1/2 each. If all three pairs were opposite almost surely, X1≠X2 and X2≠X3 would force X1=X3, a contradiction. This is not inferred merely from one displayed assignment. With the third pair equal, the joint law P(010)=P(101)=1/2 realizes all three pair laws. Buttons flip all bits, retaining the same fair one-dimensional marginals. The picture shows a necessary consistency condition, not the extension theorem.')
 return body,cap,[scene08(lg,'impossible'),scene08(lg,'consistent')]
def body16(lg):
 for k in [0,1]:save(scene16(lg,bool(k)),f'E16-{lg}-{k}.svg','One prefix, different last returns')
 body=para(tr(lg,'看到0→1→0，首次返回已发生。但“这就是最后一次吗”仍取决于没有出现的步子。','After 0→1→0, the first return is known. Whether it is the last still depends on unseen steps.'))+buttons('data-reveal',[('0',tr(lg,'只看到现在','See only the present')),('1',tr(lg,'揭晓两种未来','Reveal two futures'))],'0')+'<div class="early-single">'+img(f'E16-{lg}-0.svg','A shared random-walk prefix with its future hidden','data-prefix-scene')+'</div><output data-reading>'+tr(lg,'T=2可确认；L=2目前不能确认。','T=2 is decidable now; L=2 is not.')+'</output>'
 cap=tr(lg,'简单对称游走，S₀=0，自然滤过。T=inf{n≥1:Sₙ=0}，L=max{0≤n≤4:Sₙ=0}。图中共同前缀(0,1,0)对应同一个F₂原子；继续为(1,2)或(1,0)都具有正概率，分别给L=2或4，而两条都给T=2。因此{L≤2}在该原子上并非常量，不是F₂事件。仅画两种合法完成以证明不能判断，并未枚举全部未来或给它们任意总概率。停止信息合法不自动保证无界optional sampling可用，UI等条件仍见正文。','Simple symmetric walk starts at 0 with its natural filtration. T=inf{n≥1:Sn=0}; L=max{0≤n≤4:Sn=0}. The shared prefix (0,1,0) is one F2 atom. The positive-probability continuations (1,2) and (1,0) give L=2 and L=4 respectively, while both give T=2. Hence {L≤2} is not constant on that atom and is not an F2 event. Two completions suffice to disprove decidability; they do not enumerate all futures or receive an arbitrary total probability. A legitimate stopping rule alone does not justify unbounded optional sampling; its UI conditions remain in the text.')
 return body,cap,[scene16(lg,True)]
def body20(lg):
 for mode in ['P','Q']:
  for j in range(4):save(scene20(lg,mode,j),f'E20-{lg}-{mode}-{j}.svg','A family law and an individual-weighted law differ')
 body=para(tr(lg,'两种家族原本各占一半。先选家族再均匀选孩子，与按个体加权选家族，给出的联合权重不同。','Two family types originally have equal probability. Choosing a family first differs from weighting families by their number of children.'))+buttons('data-family-law',[('P',tr(lg,'先等概率选家族','Equal family weights')),('Q',tr(lg,'家族按人数加权','Population-weighted families'))],'P')+'<div class="early-single wide">'+img(f'E20-{lg}-P-1.svg','Fixed trees with probability areas and one marked ancestor line','data-family-scene')+'</div>'+buttons('data-child',[(str(i),x) for i,x in enumerate(['A₁','B₁','B₂','B₃'])],'1')+'<output data-reading>'+tr(lg,'原家族各1/2：单孩联合概率1/2，三孩各1/6。','Original family weights 1/2: joint child weights 1/2,1/6,1/6,1/6.')+'</output>'
 cap=tr(lg,'第一代精确例：P(L=1)=P(L=3)=1/2，m=2。P模式先按原律选树，再条件于该树均匀选孩子；Q模式先用Q₁(t)=Z₁(t)P₁(t)/2选树，所以家族权重为1/4、3/4，Q₁*(t,v)=P₁(t)/2=1/4。两模式给定树后都均匀选孩子；只有选树权重不同。圆面积编码联合概率，树的边长和位置不变；孩子按钮只移动标记。此例P下本已必然生存，Q仍改变生育律，所以大小偏置不是条件生存。图只核对第一代，不未经证明写无限层dQ=W dP。','Exact first-generation example: P(L=1)=P(L=3)=1/2, m=2. In P mode choose a tree under its original law, then choose a child uniformly. In Q mode choose it using Q1(t)=Z1(t)P1(t)/2, giving family weights 1/4,3/4 and Q1*(t,v)=P1(t)/2=1/4. Both modes choose a child uniformly conditional on the selected tree; only the tree weights change. Disk areas encode joint probabilities; edge lengths and positions stay fixed. Child buttons only move the mark. P already survives surely here, yet Q changes reproduction: size bias is not conditioning on survival. Only the first generation is illustrated; no infinite-level density dQ=W dP is asserted.')
 return body,cap,[scene20(lg,'P',1),scene20(lg,'Q',1)]
def body24(lg):
 for d,key in [(.25,'4'),(.125,'8'),(.0625,'16')]:
  save(clock24(lg,d),f'E24-{lg}-clock-{key}.svg','A homeomorphism sends a to a+delta')
  for mode in ['jump','pulse']:
   for align in [0,1]:save(path24(lg,d,mode,bool(align)),f'E24-{lg}-{key}-{mode}-{align}.svg','A clock can align a jump but cannot erase a pulse')
 body=para(tr(lg,'让参考时刻a对应原记录的a+δ。单跳可以精确对齐；一次往返仍必须经过高度1。','Match reference time a to original time a+δ. One jump aligns exactly; a pulse must still reach height 1.'))+buttons('data-path-mode',[('jump',tr(lg,'一次跳跃','One jump')),('pulse',tr(lg,'一次往返','One pulse'))],'jump')+buttons('data-delta',[('4','δ=1/4'),('8','δ=1/8'),('16','δ=1/16')],'8')
 body+='<div class="early-flow"><section><h4>'+tr(lg,'原记录 / 对齐后','Original / aligned')+'</h4>'+img(f'E24-{lg}-8-jump-0.svg','A later jump compared with the reference jump','data-path-scene')+'</section><div class="flow-arrow">⇄</div><section><h4>'+tr(lg,'上：参考t；下：原记录λ(t)','Top: reference t; bottom: original λ(t)')+'</h4>'+img(f'E24-{lg}-clock-8.svg','Three matched time pairs including fixed endpoints','data-clock-scene')+'</section></div>'+buttons('data-aligned',[('0',tr(lg,'原始时刻','Original times')),('1',tr(lg,'应用时钟','Apply the clock'))],'0')+'<output data-reading>'+tr(lg,'未对齐：一致误差1。时钟误差δ=1/8可将单跳对齐。','Unaligned: uniform error 1. Clock error δ=1/8 can align the jump.')+'</output>'
 cap=tr(lg,'a=1/2，0<δ≤1/4。x=1_[a,1]，xδ=1_[a+δ,1]。λ在0,a,1间分段线性，送到0,a+δ,1，是递增连续同胚；‖λ−id‖∞=δ，xδ∘λ=x，而‖xδ−x‖∞=1。往返zδ=1_[a+δ,a+δ+δ²)在任意时间同胚后仍上确界1，因此不能在J₁中趋零。图用同一λ显示窄带仍存在，并由满射性给出所有λ的结论，不由单个画面推断。点的实空表示右连续取值；不以竖直连接线当跳跃之间的路径。让δ趋0才是收敛陈述。','Let a=1/2 and 0<δ≤1/4. For x=1_[a,1] and xδ=1_[a+δ,1], λ is piecewise linear through (0,0),(a,a+δ),(1,1), an increasing continuous homeomorphism. Then ‖λ−id‖∞=δ, xδ∘λ=x, but ‖xδ−x‖∞=1. The pulse zδ=1_[a+δ,a+δ+δ²) retains supremum 1 after every time homeomorphism, so cannot tend to zero in J1. One λ displays the surviving pulse; surjectivity proves the claim for all λ. Filled/open endpoints encode right-continuous values; vertical connectors are not interpolated paths. A convergence statement requires δ→0.')
 return body,cap,[path24(lg,.25,'jump'),path24(lg,.25,'jump',True),clock24(lg,.25),path24(lg,.25,'pulse',True)]
FUNCS={'E06':body06,'E08':body08,'E16':body16,'E20':body20,'E24':body24}
def static(code,lg,title,cap,panes):
 s=Svg(900,1200);s.rect(0,0,900,1200,'white');s.text(30,45,title,27,weight='bold');s.line(30,65,870,65,RULE,1)
 labels={'E06':[tr(lg,'位置顺序','Spatial order'),tr(lg,'按取值归组','Group by value')], 'E08':[tr(lg,'三对相反：矛盾','All opposite: impossible'),tr(lg,'第三对相同：可实现','Third equal: consistent')], 'E16':[tr(lg,'同一前缀，两种合法完成','One prefix, two valid completions')], 'E20':[tr(lg,'先选家族 P','Choose family under P'),tr(lg,'按人数加权 Q','Population-weighted Q')], 'E24':[tr(lg,'原单跳：差1','Unaligned jump: error 1'),tr(lg,'对齐单跳：差0','Aligned jump: error 0'),tr(lg,'时钟误差 δ=1/4','Clock error δ=1/4'),tr(lg,'对齐往返：高度仍为1','Aligned pulse: height remains 1')]}[code]
 if code=='E16':positions=[(170,115,560,482)];bottom=645
 elif code=='E24':positions=[(35,120,395,228),(470,120,395,228),(35,410,395,154),(470,390,395,228)];bottom=660
 else:positions=[(30,125,395,320),(475,125,395,320)];bottom=490
 for j,(p,(x,y,w,h)) in enumerate(zip(panes,positions)):
  s.text(x+w/2,y-24,labels[j],21,anchor='middle');s.nodes.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {p.w} {p.h}" preserveAspectRatio="xMidYMid meet">{p.fragment()}</svg>')
 if code=='E06':s.text(450,470,'1×3/8 + 3×2/8 + 5×3/8 = 3',24,anchor='middle')
 s.line(30,bottom,870,bottom,RULE,1);lines=wrap_caption(cap,lg)
 for i,line in enumerate(lines):s.text(30,bottom+31+24*i,line,17,GRAY)
 s.h=bottom+65+24*len(lines);s.nodes[0]=f'<rect width="900" height="{s.h}" fill="white"/>';save(s,f'{code}.{lg}.svg',title)
def main():
 A.mkdir(parents=True,exist_ok=True);rows=[]
 for code,meta in PILOTS.items():
  for lg in ['zh','en']:
   body,cap,panes=FUNCS[code](lg);title=meta[3 if lg=='zh' else 4]
   html=f'<figure class="explain-figure early-figure" id="visual-{code}" data-early="{code}" lang="{lg}"><header><span>{code}</span><h3>{E(title)}</h3></header>{body}<figcaption id="visual-{code}-end">{E(cap)}</figcaption><nav class="ex-downloads"><a href="{BASE}{code}.{lg}.svg">{tr(lg,"完整静态SVG","Complete static SVG")}</a><a href="/print/{code}.{lg}.html">{tr(lg,"打印页","Print view")}</a></nav></figure>'
   static(code,lg,title,cap,panes);rows.append(dict(id=code,chapter=meta[0],slug=meta[1],section=meta[2],lang=lg,title=title,html=html,condition=cap,status='author visual review pending'))
 (R/'publication/explanatory-early-pilots-working.json').write_text(json.dumps({'canonical_manuscript_changes':False,'automatic_formal_site_injection':False,'scope':'Five pilots in volumes I–IV after chapter-by-chapter I–V review','figures':rows},ensure_ascii=False,indent=2),encoding='utf-8')
 (A/'figures.css').write_text(CSS,encoding='utf-8',newline='\n');(A/'interactions.js').write_text((Path(__file__).parent/'early_interactions.js').read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
 print('Five bilingual early-volume pilots generated in independent namespace.')
CSS='''
.early-figure{background:#fffefa;color:#173f39;border:1px solid #d0ddd4;padding:24px;margin:2rem 0;font:18px/1.7 "Microsoft YaHei","Noto Sans SC",sans-serif;max-width:100%;box-sizing:border-box;break-inside:avoid}.early-figure *{box-sizing:border-box}.early-figure header{display:flex;gap:16px;align-items:baseline}.early-figure header span{font-size:13px;color:#718178}.early-figure h3{font-size:25px;line-height:1.4;margin:0 0 20px}.early-figure h4{text-align:center;font-size:18px;font-weight:500;margin:8px}.early-figure p{font-size:18px;color:inherit;line-height:1.7}.early-flow{display:grid;grid-template-columns:1fr 35px 1fr;align-items:center;gap:10px;margin:20px 0}.flow-arrow{font-size:30px;text-align:center;color:#16776d}.early-figure img.ex-svg{display:block;width:100%;height:auto;max-height:none!important;margin:0;border:0;object-fit:contain;box-shadow:none}.e06-mobile{display:none}.early-single{max-width:425px;margin:24px auto}.early-single.wide{max-width:490px}.early-figure .v5-controls{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:18px 0}.early-figure button{font-family:inherit;font-size:17px;line-height:1.4;color:#173f39;background:#fffefa;border:1px solid #bdcbc2;border-radius:4px;padding:9px 13px;cursor:pointer}.early-figure button[aria-pressed=true]{background:#e8f2eb;border:2px solid #16776d;padding:8px 12px}.early-figure output{display:block;border-top:1px solid #ccd9d1;padding-top:18px;margin:18px 0;font-size:18px}.early-figure .early-result{text-align:center;color:#16776d;font-size:25px}.early-figure figcaption{font-size:15px;line-height:1.8;border-top:1px solid #ccd9d1;padding-top:18px;color:#52665b;overflow-wrap:anywhere}.early-figure nav{display:flex;gap:16px;font-size:14px;margin-top:14px;flex-wrap:wrap}.early-figure a{color:#146d61}
@media(max-width:700px){.early-figure{padding:16px;margin:1.5rem 0}.early-figure header{display:block}.early-figure h3{font-size:22px;margin-top:4px}.early-flow{grid-template-columns:1fr;gap:0;margin:12px 0}.flow-arrow{transform:rotate(90deg);font-size:24px;margin:0}.early-figure h4{font-size:17px}.early-single{margin:16px auto}.early-figure .early-result{font-size:22px}.early-figure button{font-size:16px}.early-figure p,.early-figure output{font-size:17px}.early-figure[data-early=E06] .early-flow{display:none}.e06-mobile{display:block}}
@media print{.early-figure{border:0;background:white;padding:0}.early-figure .v5-controls,.early-figure nav{display:none}}
'''
if __name__=='__main__':main()
