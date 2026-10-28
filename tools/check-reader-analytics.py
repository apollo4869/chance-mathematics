"""Ensure reader instrumentation stays outside manuscripts and secrets stay out of downloads."""
from pathlib import Path
from io import BytesIO
import json,re,zipfile
ROOT=Path(__file__).resolve().parents[1]
secrets=[]
dev=ROOT/'analytics-host/.dev.vars'
if dev.exists():
    match=re.search(r'ANALYTICS_SECRET="([^"]+)"',dev.read_text('utf-8'))
    if match:secrets.append(match[1].encode())
def check_zip(data,label):
    with zipfile.ZipFile(BytesIO(data)) as archive:
        for name in archive.namelist():
            p=Path(name)
            assert not any(part in {'.wrangler','.sites-runtime','node_modules'} for part in p.parts),(label,name)
            assert p.name=='.env.example' or not p.name.startswith(('.dev.vars','.env')),(label,name)
            assert p.suffix not in {'.sqlite','.db','.wal','.shm'},(label,name)
            content=archive.read(name)
            assert not any(secret in content for secret in secrets),(label,name,'local secret')
            if name.endswith('.zip'):check_zip(content,label+'/'+name)
for name in ['complete-offline.zip','editable-manuscript.zip','english-manuscript.zip']:
    check_zip((ROOT/'dist/downloads'/name).read_bytes(),name)
for folder in ['chapters','en/chapters']:
    for p in (ROOT/'dist'/folder).glob('*.html'):
        html=p.read_text('utf-8')
        assert 'reading-analytics-' in html and 'campaign-attribution-' in html,p
assert not (ROOT/'dist/admin/analytics.html').exists(),'Never generate an unprotected static admin page'
config=json.loads((ROOT/'analytics-host/.openai/hosting.json').read_text('utf-8'))
assert config['d1']=='DB' and 'static' not in config
print(json.dumps({'analytics_public_boundary':'PASS','secrets_and_local_D1_in_downloads':False,'instrumented_chapter_pages':sum(len(list((ROOT/'dist'/f).glob('*.html'))) for f in ['chapters','en/chapters']),'static_admin_page':False,'deployment_performed':False}))
