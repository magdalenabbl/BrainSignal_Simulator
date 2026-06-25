from typing import Dict, Any

from app.solvers.ode_solver import ODESolver


class ImprovedEulerSolver(ODESolver):
    """
    Second order Improved Euler solver.
    """

    def step(
        self,
        model: Any,
        t: float,
        state: Dict[str, float],
        dt: float
    ) -> Dict[str, float]:
        """
        Perform Improved Euler integration step.
        """

        k1 = model.derivatives(
            t,
            state
        )

        predicted_state = {
            key: state[key] + dt * k1[key]
            for key in state
        }

        k2 = model.derivatives(
            t + dt,
            predicted_state
        )

        return {
            key: state[key]
            + (dt / 2.0)
            * (k1[key] + k2[key])
            for key in state
        }