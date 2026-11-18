// Render existing artwork only. No browser, screenshots, redesign or simulation.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const sharp=require('C:/Users/golde/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../..'),version='volume7-visual-review-69f0b1ac-r1-20261106';
const out=path.join(root,'deliverables',version),art=path.join(out,'site/assets/visuals/explanatory-volume7-v1');
const files=fs.readdirSync(art).filter(n=>n.endsWith('.svg')).sort(),records=[];
const digest=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
let cursor=0,done=0;
async function worker(){while(cursor<files.length){const name=files[cursor++],id=name.slice(0,3),source=path.join(art,name),dest=path.join(out,'png',id,name.replace(/\.svg$/,'.png'));
 fs.mkdirSync(path.dirname(dest),{recursive:true});
 await sharp(source,{limitInputPixels:false}).resize({width:2400}).flatten({background:'#fffefa'}).withMetadata({density:300}).png({compressionLevel:9}).toFile(dest);
 const m=await sharp(dest).metadata();if(m.width!==2400||m.height<1)throw Error(name);
 records.push({svg:path.relative(out,source).replaceAll('\\','/'),png:path.relative(out,dest).replaceAll('\\','/'),svg_sha256:digest(source),png_sha256:digest(dest),width:m.width,height:m.height,density:m.density,method:'sharp/librsvg static raster; full SVG viewBox, no crop; NOT a browser screenshot'});
 if(++done%50===0)process.stdout.write(`${done}/${files.length} SVGs rendered\n`);
}}
(async()=>{await Promise.all([worker(),worker()]);records.sort((a,b)=>a.svg.localeCompare(b.svg));fs.writeFileSync(path.join(out,'records/png-renders.json'),JSON.stringify(records,null,2)+'\n');console.log(`${records.length} full-canvas high-resolution PNGs rendered; no browser used.`);})().catch(e=>{console.error(e);process.exitCode=1;});
