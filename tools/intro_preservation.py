"""Exact additive Chapter11 introduction; every previously written byte stays intact."""
from pathlib import Path
import json,hashlib,subprocess,re
from functools import lru_cache
from copy import deepcopy
ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'provenance/authorized-chapter11-intro.json'
POLISH=ROOT/'provenance/authorized-opening-polish.json'

def before_polish(name):
    current=(ROOT/name).read_bytes()
    if not POLISH.exists():return current
    record=json.loads(POLISH.read_text('utf8'))
    if name not in record['files']:return current
    item=record['files'][name];old=(ROOT/record['archive']/name).read_bytes()
    assert hashlib.sha256(old).hexdigest()==item['before_sha256']
    assert old==subprocess.check_output(['git','show',record['snapshot_ref']+':'+name],cwd=ROOT)
    expected=old.decode()
    for patch in item['patches']:
        assert expected.count(patch['before'])==1
        expected=expected.replace(patch['before'],patch['after'],1)
    assert expected.encode()==current,('unapproved change beyond opening polish',name)
    math=lambda b:re.findall(rb'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)',b)
    assert math(old)==math(current),'mathematical formula altered'
    marker=item['unchanged_from'].encode()
    assert old.split(marker,1)[1]==current.split(marker,1)[1],'11.2 onward changed'
    return old

@lru_cache(maxsize=2)
def old_first_section(name):
    from bs4 import BeautifulSoup
    folder='en/chapters' if name.startswith('chapters-en/') else 'chapters'
    raw=subprocess.check_output(['git','show','snapshot/before-chapter11-introduction-2026-10-26:dist/'+folder+'/11-characteristic-functions.html'],cwd=ROOT)
    return BeautifulSoup(raw,'html.parser').select_one('#chapter-11-unit-1')
def before_introduction(name):
    current=before_polish(name)
    if not LEDGER.exists():return current
    record=json.loads(LEDGER.read_text('utf8'))
    if name not in record['files']:return current
    item=record['files'][name];old=(ROOT/record['archive']/name).read_bytes()
    assert hashlib.sha256(old).hexdigest()==item['before_sha256']
    assert old==subprocess.check_output(['git','show',record['snapshot_ref']+':'+name],cwd=ROOT)
    assert old.count(item['following_heading'].encode())==1
    expected=old.replace(item['following_heading'].encode(),(item['introduction']+item['following_heading']).encode(),1)
    assert current==expected,('edit beyond authorized introduction',name)
    assert re.findall(rb'^## 11\.\d+ .+$',old,re.M)==re.findall(rb'^## 11\.\d+ .+$',current,re.M)
    assert old.split(item['following_heading'].encode(),1)[1]==current.split(item['following_heading'].encode(),1)[1]
    return old
def remove_introduction_nodes(fragment):
    """Only the numbered new paragraphs, independently checked against the ledger."""
    nodes=list(fragment.select('p[id^="chapter-11-intro-p"]'))
    if nodes and POLISH.exists() and len(nodes)==3:
        record=json.loads(POLISH.read_text('utf8'));compact=lambda s:re.sub(r'\s+','',s)
        actual=[compact(n.get_text()) for n in nodes]
        name=next((name for name,item in record['files'].items() if [compact(b.replace('[第三章](03-normal.md)','第三章').replace('[Chapter 3](03-normal.md)','Chapter 3')) for b in re.split(r'\n\s*\n',item['opening'].strip())]==actual),None)
        assert name,'unapproved polished opening DOM';before_polish(name)
        for alias in list(fragment.select('.opening-retired-anchor')):alias.decompose()
        unit=fragment.select_one('#chapter-11-unit-1')
        assert unit is not None
        unit.clear();unit.extend(deepcopy(old_first_section(name).contents))
        for p in nodes:
            following=p.next_sibling
            if isinstance(following,str) and not following.strip():following.extract()
            p.decompose()
        return fragment
    if nodes and LEDGER.exists():
        record=json.loads(LEDGER.read_text('utf8'));compact=lambda s:re.sub(r'\s+','',s.replace('**',''))
        actual=[compact(p.get_text()) for p in nodes]
        options={n:[compact(b) for b in re.split(r'\n\s*\n',v['introduction'].strip())] for n,v in record['files'].items()}
        name=next((n for n,texts in options.items() if texts==actual),None)
        assert name and [p['id'] for p in nodes]==['chapter-11-intro-p'+str(i) for i in range(1,8)],'unapproved introduction DOM'
        before_introduction(name)
    for p in nodes:
        following=p.next_sibling
        if isinstance(following,str) and not following.strip():following.extract()
        p.decompose()
    return fragment
