# solvers/verlet_solver.py

from solvers.ode_solver import ODESolver

class VerletSolver(ODESolver):
    """
    Used for physics systems (stable energy conservation).
    """

    def step(self, model, t: float, dt: float) -> dict:

        state = model.get_state()

        new_state = {}

        for k in state.keys():
            x = state[k]
            dx = model.derivatives(t, state)[k]

            new_state[k] = x + dx * dt + 0.5 * dx * dt * dt

        model.set_state(new_state)

        return new_state