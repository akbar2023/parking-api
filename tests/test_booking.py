from fastapi.testclient import TestClient
from main import app
from firebase_admin import auth
import pytest

client = TestClient(app)







# Test Get all bookings
def test_get_all_bookings():
  res = client.get("/bookings")
  assert res.status_code == 200


# Test post Bookings success



# Test create Bookings error



# Test Patch Bookings success
  
# Test Patch Bookings error
  
# Test Bookings Delete Success
  
# Test Bookings Delete Error