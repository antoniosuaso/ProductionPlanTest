from fastapi import APIRouter
from constants import URL_PREFIX
from api.endpoints import production_plant

# Declaration of the APIRouter with prefix

api_router = APIRouter(prefix=URL_PREFIX)

# Include the endpoint router to the APIRouter with it's own prefix

api_router.include_router(production_plant.router, prefix="/calculate")
