"""Separate content, formula, provenance, math/history status, and page audits."""
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit,unquote
import sys,re,json,hashlib,subprocess,shutil,base64,csv
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
REPORTS=ROOT/'reports';REPORTS.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda s:re.sub(r'\s+','',s)
def save(name,obj):(REPORTS/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
baseline=json.loads((ROOT/'baseline-manuscript.json').read_text(encoding='utf-8'))
inputs=json.loads((ROOT/'provenance/build-inputs.json').read_text(encoding='utf-8'))
slugs=[Path(n).stem for n in inputs['chapters']]
items=[{'id':f'chapter-{i}','path':str(ROOT/'chapters'/n),'syntax':'slash'} for i,n in enumerate(inputs['chapters'],1)]
items += [{'id':key,'path':str(ROOT/name),'syntax':'slash'} for key,name in [('rules','写作约定与全书编排.md'),('supplement','校订与证明补充.md'),('references','引用与配图来源.md')]]
node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
engine=ROOT if (ROOT/'node_modules/markdown-it').exists() else ROOT.parent/'chance-mathematics-restored-v2'
request={'engineProject':str(engine),'items':items,'output':str(REPORTS/'expected-content.json')}
save('renderer-request.json',request)
subprocess.run([node,str(ROOT/'tools/expected-content.cjs'),str(REPORTS/'renderer-request.json')],check=True)
expected={r['id']:r for r in json.loads((REPORTS/'expected-content.json').read_text(encoding='utf-8'))}
routes={f'chapter-{i}':ROOT/'dist/chapters'/f'{slug}.html' for i,slug in enumerate(slugs,1)}
routes.update({'rules':ROOT/'dist/writing-rules.html','supplement':ROOT/'dist/proofs.html','references':ROOT/'dist/references.html'})
def inspect(fragment,base):
    soup=BeautifulSoup(fragment,'html.parser');formulas=[];images=[]
    for n in soup.select('.section-kicker,.chapter-links,.chart,.numeric-chart'):n.decompose()
    for n in soup.select('.audit-math,.formula'):
        formulas.append(n.get('data-tex',n.get('data-audit-tex','')).replace('\r\n','\n').replace('\r','\n').strip());n.replace_with(' ⟦MATH⟧ ')
    for n in soup.find_all('img'):
        src=n.get('src','');p=(ROOT/'dist'/src.lstrip('/')) if src.startswith('/') else base/src
        try:images.append(sha(base64.b64decode(src.split(',',1)[1])) if src.startswith('data:') else sha(p.resolve().read_bytes()))
        except Exception:images.append('MISSING:'+src)
    return {'text':canon(soup.get_text()),'headings':[(n.name,canon(n.get_text())) for n in soup.find_all(re.compile('^h[1-6]$'))],'formulas':formulas,'images':images,'widgets':[n.get('data-widget') for n in soup.select('[data-widget]')],'inline_svg':[str(n) for n in soup.find_all('svg')]}
rows=[];formula_rows=[]
for item in items:
    key=item['id'];p=Path(item['path']);actual=BeautifulSoup(routes[key].read_text(encoding='utf-8'),'html.parser').find('section',id=key)
    e=inspect(expected[key]['html'],p.parent);a=inspect(str(actual),routes[key].parent)
    content_fields=['text','headings','images','widgets','inline_svg']
    row={'section':key,'source_bytes':p.stat().st_size,'source_sha256':sha(p.read_bytes()),'baseline_bytes_unchanged':sha(p.read_bytes())==baseline['files'][p.relative_to(ROOT).as_posix()],**{k+'_equal':a[k]==e[k] for k in content_fields},'formula_order_equal':a['formulas']==e['formulas'],'formula_count':len(e['formulas'])}
    row['migration_status']='PASS' if all(row[k] for k in ['baseline_bytes_unchanged','formula_order_equal']+[f+'_equal' for f in content_fields]) else 'FAIL';rows.append(row)
    fsoup=BeautifulSoup(str(actual),'html.parser');formula_nodes=fsoup.select('.formula')
    formula_rows.append({'section':key,'expected':len(e['formulas']),'rendered':len(formula_nodes),'tex_exact_and_ordered':a['formulas']==e['formulas'],'missing_svg':sum(n.find('mjx-container') is None or n.find('svg') is None for n in formula_nodes),'render_errors':len(fsoup.select('merror,[data-mjx-error],.math-failed'))})
    if row['migration_status']=='FAIL':save('difference-'+key+'.json',{'expected':e,'actual':a})
    else:(REPORTS/('difference-'+key+'.json')).unlink(missing_ok=True)
save('content-integrity.json',{'scope':'Confirmed reorganized long working manuscript to candidate HTML; not original ChatGPT equivalence or math truth. Whitespace-only prose differences ignored; source bytes separately pinned.','status':'PASS' if all(r['migration_status']=='PASS' for r in rows) else 'FAIL','sections':rows})
save('formula-rendering.json',{'scope':'TeX preservation, order, SVG presence and parser errors only; not correctness of mathematical assertions or complete visual QA.','status':'PASS' if all(r['tex_exact_and_ordered'] and r['rendered']==r['expected'] and not r['missing_svg'] and not r['render_errors'] for r in formula_rows) else 'FAIL','sections':formula_rows,'total':sum(r['rendered'] for r in formula_rows),'mathematical_correctness':'PENDING_REVIEW'})
with (REPORTS/'chapter-integrity.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Replay available archived extracts, while explicitly refusing completeness certification.
ledger=json.loads((ROOT/'provenance/conversion-ledger.json').read_text(encoding='utf-8'))
corrections=json.loads((ROOT/'provenance/corrections.json').read_text(encoding='utf-8'))
source_rows=[];block_rows=[]
for filename in inputs['chapters']:
    key=filename.replace('.md','-chat');raw=(ROOT/'provenance/mother'/(key+'.txt')).read_text(encoding='utf-8');current=(ROOT/'chapters'/filename).read_text(encoding='utf-8');replay=raw;reversed_text=current;failures=[];shielded=[]
    for c in reversed(corrections):
        if c['file']=='chapters/'+filename:
            if c['after'] not in reversed_text:failures.append('correction not replayable: '+c['reason'])
            reversed_text=reversed_text.replace(c['after'],c['before'],1)
    records=[r for r in ledger if r['chapter']==key]
    for record in records:
        if record['kind']=='layout-only' and not shielded:replay=re.sub(r'<svg\b.*?</svg>',lambda m:shielded.append(m.group()) or f'SVGPLACEHOLDER{len(shielded)-1}END',replay,flags=re.S)
        if record['source'] not in replay:failures.append('conversion not replayable: '+record['kind'])
        replay=replay.replace(record['source'],record['replacement'],1)
    for i,v in enumerate(shielded):replay=replay.replace(f'SVGPLACEHOLDER{i}END',v)
    match=canon(replay)==canon(reversed_text)
    source_rows.append({'chapter':filename,'available_archive_sha256':sha((ROOT/'provenance/mother'/(key+'.txt')).read_bytes()),'registered_transform_replay':'MATCH' if match and not failures else 'DIFFERENCE','failures':failures,'initial_full_chat_equivalence':'UNVERIFIED','reason':'Available extracts and prior conversion records were retained; completeness/authenticity of the initial full ChatGPT conversation has not been independently established.'})
    offset=0
    for i,block in enumerate(re.split(r'\n\s*\n',current.strip()),1):
        start=current.find(block,offset);offset=start+len(block)
        status='EXACT_FRAGMENT_IN_AVAILABLE_ARCHIVE' if canon(block) in canon(raw) else 'NO_DIRECT_BLOCK_MATCH_REQUIRES_REVIEW'
        if status.startswith('NO_DIRECT') and any(c['file']=='chapters/'+filename and (canon(c['after']) in canon(block) or canon(block) in canon(c['after'])) for c in corrections):status='PREEXISTING_REGISTERED_CORRECTION_NOT_NEW_STAGE1_EDIT'
        elif status.startswith('NO_DIRECT') and any(canon(block) in canon(r['replacement']) for r in records if r['replacement'].strip()):status='REGISTERED_COMPONENT_TRANSFORMATION'
        block_rows.append({'chapter':filename,'block':i,'line_start':current.count('\n',0,start)+1,'excerpt':block.replace('\n',' ')[:90],'sha256':sha(block.encode()),'available_archive_mapping':status,'initial_chat_status':'UNVERIFIED'})
save('source-provenance.json',{'initial_chat_status':'UNVERIFIED','available_archive_replay_status':'MATCH' if all(x['registered_transform_replay']=='MATCH' for x in source_rows) else 'DIFFERENCE','not_a_certificate':'A replay match establishes consistency with available local extracts and registered transformations, not completeness of the original ChatGPT six chapters.','chapters':source_rows,'block_mapping_counts':dict(Counter(x['available_archive_mapping'] for x in block_rows))})
save('source-block-map.json',block_rows)
# Static page structure is separate from content and mathematical status.
dist=ROOT/'dist';pages={p:BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser') for p in sorted(dist.rglob('*.html'))};ids={p:Counter(n['id'] for n in s.select('[id]')) for p,s in pages.items()};web_failures=[];count=0
for p,s in pages.items():
    web_failures += [{'page':str(p.relative_to(dist)),'duplicate_id':k} for k,v in ids[p].items() if v>1]
    for n in s.select('a[href],script[src],link[href],img[src]'):
        value=n.get('href',n.get('src'));u=urlsplit(value)
        if u.scheme or u.netloc:continue
        target=(dist/unquote(u.path).lstrip('/')) if u.path.startswith('/') else (p.parent/unquote(u.path) if u.path else p)
        if target.is_dir():target=target/'index.html'
        target=target.resolve();count+=1
        if not target.exists():web_failures.append({'page':str(p.relative_to(dist)),'missing_file':value})
        elif u.fragment and target in ids and unquote(u.fragment) not in ids[target]:web_failures.append({'page':str(p.relative_to(dist)),'missing_anchor':value})
save('web-quality.json',{'static_status':'PASS' if not web_failures else 'FAIL','pages':len(pages),'local_references':count,'failures':web_failures,'browser_status':'NOT_RUN_BY_THIS_SCRIPT','math_status':'NOT_ASSESSED','history_status':'NOT_ASSESSED'})
print(json.dumps({'content':json.loads((REPORTS/'content-integrity.json').read_text())['status'],'formula_rendering':json.loads((REPORTS/'formula-rendering.json').read_text())['status'],'available_archive_replay':json.loads((REPORTS/'source-provenance.json').read_text())['available_archive_replay_status'],'initial_chat':'UNVERIFIED','static_web':'PASS' if not web_failures else 'FAIL','math_and_history':'PENDING_REVIEW'},ensure_ascii=False))
raise SystemExit(any(r['migration_status']=='FAIL' for r in rows) or bool(web_failures) or any(r['missing_svg'] or r['render_errors'] or not r['tex_exact_and_ordered'] for r in formula_rows))
