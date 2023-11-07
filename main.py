from fastapi import FastAPI, HTTPException

#Routers
import routers.router_auth, routers.router_parkings, routers.router_stripe, routers.router_customers, routers.router_bookings

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata


app = FastAPI(
  title="Parking API",
  description= api_description,
  opean_api_tags= tags_metadata,
  docs_url='/'
)


# Routers Parkings
app.include_router(routers.router_parkings.router)
app.include_router(routers.router_auth.router)
app.include_router(routers.router_stripe.router)
app.include_router(routers.router_customers.router)
app.include_router(routers.router_bookings.router)


