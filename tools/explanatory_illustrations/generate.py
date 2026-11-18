"""Generate the reviewed pilots and the first volume-V explanatory batch only."""
from pathlib import Path
import json,shutil
from . import pilot_shapes as pilots
from . import volume5
ROOT=Path(__file__).resolve().parents[2];ASSETS=ROOT/'assets/visuals/explanatory-v1'
def main():
 ASSETS.mkdir(exist_ok=True,parents=True);rows=[]
 for code,meta in pilots.META.items():
  for lang in ['zh','en']:
   html,condition,panes=pilots.figure(code,lang);pilots.print_svg(code,lang,condition,panes)
   rows.append(dict(id=code,lang=lang,slug=meta[0],section=meta[1],title=meta[2 if lang=='zh' else 3],html=html,condition=condition,category='adopted-pilot',book_preview=code=='P01',status='visual working draft adopted; local precision pending review' if code in ['P02','P05'] else 'visual working draft adopted'))
 for code,meta in volume5.META.items():
  for lang in ['zh','en']:
   html,condition=volume5.figure(code,lang)
   rows.append(dict(id=code,lang=lang,slug=meta[0],section=meta[1],title=meta[2 if lang=='zh' else 3],html=html,condition=condition,category='new-explanatory-gap',book_preview=True,status='author visual review pending'))
 for name in ['figures.css','interactions.js']:shutil.copyfile(Path(__file__).parent/name,ASSETS/name)
 manifest={'schema':1,'scope':'Four priority additions in chapters 31–40; P01 adopted, P02/P05 local precision only; remaining pilots preserved','canonical_manuscript_changes':False,'automatic_formal_site_injection':False,'figures':rows}
 (ROOT/'publication/explanatory-figures-working.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Generated nine bilingual working groups; canonical site not rebuilt.')
if __name__=='__main__':main()
