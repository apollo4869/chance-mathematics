// Stream immutable public ZIP pieces; never buffer the entire book in a Worker.
export function downloadRange(value,size){
  if(!value)return {start:0,end:size-1,partial:false};
  const m=/^bytes=(\d*)-(\d*)$/.exec(value);if(!m||(!m[1]&&!m[2]))return null;
  let start,end;
  if(!m[1]){const suffix=Number(m[2]);if(!Number.isSafeInteger(suffix)||suffix<1)return null;start=Math.max(0,size-suffix);end=size-1;}
  else{start=Number(m[1]);end=m[2]?Math.min(Number(m[2]),size-1):size-1;}
  return Number.isSafeInteger(start)&&Number.isSafeInteger(end)&&start>=0&&start<size&&end>=start?{start,end,partial:true}:null;
}
export async function offlineDownload(request,assets,manifest){
  if(new URL(request.url).pathname!=='/downloads/complete-offline.zip')return null;
  if(!['GET','HEAD'].includes(request.method))return new Response(null,{status:405,headers:{Allow:'GET, HEAD'}});
  if(!assets||!manifest.bytes)return new Response('Download storage unavailable',{status:503});
  const etag='"'+manifest.sha256+'"';
  const headers=new Headers({'Content-Type':'application/zip','Content-Disposition':'attachment; filename="chance-mathematics-complete-offline.zip"','Accept-Ranges':'bytes',ETag:etag,'Cache-Control':'public, max-age=300','X-Content-Type-Options':'nosniff'});
  if(request.headers.get('If-None-Match')===etag&&!request.headers.has('Range'))return new Response(null,{status:304,headers});
  const ifRange=request.headers.get('If-Range');
  const range=downloadRange(ifRange&&ifRange!==etag?null:request.headers.get('Range'),manifest.bytes);
  if(!range){headers.set('Content-Range','bytes */'+manifest.bytes);return new Response(null,{status:416,headers});}
  headers.set('Content-Length',String(range.end-range.start+1));
  if(range.partial)headers.set('Content-Range',`bytes ${range.start}-${range.end}/${manifest.bytes}`);
  if(request.method==='HEAD')return new Response(null,{status:range.partial?206:200,headers});
  const parts=manifest.parts.filter(p=>p.start<=range.end&&p.start+p.bytes>range.start);
  let index=0,reader=null,cancelled=false;
  const body=new ReadableStream({
    async pull(controller){
      try{
        while(!cancelled){
          if(!reader){
            const part=parts[index++];if(!part){controller.close();return;}
            const url=new URL(part.path,request.url);const response=await assets.fetch(new Request(url,{method:'GET'}));
            if(!response.ok||!response.body)throw new Error('Missing public offline piece');
            const left=Math.max(0,range.start-part.start),right=Math.min(part.bytes,range.end-part.start+1);
            if(left||right!==part.bytes){
              // At most one piece (8 MiB), including for resumed/range downloads.
              const bytes=new Uint8Array(await response.arrayBuffer());if(bytes.length!==part.bytes)throw new Error('Invalid offline piece size');
              controller.enqueue(bytes.subarray(left,right));return;
            }
            reader=response.body.getReader();
          }
          const value=await reader.read();if(cancelled)return;
          if(value.done){reader=null;continue;}
          controller.enqueue(value.value);return;
        }
      }catch(error){if(reader)await reader.cancel().catch(()=>{});controller.error(error);}
    },
    async cancel(){cancelled=true;if(reader)await reader.cancel();}
  });
  return new Response(body,{status:range.partial?206:200,headers});
}
