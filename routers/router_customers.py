from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from classes.schema_dto import Customer, CustomerNoId



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
async def get_customers():
    return customers


# CREATE customer
@router.post('/', response_model=Customer, status_code=201)
async def create_customer(givenName:CustomerNoId):
    generatedId = uuid.uuid4()
    newCustomer = Customer(id=str(generatedId), name=givenName)
    customers.append(newCustomer)
    return newCustomer


# GET customer by id
@router.get('/{customer_id}', response_model=Customer)
async def get_customer_by_ID(customer_id:str):
    for customer in customers:
        if customer.id == customer_id:
            return customer
    raise HTTPException(status_code= 404, detail="customer not found")

# PATCH customer
@router.patch('/{customer_id}', status_code=204)
async def modify_customer_name(customer_id:str, modifiedCustomer: CustomerNoId):
    for customer in customers:
        if customer.id == customer_id:
            customer.name=modifiedCustomer.name
            return
    raise HTTPException(status_code= 404, detail="customer not found")


# DELETE customer
@router.delete('/{customer_id}', status_code=204)
async def delete_customer(customer_id:str):
    for customer in customers:
        if customer.id == customer_id:
            customers.remove(customer)
            return
    raise HTTPException(status_code= 404, detail="customer not found")