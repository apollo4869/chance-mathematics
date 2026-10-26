// Independent audit renderer; never writes a manuscript or deploys a website.
const fs=require('node:fs'),path=require('node:path'),{createRequire}=require('node:module');
const request=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const req=request.engineProject?createRequire(path.join(request.engineProject,'package.json')):require;
const md=req('markdown-it')({html:true,typographer:false,linkify:false});
const {mathjax}=req('mathjax-full/js/mathjax.js'),{TeX}=req('mathjax-full/js/input/tex.js'),{SVG}=req('mathjax-full/js/output/svg.js'),{liteAdaptor}=req('mathjax-full/js/adaptors/liteAdaptor.js'),{RegisterHTMLHandler}=req('mathjax-full/js/handlers/html.js'),{AllPackages}=req('mathjax-full/js/input/tex/AllPackages.js');
const adaptor=liteAdaptor();RegisterHTMLHandler(adaptor);
const doc=mathjax.document('',{InputJax:new TeX({packages:AllPackages}),OutputJax:new SVG({fontCache:'none'})});
const escape=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const result=[];
for(const item of request.items){
 let text=fs.readFileSync(item.path,'utf8'),formulas=[];
 const put=(tex,display)=>{const id=formulas.length;formulas.push({tex,display});return display?'\n\nAUDITBLOCK'+id+'END\n\n':'AUDITINLINE'+id+'END'};
 if(item.syntax==='dollar'){
 text=text.replace(/\$\$([\s\S]*?)\$\$/g,(_,x)=>put(x,true));
 text=text.replace(/(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)/g,(_,x)=>put(x,false));
 }else text=text.replace(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g,(_,a,b)=>put(a??b,a!==undefined));
 let html=md.render(text);
 html=html.replace(/<p>AUDITBLOCK(\d+)END<\/p>/g,(_,n)=>'AUDITFORMULA'+n+'END');
 html=html.replace(/AUDIT(?:INLINE|BLOCK)(\d+)END/g,(_,n)=>'AUDITFORMULA'+n+'END');
 html=html.replace(/AUDITFORMULA(\d+)END/g,(_,n)=>{
 const f=formulas[+n];const render=item.syntax==='dollar'?adaptor.outerHTML(doc.convert(f.tex,{display:f.display})):'';
 return '<span class="audit-math" data-audit-tex="'+escape(f.tex.trim())+'">'+render+'</span>';
 });
 result.push({id:item.id,path:item.path,html,formulas});
}
fs.writeFileSync(request.output,JSON.stringify(result));
console.log(JSON.stringify({items:result.length,formulas:result.reduce((n,x)=>n+x.formulas.length,0)}));
