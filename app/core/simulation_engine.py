from app.core.scheduler import Scheduler
from app.core.logger import Logger


class SimulationEngine:
    """
    Core simulation runtime engine.

    Responsible for:
    - time management
    - solver orchestration
    - model execution
    - state tracking
    """

    def __init__(self, model=None, solver=None, dt: float = 0.01):
        self.model = model
        self.solver = solver

        self.scheduler = Scheduler(dt)
        self.logger = Logger()

        self.state = None

    def attach_model(self, model) -> None:
        """
        Attach dynamical system model and initialize state.
        """
        self.model = model
        self.state = model.initialize()

        if hasattr(self.model, "set_state"):
            self.model.set_state(self.state)

        self.logger.info("Model attached and initialized.")

    def attach_solver(self, solver) -> None:
        """
        Attach numerical solver.
        """
        self.solver = solver
        self.logger.info("Solver attached.")

    def step(self) -> dict:
        """
        Perform a single simulation step.
        Returns updated state.
        """

        if self.model is None or self.solver is None:
            raise ValueError("Model or solver not attached.")

        t = self.scheduler.step()
        dt = self.scheduler.dt

        self.state = self.solver.step(
            model=self.model,
            t=t,
            state=self.state,
            dt=dt
        )

        if hasattr(self.model, "set_state"):
            self.model.set_state(self.state)

        self.logger.info(f"Step completed at t={t}")

        return self.state

    def run(self, steps: int = 100) -> dict:
        """
        Run full simulation for given number of steps.
        """

        self.logger.info("Simulation started")
        self.scheduler.start()

        for _ in range(steps):
            self.step()

        self.scheduler.stop()

        self.logger.info("Simulation finished")

        return self.state

    def reset(self) -> None:
        """
        Reset simulation state and scheduler.
        """

        self.scheduler.reset()

        if self.model is not None:
            self.state = self.model.initialize()

            if hasattr(self.model, "set_state"):
                self.model.set_state(self.state)

        self.logger.info("Simulation reset.")