from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import Annotated
import uuid
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from classes.schema_dto import Parking
import uuid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

router = APIRouter(
    prefix='/parkings',
    tags=['Parkings']
)

from database.firebase import db



parkings = [
  Parking(id= str(uuid.uuid4()), ref_num= 15, is_available=True, price_per_hour=3.99, lon=3.10, lar= 2.01, adress= "12 rue jean rostand 75019 Paris"),
  Parking(id= str(uuid.uuid4()), ref_num= 20, is_available=True, price_per_hour=4.99, lon=4.00, lar= 2.20, adress= "10 rue manin 75019 Paris"),
  Parking(id= str(uuid.uuid4()), ref_num= 45, is_available=True, price_per_hour=5.99, lon=3.80, lar= 2.50, adress= "2 avenue victor hugo 75010 Paris"),
]


@router.get('/parkings', response_model=list[Parking])
async def get_parking_places():
  return parkings


# @router.post('/', response_model= Parking, status_code=201)
# async def create_parking_place(availability: bool):
#   generatedId= "fdgr"
#   new_parking = Parking(id=generatedId, is_available=availability, price_per_hour=4.99)
#   parkings.append(new_parking)
#   return parkings


# @app.get('/{parking_id}', response_model=Parking)
# async def get_parking_by_id(parking_id:str):
#   for parking in parkings:
#     if parking.id == parking_id:
#       return parking
    
#   raise HTTPException(status_code=404,detail="Parking not found") 


# @app.patch('/{parking_id}/{availability}')
# async def update_parking_avilability(parking_id:str,availability:bool):
#   fireBaseobject = db.child('parking').child(parking_id).get().val()
#   if fireBaseobject is not None:
#     update_parking_avilability = Parking(id=parking_id, is_available=)
#   for parking in parkings:
#     if parking.id == parking_id:
#        parking.available = availability
#        return
#   raise HTTPException(status_code=404, detail="parking not found")