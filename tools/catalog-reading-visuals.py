"""Catalogue actual reading-site visual files; do not regenerate any artwork."""
from pathlib import Path
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];SITE=R/'work/reading-acceptance/site';O=R/'reports/full-book-reading-2026-11-07'

def main():
 refs=json.loads((O/'visual-resource-inventory.json').read_text('utf8'))['resources'];used={x['path']:x['used_by'] for x in refs};rows=[]
 for root in [SITE/'assets/visuals',SITE/'assets/images']:
  for p in sorted(root.rglob('*')):
   if not p.is_file():continue
   rel=p.relative_to(SITE).as_posix();parts=p.relative_to(root).parts
   match=re.match(r'((?:P|V|E)[0-9]+[A-Z]?)',p.name)
   category='adopted explanatory figure/state/style/runtime' if 'explanatory-' in rel else 'retained engineering/helper figure or mathematical interaction' if root.name=='visuals' else 'retained historical/illustrative image'
   rows.append(dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),category=category,group=match[1] if match else '',file_type=p.suffix,referenced_by_initial_HTML=bool(used.get(rel)),initial_HTML_pages=used.get(rel,[]),scope='State resources not referenced by initial HTML may be selected by the unchanged interaction code.'))
 data=dict(version='2026-11-07-reading-acceptance',groups=45,group_languages=90,artwork_redesigned=False,final_author_aesthetics='open',physical_devices='open',native_pdf='open',independent_expert_mathematics='open',files=rows)
 (O/'all-visual-assets.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 with (O/'all-visual-assets.csv').open('w',encoding='utf-8-sig',newline='') as f:
  cols=['path','bytes','sha256','category','group','file_type','referenced_by_initial_HTML'];w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(rows)
 print(json.dumps(dict(visual_files=len(rows),adopted_groups=45,initial_HTML_referenced=sum(x['referenced_by_initial_HTML'] for x in rows)),ensure_ascii=False))

if __name__=='__main__':main()
