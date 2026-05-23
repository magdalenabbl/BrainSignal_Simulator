# solvers/improved_euler_solver.py

from solvers.ode_solver import ODESolver


class ImprovedEulerSolver(ODESolver):
    """
    Heun's method (predictor-corrector).
    """

    def step(self, model, t: float, dt: float) -> dict:

        state = model.get_state()

        k1 = model.derivatives(t, state)

        temp_state = {
            k: state[k] + dt * k1[k]
            for k in state.keys()
        }

        k2 = model.derivatives(t + dt, temp_state)

        new_state = {
            k: state[k] + (dt / 2) * (k1[k] + k2[k])
            for k in state.keys()
        }

        model.set_state(new_state)

        return new_state