from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid
from classes.schema_dto import Customer, CustomerNoId
from database.firebase import db

from routers.router_auth import get_current_user


router= APIRouter(
    prefix='/customers',
    tags=["Customers"]
)



customers = [
    Customer(id="customer1", name="Jhon Doe"),
    Customer(id="customer2", name="Maria Dias"),
    Customer(id="customer3", name="Karl Page")
]


# GET all customers
@router.get('/', response_model=List[Customer])
async def get_customers(userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("users").child(userData['uid']).child('customer').get(userData['idToken']).val()
    resultArray = [value for value in fireBaseobject.values()]
    return resultArray


# CREATE customer
@router.post('/', response_model=Customer, status_code=201)
async def create_customer(givenName:CustomerNoId, userData: int = Depends(get_current_user)):
    generatedId = uuid.uuid4()
    newCustomer = Customer(id=str(generatedId), name=givenName.name)
    
    db.child("users").child(userData['uid']).child("customer").child(str(generatedId)).set(newCustomer.model_dump(), userData['idToken'])
    customers.append(newCustomer)
    return newCustomer


# Get a customer by ID
@router.get('/{customer_id}', response_model=Customer)
async def get_customer_by_id(customer_id: str, userData: dict = Depends(get_current_user)):
    customer_data = db.child("users").child(userData['uid']).child('customer').child(str(customer_id)).get(userData['idToken']).val()
    
    if customer_data is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer = Customer(**customer_data)
    return customer


# PATCH customer
@router.patch('/{customer_id}', status_code=204)
async def modify_customer_name(customer_id:str, modifiedCustomer: CustomerNoId, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("users").child(userData['uid']).child('customer').child(customer_id).get(userData['idToken']).val()
    if fireBaseobject is not None:
        updatedCustomer = Customer(id=customer_id, **modifiedCustomer.model_dump())
        return db.child("users").child(userData['uid']).child('customer').child(customer_id).update(updatedCustomer.model_dump(), userData['idToken'] )
    raise HTTPException(status_code= 404, detail="Customer not found")


# DELETE customer
@router.delete('/{customer_id}', status_code=204)
async def delete_customer(customer_id: str, userData: int = Depends(get_current_user)):
    # Check if the customer exists in the database
    customer_data = db.child("users").child(userData['uid']).child('customer').child(str(customer_id)).get(userData['idToken']).val()
    
    if customer_data is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Delete the customer data
    db.child("users").child(userData['uid']).child('customer').child(str(customer_id)).remove(userData['idToken'])

    # Return a response with status code 204 (No Content) to indicate success
    return None