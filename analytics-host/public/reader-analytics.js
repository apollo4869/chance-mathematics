/* First-party, chapter-only analytics. No external library, fingerprint or raw URL transmission. */
(() => {
  'use strict';
  const book=document.querySelector('.book-section');
  const chapter=Number(document.body.dataset.readerPage?.replace('chapter-',''));
  if(!book||!Number.isInteger(chapter)||chapter<1||chapter>31||location.protocol==='file:')return;
  const read=(store,key)=>{try{return JSON.parse(store.getItem(key));}catch{return null;}};
  const save=(store,key,value)=>{try{store.setItem(key,JSON.stringify(value));}catch{}};
  const enabled=()=>navigator.doNotTrack!=='1'&&!navigator.globalPrivacyControl&&read(localStorage,'chance-analytics-opt-out')!==true;
  if(!enabled())return;
  const uuid=()=>crypto.randomUUID();const locale=document.documentElement.lang==='en'?'en':'zh-CN';
  const today=()=>new Date().toISOString().slice(0,10);
  let reader=read(localStorage,'chance-anonymous-day');
  if(!reader||reader.day!==today()){reader={day:today(),id:uuid()};save(localStorage,'chance-anonymous-day',reader);}
  const storageKey='chance-reading-session:'+locale+':'+chapter;
  let session=read(sessionStorage,storageKey);
  if(!session||session.day!==today()||Date.now()-session.lastSeen>1800000)session={visit:uuid(),day:today(),active:0,progress:0,seq:0,lastSeen:Date.now()};
  let ready=false,pending=false,active=session.active,progress=session.progress,lastTick=performance.now(),lastInput=performance.now(),next=null,interest=null;
  const units=[...book.querySelectorAll(':scope > .reading-unit')];
  const weights=units.map(u=>Math.max(200,u.textContent.length+u.querySelectorAll('.formula').length*40));
  const total=weights.reduce((a,b)=>a+b,0)||1;
  function measure(){
    let done=0,best=0;
    units.forEach((u,i)=>{if(!u.hidden){const r=u.getBoundingClientRect();const fraction=Math.min(1,Math.max(0,(innerHeight-r.top)/Math.max(1,r.height)));best=Math.max(best,(done+weights[i]*fraction)/total);}done+=weights[i];});
    progress=Math.max(progress,Math.min(100,Math.floor(best*100)));
  }
  function tick(){const now=performance.now();const elapsed=now-lastTick;lastTick=now;
    if(document.visibilityState==='visible'&&document.hasFocus()&&now-lastInput<120000&&elapsed<5000){active+=Math.min(elapsed,2000);measure();}
  }
  function persist(){session={...session,active:Math.floor(active),progress,seq:session.seq,lastSeen:Date.now()};save(sessionStorage,storageKey,session);}
  async function flush(final=false){
    if(!ready||!enabled()||(!final&&pending))return;tick();persist();session.seq++;persist();
    const payload={visit:session.visit,token:session.token,seq:session.seq,active:Math.floor(active),progress,next,interest,final};
    if(final&&navigator.sendBeacon){navigator.sendBeacon('/api/reading/event',new Blob([JSON.stringify(payload)],{type:'application/json'}));return;}
    pending=true;try{await fetch('/api/reading/event',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),credentials:'same-origin',keepalive:true});}catch{}finally{pending=false;}
  }
  const params=new URLSearchParams(location.search);let source=params.get('utm_source')||'';
  if(source&&!/^[a-z][a-z0-9_-]{0,39}$/.test(source))source='other';
  const referral=read(sessionStorage,'chance-reading-campaign');
  if(!source&&referral&&Date.now()-referral.at<1800000)source=referral.source;
  // Only coarse campaign codes reach the server; arbitrary values become "other" there.
  if(!source){try{source=document.referrer?(new URL(document.referrer).origin===location.origin?'internal':'external'):'direct';}catch{source='other';}}
  const previous=read(sessionStorage,'chance-previous-reading');
  fetch('/api/reading/start',{method:'POST',headers:{'Content-Type':'application/json'},credentials:'same-origin',body:JSON.stringify({visit:session.visit,reader:reader.id,chapter,locale,source,previous})})
    .then(r=>{if(!r.ok)throw Error('disabled');return r.json();}).then(data=>{
      session.token=data.token;session.seq=Math.max(session.seq,data.seq);active=Math.max(active,data.active);progress=Math.max(progress,data.progress);ready=true;persist();
    }).catch(()=>{}); // Failure never blocks reading; no retries or external fallback.
  ['pointerdown','keydown','touchstart','wheel'].forEach(name=>addEventListener(name,()=>{lastInput=performance.now();},{passive:true}));
  addEventListener('focus',()=>{lastInput=performance.now();lastTick=performance.now();});
  document.addEventListener('visibilitychange',()=>{tick();if(document.hidden)flush(true);else{lastTick=performance.now();lastInput=performance.now();}});
  addEventListener('pagehide',()=>flush(true));addEventListener('pageshow',()=>{lastTick=performance.now();});
  document.addEventListener('click',event=>{
    const link=event.target.closest('a[href]');if(!link||!ready)return;
    const url=new URL(link.href,location.href);const m=url.pathname.match(/\/(?:en\/)?chapters\/(\d+)-/);
    if(url.origin===location.origin&&m&&Number(m[1])!==chapter){
      save(sessionStorage,'chance-previous-reading',{visit:session.visit,token:session.token});
      if(Number(m[1])===chapter+1&&link.closest('.chapter-links'))next=Number(m[1]);
      flush(true);
    }
  });
  setInterval(tick,1000);setInterval(()=>{if(document.visibilityState==='visible'&&document.hasFocus())flush();},15000);
  const feedback=document.createElement('details');feedback.className='reading-feedback';
  const summary=document.createElement('summary');summary.textContent=locale==='en'?'Optional anonymous interest feedback':'可选：匿名阅读兴趣反馈';feedback.append(summary);
  const names=locale==='en'?['Historical ideas','Proofs','More examples','Applications']:['历史与思想','数学证明','更多例子','应用联系'];
  ['history','proofs','examples','applications'].forEach((value,i)=>{const button=document.createElement('button');button.type='button';button.textContent=names[i];button.addEventListener('click',()=>{if(!ready)return;interest=value;flush(true);feedback.querySelectorAll('button').forEach(b=>b.disabled=true);summary.textContent=locale==='en'?'Thank you. Anonymous preference recorded.':'谢谢，已提交匿名兴趣偏好。';});feedback.append(button);});
  const footer=book.parentElement.querySelector('footer');
  book.parentElement.insertBefore(feedback,footer||null);
})();
