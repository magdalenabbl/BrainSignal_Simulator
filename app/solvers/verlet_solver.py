from app.solvers.ode_solver import ODESolver


class VerletSolver(ODESolver):

    def step(self, model, t: float, state: dict, dt: float) -> dict:

        derivatives = model.derivatives(t, state)

        new_state = {
            k: state[k] + dt * derivatives[k] + 0.5 * dt * dt * derivatives[k]
            for k in state
        }

        return new_state