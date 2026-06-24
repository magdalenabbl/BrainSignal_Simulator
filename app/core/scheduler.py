class Scheduler:
    """
    Controls simulation time progression.
    """

    def __init__(self, dt: float = 0.01):
        self.dt = dt
        self.time = 0.0
        self.running = False

    def step(self) -> float:
        """
        Advance simulation time.
        """
        self.time += self.dt
        return self.time

    def reset(self):
        self.time = 0.0
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False