from typing import Dict, List
from app.data.time_series import TimeSeries


class SimulationResult:

    def __init__(self, time_points: List[float], states: List[Dict[str, float]], model_name: str, solver_name: str):
        self.time_points = time_points
        self.states = states
        self.model_name = model_name
        self.solver_name = solver_name

    def get_final_state(self) -> Dict[str, float]:
        return self.states[-1]

    def to_dataset(self) -> TimeSeries:
        return TimeSeries(time_points=self.time_points, states=self.states
        )

    def to_dict(self) -> dict:
        return {
            "model": self.model_name,
            "solver": self.solver_name,
            "time": self.time_points,
            "states": self.states
        }