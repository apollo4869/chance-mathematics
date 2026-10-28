"""Local-only HTTP/D1 fixtures, never production readership. Run against 127.0.0.1."""
import json,time,uuid,urllib.request,urllib.error
BASE='http://127.0.0.1:8775'
COOKIE={'Cookie':'__sites_local_auth=1'}
def call(path,data=None,headers=None):
    h={'User-Agent':'Local-acceptance-test','Origin':BASE,'Content-Type':'application/json',**(headers or {})}
    req=urllib.request.Request(BASE+path,data=json.dumps(data).encode() if data is not None else None,headers=h)
    try:r=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:r=e
    raw=r.read();body=json.loads(raw) if r.headers.get('Content-Type','').startswith('application/json') else raw
    return r.status,body,r.headers
for path in ['/admin/analytics','/api/admin/analytics','/api/admin/analytics?format=csv']:
    assert call(path)[0]==401,path
assert call('/api/admin/analytics',headers={'oai-authenticated-user-id':'local_seedy','oai-authenticated-user-email':'seedy@sites.test'})[0]==401
reader=str(uuid.uuid4());visit=str(uuid.uuid4());payload={'visit':visit,'reader':reader,'chapter':7,'locale':'zh-CN','source':'LOCAL-TEST-NOT-A-READER'}
status,session,_=call('/api/reading/start',payload);assert status==200,(status,session)
assert call('/api/reading/start',payload)[1]['token']==session['token']
start=time.monotonic()
for seq in range(1,8):
    # Real wall-clock boundary: fixture reaches 90 seconds, not a backdated database row.
    time.sleep(13.1)
    event={'visit':visit,'token':session['token'],'seq':seq,'active':int((time.monotonic()-start)*1000),'progress':90,'next':8,'interest':'proofs','final':False}
    status,body,_=call('/api/reading/event',event);assert status==200,(status,body)
assert call('/api/reading/event',event)[1]['duplicate'] is True
_,again,_=call('/api/reading/start',payload);assert again['seq']==7 and again['active']>=90000,again
target={'visit':str(uuid.uuid4()),'reader':reader,'chapter':8,'locale':'zh-CN','source':'internal','previous':{'visit':visit,'token':session['token']}}
assert call('/api/reading/start',target)[0]==200
assert call('/api/reading/start',target)[0]==200
status,report,headers=call('/api/admin/analytics?chapter=7',headers=COOKIE)
assert status==200 and report['totals']['opens']==1 and report['totals']['effective']==1,report
assert all(report['totals'][k]==1 for k in ['depth50','depth75','depth90','next_clicks'])
assert report['transitions']==[{'from_chapter':7,'to_chapter':8,'opens':1}],report['transitions']
assert report['sources'][0]['source']=='other'
assert report['feedback'][0]['interest']=='proofs'
assert report['platform']['visits'] is None
assert 'no-store' in headers['Cache-Control']
assert call('/api/admin/analytics?chapter=99',headers=COOKIE)[0]==400
status,body,_=call('/api/admin/analytics?format=csv',headers=COOKIE);assert status==200 and b'visitor_days' in body
assert call('/api/reading/start',payload,{'Origin':'https://other.test'})[0]==403
assert call('/api/reading/start',payload,{'User-Agent':'Googlebot'})[0]==403
event['seq']=8;event['token']='forged';assert call('/api/reading/event',event)[0]==403
print(json.dumps({'local_http_d1':'PASS','real_elapsed_seconds':round(time.monotonic()-start,1),'refresh_dedup':True,'thresholds_once':True,'transition_once':True,'unauthorized_and_spoofed_headers':401,'csv':'PASS','production_data_used':False}))
