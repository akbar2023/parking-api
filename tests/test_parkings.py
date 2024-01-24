from fastapi.testclient import TestClient
from main import app
from firebase_admin import auth
import pytest

client = TestClient(app)



# Test create parking success
def test_post_parking_success():
  res = client.post("/parkings", json={
  "is_available": 'true',
  "price_per_hour": '4.99',
  "adress": "10 rue manin 75019 Paris"
})
  assert res.status_code == 201 


# Test create parking error
def test_post_parking_error():
  res = client.post("/parkings", json={
  "price_per_hour": '4.99',
  "adress": "10 rue manin 75019 Paris"
})
  assert res.status_code == 422

# Test get all parkings
def test_get_all_parkings():
  res = client.get("/parkings")
  assert res.status_code == 200

# Test get parking by id
def test_get_parking_by_id_success():
  res = client.get("/parkings/parking1")
  assert res.status_code == 200

# Test Get parking by id error
def test_get_parking_by_id_error():
  res = client.get("/parkings/wrongId")
  assert res.status_code == 404

# Test Patch parking availability
def test_patch_parking_availability():
  res = client.patch("/parkings/parking1/false")
  assert res.status_code == 204


# Test Patch parking availability error
def test_patch_parking_availability_error():
  res = client.patch("/parkings/parking1/hfdhfj")
  assert res.status_code == 422


# Test Delete parking success
def test_delete_parking_success():
  res = client.delete("/parkings/parking1")
  assert res.status_code == 204

# Test Delete parking Error (Delete again with same id)
def test_delete_parking_error():
  res = client.delete("/parkings/parking1")
  assert res.status_code == 404