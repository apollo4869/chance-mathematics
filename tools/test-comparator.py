"""Load comparator functions only; alter small fixtures, not real manuscripts."""
from pathlib import Path
import ast,re,json,hashlib,sys,base64,unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
sha=lambda b:hashlib.sha256(b).hexdigest();canon=lambda s:re.sub(r'\s+','',s)
tree=ast.parse((ROOT/'tools/check-stage1.py').read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='inspect'],type_ignores=[]),'<comparator>','exec'))
base='<h2>故事标题</h2><p>史实甲</p><p>推导乙<span class="formula" data-tex="x^2">svg</span></p><div data-widget="walk"></div><img src="data:image/png;base64,YWJj">'
checks=[]
for name,modified,field in [('deleted-paragraph',base.replace('<p>史实甲</p>',''),'text'),('reordered-prose',base.replace('史实甲','TEMP').replace('推导乙','史实甲').replace('TEMP','推导乙'),'text'),('math-change',base.replace('x^2','x^3'),'formulas'),('heading-level',base.replace('h2','h3'),'headings'),('widget-missing',base.replace('data-widget','data-hidden'),'widgets'),('image-change',base.replace('YWJj','YWJk'),'images')]:
    checks.append({'test':name,'detected':inspect(base,ROOT)[field]!=inspect(modified,ROOT)[field]})
checks.append({'test':'CRLF-only-normalization','detected':inspect(base.replace('x^2','x\r\ny'),ROOT)['formulas']==inspect(base.replace('x^2','x\ny'),ROOT)['formulas']})
result={'status':'PASS' if all(x['detected'] for x in checks) else 'FAIL','fixture_only':True,'checks':checks}
(ROOT/'reports/comparator-regression.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False));raise SystemExit(result['status']!='PASS')
