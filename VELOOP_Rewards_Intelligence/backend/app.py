from pathlib import Path
import os,sqlite3,functools
from flask import Flask,jsonify,request,session,send_from_directory
from flask_cors import CORS
ROOT=Path(__file__).resolve().parents[1]; DB=Path(os.getenv('DATABASE_PATH',ROOT/'backend'/'veloop_demo.db'))
app=Flask(__name__,static_folder=None); app.secret_key=os.getenv('SECRET_KEY','local-demo-secret-change-before-deploy')
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax', SESSION_COOKIE_SECURE=os.getenv('COOKIE_SECURE','false').lower()=='true')
CORS(app,supports_credentials=True,origins=os.getenv('CORS_ORIGINS','http://127.0.0.1:5000,http://localhost:5000').split(','))
DEMO_USER=os.getenv('DEMO_ADMIN_USER','admin@demo.veloop'); DEMO_PASSWORD=os.getenv('DEMO_ADMIN_PASSWORD','DemoOnly!2026')
if not DB.exists():
 from backend.seed_database import seed
 seed()
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def auth(fn):
 @functools.wraps(fn)
 def wrap(*a,**k):
  if not session.get('user'): return jsonify({'error':'Authentication required'}),401
  return fn(*a,**k)
 return wrap
def count(c,q):
 r=c.execute(q).fetchone(); return r[0] if r else 0
@app.get('/')
def home(): return send_from_directory(ROOT/'frontend','index.html')
@app.get('/<path:p>')
def static(p): return send_from_directory(ROOT/'frontend',p)
@app.get('/api/health')
def health(): return jsonify({'status':'ok','data_mode':'SIMULATED','production_connected':False})
@app.post('/api/login')
def login():
 b=request.get_json(silent=True) or {}
 if b.get('email')==DEMO_USER and b.get('password')==DEMO_PASSWORD:
  session['user']=DEMO_USER; return jsonify({'ok':True,'user':DEMO_USER,'mode':'demo'})
 return jsonify({'error':'Invalid demo credentials'}),401
@app.post('/api/logout')
def logout(): session.clear(); return jsonify({'ok':True})
@app.get('/api/me')
@auth
def me(): return jsonify({'user':session['user'],'mode':'demo'})
@app.get('/api/overview')
@auth
def overview():
 c=db(); total=count(c,'select count(*) from task_activity'); completed=count(c,"select count(*) from task_activity where status='completed'")
 out={'users':count(c,'select count(*) from users'),'active_users':count(c,"select count(*) from users where account_status='active'"),'task_activities':total,'task_completion_rate':round(completed/max(total,1)*100,1),'rewards_credited':count(c,"select count(*) from rewards where status='credited'"),'pending_rewards':count(c,"select count(*) from rewards where status='pending'"),'wallet_transactions':count(c,'select count(*) from wallet_transactions'),'withdrawal_pending':count(c,"select count(*) from withdrawals where status in ('pending','processing')"),'withdrawal_completed':count(c,"select count(*) from withdrawals where status='completed'"),'referrals_converted':count(c,"select count(*) from referrals where status='converted'"),'data_mode':'SIMULATED'}; c.close(); return jsonify(out)
@app.get('/api/breakdowns')
@auth
def breakdowns():
 c=db()
 def rows(q): return [dict(x) for x in c.execute(q).fetchall()]
 out={'platforms':rows('select platform label,count(*) value from users group by platform'),'task_status':rows('select status label,count(*) value from task_activity group by status'),'reward_status':rows('select status label,count(*) value from rewards group by status'),'withdrawal_status':rows('select status label,count(*) value from withdrawals group by status'),'top_features':rows('select feature label,count(*) value from task_activity group by feature order by value desc limit 6'),'monthly_users':rows('select substr(registered_at,1,7) label,count(*) value from users group by label order by label'),'recent_withdrawals':rows('select withdrawal_id,user_id,requested_amount,method,status,requested_at from withdrawals order by requested_at desc limit 12')}; c.close(); return jsonify(out)
@app.get('/api/quality')
@auth
def quality():
 c=db(); out=[{'check':'Duplicate task activity IDs','count':count(c,'select count(*) from (select activity_id from messy_data group by activity_id having count(*)>1)'),'severity':'Critical'},{'check':'Missing task user IDs','count':count(c,'select count(*) from messy_data where user_id is null'),'severity':'High'},{'check':'Orphan task user IDs','count':count(c,'select count(*) from messy_data t left join users u on t.user_id=u.user_id where t.user_id is not null and u.user_id is null'),'severity':'High'},{'check':'Unknown task statuses','count':count(c,"select count(*) from messy_data where status not in ('completed','pending','failed','abandoned')"),'severity':'High'},{'check':'Self-referrals','count':count(c,'select count(*) from referrals where referrer_user_id=referred_user_id'),'severity':'Review'}]; c.close(); return jsonify({'checks':out,'notice':'Synthetic demonstration tables only.'})
@app.get('/api/transactions')
@auth
def transactions():
 s=request.args.get('status'); c=db(); q='select withdrawal_id,user_id,requested_amount,method,status,requested_at from withdrawals'; args=[]
 if s: q+=' where status=?'; args.append(s)
 q+=' order by requested_at desc limit 100'; out=[dict(x) for x in c.execute(q,args).fetchall()]; c.close(); return jsonify(out)
if __name__=='__main__':
 if not DB.exists():
  from backend.seed_database import seed; seed()
 app.run(host='0.0.0.0',port=int(os.getenv('PORT',5000)),debug=False)
