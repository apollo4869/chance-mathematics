// Deterministic local fixtures only. Never sent to production or shown as real readership.
import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFile} from 'node:fs/promises';
import {authorize,boundedUpdate,dateRange,csv,checkWrite,chapterCount,validChapter} from '../lib/reading-analytics.mjs';
const request=(headers={})=>new Request('https://book.test/api/reading/event',{method:'POST',headers:{Origin:'https://book.test','Content-Type':'application/json','User-Agent':'Test browser',...headers}});

test('thirty-one published chapters share the server and collector boundary',async()=>{
  assert.equal(chapterCount({}),31);
  assert.equal(chapterCount({ANALYTICS_CHAPTER_COUNT:'12'}),12);
  assert.equal(validChapter(31),true);assert.equal(validChapter(32),false);
  assert.equal(dateRange(new URL('https://book.test/api?chapter=31')).chapter,31);
  assert.throws(()=>dateRange(new URL('https://book.test/api?chapter=32')));
  const source=await readFile(new URL('../public/reader-analytics.js',import.meta.url),'utf8');
  assert.match(source,/chapter>31/);
});
test('anonymous, wrong author, and changed stable identity are rejected server-side',async()=>{
  await assert.rejects(authorize(request(),{}),e=>e.status===401);
  await assert.rejects(authorize(request({'oai-authenticated-user-id':'other','oai-authenticated-user-email':'other@example.test'}),{ANALYTICS_OWNER_EMAIL:'author@example.test'}),e=>e.status===403);
  const DB={prepare:()=>({bind(){return this;},run:async()=>({}),first:async()=>({subject:'pinned-author'})})};
  await assert.rejects(authorize(request({'oai-authenticated-user-id':'replacement','oai-authenticated-user-email':'author@example.test'}),{ANALYTICS_OWNER_EMAIL:'author@example.test',DB}),e=>e.status===403);
  await authorize(request({'oai-authenticated-user-id':'pinned-author','oai-authenticated-user-email':'author@example.test'}),{ANALYTICS_OWNER_EMAIL:'author@example.test',DB});
});
test('cross-origin JSON and known automation are excluded',()=>{
  assert.throws(()=>checkWrite(request({Origin:'https://other.test'})),e=>e.status===403);
  assert.throws(()=>checkWrite(request({'User-Agent':'Googlebot'})),e=>e.status===403);
  checkWrite(request());
});
test('server bounds clock jumps and claimed active time; no regression',()=>{
  const row={last_ms:100000,started_ms:10000,active_ms:30000,progress:50};
  assert.deepEqual(boundedUpdate(row,{seq:3,active:1e9,progress:90},115000),{active:47000,progress:90,rejectedTime:true});
  assert.equal(boundedUpdate(row,{seq:4,active:0,progress:0},120000).active,30000);
  assert.throws(()=>boundedUpdate(row,{seq:5,active:1,progress:101},120000));
});
test('date range and CSV are bounded and safe',()=>{
  const now=Date.parse('2026-10-26T12:00:00Z');
  assert.equal(dateRange(new URL('https://book.test/api'),now).from,'2026-09-27');
  assert.throws(()=>dateRange(new URL('https://book.test/api?from=2026-02-30'),now));
  assert.throws(()=>dateRange(new URL('https://book.test/api?chapter=99'),now));
  assert.ok(csv({chapters:[{chapter:'=BAD'}]}).includes("'=BAD"));
});
test('collector excludes hidden/unfocused time, rejects timer suspension, reuses visit on refresh, rotates daily IDs',async()=>{
  const source=await readFile(new URL('../public/reader-analytics.js',import.meta.url),'utf8');
  let clock=0,wall=Date.parse('2026-10-26T12:00:00Z'),focused=true;
  const storage=()=>{const m=new Map();return{getItem:k=>m.get(k)||null,setItem:(k,v)=>m.set(k,v),removeItem:k=>m.delete(k)}};
  const localStorage=storage(),sessionStorage=storage();sessionStorage.setItem("chance-reading-campaign",JSON.stringify({source:"university-course",at:wall}));let id=0;
  const load=async()=>{
    const intervals=[],handlers={},calls=[];const unit={hidden:false,textContent:'x'.repeat(2000),querySelectorAll:()=>[],getBoundingClientRect:()=>({top:0,height:1000})};
    const element=()=>({append(){},insertBefore(){},querySelector(){return null;},addEventListener(){},querySelectorAll:()=>[]});const doc={documentElement:{lang:'zh-CN'},body:{dataset:{readerPage:'chapter-7'}},visibilityState:'visible',referrer:'',hasFocus:()=>focused,addEventListener:(n,f)=>handlers[n]=f,createElement:element,querySelector:()=>({querySelectorAll:()=>[unit],parentElement:element()})};
    class ClockDate extends Date{constructor(...a){super(...(a.length?a:[wall]));}static now(){return wall;}}
    const context={document:doc,localStorage,sessionStorage,location:{protocol:'https:',pathname:'/chapters/07-convergence.html',origin:'https://book.test',href:'https://book.test/chapters/07-convergence.html',search:''},navigator:{doNotTrack:'0',sendBeacon:(_u,b)=>{calls.push({beacon:b});return true;}},crypto:{randomUUID:()=>String(++id).padStart(36,'0')},performance:{now:()=>clock},Date:ClockDate,URL,URLSearchParams,innerHeight:600,Blob,JSON,Math,setInterval:(fn,ms)=>intervals.push({fn,ms}),addEventListener:(n,f)=>handlers[n]=f,fetch:async(url,options)=>{calls.push({url,body:JSON.parse(options.body)});return{ok:true,json:async()=>({token:'test-only',active:0,progress:0,seq:0})}}};
    vm.runInNewContext(source,context);await new Promise(r=>setImmediate(r));return{doc,handlers,calls,tick:()=>intervals.find(x=>x.ms===1000).fn(),flush:()=>intervals.find(x=>x.ms===15000).fn()};
  };
  const a=await load();for(let i=0;i<90;i++){clock+=1000;wall+=1000;a.tick();}a.flush();await new Promise(r=>setImmediate(r));
  assert.equal(a.calls.findLast(x=>x.body?.seq)?.body.active,90000);assert.equal(a.calls.findLast(x=>x.body?.seq)?.body.progress,60);
  a.doc.visibilityState='hidden';clock+=3600000;wall+=3600000;a.tick();a.doc.visibilityState='visible';focused=false;clock+=1000;wall+=1000;a.tick();focused=true;a.flush();await new Promise(r=>setImmediate(r));
  assert.equal(a.calls.findLast(x=>x.body?.seq)?.body.active,90000);
  const first=a.calls[0].body;assert.equal(first.source,"university-course");const b=await load();assert.equal(b.calls[0].body.visit,first.visit);
  wall+=86400000;const c=await load();assert.notEqual(c.calls[0].body.reader,first.reader);assert.notEqual(c.calls[0].body.visit,first.visit);
});
