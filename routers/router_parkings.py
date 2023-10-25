from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from classes.database import get_cursor
from classes import models_orm, schemas_dto
import utilities
from typing_extensions import Annotated
import uuid
from fastapi.security import OAuth2PasswordBearer
from main import Parking 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

router = APIRouter(
    prefix='/parkings',
    tags=['Parkings']
)

from database.firebase import db


@router.post('/', response_model= Parking, status_code=201)
async def create_parking_place(availability: bool):
  generatedId= "fdgr"
  new_parking = Parking(id=generatedId, is_available=availability, price_per_hour=4.99)
  parkings.append(new_parking)
  return parkings


@app.get('/{parking_id}', response_model=Parking)
async def get_parking_by_id(parking_id:str):
  for parking in parkings:
    if parking.id == parking_id:
      return parking
    
  raise HTTPException(status_code=404,detail="Parking not found") 


@app.patch('/{parking_id}/{availability}')
async def update_parking_avilability(parking_id:str,availability:bool):
  fireBaseobject = db.child('parking').child(parking_id).get().val()
  if fireBaseobject is not None:
    update_parking_avilability = Parking(id=parking_id, is_available=)
  for parking in parkings:
    if parking.id == parking_id:
       parking.available = availability
       return
  raise HTTPException(status_code=404, detail="parking not found")