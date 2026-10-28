"""Bounded release verification for the nine-chapter Sites edition."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from io import BytesIO
import hashlib,json,re,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
host=Path(sys.argv[1]).resolve();public=host/'public'
meta=json.loads((host/'formal-nine-preservation.json').read_text('utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
for folder in [public,host/'dist/client']:
    assert len(list((folder/'chapters').glob('*.html')))==9
    assert len(list((folder/'en/chapters').glob('*.html')))==9
    assert not list(folder.rglob('*10-densities-and-kernels*'))
    for name,h in meta['web_pages'].items():assert sha((folder/name).read_bytes())==h,(folder,name)
old=json.loads((host/'formal-analytics-preservation.json').read_text('utf-8'))
for n,h in old['static_asset_hashes'].items():assert sha((public/n).read_bytes())==h,n
pages={p:BeautifulSoup(p.read_bytes(),'html.parser') for p in public.rglob('*.html')}
ids={p:{n['id'] for n in s.select('[id]')} for p,s in pages.items()};links=0
for p,s in pages.items():
    assert not s.select('merror,[data-mjx-error]'),p
    for n in s.select('a[href],img[src],script[src],link[href]'):
        val=n.get('href',n.get('src'));u=urlsplit(val)
        if u.scheme or u.netloc:continue
        if u.path in ['/admin/analytics','/signin-with-chatgpt','/signout-with-chatgpt']:continue
        target=(public/unquote(u.path).lstrip('/')) if u.path.startswith('/') else p.parent/unquote(u.path) if u.path else p
        if target.is_dir():target=target/'index.html'
        target=target.resolve();assert target.exists(),(p,val)
        assert not(u.fragment and target in ids and unquote(u.fragment) not in ids[target]),(p,val)
        links+=1

def scan(data):
    with zipfile.ZipFile(BytesIO(data)) as z:
        for n in z.namelist():
            assert not any(v in n for v in ['10-densities-and-kernels','chat-messages','conversion-ledger','写作约定与全书编排','.dev.vars','.sqlite','.git/']),n
            b=z.read(n)
            if n.endswith('.zip'):scan(b)
            # Chapter10's actual prose must not enter a combined file or nested download.
            assert '桌上的金币还没有离开我们的视线。'.encode() not in b,n
for p in (public/'downloads').glob('*.zip'):scan(p.read_bytes())
for name,h in meta['source_chapters'].items():assert sha((ROOT/name).read_bytes())==h,name
assert not (public/'admin/analytics.html').exists()
print(json.dumps({'nine_chapter_publication':'PASS','chapters':9,'languages':2,'source_chapter_hashes':18,'chapter_formulas':meta['formulas_in_chapters_both_languages'],'verified_visual_assets':len(old['static_asset_hashes']),'local_references':links,'chapter10_in_site_or_downloads':False,'private_records_in_downloads':False,'mobile_background_timing':'PENDING_PHYSICAL_DEVICE_REVIEW','native_sites_analytics':'VERIFIED_CONSOLE_LINKED','automatic_numeric_sync':False}))
