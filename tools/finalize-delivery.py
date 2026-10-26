"""Collect review metadata and export Git diffs; never edits protected content."""
from pathlib import Path
import subprocess,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'reports'
def git(*args):return subprocess.check_output(['git','-c','core.quotePath=false','-C',str(ROOT),*args])
baseline=json.loads((ROOT/'baseline-manuscript.json').read_text(encoding='utf-8'))
origin=Path(baseline['source_root']);checks=[]
for rel,h in baseline['files'].items():
    checks.append({'file':rel,'source_sha256':hashlib.sha256((origin/rel).read_bytes()).hexdigest(),'import_sha256':hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),'git_blob_sha256':hashlib.sha256(git('show','HEAD:'+rel)).hexdigest(),'expected':h})
assert all(x['source_sha256']==x['import_sha256']==x['git_blob_sha256']==x['expected'] for x in checks)
(R/'protected-imports.json').write_text(json.dumps({'protected_files':len(checks),'byte_identical':True,'files':checks},ensure_ascii=False,indent=2),encoding='utf-8')
status={
 'content_integrity':json.loads((R/'content-integrity.json').read_text(encoding='utf-8'))['status'],
 'formula_rendering':json.loads((R/'formula-rendering.json').read_text(encoding='utf-8'))['status'],
 'mathematical_correctness':'PENDING_AUTHOR_REVIEW_NO_EDITS_APPLIED',
 'historical_authenticity':'PENDING_REVIEW',
 'initial_full_chat_equivalence':'UNVERIFIED',
 'web_quality':{'static':json.loads((R/'web-quality.json').read_text(encoding='utf-8'))['static_status'],'listed_http_browser_checks':'PASS','print_visual_review':'PENDING','file_protocol_browser_test':'BLOCKED_BY_BROWSER_URL_POLICY'},
 'production_deployments':0,'production_source_pushes':0,
 'policy':'No combined academic PASS/FAIL. Technical exit codes do not approve math, history or publication.'}
(R/'audit-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
base=git('rev-parse','2080f1a').decode().strip();head=git('rev-parse','HEAD').decode().strip()
for name,args in [('review.diff',['diff','--no-ext-diff','--no-color',base,head]),('review-stat.txt',['diff','--stat',base,head])]:
    (R/name).write_bytes(git(*args))
import_commit=git('rev-parse','37b41ff').decode().strip()
(R/'engineering.diff').write_bytes(git('diff','--no-ext-diff','--no-color',import_commit,head))
manuscript_diff=git('diff','--no-ext-diff','--no-color',import_commit,head,'--','chapters','assets','provenance','app.js','experiments.js','写作约定与全书编排.md','校订与证明补充.md','引用与配图来源.md')
(R/'manuscript.diff').write_bytes(manuscript_diff)
assert not manuscript_diff,'Migration changed protected manuscript after import'
(R/'git-review.json').write_text(json.dumps({'baseline_commit':base,'manuscript_import_commit':import_commit,'candidate_commit':head,'manuscript_diff_bytes':len(manuscript_diff),'branch':git('branch','--show-current').decode().strip(),'remote_pushes':0,'diff_policy':'Complete Git textual diff. Generated pages/ZIP and image blobs have binary diff summaries; independent manuscript and asset checks provide content evidence.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'protected_imports':len(checks),'byte_identical':True,'candidate':head,'diff_bytes':(R/'review.diff').stat().st_size}))
