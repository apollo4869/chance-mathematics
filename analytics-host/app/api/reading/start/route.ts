import {env} from 'cloudflare:workers';
import {startVisit,errorResponse} from '../../../../lib/reading-analytics.mjs';
export const dynamic='force-dynamic';
export async function POST(request:Request){try{return await startVisit(request,env);}catch(error){return errorResponse(error);}}
