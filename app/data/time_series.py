from typing import Dict, List

from app.data.dataset import Dataset


class TimeSeries(Dataset):

    def __init__(self, time_points: List[float], states: List[Dict[str, float]]):
        super().__init__(states)

        self.time_points = time_points

    def get_time(self) -> List[float]:
        return self.time_points

    def get_states(self) -> List[Dict[str, float]]:
        return self.values