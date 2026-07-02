from app.data.dataset import Dataset


class SpikeTrain(Dataset):

    def add_spike(self, time: float):
        self.values.append(time)

    def get_spikes(self) -> list[float]:
        return self.values

    def spike_count(self) -> int:
        return self.size()