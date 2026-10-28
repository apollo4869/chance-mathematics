"""Compare every English source unit with generated pages and paired anchor structure."""
from pathlib import Path
from collections import Counter
import json,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
from academic_navigation import module_body_html,split_supplement
from math_visuals import remove_figures
manifest=json.loads((ROOT/'translations/en/manifest.json').read_text('utf-8'))
inputs=json.loads((ROOT/'provenance/build-inputs.json').read_text('utf-8'))
items=[];routes={}
shared={'publication/writing-principles.en.md':('rules','writing-rules.html'),
        'translations/en/proofs.md':('supplement','proofs.html'),
        'translations/en/reading-routes.md':('reading-routes','reading-routes.html'),
        'translations/en/references.md':('references','references.html')}
routes.update({'errata':'errata.html','finite-dimensional-proof':'proofs/finite-dimensional.html','proof-boundaries':'proof-boundaries.html'})
for row in manifest['files']:
    target=row['translation'];p=Path(target)
    if target.startswith('chapters-en/'):
        key='chapter-'+str(int(p.name[:2]));route='chapters/'+p.with_suffix('.html').name
    elif target.startswith('advanced-en/'):
        key='advanced-'+p.stem;route='advanced/'+p.with_suffix('.html').name
    elif target.startswith('foundations-en/'):
        key='foundation-'+p.stem.removeprefix('t-');route='proofs/'+p.with_suffix('.html').name
    else:key,route=shared[target]
    items.append({'id':key,'path':str(ROOT/target),'syntax':'slash'})
    routes[key]=route
request={'engineProject':str(ROOT if (ROOT/'node_modules/markdown-it').exists() else ROOT.parent/'chance-mathematics-restored-v2'),
         'items':items,'output':str(ROOT/'build/english-expected.json')}
(ROOT/'build/english-request.json').write_text(json.dumps(request),'utf-8')
node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
subprocess.run([node,str(ROOT/'tools/expected-content.cjs'),str(ROOT/'build/english-request.json')],check=True)
def inspect(fragment):
    soup=BeautifulSoup(str(fragment),'html.parser')
    from volume_navigation import restore_reader_fragment
    restore_reader_fragment(soup)
    remove_figures(soup)
    for n in soup.select('.section-kicker,.chapter-links,.chart,.numeric-chart'):n.decompose()
    tex=[]
    for n in soup.select('.formula,.audit-math'):
        tex.append(n.get('data-tex',n.get('data-audit-tex','')).replace('\r\n','\n').strip());n.replace_with(' ⟦MATH⟧ ')
    compact=lambda s:re.sub(r'\s+','',s)
    return {'text':compact(soup.get_text()),'tex':tex,
            'heads':[(n.name,compact(n.get_text())) for n in soup.find_all(re.compile('^h[1-6]$'))],
            'images':[Path(n.get('src','')).name for n in soup.find_all('img')],
            'widgets':[n.get('data-widget') for n in soup.select('[data-widget]')]}
count=0;audited=[]
for expected in json.loads((ROOT/'build/english-expected.json').read_text('utf-8')):
    key=expected['id']
    if key.startswith('advanced-'):
        expected['html']=module_body_html('<section class="book-section">'+expected['html']+'</section>')
    if key=='supplement':
        audited.extend({'id':k,'html':v} for k,v in split_supplement('<section class="book-section">'+expected['html']+'</section>',True).items())
    else:audited.append(expected)
for expected in audited:
    key=expected['id'];p=ROOT/'dist/en'/routes[key];soup=BeautifulSoup(p.read_text('utf-8'),'html.parser')
    body=soup.find('section',id=key)
    a,b=inspect(body),inspect(expected['html'])
    if a!=b:
        (ROOT/'build/english-content-difference.json').write_text(json.dumps({'section':key,'actual':a,'expected':b},ensure_ascii=False),'utf-8')
        raise AssertionError('English content mismatch: '+key)
    assert soup.html.get('lang')=='en',key
    assert not soup.select('merror,[data-mjx-error]'),key
    count+=len(a['tex'])
    if key.startswith('chapter-'):
        zh=BeautifulSoup((ROOT/'dist'/routes[key]).read_text('utf-8'),'html.parser').find('section',id=key)
        assert [n.get('id') for n in zh.find_all(re.compile('^h[1-6]$'))]==[n.get('id') for n in body.find_all(re.compile('^h[1-6]$'))],(key,'paired headings')
        assert len(zh.select('.reading-unit'))==len(body.select('.reading-unit')),(key,'reading boundaries',len(zh.select('.reading-unit')),len(body.select('.reading-unit')))
print(json.dumps({'english_source_to_web':'PASS','source_units':len(items),'reader_units':len(audited),'formulas':count,'paired_chapter_anchors':'PASS','author_acceptance':'PENDING','publication':False}))
