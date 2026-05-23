# solvers/adaptive_rk_solver.py

from solvers.ode_solver import ODESolver
from solvers.rk4_solver import RK4Solver
from solvers.euler_solver import EulerSolver


class AdaptiveRK(ODESolver):
    """
    Adaptive step solver using error estimation.
    """

    def __init__(self):
        self.rk4 = RK4Solver()
        self.euler = EulerSolver()

    def step(self, model, t: float, dt: float) -> dict:

        state1 = self.euler.step(model, t, dt)
        model.set_state(state1)

        state2 = self.rk4.step(model, t, dt)

        error = max(
            abs(state2[k] - state1[k]) for k in state1.keys()
        )

        # Adaptive step control (simplified)
        if error > 0.01:
            dt *= 0.5
        elif error < 0.001:
            dt *= 1.1

        model.set_state(state2)

        return state2