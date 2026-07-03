import json

from app.data.simulation_result import SimulationResult


class SimulationStorage:

    def save(self, result: SimulationResult, path: str):
        with open(path, "w") as file:
            json.dump(result.to_dict(), file)

    def load(self, path: str) -> SimulationResult:
        with open(path, "r") as file:
            data = json.load(file)

        return SimulationResult(
            time_points=data["time"],
            states=data["states"],
            model_name=data["model"],
            solver_name=data["solver"]
        )