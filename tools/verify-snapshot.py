"""Verify an immutable publication manifest and its separate source archive."""
from pathlib import Path
import hashlib,json,sys,zipfile
p=Path(sys.argv[1]);record=json.loads(p.read_text('utf-8'));archive=p.parent/record['archive_file']
assert hashlib.sha256(archive.read_bytes()).hexdigest()==record['archive_sha256'],'Archive changed'
with zipfile.ZipFile(archive) as z:
    assert set(z.namelist())==set(record['files'])|{'contents-sha256.json'},'Unexpected file'
    assert json.loads(z.read('contents-sha256.json'))==record['files']
    for name,digest in record['files'].items():
        assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
        assert name.startswith(('chapters/','chapters-en/','advanced/','advanced-en/')) or name in {'校订与证明补充.md','引用与配图来源.md','延伸阅读与证明路线.md'}
print(json.dumps({'snapshot':'PASS','release_id':record['release_id'],'files':len(record['files'])}))
