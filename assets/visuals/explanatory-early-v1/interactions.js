document.querySelectorAll('[data-early]').forEach(root=>{
 const id=root.dataset.early,lg=root.lang,en=lg==='en',base='/assets/visuals/explanatory-early-v1/';
 const press=(attr,b)=>root.querySelectorAll('['+attr+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 const put=t=>root.querySelector('[data-reading]').textContent=t;
 if(id==='E06')root.querySelectorAll('[data-value]').forEach(b=>b.addEventListener('click',()=>{
  press('data-value',b);const v=Number(b.dataset.value);for(const p of ['domain','values'])root.querySelector('[data-'+p+']').src=base+`E06-${lg}-${p}-${v}.svg`;root.querySelector('[data-mobile-group]').src=base+`E06-${lg}-mobile-${v}.svg`;
  const n={1:3,3:2,5:3}[v];put(!v?(en?'Add the three contributions; the original function is unchanged.':'三组面积相加，函数没有被改动。'):(en?`Value ${v}: preimage measure ${n}/8; integral contribution ${v*n}/8.`:`取值${v}：原像测度${n}/8；积分贡献${v*n}/8。`));
 }));
 if(id==='E08'){
  let mode='impossible',flip=0;function draw(){root.querySelector('[data-pair-scene]').src=base+`E08-${lg}-${mode}-${flip}.svg`;put(mode==='impossible'?(en?'Two opposite relations force the third pair equal. No triple law can meet all three opposite constraints.':'前两对相反，迫使第三对相同。没有三元律能满足三对全相反。'):(en?'P(010)=P(101)=1/2 realizes the three pair laws and keeps every bit fair.':'P(010)=P(101)=1/2真实实现三份二元律，每个单独变量仍公平。'));}
  for(const attr of ['data-pairs','data-flip'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr==='data-pairs')mode=b.dataset.pairs;else flip=Number(b.dataset.flip);draw();}));
 }
 if(id==='E16')root.querySelectorAll('[data-reveal]').forEach(b=>b.addEventListener('click',()=>{press('data-reveal',b);const k=Number(b.dataset.reveal);root.querySelector('[data-prefix-scene]').src=base+`E16-${lg}-${k}.svg`;put(k?(en?'The same observed prefix permits L=2 or L=4. First return T=2 was already known.':'同一个已见前缀，允许L=2或L=4；首次返回T=2此前已经知道。'):(en?'T=2 is decidable now; L=2 is not.':'T=2可确认；L=2目前不能确认。'));}));
 if(id==='E20'){
  let mode='P',child=1;function draw(){root.querySelector('[data-family-scene]').src=base+`E20-${lg}-${mode}-${child}.svg`;put(mode==='P'?(en?'Original family weights 1/2: joint child weights 1/2,1/6,1/6,1/6.':'原家族各1/2：单孩联合概率1/2，三孩各1/6。'):(en?'Family weights 1/4,3/4. Each of the four tree–child pairs now has weight 1/4.':'家族权重1/4、3/4；四个“树＋孩子”联合权重都为1/4。'));}
  for(const attr of ['data-family-law','data-child'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr==='data-family-law')mode=b.dataset.familyLaw;else child=Number(b.dataset.child);draw();}));
 }
 if(id==='E24'){
  let mode='jump',key='8',aligned=0;function draw(){root.querySelector('[data-path-scene]').src=base+`E24-${lg}-${key}-${mode}-${aligned}.svg`;root.querySelector('[data-clock-scene]').src=base+`E24-${lg}-clock-${key}.svg`;put(mode==='pulse'?(en?'After any clock homeomorphism, pulse height remains 1. Shrinking width cannot erase it.':'任意时间同胚后，往返高度仍是1；宽度缩小不能删除它。'):(aligned?(en?`Aligned value error 0; clock error δ=1/${key}.`:`对齐后的取值误差0；时钟误差δ=1/${key}。`):(en?`Uniform error 1 before alignment; clock error δ=1/${key} can align the jump.`:`未对齐时一致误差1；时钟误差δ=1/${key}可将单跳对齐。`)));}
  for(const attr of ['data-path-mode','data-delta','data-aligned'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr==='data-path-mode')mode=b.dataset.pathMode;else if(attr==='data-delta')key=b.dataset.delta;else aligned=Number(b.dataset.aligned);draw();}));
 }
});
