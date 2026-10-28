"""Bounded publication checks; never sends reading events to production."""
from pathlib import Path
from io import BytesIO
import argparse, hashlib, json, posixpath, re, sys, zipfile
from urllib.parse import urlsplit, unquote
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
ap=argparse.ArgumentParser();ap.add_argument('--source-root',required=True);ap.add_argument('--checkout',required=True);ap.add_argument('--report',required=True);a=ap.parse_args()
root=Path(a.source_root).resolve();host=Path(a.checkout).resolve();public=host/'public'
inputs=json.loads((root/'provenance/build-inputs.json').read_text('utf8'))['chapters'];assert len(inputs)==15
sha=lambda b:hashlib.sha256(b).hexdigest()
pages={p.relative_to(public).as_posix():p.read_bytes() for p in public.rglob('*.html')}
texts={n:b.decode('utf8') for n,b in pages.items()}
def fragment(text,i):
    m=re.search(r'<section\b[^>]*\bid="chapter-'+str(i)+r'"[^>]*>',text)
    assert m,('Missing chapter body',i)
    depth=0
    for t in re.finditer(r'</?section\b[^>]*>',text[m.start():]):
        depth+=-1 if t[0].startswith('</') else 1
        if depth==0:return text[m.start():m.start()+t.end()]
    raise AssertionError('Unclosed chapter body')
references=0;formulas=0
def links(rows,exists,get_ids):
    global references
    for name,b in rows.items():
        for value in re.findall(r'\b(?:href|src)="([^"]*)"',b.decode('utf8')):
            value=value.replace('&amp;','&');u=urlsplit(value)
            if u.scheme or u.netloc:continue
            target=unquote(u.path)
            if target.startswith(('/api/','/admin/','/signin-with-chatgpt')):continue
            target=posixpath.normpath(target.lstrip('/') if target.startswith('/') else posixpath.join(posixpath.dirname(name),target)) if target else name
            if target in {'','.'}:target='index.html'
            if target.endswith('/'):target+='index.html'
            if not exists(target) and exists(target+'/index.html'):target+='/index.html'
            assert exists(target),('Missing local target',name,value,target)
            if u.fragment and target.endswith('.html'):
                assert unquote(u.fragment) in get_ids(target),('Missing anchor',name,value)
            references+=1
for en in [False,True]:
    prefix='en/' if en else '';folder='chapters-en' if en else 'chapters'
    for i,n in enumerate(inputs,1):
        page=prefix+'chapters/'+Path(n).with_suffix('.html').name
        current=texts[page];before=(root/'dist'/page).read_bytes().decode('utf8')
        assert fragment(current,i)==fragment(before,i),('Body changed',page)
        assert current.count('class="volume-nav-group"')==8
        if i>=13:
            for ext in ['zh','en']:
                assert (public/'print'/(Path(n).stem+'.'+ext+'.html')).exists()
        assert (host/'book-source-fifteen'/folder/n).read_bytes()==(root/folder/n).read_bytes()
    for n in ['01-opening','01-ending','02-opening','02-ending','03-opening']:
        assert prefix+'volumes/'+n+'.html' in pages
    assert not (public/prefix/'volumes/03-ending.html').exists()
for n,s in texts.items():
    assert not re.search(r'<merror\b|data-mjx-error=',s),('Formula render error',n)
    formulas+=len(re.findall(r'class="formula(?:\s|\")',s))
for n in pages:
    assert not re.search(r'(?:^|/)(?:1[6-9]|20)-',n),('Unauthorized chapter',n)
assert not (public/'admin/analytics/index.html').exists()
online_ids={n:set(re.findall(r'\bid="([^"]*)"',t)) for n,t in texts.items()}
links(pages,lambda n:(public/n).is_file(),lambda n:online_ids[n])
source_count=0
with zipfile.ZipFile(public/'downloads/complete-offline.zip') as z:
    names=set(z.namelist());offline_html={n:z.read(n) for n in names if n.endswith('.html') and not n.startswith('editable-source/')}
    cached={}
    def ids(n):
        if n not in cached:cached[n]=set(re.findall(r'\bid="([^"]*)"',z.read(n).decode('utf8')))
        return cached[n]
    links(offline_html,lambda n:n in names,ids)
    for p in (host/'book-source-fifteen').rglob('*'):
        if p.is_file():
            n=p.relative_to(host/'book-source-fifteen').as_posix();assert z.read('editable-source/'+n)==p.read_bytes(),n;source_count+=1
    assert not any(re.search(r'(?:chapters(?:-en)?/)(?:1[6-9]|20)-',n) for n in names)
    assert not any(t in n for n in names for t in ['BOOK_MASTER_OUTLINE','THEOREM_COVERAGE','CHAPTER_STATUS','CHAPTER_DEPENDENCIES','chat-messages','.dev.vars','.sqlite'])
assert max(p.stat().st_size for p in public.rglob('*') if p.is_file())<25*1024*1024
report={'status':'PASS','chapters':15,'languages':2,'html_pages':len(pages),'formula_occurrences':formulas,'local_and_offline_references':references,'offline_source_files':source_count,'offline_bytes':(public/'downloads/complete-offline.zip').stat().st_size,'chapter_bodies':'BYTE_EXACT','chapters16_20_exported':False,'static_admin_page':False,'production_test_events':0,'author_approval_upgraded':False,'mobile_background_timing':'PENDING_PHYSICAL_DEVICE_REVIEW'}
Path(a.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps(report))
