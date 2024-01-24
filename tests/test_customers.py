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



# Test Get all customers error while unauthentified
def test_get_customers_unauthorized_if_not_authentified():
  res = client.get("/customers")
  assert res.status_code == 401


# Test post customer success
def test_post_customer_success(auth_user):
  res = client.post("/customers", json={"name": "Alex"}, headers={"Authorization": f"Bearer {auth_user['access_token']}"})
  assert res.status_code == 201 


# Test create customer error
def test_post_customer_unauthorized_if_not_athentified():
  res = client.post("/customers", json={
  "name": "Alice"
})
  assert res.status_code == 401


# Test Patch customer success
  
# Test Patch customer error
  
# Test customer Delete Success
  
# Test customer Delete Error