from pydantic import BaseModel
from typing import Dict, Any, Literal, List


class SimulationRequest(BaseModel):
    model: Literal[
        "lif",
        "lorenz",
        "izhikevich"
    ]

    solver: Literal[
        "euler",
        "rk4",
        "adaptive_rk"
    ]

    T: float
    dt: float

    params: Dict[str, Any] = {}


class SimulationResponse(BaseModel):
    model: str
    solver: str
    time: List[float]
    states: List[Dict[str, float]]