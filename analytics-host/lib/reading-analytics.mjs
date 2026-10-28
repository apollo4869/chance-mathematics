// Server-only analytics. No IP, raw referrer, visitor email or user-agent is persisted.
const encoder = new TextEncoder();
export const PRIVATE_HEADERS = {'Cache-Control':'private, no-store, max-age=0', 'Vary':'Cookie, oai-authenticated-user-id', 'X-Robots-Tag':'noindex, nofollow', 'X-Content-Type-Options':'nosniff'};
export const interests = ['history','proofs','examples','applications'];
export function response(value, status=200) {return Response.json(value,{status,headers:PRIVATE_HEADERS});}
export function fail(message,status=400){throw Object.assign(new Error(message),{status});}
export function chapterCount(env){const n=Number(env.ANALYTICS_CHAPTER_COUNT||31);return Number.isInteger(n)&&n>=1&&n<=99?n:31;}
export function validChapter(n,max=31){return Number.isInteger(n)&&n>=1&&n<=max;}
export function uuid(s){return typeof s==='string'&&/^[a-f0-9-]{36}$/.test(s);}
export function dayOf(now=Date.now()){return new Date(now).toISOString().slice(0,10);}
export function campaign(value, allowed){return typeof value==='string'&&Object.hasOwn(allowed,value)?value:'other';}
export async function hmac(secret,value){
  const key=await crypto.subtle.importKey('raw',encoder.encode(secret),{name:'HMAC',hash:'SHA-256'},false,['sign']);
  return [...new Uint8Array(await crypto.subtle.sign('HMAC',key,encoder.encode(value)))].map(n=>n.toString(16).padStart(2,'0')).join('');
}
function constantEqual(a,b){if(typeof a!=='string'||a.length!==b.length)return false;let diff=0;for(let i=0;i<a.length;i++)diff|=a.charCodeAt(i)^b.charCodeAt(i);return diff===0;}
export async function signVisit(env,row){return hmac(env.ANALYTICS_SECRET,`${row.id}|${row.day}|${row.chapter}|${row.locale}`);}
async function verifyVisit(env,id,token){
  if(!uuid(id)||typeof token!=='string')fail('Invalid visit',400);
  const row=await env.DB.prepare('SELECT * FROM reading_visits WHERE id=?').bind(id).first();
  if(!row||!constantEqual(token,await signVisit(env,row)))fail('Invalid visit token',403);
  if(Date.now()-row.started_ms>86400000)fail('Visit expired',410);
  return row;
}
export function settings(env){
  if(!env.DB||!env.ANALYTICS_SECRET||env.ANALYTICS_SECRET.length<32)fail('Analytics not configured',503);
}
export async function authorize(request,env){
  // Sites dispatch owns and replaces these headers. Never expose a direct Worker origin.
  const subject=request.headers.get('oai-authenticated-user-id');
  const email=request.headers.get('oai-authenticated-user-email');
  if(!subject||!email)fail('Sign in with ChatGPT',401);
  if(!env.ANALYTICS_OWNER_EMAIL)fail('Owner authorization is not configured',503);
  if(email.toLowerCase()!==env.ANALYTICS_OWNER_EMAIL.toLowerCase())fail('Author access only',403);
  if(!env.DB)fail('Analytics database is not configured',503);
  // Pin the first dispatch-verified owner to this Site's stable identity, not a display name.
  await env.DB.prepare("INSERT INTO analytics_owner (id,subject) VALUES (1,?) ON CONFLICT(id) DO NOTHING").bind(subject).run();
  const owner=await env.DB.prepare('SELECT subject FROM analytics_owner WHERE id=1').first();
  if(owner?.subject!==subject)fail('Author identity does not match',403);
}
export function checkWrite(request){
  const url=new URL(request.url);
  if(request.headers.get('Origin')!==url.origin)fail('Same-origin requests only',403);
  if(request.headers.get('Sec-Fetch-Site')==='cross-site')fail('Cross-site request rejected',403);
  if(!request.headers.get('Content-Type')?.startsWith('application/json'))fail('JSON required',415);
  if(Number(request.headers.get('Content-Length')||0)>4096)fail('Payload too large',413);
  if(/bot|spider|crawler|headless|curl|wget/i.test(request.headers.get('User-Agent')||''))fail('Automated traffic excluded',403);
  if(request.cf?.botManagement?.verifiedBot||request.cf?.botManagement?.score<20)fail('Automated traffic excluded',403);
}
export async function readPayload(request){const s=await request.text();if(encoder.encode(s).length>4096)fail('Payload too large',413);let value;try{value=JSON.parse(s);}catch{fail('Invalid JSON');}if(!value||typeof value!=='object'||Array.isArray(value))fail('JSON object required');return value;}
async function purge(db,now){
  const today=dayOf(now);const result=await db.prepare('INSERT INTO analytics_maintenance(id,last_day) VALUES (1,?) ON CONFLICT(id) DO UPDATE SET last_day=excluded.last_day WHERE last_day<excluded.last_day').bind(today).run();
  if(result.meta?.changes){const cutoff=dayOf(now-89*86400000);await db.batch([db.prepare('DELETE FROM reading_transitions WHERE day<?').bind(cutoff),db.prepare('DELETE FROM reading_visits WHERE day<?').bind(cutoff)]);}
}
export async function startVisit(request,env){
  settings(env);checkWrite(request);
  if(env.ANALYTICS_OWNER_EMAIL&&request.headers.get('oai-authenticated-user-email')?.toLowerCase()===env.ANALYTICS_OWNER_EMAIL.toLowerCase())fail('Author self-traffic excluded',403);
  const body=await readPayload(request);const now=Date.now();
  if(!uuid(body.visit)||!uuid(body.reader)||!validChapter(body.chapter,chapterCount(env))||!(env.ANALYTICS_LANGUAGES||'zh-CN,en').split(',').includes(body.locale))fail('Invalid reading session');
  await purge(env.DB,now);
  const day=dayOf(now),visitor=await hmac(env.ANALYTICS_SECRET,day+'|'+body.reader);
  const limits=await env.DB.prepare('SELECT COUNT(*) AS n FROM reading_visits WHERE visitor_day=? AND started_ms>?').bind(visitor,now-3600000).first();
  let row=await env.DB.prepare('SELECT * FROM reading_visits WHERE id=?').bind(body.visit).first();
  if(!row&&limits.n>=60)fail('Reading session rate limit',429);
  const config=JSON.parse(env.ANALYTICS_CAMPAIGNS||'{"direct":"Direct","external":"External referral","internal":"Internal navigation","other":"Other"}');
  const source=campaign(body.source,config);
  if(row&&(row.chapter!==body.chapter||row.locale!==body.locale||row.day!==day||row.visitor_day!==visitor))fail('Session conflict',409);
  if(!row){
    await env.DB.prepare('INSERT INTO reading_visits(id,day,chapter,locale,visitor_day,source,started_ms,last_ms) VALUES (?,?,?,?,?,?,?,?) ON CONFLICT(id) DO NOTHING').bind(body.visit,day,body.chapter,body.locale,visitor,source,now,now).run();
    row=await env.DB.prepare('SELECT * FROM reading_visits WHERE id=?').bind(body.visit).first();
    if(body.previous&&uuid(body.previous.visit)){
      try{const previous=await verifyVisit(env,body.previous.visit,body.previous.token);
        if(previous.chapter!==row.chapter&&now-previous.last_ms<1800000){
          await env.DB.prepare('INSERT INTO reading_transitions(from_visit,to_visit,day,from_chapter,to_chapter,source) VALUES (?,?,?,?,?,?) ON CONFLICT(from_visit,to_chapter) DO NOTHING').bind(previous.id,row.id,day,previous.chapter,row.chapter,previous.source).run();
        }
      }catch(error){if(error.status>=500)throw error;}
    }
  }
  return response({visit:row.id,token:await signVisit(env,row),active:row.active_ms,progress:row.progress,seq:row.seq,serverNow:now});
}
export function boundedUpdate(row,body,now){
  if(!Number.isInteger(body.seq)||body.seq<1||body.seq>10000||!Number.isFinite(body.active)||body.active<0||!Number.isInteger(body.progress)||body.progress<0||body.progress>100)fail('Invalid reading metrics');
  const elapsed=Math.max(0,now-row.last_ms);
  const delta=Math.max(0,body.active-row.active_ms);
  const active=Math.min(14400000,Math.max(row.active_ms,Math.min(body.active,row.active_ms+Math.min(elapsed+2000,60000),now-row.started_ms+2000)));
  return {active,progress:Math.max(row.progress,body.progress),rejectedTime:delta>elapsed+2000};
}
export async function updateVisit(request,env){
  settings(env);checkWrite(request);
  if(env.ANALYTICS_OWNER_EMAIL&&request.headers.get('oai-authenticated-user-email')?.toLowerCase()===env.ANALYTICS_OWNER_EMAIL.toLowerCase())fail('Author self-traffic excluded',403);
  const body=await readPayload(request);const row=await verifyVisit(env,body.visit,body.token);const now=Date.now();
  if(body.seq<=row.seq)return response({accepted:false,duplicate:true});
  if(now-row.last_ms<2000&&!body.final)return response({accepted:false,rateLimited:true},429);
  const next=boundedUpdate(row,body,now);
  if(body.interest!=null&&!interests.includes(body.interest))fail('Invalid interest');
  const click=body.next===row.chapter+1&&validChapter(body.next,chapterCount(env))?1:0;
  await env.DB.prepare('UPDATE reading_visits SET seq=?,last_ms=?,active_ms=?,progress=?,next_clicked=MAX(next_clicked,?),interest=COALESCE(?,interest) WHERE id=? AND seq<?').bind(body.seq,now,next.active,next.progress,click,body.interest||null,row.id,body.seq).run();
  return response({accepted:true});
}
export function dateRange(url,now=Date.now(),maxChapter=31){
  const to=url.searchParams.get('to')||dayOf(now),from=url.searchParams.get('from')||dayOf(now-29*86400000);
  if(![from,to].every(s=>/^\d{4}-\d{2}-\d{2}$/.test(s)&&!isNaN(Date.parse(s))&&dayOf(Date.parse(s))===s))fail('Invalid date range');
  if(from>to||to>dayOf(now)||from<dayOf(now-89*86400000))fail('Choose a range within the last 90 UTC days');
  const chapter=url.searchParams.get('chapter')?Number(url.searchParams.get('chapter')):null;
  if(chapter!==null&&!validChapter(chapter,maxChapter))fail('Invalid chapter');
  return {from,to,chapter};
}
const measures=`COUNT(*) AS opens, COUNT(DISTINCT visitor_day) AS visitor_days, SUM(active_ms) AS active_ms, AVG(active_ms) AS avg_active_ms, AVG(progress) AS avg_progress,
  SUM(CASE WHEN progress>=50 THEN 1 ELSE 0 END) AS depth50,SUM(CASE WHEN progress>=75 THEN 1 ELSE 0 END) AS depth75,SUM(CASE WHEN progress>=90 THEN 1 ELSE 0 END) AS depth90,
  SUM(CASE WHEN active_ms>=90000 AND progress>=50 THEN 1 ELSE 0 END) AS effective,SUM(next_clicked) AS next_clicks`;
export async function report(request,env){
  await authorize(request,env);await purge(env.DB,Date.now());const range=dateRange(new URL(request.url),Date.now(),chapterCount(env));
  const where='day BETWEEN ? AND ?'+(range.chapter?' AND chapter=?':'');const args=[range.from,range.to,...(range.chapter?[range.chapter]:[])];
  const query=(sql)=>env.DB.prepare(sql).bind(...args).all().then(r=>r.results);
  const [totals,chapters,daily,weekly,monthly,sources,feedback,depth,transitions]=await Promise.all([
    query('SELECT '+measures+' FROM reading_visits WHERE '+where),
    query('SELECT chapter,'+measures+' FROM reading_visits WHERE '+where+' GROUP BY chapter ORDER BY opens DESC,chapter'),
    query('SELECT day AS period,'+measures+' FROM reading_visits WHERE '+where+' GROUP BY day ORDER BY day'),
    query("SELECT strftime('%Y-W%W',day) AS period,"+measures+' FROM reading_visits WHERE '+where+' GROUP BY period ORDER BY period'),
    query("SELECT substr(day,1,7) AS period,"+measures+' FROM reading_visits WHERE '+where+' GROUP BY period ORDER BY period'),
    query('SELECT source,'+measures+' FROM reading_visits WHERE '+where+' GROUP BY source ORDER BY opens DESC'),
    query('SELECT interest,COUNT(*) AS votes FROM reading_visits WHERE '+where+' AND interest IS NOT NULL GROUP BY interest'),
    query("SELECT CASE WHEN progress<50 THEN '0–49%' WHEN progress<75 THEN '50–74%' WHEN progress<90 THEN '75–89%' ELSE '90–100%' END AS bucket,COUNT(*) AS visits FROM reading_visits WHERE "+where+' GROUP BY bucket'),
    env.DB.prepare('SELECT t.from_chapter,t.to_chapter,COUNT(*) AS opens FROM reading_transitions t JOIN reading_visits v ON t.from_visit=v.id WHERE v.day BETWEEN ? AND ?'+(range.chapter?' AND v.chapter=?':'')+' GROUP BY from_chapter,to_chapter ORDER BY from_chapter,to_chapter').bind(...args).all().then(r=>r.results)
  ]);
  return {range,totals:totals[0],chapters,daily,weekly,monthly,sources,feedback,depth,transitions,platform:{status:'NATIVE_CONSOLE_LINKED',console_url:'https://chatgpt.com/space/sites/appgprj_6add5ada774c819199489ea9858f15c8/analytics',automatic_numeric_sync:false,visits:null,unique_visitors:null},mobileBackgroundTiming:'PENDING_PHYSICAL_DEVICE_REVIEW',retentionDays:90,definition:{activeSeconds:90,progress:50},clock:'UTC',updatedAt:new Date().toISOString()};
}
export function csv(data,table='chapters'){
  const metrics=['opens','visitor_days','active_ms','avg_active_ms','avg_progress','depth50','depth75','depth90','effective','next_clicks'];
  const columns={chapters:['chapter',...metrics],daily:['period',...metrics],weekly:['period',...metrics],monthly:['period',...metrics],sources:['source',...metrics],transitions:['from_chapter','to_chapter','opens'],depth:['bucket','visits'],feedback:['interest','votes']};
  if(!Object.hasOwn(columns,table))fail('Invalid export table');
  const fields=['from_utc','to_utc',...columns[table]];
  const cell=v=>'"'+String(v??'').replace(/^[=+@-]/,"'$&").replaceAll('"','""')+'"';
  return '\ufeff'+[fields,...data[table].map(r=>[data.range?.from,data.range?.to,...columns[table].map(f=>r[f])])].map(r=>r.map(cell).join(',')).join('\r\n');
}
export function errorResponse(error){return response({error:error.status?error.message:'Analytics temporarily unavailable'},error.status||503);}
