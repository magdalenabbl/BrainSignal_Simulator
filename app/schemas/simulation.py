from pydantic import BaseModel
from typing import Dict, Any, Literal


class SimulationRequest(BaseModel):
    model: Literal["lif", "lorenz", "izhikevich"]
    solver: Literal["euler", "rk4", "adaptive_rk"]
    T: float
    dt: float
    params: Dict[str, Any] = {}
    
class SimulationResponse(BaseModel):
    result: list
    model: str
    solver: str