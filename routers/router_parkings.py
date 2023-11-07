from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import Annotated
import uuid
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from classes.schema_dto import Parking, ParkingNoId
import uuid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

router = APIRouter(
    prefix='/parkings',
    tags=['Parkings']
)

from database.firebase import db



parkings = [
  Parking(id= "parking1", is_available=False, price_per_hour=4.99, adress= "124 rue Réaumur 75002 Paris"),
  Parking(id= "parking2", is_available=True, price_per_hour=4.99, adress= "10 rue manin 75019 Paris"),
  Parking(id= "parking3", is_available=True, price_per_hour=5.99, adress= "2 avenue victor hugo 75010 Paris"),
]



# GET parkings
@router.get('/', response_model=list[Parking])
async def get_parking_places():
  return parkings

# CREATE Parkings
@router.post('/', response_model= Parking, status_code=201)
async def create_parking_place(givenParking: ParkingNoId):
  newParking = Parking(givenParking)
  newParking.id = str(uuid.uuid4())
  parkings.append(newParking)
  return parkings

# GET BY ID parkings
@router.get('/{parking_id}', response_model=Parking)
async def get_parking_by_id(parking_id:str):
  for parking in parkings:
    if parking.id == parking_id:
      return parking
  raise HTTPException(status_code=404,detail="Parking not found") 

# PATCH Parking
@router.patch('/{parking_id}/{availability}', status_code=204)
async def update_parking_avilability(parking_id:str, availability:bool):
  for parking in parkings:
    if parking.id == parking_id:
      parking.is_available = availability
      return
  raise HTTPException(status_code= 404, detail="Parking not found")

# DELETE parking
@router.delete('/{parking_id}', status_code=204)
async def delete_student(parking_id:str):
    for parking in parkings:
        if parking.id == parking_id:
            parkings.remove(parking)
            return
    raise HTTPException(status_code= 404, detail="parking not found")