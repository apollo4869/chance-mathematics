"""Build only from protected Markdown. Never deploy or edit manuscripts."""
from pathlib import Path
import os,subprocess,sys,shutil,json,hashlib
ROOT=Path(__file__).resolve().parent
node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
env=dict(os.environ)
if not (ROOT/'node_modules/markdown-it').exists():
    fallback=ROOT.parent/'chance-mathematics-restored-v2/node_modules'
    if fallback.exists():env['NODE_PATH']=str(fallback)
baseline=json.loads((ROOT/'baseline-manuscript.json').read_text(encoding='utf-8'))
failures=[p for p,h in baseline['files'].items() if not (ROOT/p).exists() or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
if failures:raise SystemExit('Protected working manuscript changed; author review required: '+str(failures))
commands=[[node,str(ROOT/'tools/render-book.cjs')],[sys.executable,str(ROOT/'build-chapters.py')]]
if json.loads((ROOT/'site-links.json').read_text('utf-8')).get('english_content')=='full_manuscript':
    commands += [[sys.executable,str(ROOT/'tools/check-translation.py')],[node,str(ROOT/'tools/render-book.cjs'),'--english'],[sys.executable,str(ROOT/'build-chapters.py'),'--english']]
commands += [[sys.executable,str(ROOT/'tools/catalog-assets.py')],[sys.executable,str(ROOT/'tools/package-offline.py')]]
for cmd in commands:
    subprocess.run(cmd,cwd=ROOT,env=env,check=True)
