from typing import List, Dict


class SpikeTrain:

    def __init__(self):
        self.spikes: List[float] = []

    def add_spike(self, time: float):
        self.spikes.append(time)

    def get_spikes(self) -> List[float]:
        return self.spikes

    def spike_count(self) -> int:
        return len(self.spikes)