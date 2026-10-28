import {env} from 'cloudflare:workers';
import {report,csv,response,PRIVATE_HEADERS,errorResponse} from '../../../../lib/reading-analytics.mjs';
export const dynamic='force-dynamic';
export async function GET(request:Request){try{
  const data=await report(request,env);
  const params=new URL(request.url).searchParams;
  return params.get('format')==='csv'?new Response(csv(data,params.get('table')||'chapters'),{headers:{...PRIVATE_HEADERS,'Content-Type':'text/csv; charset=utf-8','Content-Disposition':'attachment; filename="reading-summary.csv"'}}):response(data);
}catch(error){return errorResponse(error);}}
