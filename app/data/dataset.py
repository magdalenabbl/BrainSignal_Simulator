from app.data.time_series import TimeSeries
from app.data.spike_train import SpikeTrain


class Dataset:
    """
    Base dataset container.
    """

    def __init__(self):
        self.time_series = None
        self.spike_train = None

    def add_time_series(
        self,
        series: TimeSeries
    ):
        """
        Attach time series data.
        """

        self.time_series = series

    def add_spike_train(
        self,
        spikes: SpikeTrain
    ):
        """
        Attach spike data.
        """

        self.spike_train = spikes