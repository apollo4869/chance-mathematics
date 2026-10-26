"""Account for every translated block and formula; does not approve mathematical claims."""
from pathlib import Path
from collections import Counter
import hashlib, json, re, sys

ROOT=Path(__file__).resolve().parents[1]
math=re.compile(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)')
han=re.compile(r'[\u4e00-\u9fff]+')
labels=json.loads((ROOT/'translations/en/math-labels.json').read_text('utf-8'))
pairs=[('chapters/'+p.name,'chapters-en/'+p.name) for p in sorted((ROOT/'chapters').glob('*.md'))]
pairs += [('advanced/'+p.name,'advanced-en/'+p.name) for p in sorted((ROOT/'advanced').glob('*.md'))]
pairs += [('校订与证明补充.md','translations/en/proofs.md'),('延伸阅读与证明路线.md','translations/en/reading-routes.md'),('引用与配图来源.md','translations/en/references.md'),('写作约定与全书编排.md','translations/en/writing-rules.md')]
rows=[]
localize=lambda formula:han.sub(lambda m:labels[m[0]],formula)
blocks=lambda s:re.split(r'\n\s*\n',s.strip())
heads=lambda s:re.findall(r'^(#{1,6})\s',s,re.M)
targets=lambda s:re.findall(r'(?:\]\(|\b(?:src|href)=\")([^\s)\"]+)',s)
for source,target in pairs:
    sb=(ROOT/source).read_bytes();tb=(ROOT/target).read_bytes()
    s=sb.decode('utf-8').replace('\r\n','\n');t=tb.decode('utf-8').replace('\r\n','\n')
    assert not han.search(t),(target,'untranslated Chinese')
    assert '\ufffd' not in t,(target,'replacement character')
    a,b=blocks(s),blocks(t)
    assert len(a)==len(b),(target,'paragraph/block count',len(a),len(b))
    assert heads(s)==heads(t),(target,'heading levels')
    assert targets(s)==targets(t),(target,'references/assets')
    count=0
    for index,(before,after) in enumerate(zip(a,b),1):
        expected=Counter(localize(x) for x in math.findall(before));actual=Counter(math.findall(after))
        assert expected==actual,(target,'formula correspondence',index)
        count+=sum(expected.values())
    rows.append({'source':source,'translation':target,'source_sha256':hashlib.sha256(sb).hexdigest(),
                 'translation_sha256':hashlib.sha256(tb).hexdigest(),'blocks':len(a),'headings':len(heads(s)),
                 'formulas':count,'status':'FULL_BLOCK_AND_FORMULA_CORRESPONDENCE'})
manifest={'scope':'Complete English working translation; structural coverage is not semantic or academic final approval',
          'author_acceptance':'PENDING','mathematical_review':'SOURCE_REVIEW_STATUS_INHERITED_NOT_UPGRADED',
          'publication':False,'files':rows,'formulas':sum(x['formulas'] for x in rows)}
if '--record' in sys.argv:
    (ROOT/'translations/en/manifest.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
else:
    recorded=json.loads((ROOT/'translations/en/manifest.json').read_text('utf-8'))
    assert manifest==recorded,'Translation source or text changed; review and record a new translation manifest'
print(json.dumps({'translation':'PASS','files':len(rows),'blocks':sum(x['blocks'] for x in rows),
                  'formulas':manifest['formulas'],'author_review':'PENDING','publication':False}))
