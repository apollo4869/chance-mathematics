"""Build only from protected Markdown. Never deploy or edit manuscripts."""
from pathlib import Path
import os,subprocess,sys,shutil,json,hashlib
ROOT=Path(__file__).resolve().parent
if (ROOT/'provenance/volume-reading.json').exists():
    subprocess.run([sys.executable,str(ROOT/'tools/check-volume-navigation.py'),'--prebuild'],cwd=ROOT,check=True)
if (ROOT/'publication/math-visuals.json').exists():
    subprocess.run([sys.executable,str(ROOT/'tools/check-math-visuals.py'),'--prebuild'],cwd=ROOT,check=True)
if (ROOT/'BOOK_MASTER_OUTLINE.md').exists():
    # Author planning is private and absent from sanitized public exports.
    # This guard validates ownership/dependencies; it never creates future chapters.
    subprocess.run([sys.executable,str(ROOT/'tools/check-book-plan.py'),'--prebuild'],cwd=ROOT,check=True)
if (ROOT/'tools/check-foundation-supplements.py').exists():
    subprocess.run([sys.executable,str(ROOT/'tools/check-foundation-supplements.py')],cwd=ROOT,check=True)
if (ROOT/'tools/academic_preservation.py').exists():
    subprocess.run([sys.executable,'-c','from tools.academic_preservation import verify_sources; print(verify_sources())'],cwd=ROOT,check=True)
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
commands += [[sys.executable,str(ROOT/'tools/build-chapter11-print.py')],[sys.executable,str(ROOT/'tools/catalog-assets.py')],[sys.executable,str(ROOT/'tools/prune-generated.py')],[sys.executable,str(ROOT/'tools/package-offline.py')]]
if len(json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'))['chapters'])>=13:
    commands.insert(-1,[sys.executable,str(ROOT/'tools/build-chapter-print.py'),'--chapter','13'])
if len(json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'))['chapters'])>=14:
    commands.insert(-1,[sys.executable,str(ROOT/'tools/build-chapter-print.py'),'--chapter','14'])
if len(json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'))['chapters'])>=15:
    commands.insert(-1,[sys.executable,str(ROOT/'tools/build-chapter-print.py'),'--chapter','15'])
for chapter_number in range(16,len(json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'))['chapters'])+1):
    commands.insert(-1,[sys.executable,str(ROOT/'tools/build-chapter-print.py'),'--chapter',str(chapter_number)])
for cmd in commands:
    subprocess.run(cmd,cwd=ROOT,env=env,check=True)
