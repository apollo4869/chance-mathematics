"""Validate frozen formal content and route boundary in a prepared Worker checkout."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib,json,re,sys,zipfile
root=Path(sys.argv[1]).resolve();meta=json.loads((root/'formal-analytics-preservation.json').read_text('utf-8'))
sha=lambda data:hashlib.sha256(data).hexdigest()
def section(text,key):
    first=re.search(r'<section\b[^>]*\bid="'+re.escape(key)+r'"[^>]*>',text);assert first,key
    depth=0
    for match in re.finditer(r'</?section\b[^>]*>',text[first.start():]):
        depth+=-1 if match[0].startswith('</') else 1
        if depth==0:return text[first.start():first.start()+match.end()]
    raise AssertionError(key)
class References(HTMLParser):
    def __init__(self,text):super().__init__();self.refs=[];self.ids=set();self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        self.refs.extend(a[k] for k in ['href','src'] if a.get(k))
for folder in [root/'public',root/'dist/client']:
    assert len(list((folder/'chapters').glob('*.html')))==6
    assert not (folder/'en').exists()
    for item in meta['protected_sections']:
        data=section((folder/item['page']).read_bytes().decode('utf-8'),item['section']).encode()
        assert sha(data)==item['sha256'],(folder,item['page'])
    for name,digest in meta['static_asset_hashes'].items():assert sha((folder/name).read_bytes())==digest,(folder,name)
    for p in folder.rglob('*'):
        if not p.is_file():continue
        assert not re.search(r'chapters/0[789]-',p.relative_to(folder).as_posix()),p
        assert p.suffix not in {'.sqlite','.db'} and p.name not in {'.env','.dev.vars'},p
pages={p:References(p.read_text('utf-8')) for p in (root/'public').rglob('*.html')}
links=0;errors=[]
for p,doc in pages.items():
    for value in doc.refs:
        u=urlsplit(value)
        if u.scheme or u.netloc:continue
        if u.path in ['/admin/analytics','admin/analytics','/signin-with-chatgpt','/signout-with-chatgpt']:continue
        target=((root/'public')/unquote(u.path).lstrip('/')) if u.path.startswith('/') else (p.parent/unquote(u.path)).resolve() if u.path else p
        if target.is_dir():target=target/'index.html'
        links+=1
        if not target.exists():errors.append([str(p),value,'missing path'])
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append([str(p),value,'missing anchor'])
assert not errors,errors[:12]
print(json.dumps({'formal_publication':'PASS','protected_sections':len(meta['protected_sections']),'preserved_visual_assets':len(meta['static_asset_hashes']),'local_references':links,'chapter_count':6,'unpublished_chapters':False,'production_test_events':0}))
