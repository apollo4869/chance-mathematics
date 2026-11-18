"""Read-only composite preview for accepted volume VI figures and two candidates."""
from pathlib import Path
import json,re,hashlib,shutil
from tools.explanatory_illustrations.volume6_review import rewrite,insert,shell,assets
from tools.explanatory_illustrations.volume6_followup import R,O,A,P,PREFIX,BASE,write,jsave
rows=json.loads((R/'publication/explanatory-volume6-batch2-working.json').read_text('utf-8'))['figures'];manifest=[];contexts=[];inc=assets(['explanatory-volume6-v1','explanatory-volume6-v2'])
for row in rows:
 code,lg,slug=row['id'],row['lang'],row['slug'];source=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');before=rewrite(source.read_text('utf-8'),lg,slug,inc)
 # Keep the adopted paintbox in the very same chapter when adding the coalescent figure.
 if code=='V47C':
  adopted=next(r for r in rows if r['id']=='V47' and r['lang']==lg);f=adopted['html'].replace('href="/print/',f'href="{PREFIX}print/');before,_=insert(before,dict(adopted,html=f))
 fragment=row['html'].replace('href="/print/',f'href="{PREFIX}print/')
 if code=='V44':
  previous=json.loads((R/'publication/explanatory-volume6-batch1-working.json').read_text('utf-8'))['figures'];old=next(r for r in previous if r['id']=='V44' and r['lang']==lg);old_fragment=old['html'].replace('href="/print/',f'href="{PREFIX}print/');before,anchor=insert(before,dict(old,html=old_fragment));after=before.replace(old_fragment,fragment,1);assert after.replace(fragment,old_fragment,1)==before
 else:after,anchor=insert(before,dict(row,html=fragment));assert after.replace(fragment,'',1)==before
 for suffix,text in [('-before',before),('',after)]:write(P/'chapters'/lg/(slug+suffix+'.html'),text)
 # V47C runs after V47 and deliberately becomes the final shared chapter page with both figures.
 other='en' if lg=='zh' else 'zh';nav=f'<nav><a href="{PREFIX}index.html">总览 / Review</a><a href="{PREFIX}chapters/{lg}/{slug}.html#visual-{code}">正文 / Chapter</a><a href="{PREFIX}print/{code}.{lg}.html">静态 / Static</a><a href="{PREFIX}figures/{code}.{other}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
 write(P/'figures'/f'{code}.{lg}.html',shell(row['title'],nav+fragment,inc,lg))
 static=row['asset_base']+code+'.'+lg+'.svg';pc='<style>@page{size:A4 portrait;margin:12mm}main{max-width:900px}img.static{width:100%}@media print{nav{display:none}main{margin:0;padding:0}body{background:white}}</style>'
 write(P/'print'/f'{code}.{lg}.html',shell(row['title'],nav+f'<img class="static" src="{static}" alt="{row["title"]}"><span id="static-end"></span>',pc,lg))
 manifest.append(dict(id=code,lang=lg,slug=slug,section=row['section'],status=row['status'],title=row['title'],source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),figure=PREFIX+f'figures/{code}.{lg}.html',chapter=PREFIX+f'chapters/{lg}/{slug}.html#visual-{code}',before=PREFIX+f'chapters/{lg}/{slug}-before.html#'+('visual-V44' if code=='V44' else anchor),print=PREFIX+f'print/{code}.{lg}.html'))
 if code in ['V42','V47C']:
  md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');parts=re.split(r'(?m)(?=^## )',md.read_text('utf-8'))
  for sec in row['coverage_sections']:
   ss=[s for s in parts if s.startswith('## '+sec+' ')];assert len(ss)==1;contexts.append(dict(id=code,lang=lg,section=sec,path=md.relative_to(R).as_posix(),sha256=hashlib.sha256(md.read_bytes()).hexdigest(),text=ss[0]))
# Repair shared chapter order: start with the unchanged adopted V47, insert V47C once.
for lg in ['zh','en']:
 a=next(r for r in rows if r['id']=='V47' and r['lang']==lg);c=next(r for r in rows if r['id']=='V47C' and r['lang']==lg);slug=a['slug'];src=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');s=rewrite(src.read_text('utf-8'),lg,slug,inc);s,_=insert(s,dict(a,html=a['html'].replace('href="/print/',f'href="{PREFIX}print/')));write(P/'chapters'/lg/(slug+'-before.html'),s);s,_=insert(s,dict(c,html=c['html'].replace('href="/print/',f'href="{PREFIX}print/')));write(P/'chapters'/lg/(slug+'.html'),s)
body=f'<h1>第六卷 · 再生与有限投影</h1><p class="note">只新增V42、V47C两组候选；V44轻量手机优化；其余已采用图保持原结构。截图重采与异常诊断单独列出。作者审美、真机、原生PDF与专家终审分别记录；不发布、不推送。</p>'
for code in ['V44','V42','V47C','V41','V45','V46','V47']:
 rr=[m for m in manifest if m['id']==code];z=next(r for r in rr if r['lang']=='zh');body+=f'<section class="review"><h2>{code} · {z["title"]}</h2><nav><a href="{z["figure"]}">中文交互</a><a href="{next(r for r in rr if r["lang"]=="en")["figure"]}">English</a><a href="{z["chapter"]}">章节嵌入</a><a href="{z["print"]}">静态打印</a>'+(f'<a href="{PREFIX}compare/{code}.html">前后对照与截图</a>' if code in ['V42','V47C','V44'] else '')+'</nav></section>'
body+=f'<nav><a href="{PREFIX}recaptures.html">V41/V44/V45黑区核查与重采</a><a href="/assets/visuals/explanatory-volume6-v1/local-preview/adopted/index.html">前五卷已采用索引（保护）</a><a href="/assets/visuals/explanatory-volume6-v1/local-preview/figures/P02.zh.html">P02原样保留</a></nav>'
write(P/'index.html',shell('第六卷第二批审阅',body))
for code in ['V42','V47C','V44']:
 body=f'<nav><a href="{PREFIX}index.html">总览</a></nav><h1>{code} · 本轮前后与截图</h1>'
 for lg in ['zh','en']:
  body+=f'<h2>{lg}</h2><nav><a href="{PREFIX}figures/{code}.{lg}.html">交互</a><a href="{PREFIX}print/{code}.{lg}.html">打印</a></nav>'
  for tags in [('desktop','mobile'),('desktop-end','mobile-end'),('interaction-desktop','interaction-mobile'),('chapter-before-desktop','chapter-after-desktop'),('chapter-before-mobile','chapter-after-mobile'),('print','print-end')]:
   body+='<div class="twins">'+''.join(f'<figure class="shots"><a href="{PREFIX}screenshots/{code}-{lg}-{t}.jpg"><img loading="lazy" src="{PREFIX}screenshots/{code}-{lg}-{t}.jpg" alt="{t}"></a><figcaption>{t}</figcaption></figure>' for t in tags)+'</div>'
 write(P/'compare'/f'{code}.html',shell(code+' comparison',body))
body=f'<nav><a href="{PREFIX}index.html">总览</a></nav><h1>默认桌面截图：旧文件与同代码重采</h1><p>旧中文文件实际有纯黑矩形；原图、HTML、CSS与JS不改，保持固定桌面视口后重采。完整诊断见审阅包SCREENSHOT_REVIEW.md。</p>'
for code in ['V41','V44','V45']:
 for lg in ['zh','en']:
  body+=f'<h2>{code} {lg}</h2><div class="twins">'
  for sub,suffix,label in [('references','-desktop','原文件'),('screenshots','-desktop-recaptured','同代码重采')]:
   src=PREFIX+f'{sub}/{code}-{lg}{suffix}.jpg';body+=f'<figure class="shots"><a href="{src}"><img loading="lazy" src="{src}"></a><figcaption>{label}</figcaption></figure>'
  body+='</div>'
write(P/'recaptures.html',shell('截图异常诊断',body));jsave(O/'manifest.json',manifest);jsave(O/'reading-contexts.json',contexts)
for folder in ['screenshots','references']:
 for p in (O/folder).glob('*.jpg'):d=P/folder/p.name;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,d)
print('14 bilingual figure views; 2 new models, V44 mobile refinement; adopted chapter 47 paintbox retained')
