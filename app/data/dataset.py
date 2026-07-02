from typing import List, Dict


class Dataset:

    def __init__(self, time: List[float], states: List[Dict[str, float]]):
        self.time = time
        self.states = states

    def size(self) -> int:
        return len(self.states)

    def is_empty(self) -> bool:
        return len(self.states) == 0

    def get(self, index: int) -> Dict[str, float]:
        return self.states[index]

    def get_time(self, index: int) -> float:
        return self.time[index]

    def to_sequences(self, window_size: int):
        sequences = []

        for i in range(len(self.states) - window_size):
            x = self.states[i:i + window_size]
            y = self.states[i + window_size]

            sequences.append((x, y))

        return sequences

    def to_spike_train(self, threshold: float = 0.5):
        spikes = []

        for state in self.states:
            spike_vector = {
                k: 1 if v > threshold else 0
                for k, v in state.items()
            }
            spikes.append(spike_vector)

        return spikes

    def to_vectors(self):
        return [
            list(state.values())
            for state in self.states
        ]