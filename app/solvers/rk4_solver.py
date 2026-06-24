from typing import Dict, Any
from app.solvers.ode_solver import ODESolver


class RK4Solver(ODESolver):
    """Runge-Kutta 4th order solver."""

    def step(
        self,
        model: Any,
        t: float,
        state: Dict[str, float],
        dt: float
    ) -> Dict[str, float]:

        k1 = model.derivatives(t, state)

        state_k2 = {
            k: state[k] + 0.5 * dt * k1[k]
            for k in state
        }
        k2 = model.derivatives(t + 0.5 * dt, state_k2)

        state_k3 = {
            k: state[k] + 0.5 * dt * k2[k]
            for k in state
        }
        k3 = model.derivatives(t + 0.5 * dt, state_k3)

        state_k4 = {
            k: state[k] + dt * k3[k]
            for k in state
        }
        k4 = model.derivatives(t + dt, state_k4)

        new_state = {
            k: state[k] + (dt / 6.0) * (
                k1[k] + 2 * k2[k] + 2 * k3[k] + k4[k]
            )
            for k in state
        }

        return new_state