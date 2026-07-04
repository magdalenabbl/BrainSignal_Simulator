from typing import List, Dict


class TimeSeries:

    def __init__(self, time_points: List[float], states: List[Dict[str, float]]):
        self.time_points = time_points
        self.states = states

    def get_time_points(self) -> List[float]:
        return self.time_points

    def get_states(self) -> List[Dict[str, float]]:
        return self.states

    def size(self) -> int:
        return len(self.states)