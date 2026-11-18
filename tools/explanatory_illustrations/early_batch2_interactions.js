document.querySelectorAll('[data-batch2]').forEach(root=>{
 const id=root.dataset.batch2,lg=root.lang,en=lg==='en',base='/assets/visuals/explanatory-early-v2/';
 const press=(attr,b)=>root.querySelectorAll('['+attr+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 const img=(sel,name)=>root.querySelector(sel).src=base+name;
 if(id==='E12')root.querySelectorAll('[data-bin]').forEach(b=>b.addEventListener('click',()=>{press('data-bin',b);img('[data-bin-scene]',`E12-${lg}-${b.dataset.bin}.svg`);}));
 if(id==='E13'){
  let n='4',w='2';for(const attr of ['data-lattice-n','data-cell-width'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr==='data-lattice-n')n=b.dataset.latticeN;else w=b.dataset.cellWidth;img('[data-lattice-scene]',`E13-${lg}-${n}.svg`);img('[data-cell-scene]',`E13-${lg}-${n}-w${w}.svg`);}));
 }
 if(id==='E14')root.querySelectorAll('[data-array-n]').forEach(b=>b.addEventListener('click',()=>{press('data-array-n',b);for(const m of ['rare','small'])img(`[data-${m}-scene]`,`E14-${lg}-${b.dataset.arrayN}-${m}.svg`);}));
 if(id==='E17')root.querySelectorAll('[data-state]').forEach(b=>b.addEventListener('click',()=>{press('data-state',b);img('[data-state-scene]',`E17-${lg}-${b.dataset.state}.svg`);root.querySelector('output').textContent=b.dataset.state==='last'?(en?'The same state 0 leads to two forecasts: information was lost.':'同一个“0”分出两个预测，压缩丢失了信息。'):(en?'Histories 01 and 10 share q=1/2 and the same next-step forecast.':'01与10共享q=1/2，也共享同一份下一步预测。');}));
 if(id==='E30')root.querySelectorAll('[data-arrival-count]').forEach(b=>b.addEventListener('click',()=>{press('data-arrival-count',b);const c=Number(b.dataset.arrivalCount);for(const m of ['pre','after'])img(`[data-${m}-scene]`,`E30-${lg}-${m}-${c}.svg`);root.querySelector('output').textContent=en?`This record: predictable ${c}−3=${c-3}; jump-only ${c}−0=${c}. Expectations remain 0 and 3.`:`这条记录：事前${c}−3=${c-3}；事后${c}−0=${c}。总体期望仍为0与3。`;}));
 if(id==='E24'){
  let k='4',a='1';for(const attr of ['data-clock-key','data-clock-apply'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr==='data-clock-key')k=b.dataset.clockKey;else a=b.dataset.clockApply;
   for(const m of ['jump','pulse'])img(`[data-${m}-scene]`,`E24-${lg}-${k}-${m}-${a}.svg`);img('[data-clock-scene]',`E24-${lg}-clock-${k}.svg`);img('[data-compact-scene]',`E24-${lg}-mobile-${k}-${a}.svg`);
   root.querySelector('[data-jump-result]').textContent=en?`Value error ${a==='1'?0:1}`:`取值误差 ${a==='1'?0:1}`;
  }));
 }
});
