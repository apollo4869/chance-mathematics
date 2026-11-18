// Local event-handler unit test with a small DOM adapter, NOT a browser/layout test.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'../..'),base='assets/visuals/explanatory-volume7-v1';
const rows=JSON.parse(fs.readFileSync(path.join(root,'publication/explanatory-volume7-batch1-working.json'),'utf8')).figures;
const all=[];let events=0;
for(const r of rows){
 const buttons=[...r.html.matchAll(/<button[^>]*data-(\w+)="([^"]+)"[^>]*>/g)].map(m=>({dataset:{[m[1]]:m[2]},attributes:{},setAttribute(k,v){this.attributes[k]=v;},closest(){return this;}}));
 const img={},source={},out={},label={},chain={},range={value:'10',addEventListener(k,fn){this[k]=fn;}};
 const picture={querySelector:q=>q==='source'?source:img},callbacks={};
 const f={dataset:{v7:r.id},lang:r.lang,querySelector(q){return {'[data-v7-result]':out,'[data-v7-picture]':picture,'[data-chain-scene]':chain,'[data-height-label]':label,'[data-height]':r.id==='V51'?range:null}[q];},querySelectorAll:()=>buttons,contains:b=>buttons.includes(b),addEventListener(k,fn){callbacks[k]=fn;}};
 all.push({r,f,buttons,img,source,out,label,range,chain,callbacks});
}
vm.runInNewContext(fs.readFileSync(path.join(root,base,'interactions.js'),'utf8'),{document:{readyState:'complete',querySelectorAll:()=>all.map(a=>a.f)}});
function valid(a){assert.equal(a.f.dataset.v7Ready,'true');assert.ok(a.out.textContent.length>12);for(const url of [a.img.src,a.source.srcset])assert.ok(fs.existsSync(path.join(root,url.replace(/^\//,''))),url);assert.match(a.img.src,/-desktop\.svg$/);assert.match(a.source.srcset,/-mobile\.svg$/);}
for(const a of all){
 valid(a);
 for(const b of a.buttons){const previous=Number(a.f.dataset.v7Sequence);a.callbacks.click({target:b});events++;valid(a);assert.equal(Number(a.f.dataset.v7Sequence),previous+1);assert.equal(b.attributes['aria-pressed'],'true');}
 function click(k,v){const b=a.buttons.find(b=>b.dataset[k]===v);assert.ok(b);a.callbacks.click({target:b});events++;valid(a);}
 if(a.r.id==='V48'){click('mode','copied');assert.match(a.out.textContent,/0\.3679/);assert.match(a.out.textContent,/V未使用|V is unused/);click('mode','independent');assert.match(a.out.textContent,/0\.1353/);assert.doesNotMatch(a.out.textContent,/V未使用|V is unused/);}
 if(a.r.id==='V49'){click('space','open');click('window','2');assert.match(a.out.textContent,/不是|not/);click('space','real');assert.match(a.out.textContent,/∞/);click('window','1');assert.match(a.out.textContent,/32767\/32768/);}
 if(a.r.id==='V51'){for(const c of ['0','1','2']){click('case',c);const labels=a.r.lang==='zh'?['高度相同','高度分离','高度重叠']:['Same heights','Separated heights','Overlapping heights'];assert.ok(a.out.textContent.includes(labels[Number(c)]));assert.ok(a.out.textContent.endsWith(['=2/5','=0','=1/4'][Number(c)]));for(let u=0;u<=20;u++){a.range.value=String(u);a.range.input();events++;valid(a);assert.equal(a.f.dataset.v7State,`${c}-${u}`);}}assert.equal(a.label.textContent,'1');assert.match(a.out.textContent,/7\/10/);}
 if(a.r.id==='V52'){click('tree','A');click('vertex','3');assert.match(a.out.textContent,/b=4/);click('tree','B');assert.match(a.out.textContent,/b=5/);}
 if(a.r.id==='V53'){click('cut','3');assert.match(a.out.textContent,/第3步|step 3/);click('chain','5');assert.ok(fs.existsSync(path.join(root,a.chain.src.replace(/^\//,''))));click('cut','1');assert.match(a.out.textContent,/第5步|step 5/);}
}
const record={scope:'Actual runtime under a local DOM adapter: no browser engine, visual rendering, accessibility tree or pointer interaction is verified.',fragments:all.length,event_transitions:events,status:'passed unit checks',real_browser:'blocked: Local browser use is disabled in Work settings'};
const recordDir=process.env.V7_CHECK_OUTPUT_DIR||path.join(root,'reports/volume7-visual-batch1-2026-11-06');fs.mkdirSync(recordDir,{recursive:true});
fs.writeFileSync(path.join(recordDir,'runtime-unit-check.json'),JSON.stringify(record,null,2)+'\n');
console.log(`${all.length} bilingual fragments / ${events} event transitions passed local runtime unit checks; NOT browser verification.`);
