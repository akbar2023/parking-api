from fastapi.testclient import TestClient
from main import app
from firebase_admin import auth
import pytest

client = TestClient(app)



# Test create parking success
def test_create_parking_success():
    res = client.post("/parkings", json={
    "is_available": 'true',
    "price_per_hour": '4.99',
    "adress": "10 rue manin 75019 Paris"
  })
    assert res.status_code == 201 

# Test create parking error
def test_create_parking_error():
    res = client.post("/parkings", json={
    "price_per_hour": '4.99',
    "adress": "10 rue manin 75019 Paris"
  })
    assert res.status_code == 422