/* Independent mathematical invariants and endpoint tests, not a visual snapshot test. */
const assert=require('assert/strict'),fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..'),M=require('../assets/visuals/math-model.js');
const close=(a,b)=>assert.ok(Math.abs(a-b)<1e-10,`${a} != ${b}`);
assert.deepEqual(JSON.parse(fs.readFileSync(path.join(root,'assets/visuals/data.json'),'utf8')),M.dataset());
for(let k=1;k<=8;k++){
 for(const u of [0,0.125,0.25,0.3,0.5,0.999]){
  let hits=0;for(let j=0;j<2**k;j++){const r=M.typewriter(k,j,u);hits+=Number(r.hit);close(r.width,2**(-k));assert.equal(r.n,2**k-1+j);}
  assert.equal(hits,1);assert.equal(M.typewriter(k,0,0).fixedHit,true);
 }
 for(let j=0;j<2**k-1;j++){const r=M.typewriter(k,j,(j+1)/2**k);assert.equal(r.hit,false);assert.equal(M.typewriter(k,j+1,r.right).hit,true);}
}
for(const u of [0.125,0.25,0.3,0.5,0.999])for(let k=4;k<=8;k++)if(2**(-k)<=u)assert.equal(M.typewriter(k,0,u).fixedHit,false);
for(const invalid of [[0,0,.3],[2,4,.3],[2,0,1],[2,-1,.3]])assert.throws(()=>M.typewriter(...invalid),RangeError);
for(const n of [16,64,256]){const p=M.walk(n);assert.equal(p.length,n+1);close(p[0][0],0);close(p[n][0],1);for(let i=1;i<=n;i++){close(p[i][0]-p[i-1][0],1/n);close(Math.abs(p[i][1]-p[i-1][1]),1/Math.sqrt(n));}}
for(const n of [1,2,4,8,101]){const s=M.spike(n);close(s.height*s.width,1);}
for(const x of [.001,.25,.6,.999]){const s=M.triangle(x);close(s.jointHeight*x,s.marginal);close(s.conditionalHeight*x,1);}
assert.throws(()=>M.triangle(0),RangeError);assert.throws(()=>M.triangle(1),RangeError);
const {X,P,other_predictor:V}=M.spec.projection;const norm=v=>v.reduce((a,x)=>a+x*x,0),sub=(a,b)=>a.map((x,i)=>x-b[i]);close(sub(X,P).reduce((a,x,i)=>a+x*(P[i]-V[i]),0),0);close(norm(sub(X,V)),norm(sub(X,P))+norm(sub(P,V)));
for(const law of [M.spec.characteristic.X,M.spec.characteristic.Y]){close(law.probabilities.reduce((a,p)=>a+p,0),1);close(law.values.reduce((a,x,i)=>a+x*law.probabilities[i],0),0);close(law.values.reduce((a,x,i)=>a+x*x*law.probabilities[i],0),1);}
for(const t of [0,.3,1,Math.PI,2*Math.PI]){
 for(const [law,f] of [[M.spec.characteristic.X,M.phiX],[M.spec.characteristic.Y,M.phiY]]){close(law.values.reduce((a,x,i)=>a+law.probabilities[i]*Math.cos(t*x),0),f(t));close(law.values.reduce((a,x,i)=>a+law.probabilities[i]*Math.sin(t*x),0),0);}
}
assert.ok(Math.abs(M.phiX(Math.PI)-M.phiY(Math.PI))>.5);
console.log(JSON.stringify({mathematical_models:'PASS',groups:6,half_open_boundary_tests:'PASS',sample_seed:918273,finite_simulation_is_proof:false}));
