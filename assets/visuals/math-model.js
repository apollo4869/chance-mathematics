/* Shared, deterministic mathematical source for print figures and web experiments.
   Original mathematical diagrams by the book project; this is not a theorem proof. */
(function(root,factory){
 'use strict';
 const legacy=typeof module==='object'&&module.exports?require('../../experiments.js'):root.BookMath;
 const api=factory(legacy);
 if(typeof module==='object'&&module.exports)module.exports=api;
 root.ChanceVisualMath=api;
 if(typeof require==='function'&&require.main===module)process.stdout.write(JSON.stringify(api.dataset(),null,2)+'\n');
})(typeof globalThis==='object'?globalThis:this,function(legacy){
 'use strict';
 const spec={schema:1,stable_ids:['walk-scaling','typewriter','spike-ui','conditional-projection','disintegration','characteristic-identification'],
  walk:{n:[16,64,256],seed:918273,generator:'Legacy BookMath.walk: unsigned 32-bit LCG a=1664525,c=1013904223',coupling:'Same pseudorandom increment prefixes, rescaled separately; not pathwise refinements or a convergence proof',time_interval:[0,1]},
  typewriter:{rounds:[1,2,3],sample:0.3,intervals:'half-open [j/2^k,(j+1)/2^k)',enumeration:'n=2^k-2+j+1, k>=1, 0<=j<2^k',left_comparison:'[0,2^-k); u=0 is the null exceptional point'},
  spike:{n:[2,4,8],support:'open (0,1/n)',height:'n',area:1,ui_tail_supremum:'sup_n E[X_n 1_{X_n>K}]=1 for every K>=0'},
  projection:{X:[3,2.3],P:[3,0],other_predictor:[1.1,0],meaning:'Abstract Hilbert-space geometry; not a literal two-dimensional model for all random variables'},
  disintegration:{slice_x:0.6,joint_density:2,support:'0<y<x<1',marginal:'2x',conditional:'1/x on (0,x), for 0<x<1',zero_slice:'No conditional formula asserted at x=0'},
  characteristic:{X:{values:[-1,1],probabilities:[0.5,0.5]},Y:{values:[-Math.sqrt(3),0,Math.sqrt(3)],probabilities:[1/6,2/3,1/6]},range:[0,2*Math.PI],mean:0,variance:1,imaginary_part:0}}
 function typewriter(k,j,u){
  if(!Number.isInteger(k)||k<1||k>20||!Number.isInteger(j)||j<0||j>=2**k||!Number.isFinite(u)||u<0||u>=1)throw new RangeError('Require 1<=k<=20, integer 0<=j<2^k, and 0<=u<1');
  const width=2**(-k),left=j*width,right=(j+1)*width;
  return {k,j,n:2**k-2+j+1,left,right,width,hit:u>=left&&u<right,fixedHit:u>=0&&u<width};
 }
 function spike(n){if(!Number.isInteger(n)||n<1)throw new RangeError('n must be a positive integer');return {n,width:1/n,height:n,area:1};}
 function walk(n){if(!legacy)throw new Error('BookMath must be loaded before the shared model');return legacy.walk(n).map((y,i)=>[i/n,y]);}
 function phiX(t){return Math.cos(t);}
 function phiY(t){return 2/3+Math.cos(Math.sqrt(3)*t)/3;}
 function triangle(x){if(!(x>0&&x<1))throw new RangeError('The displayed conditional slice requires 0<x<1');return {x,jointHeight:2,marginal:2*x,conditionalHeight:1/x,conditionalArea:1};}
 function dataset(){return {spec,walk:spec.walk.n.map(n=>({n,points:walk(n)})),typewriter:spec.typewriter.rounds.flatMap(k=>Array.from({length:2**k},(_,j)=>typewriter(k,j,spec.typewriter.sample))),spikes:spec.spike.n.map(spike),slice:triangle(spec.disintegration.slice_x),characteristic:Array.from({length:501},(_,i)=>{const t=2*Math.PI*i/500;return [t,phiX(t),phiY(t)];})};}
 return {spec,typewriter,spike,walk,phiX,phiY,triangle,dataset};
});
