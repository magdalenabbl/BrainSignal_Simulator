from app.models.lif_neuron import LIFNeuron
from app.models.lorenz_system import LorenzSystem

from app.solvers.euler_solver import EulerSolver
from app.solvers.rk4_solver import RK4Solver
from app.solvers.adaptive_rk_solver import AdaptiveRK

from app.core.simulation_engine import SimulationEngine


class SimulationService:
    """
    Connects API layer with simulation engine.
    """

    def create_model(self, model_name: str, params: dict):

        if model_name == "lif":
            return LIFNeuron(**params)

        if model_name == "lorenz":
            return LorenzSystem(**params)

        raise ValueError("Unknown model")

    def create_solver(self, solver_name: str):

        if solver_name == "euler":
            return EulerSolver()

        if solver_name == "rk4":
            return RK4Solver()

        if solver_name == "adaptive_rk":
            return AdaptiveRK()

        raise ValueError("Unknown solver")

    def run(self, request):

        model = self.create_model(request.model, request.params)
        solver = self.create_solver(request.solver)

        engine = SimulationEngine(model, solver)

        return engine.run(request.T, request.dt)