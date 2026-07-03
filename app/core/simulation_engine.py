from app.core.scheduler import Scheduler
from app.data.simulation_result import SimulationResult
from app.neural.ann import ANN


class SimulationEngine:

    def __init__(self, model=None, solver=None, dt: float = 0.01):
        self.model = model
        self.solver = solver
        self.scheduler = Scheduler(dt)

        self.state = None
        self.history = []
        self.time_history = []

    def attach_model(self, model):
        self.model = model
        self.state = model.initialize()

    def attach_solver(self, solver):
        self.solver = solver

    def step(self):

        t = self.scheduler.step()

        # =========================
        # ANN MODE (SAFE)
        # =========================
        if isinstance(self.model, ANN):

            base = self.state.get("x", 1.0)
            x = [base, base * 0.9, base * 0.8]

            self.state = self.model.step(x)

        # =========================
        # ODE MODE
        # =========================
        else:

            self.state = self.solver.step(
                model=self.model,
                t=t,
                state=self.state,
                dt=self.scheduler.dt
            )

        self.model.set_state(self.state)

        self.history.append(dict(self.state))
        self.time_history.append(t)

        return self.state

    def run(self, steps: int):

        self.history = []
        self.time_history = []

        self.history.append(dict(self.state))
        self.time_history.append(0.0)

        for _ in range(steps):
            self.step()

        return SimulationResult(
            time_points=self.time_history,
            states=self.history,
            model_name=self.model.__class__.__name__,
            solver_name=self.solver.__class__.__name__
        )