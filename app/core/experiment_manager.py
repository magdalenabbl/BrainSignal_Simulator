from app.core.configurable import Configurable
from app.core.serializable import Serializable
from app.core.simulation_engine import SimulationEngine
from app.models.base_model import BaseModel
from app.solvers.ode_solver import ODESolver


class ExperimentManager(Configurable, Serializable):
    """Manages simulation experiments."""

    def __init__(self, engine: SimulationEngine):
        """Initialize experiment manager."""

        self.engine = engine

    def configure(self, model: BaseModel, solver: ODESolver, dt: float = 0.01) -> None:
        """Configure experiment components."""

        self.engine.scheduler.dt = dt
        self.engine.attach_model(model)
        self.engine.attach_solver(solver)

    def run(self, steps: int = 100) -> dict:
        """Run experiment."""

        return self.engine.run(steps)

    def step(self) -> dict:
        """Execute one simulation step."""

        return self.engine.step()

    def reset(self) -> None:
        """Reset experiment."""

        self.engine.reset()

    def get_state(self) -> dict:
        """Return current simulation state."""

        return self.engine.state