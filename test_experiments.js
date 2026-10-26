const assert=require('node:assert/strict');
const {dependence,spike,walk}=require('./experiments.js');
for(let i=0;i<3;i++){
 const m=dependence(i);assert.equal(m.p.reduce((a,b)=>a+b,0),1);
 assert.equal(m.p[0]+m.p[1],.5);assert.equal(m.p[0]+m.p[2],.5);
 assert.equal(m.win,1-m.p[3]);assert.equal(m.stake,[48,32,64][i]);
}
for(let n of [2,4,8,16,32]){
 const s=spike(n);assert.equal(s.width*s.height,1);assert.equal(s.svgWidth*s.svgHeight,4200);
}
for(let n of [16,32,64,128,256]){
 const p=walk(n);assert.equal(p.length,n+1);assert.equal(p[0],0);
 p.slice(1).forEach((v,i)=>assert.ok(Math.abs(Math.abs(v-p[i])-1/Math.sqrt(n))<1e-12));
 assert.deepEqual(p,walk(n));
 const p2=walk(256);p.forEach((v,i)=>assert.ok(Math.abs(v*Math.sqrt(n)-p2[i]*16)<1e-10));
}
const charts=require('./provenance/charts.json');
for(const r of charts[0].data)assert.ok(Math.abs(r.sd-.5/Math.sqrt(r.n))<1e-6);
const fact=n=>{let v=1;for(let i=2;i<=n;i++)v*=i;return v};
for(const r of charts[1].data){
 for(const n of [16,64]){let k=n/2+r.z*Math.sqrt(n)/2;const h=fact(n)/fact(k)/fact(n-k)*Math.pow(.5,n)*Math.sqrt(n)/2;assert.ok(Math.abs(r['n'+n]-h)<1e-5);}
 assert.ok(Math.abs(r.normal-Math.exp(-r.z*r.z/2)/Math.sqrt(2*Math.PI))<1e-5);
}
for(const r of charts[2].data){assert.equal(r.straight,r.n);assert.ok(Object.values(r).some(v=>Math.abs(v-Math.sqrt(r.n))<1e-6));}
console.log('PASS: joint marginals and fair stakes; fixed-scale spike area; deterministic walk increments/prefixes; restored chart values.');
