"""Verify authorized changes separately from the historical phase-1 audit."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import ast,base64,difflib,hashlib,json,re,subprocess,sys,shutil
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda s:re.sub(r'\s+','',s)
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'))
manifest=load('docs/brownian-relocation.json');tag=manifest['snapshot_tag']
old=lambda p:subprocess.check_output(['git','-C',str(ROOT),'show',tag+':'+p])
original=old('chapters/04-brownian.md')
assert (ROOT/manifest['full_original_archive']).read_bytes()==original
moves=[]
for row in manifest['moves']:
    raw=original[row['start_byte']:row['end_byte']]
    assert sha(raw)==row['sha256']
    assert (ROOT/row['destination']).read_bytes().endswith(raw)
    moves.append({'destination':row['destination'],'verbatim':True,'bytes':len(raw),'sha256':sha(raw)})
unchanged=[]
inputs=load('provenance/build-inputs.json')
for i in [1,2,5,6]:
    p='chapters/'+inputs['chapters'][i-1]
    assert (ROOT/p).read_bytes()==old(p)
    unchanged.append(i)
before=old('chapters/03-normal.md').decode('utf-8').splitlines(keepends=True)
after=(ROOT/'chapters/03-normal.md').read_bytes().decode('utf-8').splitlines(keepends=True)
operations=difflib.SequenceMatcher(a=before,b=after,autojunk=False).get_opcodes()
assert all(op in ('equal','insert') for op,*_ in operations),operations
baseline=load('baseline-manuscript.json')
assert all(sha((ROOT/p).read_bytes())==h for p,h in baseline['files'].items())
# Independent renderer, including all relocated modules.
items=[{'id':'chapter-'+str(i),'path':str(ROOT/'chapters'/p),'syntax':'slash'} for i,p in enumerate(inputs['chapters'],1)]
items += [{'id':key,'path':str(ROOT/p),'syntax':'slash'} for key,p in [('rules','写作约定与全书编排.md'),('supplement','校订与证明补充.md'),('references','引用与配图来源.md')]]
items += [{'id':m['id'],'path':str(ROOT/m['file']),'syntax':'slash'} for m in inputs['advanced_modules']]
request={'engineProject':str(ROOT.parent/'chance-mathematics-restored-v2'),'items':items,'output':str(ROOT/'build/brownian-expected.json')}
(ROOT/'build/brownian-request.json').write_text(json.dumps(request),encoding='utf-8')
node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
subprocess.run([node,str(ROOT/'tools/expected-content.cjs'),str(ROOT/'build/brownian-request.json')],check=True)
tree=ast.parse((ROOT/'tools/check-stage1.py').read_text(encoding='utf-8'))
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='inspect')
exec(compile(ast.Module(body=[fn],type_ignores=[]),'independent-inspector','exec'),globals())
routes={'chapter-'+str(i):ROOT/'dist/chapters'/Path(p).with_suffix('.html').name for i,p in enumerate(inputs['chapters'],1)}
routes.update({'rules':ROOT/'dist/writing-rules.html','supplement':ROOT/'dist/proofs.html','references':ROOT/'dist/references.html'})
routes.update({m['id']:ROOT/'dist/advanced'/(m['slug']+'.html') for m in inputs['advanced_modules']})
sections=[]
for item in load('build/brownian-expected.json'):
    actual=BeautifulSoup(routes[item['id']].read_text(encoding='utf-8'),'html.parser').find('section',id=item['id'])
    a=inspect(str(actual),routes[item['id']].parent);e=inspect(item['html'],Path(item['path']).parent)
    assert a==e,item['id']
    sections.append({'section':item['id'],'source_to_html_equal':True,'formulas':len(a['formulas'])})
failures=[];checked=0;formulas=0;ids={}
for p in (ROOT/'dist').rglob('*.html'):
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    ids[p.resolve()]={n['id'] for n in soup.select('[id]')}
    for f in soup.select('.formula'):
        formulas+=1
        assert f.find('svg') and not f.select('merror,[data-mjx-error]'),str(p)
for p in (ROOT/'dist').rglob('*.html'):
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    for n in soup.select('a[href],script[src],link[href],img[src]'):
        url=n.get('href',n.get('src'));u=urlsplit(url)
        if u.scheme or u.netloc:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
        checked+=1
        if not target.is_file() or (u.fragment and target.suffix=='.html' and unquote(u.fragment) not in ids.get(target,set())):failures.append([str(p.relative_to(ROOT)),url])
assert not failures,failures
result={'status':'PASS','scope':'New reading branch, not final math/history or author acceptance','unchanged_chapters':unchanged,'chapter3_insertions_only':True,
 'full_original_archive_byte_identical':True,'moves':moves,'protected_hashes':len(baseline['files']),'source_html_units':sections,'formula_count':formulas,
 'body_formula_count':sum(x['formulas'] for x in sections),'formula_count_includes_navigation':True,
 'formula_engine_errors':0,'local_link_checks':checked,'broken_links':failures,'publication':False,'print_visual':'NOT_ACCEPTED','file_protocol_browser':'NOT_ACCEPTED'}
(ROOT/'reports/brownian-reading-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','unchanged_chapters':unchanged,'moved_modules':len(moves),'units':len(sections),'formulas':formulas,'local_links':checked},ensure_ascii=False))
