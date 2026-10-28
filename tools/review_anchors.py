"""Keep old formula links stable when a review adds inline proof details."""
import json
from collections import defaultdict
from pathlib import Path

def preserve_targeted(soup,section,search,english=False):
    config=Path(__file__).resolve().parents[1]/'publication/targeted16-20-review-anchors.json'
    if not config.exists():return
    item=json.loads(config.read_text('utf8'))['sections'].get(section)
    if not item:return
    old=item['formulas']['en' if english else 'zh'];used=set();mapping={};added=0
    for formula in soup.select('.formula'):
        parent=formula.find_parent(['p','h1','h2','h3','li','td'])
        context='display' if 'display' in formula.get('class',[]) else parent.get('id') if parent else section
        row=next((r for r in old if r['id'] not in used and r['context']==context and r['tex']==formula['data-tex'].replace('\r\n','\n')),None)
        if row:target=row['id'];used.add(target)
        else:added+=1;target=section+'-review-formula-'+str(added)
        mapping[formula['id']]=target;formula['id']=target
    for row in old:
        if row['id'] in used:continue
        # Removed repeated inline variable notation still has a nearby bookmark;
        # the original displayed proof equations themselves must remain intact.
        assert row['context']!='display',('Original proof equation lost',section,row['id'])
        alias=soup.new_tag('span',id=row['id']);alias['aria-hidden']='true';alias['class']='bookmark-alias'
        parent=soup.find(id=row['context']) or soup.select_one('.book-section') or soup
        parent.insert(0,alias)
    for item in search:
        if item['section']==section and item['id'] in mapping:item['id']=mapping[item['id']]

def preserve(soup,section,search,english=False):
    if section=='chapter-17' and (Path(__file__).resolve().parents[1]/'publication/chapter17-revision-anchors.json').exists():
        preserve_recreated20(soup,section,search,english,chapter=17)
        return
    if section=='chapter-20' and (Path(__file__).resolve().parents[1]/'publication/chapter20-recreation-anchors.json').exists():
        preserve_recreated20(soup,section,search,english)
        return
    preserve_targeted(soup,section,search,english)
    preserve_development(soup,section,search,english)
    root=Path(__file__).resolve().parents[1]
    config=root/'publication/chapter14-review-anchors.json'
    if section!='chapter-14' or not config.exists():return
    old=json.loads(config.read_text('utf8'))['formulas']['en' if english else 'zh']
    grouped=defaultdict(list)
    for row in old:grouped[row['context']].append(row)
    used=defaultdict(int);display=0;added=0;mapping={}
    for formula in soup.select('.formula'):
        if 'display' in formula.get('class',[]):
            display+=1;context='display:'+str(display)
        else:
            parent=formula.find_parent('p');assert parent and parent.get('id')
            context=parent['id']
        ordinal=used[context];rows=grouped[context]
        if ordinal<len(rows) and rows[ordinal]['tex']==formula['data-tex']:
            target=rows[ordinal]['id'];used[context]+=1
        else:
            added+=1;target='chapter-14-review-formula-'+str(added)
        mapping[formula['id']]=target;formula['id']=target
    assert all(used[k]==len(rows) for k,rows in grouped.items()),'A pre-review formula was lost, reordered or changed'
    assert len(set(mapping.values()))==len(mapping),'Formula-anchor collision'
    for item in search:
        if item['section']==section and item['id'] in mapping:item['id']=mapping[item['id']]

def preserve_recreated20(soup,section,search,english=False,chapter=20):
    charter=(Path(__file__).resolve().parents[1]/'publication/chapter17-charter-anchors.json').exists()
    filename='chapter20-recreation-anchors.json' if chapter==20 else 'chapter17-charter-anchors.json' if charter else 'chapter17-revision-anchors.json'
    config=Path(__file__).resolve().parents[1]/'publication'/filename
    record=json.loads(config.read_text('utf8'))['languages']['en' if english else 'zh']
    used=set();mapping={};added=0
    for f in soup.select('.formula'):
        tex=f['data-tex'].replace('\r\n','\n').strip();display='display' in f.get('class',[])
        row=next((r for r in record['formulas'] if r['id'] not in used and r['tex'].replace('\r\n','\n').strip()==tex and r['display']==display),None)
        if row:target=row['id'];used.add(target)
        else:added+=1;target=('chapter-20-recreation-formula-' if chapter==20 else 'chapter-17-charter-formula-' if charter else 'chapter-17-revision-formula-')+str(added)
        mapping[f['id']]=target;f['id']=target
    if chapter==17 and charter:
        import copy
        used_paragraphs=set();new_paragraph=0
        for p in soup.select('p[id]'):
            clone=copy.copy(p)
            for f in clone.select('.formula'):
                f.replace_with('MATH'+('BLOCK' if 'display' in f.get('class',[]) else 'INLINE')+json.dumps(f['data-tex'].strip(),ensure_ascii=False))
            signature=clone.get_text(' ',strip=True)
            row=next((r for r in record['paragraphs'] if r['id'] not in used_paragraphs and r['signature']==signature),None)
            if row:target=row['id'];used_paragraphs.add(target)
            else:new_paragraph+=1;target='chapter-17-charter-p'+str(new_paragraph)
            mapping[p['id']]=target;p['id']=target
    # Reorganized or deduplicated statements keep an old bookmark at their
    # corresponding new proof. An alias never pretends to be another equation.
    existing={n['id'] for n in soup.select('[id]')}
    for row in record['anchors']:
        if row['id'] in existing:continue
        target=soup.find(id=row['target']);assert target,('Legacy target missing',chapter,row)
        alias=soup.new_tag('span',attrs={'id':row['id'],'class':'bookmark-alias','aria-hidden':'true'})
        target.insert_after(alias);existing.add(row['id'])
    for item in search:
        if item['section']==section and item['id'] in mapping:item['id']=mapping[item['id']]

def preserve_development(soup,section,search,english=False):
    config=Path(__file__).resolve().parents[1]/'publication/development16-20-anchors.json'
    if not config.exists():return
    record=json.loads(config.read_text('utf8'))['sections'].get(section)
    if not record:return
    old=record['en' if english else 'zh']['formulas'];used=set();mapping={};added=0
    # Exact existing formulas remain in source order. New formulas receive a
    # separate namespace and do not consume a historical formula bookmark.
    for f in soup.select('.formula'):
        tex=f['data-tex'].replace('\r\n','\n');display='display' in f.get('class',[])
        parent=f.find_parent('p');context='display' if display else parent.get('id') if parent else section
        row=next((r for r in old if r['id'] not in used and r['context']==context and r['tex']==tex and r['display']==display),None)
        if row:
            target=row['id'];used.add(target)
        else:added+=1;target=section+'-development-formula-'+str(added)
        mapping[f['id']]=target;f['id']=target
    assert len(used)==len(old),('Existing formula removed or changed by development',section,len(used),len(old))
    for item in search:
        if item['section']==section and item['id'] in mapping:item['id']=mapping[item['id']]
