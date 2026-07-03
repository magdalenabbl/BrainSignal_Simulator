from typing import Any, Dict

from app.core.simulation_engine import SimulationEngine
from app.models.izhikevich import IzhikevichNeuron
from app.models.lif_neuron import LIFNeuron
from app.models.lorenz_system import LorenzSystem
from app.solvers.euler_solver import EulerSolver
from app.solvers.rk4_solver import RK4Solver
from app.neural.ann import ANN
from app.solvers.adaptive_rk_solver import A_RK4Solver
class SimulationService:

    MODEL_REGISTRY = {
        "lif": LIFNeuron,
        "izhikevich": IzhikevichNeuron,
        "lorenz": LorenzSystem,
        "ann": ANN
    }

    SOLVER_REGISTRY = {
        "euler": EulerSolver,
        "rk4": RK4Solver,
        "adaptive_rk": A_RK4Solver
    }

    def create_model(self, model_name: str, params: Dict[str, Any] | None = None):
        model_class = self.MODEL_REGISTRY.get(model_name)

        if model_class is None:
            raise ValueError(
                f"Unknown model: {model_name}"
            )

        return model_class(params)

    def create_solver(self, solver_name: str):
        solver_class = self.SOLVER_REGISTRY.get(solver_name)

        if solver_class is None:
            raise ValueError(
                f"Unknown solver: {solver_name}"
            )

        return solver_class()

    def run_simulation(self, model_name: str, solver_name: str, T: float, dt: float, params: Dict[str, Any] | None = None):
        model = self.create_model(
            model_name,
            params
        )

        solver = self.create_solver(
            solver_name
        )

        engine = SimulationEngine(
            dt=dt
        )

        engine.attach_model(model)
        engine.attach_solver(solver)

        steps = int(T / dt)

        return engine.run(steps)