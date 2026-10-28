"""Archive manuscripts from an already deployed release; never deploy or expose Git history."""
from pathlib import Path
import argparse, hashlib, json, re, subprocess, zipfile
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--receipt', required=True)
parser.add_argument('--release-id', required=True)
parser.add_argument('--published-date', required=True, help='Verified publication date YYYY-MM-DD')
args=parser.parse_args()
from datetime import date
published_date=date.fromisoformat(args.published_date)
assert re.fullmatch(r'[a-z0-9][a-z0-9-]{0,70}', args.release_id)
receipt=json.loads(Path(args.receipt).read_text('utf-8'))
assert receipt['status']=='succeeded' and receipt['audience']=='public'
commit=receipt['commit_sha']
assert re.fullmatch('[0-9a-f]{40}',commit)
read=lambda name:subprocess.check_output(['git','show',commit+':'+name],cwd=ROOT)
inputs=json.loads(read('provenance/build-inputs.json'))
names=['chapters/'+n for n in inputs['chapters']]
names += [m['file'] for m in inputs.get('advanced_modules',[])]
names += ['校订与证明补充.md','引用与配图来源.md','延伸阅读与证明路线.md']
files={name:read(name) for name in names}
sha=lambda b:hashlib.sha256(b).hexdigest()
contents={n:sha(b) for n,b in sorted(files.items())}
chapters=[]
for n,name in enumerate(inputs['chapters'],1):
    page='dist/chapters/'+Path(name).with_suffix('.html').name
    chapters.append({'chapter':n,'source':'chapters/'+name,'source_sha256':contents['chapters/'+name],
                     'published_html_sha256':sha(read(page))})
folder=ROOT/'publication/releases';folder.mkdir(parents=True,exist_ok=True)
archive=folder/(args.release_id+'.zip');manifest=folder/(args.release_id+'.json')
if archive.exists() or manifest.exists():raise SystemExit('Release IDs are immutable; use the existing snapshot or choose a new ID.')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for name,data in sorted(files.items()):
        info=zipfile.ZipInfo(name,date_time=(published_date.year,published_date.month,published_date.day,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data)
    z.writestr('contents-sha256.json',(json.dumps(contents,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode())
record={'schema_version':1,'release_id':args.release_id,'kind':'FORMAL_WEB_PUBLICATION',
        'published_date':args.published_date,'chapter_count':len(chapters),'languages':['zh-CN'],
        'author':'Haobai Wang','source_commit':commit,'formal_url':receipt['url'].rstrip('/')+'/',
        'hosting_version_number':receipt['version_number'],'hosting_version_id':receipt['version_id'],
        'deployment_id':receipt['deployment_id'],'original_deployment_archive_sha256':receipt['archive_sha256'],
        'snapshot_scope':'Published chapter and proof manuscripts, byte-exact from the deployed source commit. Not a copy of the deployment tar; private records and author notes excluded.',
        'archive_file':archive.name,'archive_sha256':sha(archive.read_bytes()),'files':contents,'chapters':chapters,
        'author_approval_scope':'Previously authorized public web version for phone review; academic final review not implied.'}
manifest.write_bytes((json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'release_id':args.release_id,'files':len(files),'archive_sha256':record['archive_sha256'],'deployment_unchanged':True}))
