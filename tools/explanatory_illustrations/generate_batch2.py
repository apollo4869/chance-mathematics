"""Preserve batch 1; generate four selected models and two accepted-art refinements."""
from pathlib import Path
import json,shutil
from . import pilot_shapes as shapes
from . import volume5 as first
from . import volume5_next as nxt
ROOT=Path(__file__).resolve().parents[2];A=ROOT/'assets/visuals/explanatory-v2';BASE='/assets/visuals/explanatory-v2/'

def compact_occupation(lang,eps):
 s=shapes.Svg(320,140);s.line(18,95,302,95,shapes.GRAY,1);s.nodes.append(f'<path d="M20 95 L160 30 L300 95" fill="none" stroke="{shapes.TEAL}" stroke-width="2"/>')
 if eps:
  a,b=160-140*eps,160+140*eps;y=95-65*(1-eps);s.nodes.append(f'<path d="M{a} 95 L{a} {y} L160 30 L{b} {y} L{b} 95 Z" fill="{shapes.PALE}" stroke="{shapes.TEAL}"/>')
  s.line(a,95,a,118,shapes.TEAL,1);s.line(b,95,b,118,shapes.TEAL,1);s.line(a,112,b,112,shapes.TEAL,1);s.text(160,135,'2ε',18,anchor='middle')
 else:s.line(160,30,160,95,shapes.WARM,2);s.text(160,132,shapes.tr(lang,'单点：宽度0','Point: width 0'),18,shapes.WARM,anchor='middle')
 s.circle(160,30,4);s.text(160,19,'ℓ(0)=1',18,anchor='middle')
 t=shapes.Svg(320,140);t.line(64,95,256,95,shapes.GRAY,1);t.line(70,30,250,30,shapes.GRAY,1,'4 4');t.text(268,36,'1',18,shapes.GRAY)
 if eps:
  top=95-65*(1-eps/2);t.rect(70,top,180,95-top,shapes.PALE,shapes.TEAL);t.text(160,(top+95)/2+6,shapes.tr(lang,'平均密度','Average density'),18,anchor='middle')
 else:t.rect(70,40,180,55,'white',shapes.GRAY);t.line(85,45,235,90,shapes.WARM,1.5);t.text(160,131,shapes.tr(lang,'0/0不能定义密度','0/0 is not a density'),18,shapes.WARM,anchor='middle')
 return s,t

def refined_jump(lang,k):
 s=first.jump_scene(lang,k)
 s.line(272,27,266,27,shapes.INK,1.8);s.line(266,27,266,187,shapes.INK,1.8);s.line(266,187,272,187,shapes.INK,1.8);s.text(246,126,'20',22,shapes.INK,anchor='middle')
 return s

def main():
 A.mkdir(parents=True,exist_ok=True)
 for p in (ROOT/'assets/visuals/explanatory-v1').iterdir():
  if p.is_file():shutil.copyfile(p,A/p.name)
 shapes.A=A
 original=json.loads((ROOT/'publication/explanatory-figures-working.json').read_text(encoding='utf-8'))['figures'];rows=[]
 for old in original:
  row=dict(old);row['html']=row['html'].replace('/assets/visuals/explanatory-v1/',BASE);row['book_preview']=row['id'] in ['V34','V37'];row['status']='visual working draft adopted'
  code=row['id'];lang=row['lang']
  if code=='V34':
   for k in range(3):refined_jump(lang,k).save(f'V34-{lang}-{k}.svg','Full Ito jump correction groups 12 and 8 as 20')
   callout='<p class="v5-jump-focus"><span>'+shapes.tr(lang,'完整Itô跳跃修正','Full Itô jump correction')+'</span><strong>12 + 8 = 20</strong><small>'+shapes.tr(lang,'Taylor高阶余项只是8','The Taylor residual alone is 8')+'</small></p>'
   row['html']=row['html'].replace('<div class="v5-scene">',callout+'<div class="v5-scene">',1)
   first.static(code,lang,first.META[code][2 if lang=='zh' else 3],row['condition'],[refined_jump(lang,2)])
   f=A/f'{code}.{lang}.svg';s=f.read_text(encoding='utf-8').replace('其余：8','Taylor高阶余项：8').replace('Residual: 8','Taylor residual: 8').replace('跳跃修正：20','完整跳跃修正').replace('Jump correction: 20','Itô jump correction')
   pos=s.rfind('</svg>');s=s[:pos]+'<text x="640" y="507" font-size="24" fill="#173f39">12+8=20</text>'+s[pos:];f.write_text(s,encoding='utf-8')
   row['status']='visual working draft adopted; targeted hierarchy refinement pending review'
  if code=='V37':
   for key,e in [('half',.5),('quarter',.25),('eighth',.125),('point',0)]:
    for part,scene in zip(['band','average'],compact_occupation(lang,e)):scene.save(f'V37-{lang}-mobile-{key}-{part}.svg','Compact occupation normalization; same density model')
   for part in ['band','average']:
    import re
    row['html']=re.sub(r'<img\b[^>]*data-occupation-'+part+r'[^>]*>',lambda m:'<picture><source media="(max-width:700px)" data-mobile-occupation-'+part+' srcset="'+BASE+f'V37-{lang}-mobile-quarter-{part}.svg">'+m.group(0)+'</picture>',row['html'])
   row['status']='visual working draft adopted; mobile compact layout pending review'
  rows.append(row)
 for code,meta in nxt.META.items():
  for lang in ['zh','en']:
   html,condition=nxt.figure(code,lang);rows.append(dict(id=code,lang=lang,slug=meta[0],section=meta[1],title=meta[2 if lang=='zh' else 3],condition=condition,html=html,category='new-explanatory-gap',book_preview=True,status='author visual review pending'))
 css=(ROOT/'tools/explanatory_illustrations/figures.css').read_text(encoding='utf-8')+'''
.explain-figure .v5-jump-focus{display:flex;align-items:baseline;justify-content:center;flex-wrap:wrap;gap:8px 20px;margin:20px 0 8px}.v5-jump-focus strong{font-size:29px;color:#173f39}.v5-jump-focus small{font-size:16px;color:#7257a4}.explain-figure .v5-model{font-size:18px;text-align:center}.v5-second-layer{border-top:1px solid #ccd9d1;padding-top:18px}.v5-second-layer summary{cursor:pointer}.v5-circle-key{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;font-size:16px}.v5-circle-key span{display:flex;align-items:center;gap:8px}.v5-dot-solid,.v5-dot-hollow{display:inline-block;width:12px;height:12px;border-radius:50%;border:2px solid #16776d;background:#16776d}.v5-dot-hollow{border-color:#a45b30;background:white}.v5-equation-total{font-size:22px!important;color:#16776d}.v5-occupation picture{display:block;min-width:0}
@media(max-width:700px){.explain-figure[data-explain=V37]{display:flex;flex-direction:column}.explain-figure[data-explain=V37]>header{order:0}.explain-figure[data-explain=V37]>.v5-intro{order:1}.explain-figure[data-explain=V37]>.v5-controls{order:2;margin:6px 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:4px}.explain-figure[data-explain=V37]>.v5-controls button{min-width:0}.explain-figure[data-explain=V37]>.v5-occupation{order:3;gap:0;margin:6px 0}.explain-figure[data-explain=V37]>.v5-reading{order:4}.explain-figure[data-explain=V37]>figcaption{order:5}.explain-figure[data-explain=V37]>.ex-downloads{order:6}.explain-figure[data-explain=V37] .v5-divide{font-size:18px;line-height:1.3}.explain-figure[data-explain=V37] .v5-divide span{font-size:23px}.explain-figure .v5-jump-focus{gap:5px 12px}.v5-jump-focus strong{font-size:25px}.v5-jump-focus small{font-size:15px}.v5-equation-total{font-size:19px!important}}
'''
 (A/'figures.css').write_text(css,encoding='utf-8',newline='\n')
 js=(ROOT/'tools/explanatory_illustrations/interactions.js').read_text(encoding='utf-8').replace('/assets/visuals/explanatory-v1/',BASE)+(Path(__file__).parent/'interactions_batch2.js').read_text(encoding='utf-8');(A/'interactions.js').write_text(js,encoding='utf-8')
 (ROOT/'publication/explanatory-figures-batch2-working.json').write_text(json.dumps({'schema':1,'scope':'Four selected additions in 35,36,38,40; V34 hierarchy and V37 mobile only','canonical_manuscript_changes':False,'automatic_formal_site_injection':False,'figures':rows},ensure_ascii=False,indent=2),encoding='utf-8');print('Batch 2 generated separately; batch 1 artwork untouched.')
if __name__=='__main__':main()
