"""Package only public book materials; canonical private records stay untouched."""
from pathlib import Path
import zipfile,json,re
from publication_policy import checked_public_sources
from volume_navigation import records as volume_records,label as volume_label
ROOT=Path(__file__).resolve().parents[1];dist=ROOT/'dist';downloads=dist/'downloads';downloads.mkdir(exist_ok=True)
def write_zip(target,files):
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for name,data in sorted(files):
            info=zipfile.ZipInfo(name,date_time=(2026,10,26,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,data)
source=checked_public_sources(ROOT)
if (ROOT/'publication/math-visuals.json').exists():
    selection=[(n,b) for n,b in source if n.startswith('assets/visuals/') or n in {'VISUAL_STYLE_GUIDE.md','experiments.js','publication/math-visuals.json','publication/visual-captions.zh.md','publication/visual-captions.en.md','tools/generate-math-visuals.py','tools/generate-local-clt-figure.py','tools/generate-array-budget-figure.py','tools/test-math-visuals.cjs'}]
    write_zip(downloads/'math-visuals-batch1.zip',selection)
reader_sources=dict(source);inputs=json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'))
for en,target in [(False,'manuscript.md'),(True,'manuscript-en.md')]:
    names=['publication/writing-principles.'+('en' if en else 'zh')+'.md']
    names += [('chapters-en/' if en else 'chapters/')+n for n in inputs['chapters']]
    names += ['translations/en/proofs.md' if en else '校订与证明补充.md','translations/en/reading-routes.md' if en else '延伸阅读与证明路线.md']
    names += [('advanced-en/' if en else 'advanced/')+Path(m['file']).name for m in inputs.get('advanced_modules',[])]
    names += ['translations/en/references.md' if en else '引用与配图来源.md']
    names += [('foundations-en/' if en else 'foundations/')+Path(m['file']).name for m in inputs.get('supporting_proofs',[])]
    title='# The Mathematics of Chance\n\nFull English working manuscript' if en else '# 偶然的数学\n\n完整中文工作稿'
    parts=[];lang='en' if en else 'zh';chapter_folder='chapters-en/' if en else 'chapters/'
    for n in names:
        for v in volume_records():
            if v.get('opening') and v['range'][0]<=len(inputs['chapters']) and n==chapter_folder+inputs['chapters'][v['range'][0]-1]:
                prose=reader_sources[v['opening'][lang]].decode('utf8') if v['opening'][lang] else ''
                parts.append('# '+volume_label(v,en)+'\n\n'+v['theme_'+lang]+'\n\n'+prose)
        parts.append(reader_sources[n].decode('utf8'))
        for v in volume_records():
            if v.get('ending',{}).get(lang) and v['range'][1]<=len(inputs['chapters']) and n==chapter_folder+inputs['chapters'][v['range'][1]-1]:
                parts.append('# '+v['ending']['title_'+lang]+'\n\n'+reader_sources[v['ending'][lang]].decode('utf8'))
        # Volume II's ending already occurs inside canonical Chapter 14: never duplicate it.
    combined=title+'\n\n'+ '\n\n---\n\n'.join(parts)+'\n'
    (downloads/target).write_bytes(combined.encode())
(downloads/'04-brownian-before-restructure.md').write_bytes((ROOT/'archives/before-brownian-restructure/04-brownian.md').read_bytes())
write_zip(downloads/'editable-manuscript.zip',source)
if (downloads/'manuscript-en.md').exists():
    english_source=[(n,b) for n,b in source if n.startswith(('chapters-en/','advanced-en/','foundations-en/','volumes-en/','translations/en/','assets/','licenses/','publication/'))
                    or n in {'LICENSE.md','CONTRIBUTING.md','CITATION.cff'}]
    english_source.append(('The-Mathematics-of-Chance.md',(downloads/'manuscript-en.md').read_bytes()))
    write_zip(downloads/'english-manuscript.zip',english_source)
files=[]
for p in dist.rglob('*'):
    if not p.is_file() or p.name=='complete-offline.zip':continue
    data=p.read_bytes()
    if p.suffix=='.html':
        data=re.sub(r'<a\b[^>]*href="[^"]*downloads/complete-offline\.zip"[^>]*>[\s\S]*?</a>','',data.decode('utf-8')).encode('utf-8')
    files.append((p.relative_to(dist).as_posix(),data))
files.extend(('editable-source/'+n,b) for n,b in source)
write_zip(downloads/'complete-offline.zip',files)
print(json.dumps({'offline_files':len(files),'source_files':len(source),'private_records_exported':False,'source_kind':'Full working book manuscripts; private author notes excluded'}))
