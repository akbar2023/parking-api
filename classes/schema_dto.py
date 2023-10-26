from pydantic import BaseModel
import uuid 

class User(BaseModel):
    email: str
    password: str


class Parking(BaseModel):
  id: uuid
  place_num: int
  is_available: bool
  price_per_hour: float
  lon: float
  lar: float
  location: str


class ParkingNoId(BaseModel):
  place_num: int
  is_available: bool
  price_per_hour: float
  lon: float
  lar: float
  location: str

