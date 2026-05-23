# core/simulation_engine.py

import copy


class SimulationEngine:
    """
    Main orchestrator of simulation lifecycle.
    """

    def __init__(self, model, solver, logger=None, scheduler=None):
        self.model = model
        self.solver = solver
        self.logger = logger
        self.scheduler = scheduler

        self.t = 0.0

    def run(self, T: float, dt: float):
        """
        Runs full simulation.
        """

        state = self.model.initialize()
        self.model.set_state(state)

        history = []

        if self.logger:
            self.logger.log("Simulation started")

        while self.t < T:

            if self.scheduler:
                self.scheduler.run(self.t)

            new_state = self.solver.step(self.model, self.t, dt)

            history.append({
                "t": self.t,
                "state": copy.deepcopy(new_state)
            })

            self.t += dt

        if self.logger:
            self.logger.log("Simulation finished")

        return history