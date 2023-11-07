from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str


class Parking(BaseModel):
  id: str
  is_available: bool
  price_per_hour: float
  adress: str


class ParkingNoId(BaseModel):
  is_available: bool
  price_per_hour: float
  adress: str


class Customer(BaseModel):
  id: str
  name: str

class CustomerNoId(BaseModel):
  name: str


class Booking(BaseModel):
    id:str
    customer_id:str
    parking_id:str
    is_booked: bool


class BookingNoId(BaseModel):
    customer_id:str
    parking_id:str
    is_booked: bool