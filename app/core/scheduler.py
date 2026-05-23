# core/scheduler.py


class Scheduler:
    """
    Controls simulation execution timing.
    """

    def __init__(self):
        self.events = []

    def schedule(self, time: float, callback):
        """
        Schedule a function at a specific simulation time.
        """
        self.events.append((time, callback))

    def run(self, t: float):
        """
        Executes all events for current time step.
        """
        for event_time, callback in self.events:
            if event_time <= t:
                callback()