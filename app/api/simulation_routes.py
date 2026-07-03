from fastapi import APIRouter, HTTPException

from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.services.simulation_service import SimulationService


router = APIRouter()
simulation_service = SimulationService()


@router.post("/run", response_model=SimulationResponse)
def run_simulation(request: SimulationRequest):

    try:
        result = simulation_service.run_simulation(
            model_name=request.model,
            solver_name=request.solver,
            T=request.T,
            dt=request.dt,
            params=request.params
        )

        return SimulationResponse(
            model=result.model_name,
            solver=result.solver_name,
            time=result.time_points,
            states=result.states
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )