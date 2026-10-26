"""Disposable fixture proves Markdown consumption and stale-output rejection."""
from pathlib import Path
import tempfile,shutil,subprocess,os,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
report={'fixture_only':True,'canonical_manuscripts_modified':False}
env=dict(os.environ);env['NODE_PATH']=str(ROOT/'node_modules' if (ROOT/'node_modules/markdown-it').exists() else ROOT.parent/'chance-mathematics-restored-v2/node_modules');env['PYTHONIOENCODING']='utf-8'
runtime=ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'
if runtime.exists():env['PYTHONPATH']=str(runtime)
scratch=ROOT.parent/'.stage1-fixtures';scratch.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='chance-stage1-canary-',dir=scratch) as temp:
    assert Path(temp).resolve().is_relative_to(scratch.resolve())
    fixture=Path(temp)/'candidate'
    shutil.copytree(ROOT,fixture,ignore=shutil.ignore_patterns('.git','node_modules','dist','reports','qa','*.zip'))
    p=fixture/'chapters/01-gambling.md';p.write_bytes(p.read_bytes()+b'\n\nSTAGE1_MARKDOWN_CANARY_20261025\n')
    # This baseline change exists only in disposable test data, to simulate a reviewed edit.
    baseline=json.loads((fixture/'baseline-manuscript.json').read_text(encoding='utf-8'));baseline['files']['chapters/01-gambling.md']=hashlib.sha256(p.read_bytes()).hexdigest();(fixture/'baseline-manuscript.json').write_text(json.dumps(baseline),encoding='utf-8')
    stale=subprocess.run([sys.executable,str(fixture/'build-chapters.py')],env=env,capture_output=True,text=True,encoding='utf-8')
    report['stale_generated_html_rejected']=stale.returncode!=0 and 'stale' in (stale.stdout+stale.stderr)
    build=subprocess.run([sys.executable,str(fixture/'build.py')],env=env,capture_output=True,text=True,encoding='utf-8')
    report['fixture_build_returncode']=build.returncode
    page=fixture/'dist/chapters/01-gambling.html'
    report['edited_markdown_reaches_html']=page.exists() and 'STAGE1_MARKDOWN_CANARY_20261025' in page.read_text(encoding='utf-8')
    if build.returncode:report['failure_details']=build.stderr
report['status']='PASS' if report['stale_generated_html_rejected'] and report['edited_markdown_reaches_html'] and report['fixture_build_returncode']==0 else 'FAIL'
(ROOT/'reports/pipeline-regression.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(report['status']!='PASS')
