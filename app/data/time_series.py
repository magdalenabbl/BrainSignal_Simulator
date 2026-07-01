from typing import Dict, List


class TimeSeries:
    """
    Represents values evolving over time.
    """

    def __init__(
        self,
        time: List[float],
        values: List[Dict[str, float]]
    ):
        self.time = time
        self.values = values

    def length(self) -> int:
        """
        Returns number of samples.
        """

        return len(self.time)