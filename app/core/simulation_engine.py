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

    def __init__(
        self,
        model=None,
        solver=None,
        dt: float = 0.01
    ):
        self.model = model
        self.solver = solver

        self.scheduler = Scheduler(dt)
        self.logger = Logger()

        self.state = None

        """
        Stores full simulation trajectory.
        """
        self.history = []

        """
        Stores simulation timestamps.
        """
        self.time_history = []

    def attach_model(self, model) -> None:
        """
        Attach dynamical system model and initialize state.
        """

        self.model = model
        self.state = model.initialize()

        self.logger.info(
            "Model attached and initialized."
        )

    def attach_solver(self, solver) -> None:
        """
        Attach numerical solver.
        """

        self.solver = solver

        self.logger.info(
            "Solver attached."
        )

    def step(self) -> dict:
        """
        Perform a single simulation step.
        """

        if self.model is None or self.solver is None:
            raise ValueError(
                "Model or solver not attached."
            )

        t = self.scheduler.step()
        dt = self.scheduler.dt

        self.state = self.solver.step(
            model=self.model,
            t=t,
            state=self.state,
            dt=dt
        )

        self.model.set_state(
            self.state
        )

        self.history.append(
            self.state.copy()
        )

        self.time_history.append(
            t
        )

        return self.state

    def run(self, steps: int = 100) -> dict:
        """
        Run simulation for given number of steps.
        """

        self.logger.info(
            "Simulation started."
        )

        self.scheduler.start()

        self.history = []
        self.time_history = []

        self.history.append(
            self.state.copy()
        )

        self.time_history.append(
            0.0
        )

        for _ in range(steps):
            self.step()

        self.scheduler.stop()

        self.logger.info(
            "Simulation finished."
        )

        return {
            "time": self.time_history,
            "states": self.history
        }

    def reset(self) -> None:
        """
        Reset simulation state and scheduler.
        """

        self.scheduler.reset()

        self.history = []
        self.time_history = []

        if self.model is not None:
            self.state = self.model.initialize()
            self.model.set_state(
                self.state
            )

        self.logger.info(
            "Simulation reset."
        )