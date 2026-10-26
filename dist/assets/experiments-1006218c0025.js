(function(global){
 'use strict';
 const models=[{name:'Independent',p:[.25,.25,.25,.25]},{name:'Perfect positive correlation',p:[.5,0,0,.5]},{name:'Perfect negative correlation',p:[0,.5,.5,0]}];
 function dependence(i){const m=models[i];return {...m,win:1-m.p[3],stake:64*(1-m.p[3])};}
 function spike(n){return {n,width:1/n,height:n,area:1,svgWidth:600/n,svgHeight:7*n};}
 function walk(n){let seed=918273,s=0;const values=[0];for(let i=1;i<=n;i++){seed=(Math.imul(1664525,seed)+1013904223)>>>0;s+=seed/4294967296<.5?-1:1;values.push(s/Math.sqrt(n));}return values;}
 const api={dependence,spike,walk};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;
 global.BookMath=api;
})(typeof globalThis!=='undefined'?globalThis:this);
