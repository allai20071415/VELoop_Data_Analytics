from backend.app import app

def test_health():
 with app.test_client() as c: assert c.get('/api/health').json['data_mode']=='SIMULATED'
def test_auth_required():
 with app.test_client() as c: assert c.get('/api/overview').status_code==401
def test_login_and_overview():
 with app.test_client() as c:
  assert c.post('/api/login',json={'email':'admin@demo.veloop','password':'DemoOnly!2026'}).status_code==200
  d=c.get('/api/overview').json; assert d['users']==1000 and d['data_mode']=='SIMULATED'
def test_quality():
 with app.test_client() as c:
  c.post('/api/login',json={'email':'admin@demo.veloop','password':'DemoOnly!2026'})
  assert len(c.get('/api/quality').json['checks'])>=4
