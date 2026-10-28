import {createHash} from "node:crypto";
// Reproducible public-only offline archive from committed reading pages and source.
// Generated output is deployed, not committed as a large Git blob.
import {readFile,writeFile,readdir,mkdir,unlink} from 'node:fs/promises';
import path from 'node:path';
import {deflateRawSync} from 'node:zlib';
const root=process.cwd(),pub=path.join(root,'public'),source=path.join(root,'book-source-current');
const runtime=new Set(['analytics-dashboard.js','reader-analytics.js','campaign-attribution.js','privacy-controls.js','favicon.svg','complete-offline.zip']);
const edition=JSON.parse(await readFile(path.join(root,'formal-thirtyone-preservation.json'),'utf8')).edition;
// The complete source already lives in editable-source/. Do not recursively
// embed duplicate source ZIPs; preserve their online downloads independently.
const omitted=new Map([
  ['downloads/editable-manuscript.zip','OFFLINE-README.txt'],
  ['downloads/english-manuscript.zip','downloads/manuscript-en.md'],
  ['releases/'+edition+'.zip','releases/'+edition+'.json']
]);
async function walk(base,prefix=''){
  const out=[];
  for(const d of await readdir(path.join(base,prefix),{withFileTypes:true})){
    const n=prefix?prefix+'/'+d.name:d.name;
    if(d.isDirectory())out.push(...await walk(base,n));else if(d.isFile())out.push(n);
  }
  return out.sort();
}
const rows=[];
for(const n of await walk(pub)){if(n.endsWith('.zip')&&n!=='downloads/complete-offline.zip'&&!omitted.has(n))omitted.set(n,n.startsWith('releases/')?n.slice(0,-4)+'.json':'OFFLINE-README.txt');}
for(const n of await walk(pub)){
  if(n.startsWith('downloads/offline-parts/')||runtime.has(n)||path.basename(n)==='complete-offline.zip'||omitted.has(n))continue;
  let b=await readFile(path.join(pub,n));
  if(n.endsWith('.html')){
    let html=b.toString('utf8').replace(/<a\b[^>]*href="[^"]*downloads\/complete-offline\.zip"[^>]*>[\s\S]*?<\/a>/g,'');
    html=html.replace(/<a\b([^>]*?)href="([^"]+)"([^>]*)>([\s\S]*?)<\/a>/g,(all,before,href,after,label)=>{
      const u=new URL(href,'https://offline.invalid/'+n),target=omitted.get(decodeURIComponent(u.pathname).slice(1));
      if(u.origin!=='https://offline.invalid'||!target)return all;
      const relative=path.posix.relative(path.posix.dirname(n),target);
      const name=target==='OFFLINE-README.txt'?'离线原稿目录 / Offline source folder':target.endsWith('.json')?'版本指纹 / Version fingerprints':'完整英文原稿 / Full English manuscript';
      return '<a'+before+'href="'+relative+'"'+after+'>'+name+'</a>';
    });b=Buffer.from(html);
  }
  rows.push([n,b]);
}
for(const n of await walk(source)){
  if(/(^|\/)(?:\.git|node_modules|\.sites-runtime|planning)(\/|$)|\.dev\.vars|chat-messages|conversion-ledger|\.sqlite/.test(n))throw Error('Non-public source in archive');
  rows.push(['editable-source/'+n,await readFile(path.join(source,n))]);
}
rows.push(['OFFLINE-README.txt',Buffer.from('偶然的数学 / The Mathematics of Chance\n\nOpen index.html (Chinese) or en/index.html (English).\n完整中英文原稿、数学证明与图片源文件位于 editable-source/。\nComplete editable manuscripts, proofs, figure sources and engineering: editable-source/.\nCombined manuscripts: downloads/manuscript.md and downloads/manuscript-en.md.\nThe standalone source ZIP downloads and current release ZIP are omitted from this ZIP to avoid recursive duplication; their complete contents are retained as files. Historical snapshots remain available from the official website; offline records retain their JSON fingerprints.\n')]);
rows.sort((a,b)=>a[0].localeCompare(b[0],'en'));
const crcTable=Uint32Array.from({length:256},(_,n)=>{for(let i=0;i<8;i++)n=n&1?0xedb88320^(n>>>1):n>>>1;return n>>>0;});
const crc32=b=>{let v=0xffffffff;for(const x of b)v=crcTable[(v^x)&255]^(v>>>8);return (v^0xffffffff)>>>0;};
const local=[],central=[];let offset=0;
const date=((2026-1980)<<9)|(10<<5)|28;
for(const [n,b] of rows){
  const name=Buffer.from(n),packed=deflateRawSync(b,{level:6}),crc=crc32(b);
  const h=Buffer.alloc(30);h.writeUInt32LE(0x04034b50);h.writeUInt16LE(20,4);h.writeUInt16LE(0x800,6);h.writeUInt16LE(8,8);h.writeUInt16LE(date,12);h.writeUInt32LE(crc,14);h.writeUInt32LE(packed.length,18);h.writeUInt32LE(b.length,22);h.writeUInt16LE(name.length,26);
  local.push(h,name,packed);
  const c=Buffer.alloc(46);c.writeUInt32LE(0x02014b50);c.writeUInt16LE(20,4);c.writeUInt16LE(20,6);c.writeUInt16LE(0x800,8);c.writeUInt16LE(8,10);c.writeUInt16LE(date,14);c.writeUInt32LE(crc,16);c.writeUInt32LE(packed.length,20);c.writeUInt32LE(b.length,24);c.writeUInt16LE(name.length,28);c.writeUInt32LE(offset,42);central.push(c,name);
  offset+=h.length+name.length+packed.length;
}
const directory=Buffer.concat(central),end=Buffer.alloc(22);end.writeUInt32LE(0x06054b50);end.writeUInt16LE(rows.length,8);end.writeUInt16LE(rows.length,10);end.writeUInt32LE(directory.length,12);end.writeUInt32LE(offset,16);
const archive=Buffer.concat([...local,directory,end]);
const partDir=path.join(pub,'downloads/offline-parts');await mkdir(partDir,{recursive:true});
for(const name of await readdir(partDir)){if(/^part-[a-f0-9]+-\d+\.bin$/.test(name))await unlink(path.join(partDir,name));}
const digest=createHash('sha256').update(archive).digest('hex'),parts=[];
for(let start=0,i=0;start<archive.length;start+=8*1024*1024,i++){
 const bytes=archive.subarray(start,Math.min(start+8*1024*1024,archive.length));
 const name='part-'+digest.slice(0,16)+'-'+i+'.bin';await writeFile(path.join(partDir,name),bytes);
 parts.push({path:'/downloads/offline-parts/'+name,start,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')});
}
const manifest={bytes:archive.length,sha256:digest,parts};
await writeFile(path.join(root,'lib/offline-manifest.json'),JSON.stringify(manifest,null,2)+'\n');
await writeFile(path.join(root,'.sites-runtime/complete-offline.zip'),archive);
await unlink(path.join(pub,'downloads/complete-offline.zip')).catch(e=>{if(e.code!=='ENOENT')throw e;});
console.log(JSON.stringify({offlineArchive:'complete-offline.zip',files:rows.length,bytes:archive.length,source:'committed public reading edition and source'}));
