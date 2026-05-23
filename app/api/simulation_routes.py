from fastapi import APIRouter

from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.services.simulation_service import SimulationService

router = APIRouter()
service = SimulationService()


@router.post("/simulate", response_model=SimulationResponse)
def simulate(request: SimulationRequest):

    result = service.run(request)

    return SimulationResponse(
        result=result,
        model=request.model,
        solver=request.solver
    )