from pathlib import Path
import sqlite3,os,pandas as pd
ROOT=Path(__file__).resolve().parents[1]; DB=Path(os.getenv('DATABASE_PATH',ROOT/'backend'/'veloop_demo.db'))
def seed():
 if DB.exists(): DB.unlink()
 con=sqlite3.connect(DB)
 for fn,t in [('users.csv','users'),('task_activity.csv','task_activity'),('rewards.csv','rewards'),('wallet_transactions.csv','wallet_transactions'),('withdrawals.csv','withdrawals'),('referrals.csv','referrals'),('feature_events.csv','feature_events'),('messy_data.csv','messy_data')]:
  pd.read_csv(ROOT/'data'/fn,comment='#').to_sql(t,con,index=False,if_exists='replace')
 con.close(); print('Demo database seeded:',DB)
if __name__=='__main__': seed()
