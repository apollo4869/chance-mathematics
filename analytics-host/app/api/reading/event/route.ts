import {env} from 'cloudflare:workers';
import {updateVisit,errorResponse} from '../../../../lib/reading-analytics.mjs';
export const dynamic='force-dynamic';
export async function POST(request:Request){try{return await updateVisit(request,env);}catch(error){return errorResponse(error);}}
