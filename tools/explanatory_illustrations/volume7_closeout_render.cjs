// Targeted SVG raster inspection only; no browser, redesign or new mathematical models.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const sharp=require('C:/Users/golde/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../..'),asset=path.join(root,'assets/visuals/explanatory-volume7-v1'),out=path.join(root,'reports/volume7-visual-closeout-2026-11-06/static-renders');
fs.mkdirSync(out,{recursive:true});
const names=fs.readdirSync(asset).filter(n=>n.endsWith('.svg')&&(
 /^V48-(zh|en)-copied-/.test(n)||/^V48\.(zh|en)(\.page2)?\.svg$/.test(n)||
 /^V51-(zh|en)-[012]-10-(desktop|mobile)\.svg$/.test(n)||/^V51\.(zh|en)(\.page[123])?\.svg$/.test(n)));
const records=[];const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
(async()=>{for(const name of names){const src=path.join(asset,name),png=path.join(out,name.replace(/\.svg$/,'.png'));await sharp(src).resize({width:2000}).flatten({background:'#fffefa'}).withMetadata({density:300}).png().toFile(png);const m=await sharp(png).metadata();records.push({source:name,source_sha256:hash(src),png:path.basename(png),width:m.width,height:m.height,kind:'static SVG raster; NOT browser screenshot'});}
fs.writeFileSync(path.join(out,'index.json'),JSON.stringify(records,null,2)+'\n');console.log(`${records.length} targeted static PNGs rendered; protected figures not regenerated.`);})().catch(e=>{console.error(e);process.exitCode=1;});
