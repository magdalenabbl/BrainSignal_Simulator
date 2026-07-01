from typing import Dict, Any

from app.core.simulation_engine import SimulationEngine

from app.models.lif_neuron import LIFNeuron
from app.models.izhikevich import IzhikevichNeuron
from app.models.lorenz_system import LorenzSystem

from app.solvers.euler_solver import EulerSolver
from app.solvers.rk4_solver import RK4Solver


class SimulationService:
    """
    Service layer for creating and running simulations.
    """

    MODEL_REGISTRY = {
        "lif": LIFNeuron,
        "izhikevich": IzhikevichNeuron,
        "lorenz": LorenzSystem,
    }

    SOLVER_REGISTRY = {
        "euler": EulerSolver,
        "rk4": RK4Solver,
    }

    def create_model(
        self,
        model_name: str,
        params: Dict[str, Any] | None = None
    ):
        """
        Create model instance by name.
        """

        model_class = self.MODEL_REGISTRY.get(model_name)

        if model_class is None:
            raise ValueError(
                f"Unknown model: {model_name}"
            )

        return model_class(params)

    def create_solver(
        self,
        solver_name: str
    ):
        """
        Create solver instance by name.
        """

        solver_class = self.SOLVER_REGISTRY.get(solver_name)

        if solver_class is None:
            raise ValueError(
                f"Unknown solver: {solver_name}"
            )

        return solver_class()

    def run_simulation(
        self,
        model_name: str,
        solver_name: str,
        T: float,
        dt: float,
        params: Dict[str, Any] | None = None
    ):
        """
        Configure and execute simulation.
        """

        model = self.create_model(
            model_name,
            params
        )

        solver = self.create_solver(
            solver_name
        )

        steps = int(T / dt)

        engine = SimulationEngine(
            dt=dt
        )

        engine.attach_model(model)
        engine.attach_solver(solver)

        return engine.run(steps)