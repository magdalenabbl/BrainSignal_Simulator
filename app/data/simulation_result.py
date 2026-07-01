from typing import Dict, List


class SimulationResult:
    """
    Stores complete simulation output.
    """

    def __init__(
        self,
        time: List[float],
        states: List[Dict[str, float]],
        model: str,
        solver: str
    ):
        self.time = time
        self.states = states
        self.model = model
        self.solver = solver

    def to_dict(self) -> dict:
        """
        Convert result to serializable format.
        """

        return {
            "model": self.model,
            "solver": self.solver,
            "time": self.time,
            "states": self.states
        }