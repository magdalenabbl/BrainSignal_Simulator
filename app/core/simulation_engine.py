from typing import Dict, Optional

from app.core.scheduler import Scheduler
from app.core.logger import Logger
from app.core.simulation_component import SimulationComponent
from app.solvers.ode_solver import ODESolver


class SimulationEngine:
    """
    Core simulation runtime engine.

    Responsible for:
    - time management
    - solver orchestration
    - model execution
    - state tracking
    """

    def __init__(
        self,
        model: Optional[SimulationComponent] = None,
        solver: Optional[ODESolver] = None,
        dt: float = 0.01
    ):
        self.model = model
        self.solver = solver

        self.scheduler = Scheduler(dt)
        self.logger = Logger()

        self.state: Optional[Dict[str, float]] = None

    def attach_model(
        self,
        model: SimulationComponent
    ) -> None:
        """
        Attach simulation model.
        """

        self.model = model
        self.state = model.initialize()

        self.model.set_state(self.state)

        self.logger.info(
            "Model attached and initialized."
        )

    def attach_solver(
        self,
        solver: ODESolver
    ) -> None:
        """
        Attach numerical solver.
        """

        self.solver = solver

        self.logger.info(
            "Solver attached."
        )

    def step(self) -> Dict[str, float]:
        """
        Perform one simulation step.
        """

        if self.model is None:
            raise ValueError(
                "Model is not attached."
            )

        if self.solver is None:
            raise ValueError(
                "Solver is not attached."
            )

        t = self.scheduler.step()
        dt = self.scheduler.dt

        self.state = self.solver.step(
            model=self.model,
            t=t,
            state=self.state,
            dt=dt
        )

        self.model.set_state(self.state)

        self.logger.info(
            f"Step completed at t={t}"
        )

        return self.state

    def run(
        self,
        steps: int = 100
    ) -> Dict[str, float]:
        """
        Run simulation.
        """

        self.logger.info(
            "Simulation started."
        )

        self.scheduler.start()

        for _ in range(steps):
            self.step()

        self.scheduler.stop()

        self.logger.info(
            "Simulation finished."
        )

        return self.state

    def reset(self) -> None:
        """
        Reset simulation.
        """

        self.scheduler.reset()

        if self.model:
            self.model.reset()
            self.state = self.model.get_state()

        self.logger.info(
            "Simulation reset."
        )