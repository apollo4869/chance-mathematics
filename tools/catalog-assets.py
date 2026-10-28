"""Export independent assets and per-occurrence migration status; no prose edits."""
from pathlib import Path
import json,re,hashlib,sys,shutil
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
sha=lambda b:hashlib.sha256(b).hexdigest()
dist=ROOT/'dist';registry=[]
formulas=json.loads((ROOT/'build/formulas.json').read_text(encoding='utf-8'))
for section in dict.fromkeys(f['section'] for f in formulas):
    path=dist/'assets/formulas'/f'{section}.json';path.parent.mkdir(exist_ok=True)
    fs=[f for f in formulas if f['section']==section];path.write_text(json.dumps(fs,ensure_ascii=False,indent=2),encoding='utf-8')
    registry.append({'type':'formula-source','section':section,'source':'Markdown LaTeX environments','output':path.relative_to(dist).as_posix(),'count':len(fs),'status':'COPIED_TEX_TO_INDEPENDENT_SIDECAR','mathematical_correctness':'PENDING_REVIEW'})
charts=json.loads((ROOT/'provenance/charts.json').read_text(encoding='utf-8'))
inputs=json.loads((ROOT/'provenance/build-inputs.json').read_text(encoding='utf-8'))
units=[(p,'chapter-'+str(int(p.name[:2])),dist/'chapters'/p.with_suffix('.html').name) for p in sorted((ROOT/'chapters').glob('*.md'))]
units.extend((ROOT/m['file'],m['id'],dist/'advanced'/(m['slug']+'.html')) for m in inputs.get('advanced_modules',[]))
for chapter,section,page in units:
    text=chapter.read_text(encoding='utf-8')
    soup=BeautifulSoup(page.read_text(encoding='utf-8'),'html.parser').find('section',id=section)
    # Author-written figures use HTML for captions/alt text; catalogue their
    # assets just as Markdown images, without recording the same source twice.
    image_sources=list(dict.fromkeys(
        re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text)
        +re.findall(r'<img\b[^>]*\bsrc="([^"]+)"',text)))
    for src in image_sources:
        source=(chapter.parent/src).resolve();out=(dist/source.relative_to(ROOT)) if source.is_relative_to(ROOT/'assets/visuals') else dist/'assets/images'/source.name
        registry.append({'type':'image','section':section,'source':source.relative_to(ROOT).as_posix(),'output':out.relative_to(dist).as_posix(),'source_sha256':sha(source.read_bytes()),'output_sha256':sha(out.read_bytes()),'status':'BYTE_IDENTICAL' if source.read_bytes()==out.read_bytes() else 'FAIL','history_and_license':'PENDING_REVIEW'})
    for i,svg in enumerate(re.findall(r'<svg\b[\s\S]*?</svg>',text),1):
        out=dist/'assets/diagrams'/f'{section}-{i}.svg';out.parent.mkdir(exist_ok=True);out.write_text(svg,encoding='utf-8')
        registry.append({'type':'inline-diagram','section':section,'output':out.relative_to(dist).as_posix(),'status':'PRESERVED_INLINE_AND_EXPORTED','source_sha256':sha(svg.encode())})
    figures=soup.select('figure.chart')
    for chart_id,figure in zip(re.findall(r'data-chart="(\d+)"',text),figures):
        out=dist/'assets/charts'/f'chart-{chart_id}.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(charts[int(chart_id)],ensure_ascii=False,indent=2),encoding='utf-8')
        svg=out.with_suffix('.svg');svg.write_text(str(figure.find('svg')),encoding='utf-8')
        registry.append({'type':'numeric-chart','section':section,'source':f'provenance/charts.json#{chart_id}','output':out.relative_to(dist).as_posix(),'svg':svg.relative_to(dist).as_posix(),'status':'DATA_AND_SVG_EXPORTED','math_validation':'SEPARATE_MODEL_CHECKS'})
    for widget in re.findall(r'data-widget="([^"]+)"',text):
        target=dist/'assets/interactive';target.mkdir(exist_ok=True)
        for name in ['experiments.js','app.js']:shutil.copyfile(ROOT/name,target/name)
        registry.append({'type':'interaction','section':section,'widget':widget,'source':['experiments.js','app.js'],'output':['assets/interactive/experiments.js','assets/interactive/app.js'],'runtime':'shared hashed experiment/app scripts linked by chapter HTML','status':'SOURCE_AND_RUNTIME_PRESERVED','behavior_check':'SEPARATE_BROWSER_AND_MODEL_REPORT'})
    for ref in re.findall(r'\]\(#(ref-[^)]+)\)',text):registry.append({'type':'citation','section':section,'source_anchor':ref,'output':'references.html#'+ref,'status':'LINK_MIGRATED','historical_authenticity':'PENDING_REVIEW'})
(ROOT/'reports').mkdir(exist_ok=True)
if (ROOT/'publication/math-visuals.json').exists():
    figures=json.loads((ROOT/'publication/math-visuals.json').read_text('utf8'))['figures']
    for row in figures:
        for lang in ['zh','en']:
            for fmt in ['svg','pdf']:
                name='assets/visuals/print/'+row['id']+'.'+lang+'.'+fmt
                assert (ROOT/name).read_bytes()==(dist/name).read_bytes(),name
                registry.append({'type':'publication-math-figure','section':'chapter-'+str(row['chapter']),'stable_id':row['id'],'language':lang,'format':fmt,'source':'assets/visuals/math-model.js','parameters':'assets/visuals/spec.json','caption_and_placement':'publication/math-visuals.json','output':name,'sha256':sha((ROOT/name).read_bytes()),'status':'VECTOR_SOURCE_BYTE_IDENTICAL','mathematical_correctness':'MODEL_INVARIANTS_CHECKED_NOT_FINAL_REVIEW'})
    registry.append({'type':'interaction','section':'chapter-7','widget':'typewriter','stable_id':'experiment-typewriter','source':['assets/visuals/math-model.js','assets/visuals/typewriter.js'],'static_alternative':'assets/visuals/print/typewriter.zh.svg','status':'DETERMINISTIC_SHARED_MODEL','behavior_check':'SEPARATE_BROWSER_AND_MODEL_CHECK'})
(ROOT/'reports/asset-migration.json').write_text(json.dumps({'assets':registry,'policy':'Asset migration status does not certify math, historical truth, or license.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'asset_occurrences':len(registry),'types':{t:sum(r['type']==t for r in registry) for t in sorted(set(r['type'] for r in registry))}}))
