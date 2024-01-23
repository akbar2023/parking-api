from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    res = client.post("/auth/signup", json={
        "email": "test.user1@gmail.com" , "password": "password"
    })
    assert res.status_code == 201 