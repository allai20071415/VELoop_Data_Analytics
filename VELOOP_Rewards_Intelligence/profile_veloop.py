from pathlib import Path
import pandas as pd,json
ROOT=Path(__file__).resolve().parent
def profile():
 out=[]
 for p in (ROOT/'data').glob('*.csv'):
  df=pd.read_csv(p,comment='#'); out.append({'dataset':p.name,'rows':len(df),'columns':len(df.columns),'duplicate_rows':int(df.duplicated().sum()),'missing_cells':int(df.isna().sum().sum())})
 (ROOT/'reports'/'profile_run.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
if __name__=='__main__': profile()
