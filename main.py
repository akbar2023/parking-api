from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid 

import routers.router_auth, routers.router_parkings, routers.router_stripe


app = FastAPI(
  title="Parking API"
)


# Router dédié aux Parkings
app.include_router(routers.router_parkings, routers.router_auth,routers.router_stripe)

# Model static
class Parking(BaseModel):
  id: uuid
  is_available: bool
  price_per_hour: float

parkings = [
  Parking(id="1",is_available=True,price_per_hour=3.99),
  Parking(id="2",is_available=False,price_per_hour=2.99),
  Parking(id="3",is_available=True,price_per_hour=3.99),
]


@app.get('/parkings', response_model=list[Parking])
async def get_parking_places():
  return parkings

@app.post('/parkings', response_model=list[Parking], status_code=201)
async def create_parking_place(availability: bool):
  generatedId=uuid.uuid4()
  new_parking = Parking(id=generatedId, is_available=availability, price_per_hour=4.99)
  parkings.append(new_parking)
  return parkings

@app.get('/parkings/{parking_id}', response_model=Parking)
async def get_parking_by_id(parking_id:str):
  for parking in parkings:
    if parking.id == parking_id:
      return parking
    
  raise HTTPException(status_code=404,detail="Parking not found") 


@app.patch('/parkings/{parking_id}/{availability}')
async def update_parking_avilability(parking_id:str,availability:bool):
  for parking in parkings:
    if parking.id == parking_id:
       parking.available = availability
       return
  raise HTTPException(status_code=404, detail="parking not found")


