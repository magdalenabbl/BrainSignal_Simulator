from fastapi import APIRouter #instrument that makes groups of API funcs
from app.api.simulation_routes import router as simulation_router


api_router = APIRouter()

api_router.include_router(
    simulation_router,
    prefix="/simulation",
    tags=["Simulation"]
)