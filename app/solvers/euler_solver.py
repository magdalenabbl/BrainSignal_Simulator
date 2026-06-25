from typing import Dict, Any

from app.solvers.ode_solver import ODESolver


class EulerSolver(ODESolver):
    """
    First order Euler ODE solver.
    """

    def step(
        self,
        model: Any,
        t: float,
        state: Dict[str, float],
        dt: float
    ) -> Dict[str, float]:
        """
        Perform Euler integration step.
        """

        derivatives = model.derivatives(
            t,
            state
        )

        return {
            key: state[key] + dt * derivatives[key]
            for key in state
        }