from fastapi import APIRouter, HTTPException

from app.services.simulation_service import SimulationService
from app.schemas.simulation import SimulationRequest


router = APIRouter()

simulation_service = SimulationService()


@router.post("/run")
def run_simulation(request: SimulationRequest):
    """
    Run numerical simulation.
    """

    try:
        result = simulation_service.run_simulation(
            model_name=request.model,
            solver_name=request.solver,
            steps=request.steps,
            params=request.params
        )

        return {
            "status": "success",
            "state": result
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )