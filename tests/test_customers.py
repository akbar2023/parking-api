from fastapi.testclient import TestClient
from main import app
from firebase_admin import auth
import pytest

client = TestClient(app)




# Test Get all customers being authentified
def test_get_customers_success(auth_user):
  res = client.get("/customers", headers={
    "Authorization": f"Bearer {auth_user['access_token']}"
  })
  assert res.status_code == 200



# Test Get all customers being unauthentified
def test_get_customers_error():
  res = client.get("/customers")
  assert res.status_code == 401