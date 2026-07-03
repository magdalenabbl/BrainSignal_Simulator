from typing import Dict, Any


class A_RK4Solver:
    """
    Classic 4th-order Runge-Kutta solver for ODE systems.

    Works with:
    model.derivatives(t, state)
    state: dict-based system state
    """

    def step(
        self,
        model: Any,
        t: float,
        state: Dict[str, float],
        dt: float
    ) -> Dict[str, float]:
        """
        Perform one RK4 integration step.
        """

        # k1
        k1 = model.derivatives(t, state)

        # k2 state
        state_k2 = {
            key: state[key] + 0.5 * dt * k1[key]
            for key in state
        }
        k2 = model.derivatives(t + 0.5 * dt, state_k2)

        # k3 state
        state_k3 = {
            key: state[key] + 0.5 * dt * k2[key]
            for key in state
        }
        k3 = model.derivatives(t + 0.5 * dt, state_k3)

        # k4 state
        state_k4 = {
            key: state[key] + dt * k3[key]
            for key in state
        }
        k4 = model.derivatives(t + dt, state_k4)

        # final update
        new_state = {}

        for key in state:
            new_state[key] = state[key] + (dt / 6.0) * (
                k1[key]
                + 2.0 * k2[key]
                + 2.0 * k3[key]
                + k4[key]
            )

        return new_state