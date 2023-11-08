import uuid
from fastapi import APIRouter, HTTPException

from classes.schema_dto import Booking, BookingNoId



router= APIRouter(
    prefix='/bookings',
    tags=["Bookings"]
)


bookings = [
    Booking(id="booking1", customer_id="customer1", parking_id="parking1", is_booked=True),
    Booking(id="booking2", customer_id="customer2", parking_id="parking2", is_booked=False),
    Booking(id="booking3", customer_id="customer3", parking_id="parking3", is_booked=True)
]


@router.get('/')
async def create_booking():
    return bookings


@router.post('/')
async def create_booking(givenBooking:BookingNoId):
    newbooking= Booking(id=str(uuid.uuid4()), **givenBooking.model_dump())
    bookings.append(newbooking)
    return newbooking



@router.get('/{booking_id}')
async def get_booking_by_ID(booking_id:str):
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise HTTPException(status_code= 404, detail="booking not found")


@router.patch('/{booking_id}')
async def modify_booking(booking_id:str, modifiedBooking:BookingNoId):
    for booking in bookings : 
        if booking.id == booking_id and booking.customer_id == modifiedBooking.customer_id and booking.parking_id == modifiedBooking.parking_id:
            booking.is_booked = modifiedBooking.is_booked        
            return booking
    raise HTTPException(status_code= 404, detail="booking not found")



@router.delete('/{booking_id}', status_code=204)
async def delete_booking(booking_id:str):
    for booking in bookings:
        if booking.id == booking_id:
            bookings.remove(booking)
            return
    raise HTTPException(status_code= 404, detail="booking not found")