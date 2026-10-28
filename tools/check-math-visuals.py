"""Independent figure registry/placement/source preservation check; never academic approval."""
from pathlib import Path
import json,hashlib,subprocess,sys,re
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
from math_visuals import records,figure_html,remove_figures
from intro_preservation import remove_introduction_nodes
manifest=json.loads((ROOT/'assets/visuals/print-manifest.json').read_text('utf8'))
assert len(records())==8 and len({r['id'] for r in records()})==8
new_manifest=json.loads((ROOT/'assets/visuals/local-clt-manifest.json').read_text('utf8'))
array_manifest=json.loads((ROOT/'assets/visuals/array-budget-manifest.json').read_text('utf8'))
from fractions import Fraction
from math import comb,sqrt,exp,pi
model=json.loads((ROOT/'assets/visuals/local-clt-data.json').read_text('utf8'))
for row in model['rows']:
    n=row['n'];total=Fraction(0);mean=Fraction(0);second=Fraction(0)
    for point in row['full_support']:
        k=point['k'];allowed=(k-n)%2==0
        mass=Fraction(point['numerator'],point['denominator'])
        assert mass==Fraction(comb(n,(n+k)//2) if allowed else 0,2**n)
        assert point['allowed']==allowed
        if allowed:assert abs(point['local_gaussian']-2/sqrt(n)*exp(-k*k/(2*n))/sqrt(2*pi))<1e-15
        else:assert point['local_gaussian'] is None
        total+=mass;mean+=k*mass;second+=k*k*mass
    assert (total,mean,second)==(1,0,n)
for lang in ['zh','en']:
    captions=(ROOT/('publication/visual-captions.'+lang+'.md')).read_text('utf8')
    for row in records():assert all(row[lang][field] in captions for field in ['title','caption','alt']),('caption source drift',row['id'],lang)
for n in array_manifest['model']['n']:
    rare_variance=2*Fraction(1,2*n)
    small_variance=Fraction(1,n)
    assert rare_variance==small_variance and n*rare_variance==1
    assert n>=16 and 1/sqrt(n)<.3<1
for name,info in (manifest['files']|new_manifest['files']|array_manifest['files']).items():
    data=(ROOT/name).read_bytes();assert hashlib.sha256(data).hexdigest()==info['sha256'],name
    if name.endswith('.svg'):
        tree=ET.fromstring(data);assert not tree.findall('.//{http://www.w3.org/2000/svg}image'),'raster in print original'
    if name.endswith('.pdf'):assert data.startswith(b'%PDF-') and b'/Subtype /Image' not in data,name
node=r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
subprocess.run([node,str(ROOT/'tools/test-math-visuals.cjs')],cwd=ROOT,check=True)
if '--prebuild' in sys.argv:print('Publication math assets and invariants PASS');sys.exit(0)
ref='snapshot/before-math-visuals-batch1-2026-10-26';placed=[]
for en,folder in [(False,''),(True,'en/')]:
 for page in (ROOT/'dist'/folder/'chapters').glob('*.html'):
    if int(page.name[:2])>12:continue  # New chapters have independent source-to-reader checks.
    old=BeautifulSoup(subprocess.check_output(['git','show',ref+':dist/'+folder+'chapters/'+page.name],cwd=ROOT),'html.parser').select_one('.book-section')
    soup=BeautifulSoup(page.read_bytes(),'html.parser');body=soup.select_one('.book-section');chapter=int(page.name[:2]);expected=[r for r in records() if r['chapter']==chapter]
    assert {f['data-math-visual'] for f in body.select('[data-math-visual]')}=={r['id'] for r in expected}
    for row in expected:
        actual=body.select_one('[data-math-visual="'+row['id']+'"]');want=BeautifulSoup(figure_html(row,en),'html.parser').div
        assert re.sub(r'\s+','',actual.get_text())==re.sub(r'\s+','',want.get_text()),row['id']
        image=actual.find('img');assert image.get('alt')==row['en' if en else 'zh']['alt']
        assert image['src'].endswith(row['id']+'.'+('en' if en else 'zh')+'.svg')
        # The declared semantic position must match; no placement is inferred silently.
        next_node=actual.find_next_sibling();prev=actual.find_previous_sibling();position=row['placement']
        if 'before_widget' in position:assert next_node.get('data-widget')==position['before_widget']
        elif 'before_heading' in position:
            next_node=actual.find_next(['h2','h3'])
            assert next_node and next_node.get_text().startswith(position['before_heading']+' ')
        else:assert prev.name=='p' and prev.get_text(' ',strip=True).startswith(position['after_paragraph']['en' if en else 'zh'])
        placed.append(row['id'])
    remove_figures(body)
    remove_introduction_nodes(body)
    for fragment in [old,body]:
        for n in fragment.select('.chapter-links,.section-kicker'):n.decompose()
    assert str(old)==str(body),('original chapter DOM changed',page)
assert len(placed)==12
for en,folder in [(False,''),(True,'en/')]:
    page=ROOT/'dist'/folder/'chapters/13-rare-events.html';s=BeautifulSoup(page.read_bytes(),'html.parser')
    row=next(r for r in records() if r['id']=='local-clt-parity')
    actual=s.select_one('[data-math-visual="local-clt-parity"]');want=BeautifulSoup(figure_html(row,en),'html.parser').div
    assert actual and actual.get_text()==want.get_text()
    assert actual.find('img')['alt']==row['en' if en else 'zh']['alt']
    assert actual.find_next(['h2','h3']).get_text().startswith('13.18 ')
for en,folder in [(False,''),(True,'en/')]:
    page=ROOT/'dist'/folder/'chapters/14-arrays-and-stability.html';s=BeautifulSoup(page.read_bytes(),'html.parser')
    row=next(r for r in records() if r['id']=='lindeberg-budget')
    actual=s.select_one('[data-math-visual="lindeberg-budget"]');want=BeautifulSoup(figure_html(row,en),'html.parser').div
    assert actual and actual.get_text()==want.get_text()
    assert actual.find('img')['alt']==row['en' if en else 'zh']['alt']
    assert actual.find_next(['h2','h3']).get_text().startswith('14.4 ')
print(json.dumps({'math_visuals':'PASS','vector_outputs':32,'bilingual_placements':16,'original_chapter_dom':'EXACT_AFTER_REMOVING_VERIFIED_ADDITIONS','new_interactions':1,'mathematical_final_review':False,'publication':False}))
