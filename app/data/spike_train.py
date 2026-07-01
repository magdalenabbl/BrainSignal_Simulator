from typing import List


class SpikeTrain:
    """
    Represents neuron spike events.
    """

    def __init__(
        self,
        spikes: List[float]
    ):
        self.spikes = spikes

    def add_spike(
        self,
        time: float
    ):
        """
        Add spike timestamp.
        """

        self.spikes.append(time)