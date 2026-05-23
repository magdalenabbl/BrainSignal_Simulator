# solvers/leapfrog_solver.py

from solvers.ode_solver import ODESolver

class LeapfrogSolver(ODESolver):
    """
    Stable for oscillatory / chaotic systems.
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