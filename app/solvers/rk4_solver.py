# solvers/rk4_solver.py

from solvers.ode_solver import ODESolver


class RK4Solver(ODESolver):
    """
    4th order Runge-Kutta method.
    """

    def step(self, model, t: float, dt: float) -> dict:

        state = model.get_state()

        k1 = model.derivatives(t, state)

        k2_state = {
            k: state[k] + dt * 0.5 * k1[k]
            for k in state.keys()
        }
        k2 = model.derivatives(t + dt * 0.5, k2_state)

        k3_state = {
            k: state[k] + dt * 0.5 * k2[k]
            for k in state.keys()
        }
        k3 = model.derivatives(t + dt * 0.5, k3_state)

        k4_state = {
            k: state[k] + dt * k3[k]
            for k in state.keys()
        }
        k4 = model.derivatives(t + dt, k4_state)

        new_state = {
            k: state[k] + (dt / 6) * (
                k1[k] + 2*k2[k] + 2*k3[k] + k4[k]
            )
            for k in state.keys()
        }

        model.set_state(new_state)

        return new_state