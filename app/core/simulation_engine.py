from app.core.logger import Logger
from app.core.scheduler import Scheduler
from app.data.simulation_result import SimulationResult


class SimulationEngine:

    def __init__(self, model=None, solver=None, dt: float = 0.01):
        self.model = model
        self.solver = solver

        self.scheduler = Scheduler(dt)
        self.logger = Logger()

        self.state = None
        self.history = []
        self.time_history = []

    def attach_model(self, model) -> None:
        self.model = model
        self.state = model.initialize()

        self.logger.info(
            "Model attached and initialized."
        )

    def attach_solver(self, solver) -> None:
        self.solver = solver

        self.logger.info(
            "Solver attached."
        )

    def step(self) -> dict:
        if self.model is None or self.solver is None:
            raise ValueError(
                "Model or solver not attached."
            )

        current_time = self.scheduler.step()
        time_step = self.scheduler.dt

        self.state = self.solver.step(
            model=self.model,
            t=current_time,
            state=self.state,
            dt=time_step
        )

        self.model.set_state(self.state)

        self.history.append(
            self.state.copy()
        )

        self.time_history.append(
            current_time
        )

        return self.state

    def run(self, steps: int = 100) -> SimulationResult:
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

        return SimulationResult(
            time_points=self.time_history,
            states=self.history,
            model_name=self.model.__class__.__name__,
            solver_name=self.solver.__class__.__name__
        )

    def reset(self) -> None:
        self.scheduler.reset()

        self.history = []
        self.time_history = []

        if self.model is not None:
            self.state = self.model.initialize()
            self.model.set_state(self.state)

        self.logger.info(
            "Simulation reset."
        )