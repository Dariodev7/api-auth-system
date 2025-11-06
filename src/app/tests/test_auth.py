from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_register_and_login():
    r = client.post('/auth/register', json={'name':'Dario','email':'dario@test.com','password':'senha123'})
    assert r.status_code == 200
    r2 = client.post('/auth/login', json={'name':'Dario','email':'dario@test.com','password':'senha123'})
    assert r2.status_code == 200
    assert 'access_token' in r2.json()
