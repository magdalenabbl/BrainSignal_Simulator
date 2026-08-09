from fastapi import APIRouter  # Tool for grouping API endpoints
from app.api.simulation_routes import router as simulation_router
from app.api.ann_routes import router as ann_router


# Main API router - routers from different parts of the application
api_router = APIRouter()

# simulation endpoints  /simulation/run
api_router.include_router(
    simulation_router,
    prefix="/simulation",
    tags=["Simulation"]
)

# ANN endpoints  /ann/train; /ann/infer
api_router.include_router(
    ann_router,
    prefix="/ann",
    tags=["ANN"]
)