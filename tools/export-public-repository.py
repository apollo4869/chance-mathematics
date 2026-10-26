"""Export book manuscripts and engineering; keep private conversation archives local.

Never edits the canonical manuscripts or their local protection baseline.
The public baseline retains the original hashes for every included protected file.
Generated downloads must be rebuilt inside this clean export, never copied in.
"""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'release/github-public-source'
if target.exists():
    raise SystemExit('Destination must be new; existing files are never removed: ' + str(target))
target.mkdir(parents=True)
folders = {'chapters', 'chapters-en', 'advanced', 'advanced-en', 'translations', 'assets', 'tools', 'docs'}
metadata = {'provenance/build-inputs.json', 'provenance/charts.json'}
archive = 'archives/before-brownian-restructure/04-brownian.md'
paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode('utf-8').split('\0')
paths += ['tools/export-public-repository.py']
included = []
for name in sorted(set(filter(None, paths))):
    p = Path(name)
    top = len(p.parts) == 1 and (p.suffix in {'.md', '.py', '.json', '.css', '.js', '.yaml', '.txt', '.ps1'} or name in {'.gitignore', '.gitattributes'})
    if not (top or p.parts[0] in folders or name in metadata or name == archive):
        continue
    if name == 'docs/README-history-before-github.md':
        continue
    dest = target / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / name, dest)
    included.append(name)
baseline = json.loads((ROOT / 'baseline-manuscript.json').read_text('utf-8'))
original = baseline['files']
baseline['files'] = {p: h for p, h in original.items() if p in included}
baseline['source_root'] = 'public-source-snapshot'
baseline['author_policy'] = 'Public manuscripts and website source authorized 2026-10-26; no formal website deployment. No manuscript edits.'
baseline['public_export_scope'] = 'Original hashes retained for included book files. Private conversation and audit archives remain local; no claim of original-chat equivalence.'
baseline.pop('previous_baseline', None)
baseline.pop('previous_baseline_git_ref', None)
(target / 'baseline-manuscript.json').write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + '\n', 'utf-8')
readme = (target / 'README.md').read_text('utf-8').replace('| `provenance/`, `archives/` | 来源记录、保护基准及旧稿快照 |', '| `provenance/`, `archives/` | 构建所需图表数据与章节清单、完整旧第四章快照 |')
readme = readme.replace('此前工程说明完整保留于 [README 历史记录](docs/README-history-before-github.md)。', '公开副本只包含教材原稿与工程。早期聊天、来源对照档案和本机审计快照留在作者本地，不随原稿下载包公开。所有现行中英文正文、证明与图片完整保留；公开保护清单沿用相应原始文件哈希。')
(target / 'README.md').write_text(readme, 'utf-8')
protected = {}
for name in included:
    if name.startswith(('chapters/', 'chapters-en/', 'advanced/', 'advanced-en/', 'translations/', 'assets/')):
        digest = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        assert hashlib.sha256((target / name).read_bytes()).hexdigest() == digest, name
        protected[name] = digest
(target / 'docs/PUBLIC_SOURCE_INTEGRITY.json').write_text(json.dumps({
    'source_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
    'scope': 'Complete bilingual book files and independent assets; private chat archives excluded.',
    'files': protected,
    'formal_website_deployed': False
}, ensure_ascii=False, indent=2) + '\n', 'utf-8')
print(json.dumps({'target': str(target), 'source_files': len(included), 'protected_book_files': len(protected), 'protected_hashes_inherited': len(baseline['files']), 'private_archives_exported': False}, ensure_ascii=False))
