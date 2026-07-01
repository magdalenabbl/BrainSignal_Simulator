from fastapi import APIRouter

from app.api.simulation_routes import router as simulation_router


api_router = APIRouter()


api_router.include_router(
    simulation_router,
    prefix="/simulation",
    tags=["Simulation"]
)