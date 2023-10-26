from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str


class Parking(BaseModel):
  id: str
  ref_num: int
  is_available: bool
  price_per_hour: float
  lon: float
  lar: float
  adress: str


class ParkingNoId(BaseModel):
  ref_num: int
  is_available: bool
  price_per_hour: float
  lon: float
  lar: float
  adress: str

