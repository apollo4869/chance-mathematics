"""Create a new public-only source tree; canonical notes and Git history never leave."""
from pathlib import Path
import hashlib,json,subprocess,sys
from publication_policy import checked_public_sources
ROOT=Path(__file__).resolve().parents[1]
target=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'release/github-public-source'
if target.exists():raise SystemExit('Destination must be new; no existing files are removed: '+str(target))
target.mkdir(parents=True)
files=dict(checked_public_sources(ROOT))
for name,data in files.items():
    p=target/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
# Public engineering guidance contains no private prompts or inherited chat history.
(target/'AGENTS.md').write_bytes(('# Public book engineering\n\n'
    'Read LICENSE.md and publication/book.json. Do not edit chapter manuscripts without author approval. '
    'Keep author adoption, academic review and formal publication separate. '
    'Use the public-content allowlist; never add private notes, prompts or research. '
    'Build locally with python build.py. No automatic formal deployment.\n').encode())
protected={n:hashlib.sha256(b).hexdigest() for n,b in files.items() if n.startswith(('chapters/','chapters-en/','advanced/','advanced-en/','assets/'))}
manifest={'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),
          'scope':'Complete book chapters, proofs, references, assets and public engineering; private author notes excluded.',
          'files':protected,'formal_website_deployed':False}
(target/'docs').mkdir(exist_ok=True)
(target/'docs/PUBLIC_SOURCE_INTEGRITY.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'target':str(target),'source_files':len(files),'protected_book_files':len(protected),'private_records_exported':False},ensure_ascii=False))
