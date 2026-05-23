# solvers/euler_solver.py

from solvers.ode_solver import ODESolver


class EulerSolver(ODESolver):
    """
    Simple Euler integration method.
    """

    def step(self, model, t: float, dt: float) -> dict:
        state = model.get_state()

        derivatives = model.derivatives(t, state)

        new_state = {
            k: state[k] + dt * derivatives[k]
            for k in state.keys()
        }

        model.set_state(new_state)

        return new_state