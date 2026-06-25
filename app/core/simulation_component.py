from abc import ABC, abstractmethod
from typing import Dict


class SimulationComponent(ABC):
    """
    Base interface for simulation components.
    """

    @abstractmethod
    def initialize(self):
        """Initialize component state."""
        pass

    @abstractmethod
    def reset(self):
        """Reset component state."""
        pass

    @abstractmethod
    def set_state(self, state: Dict[str, float]):
        """Set component state."""
        pass

    @abstractmethod
    def get_state(self) -> Dict[str, float]:
        """Return current component state."""
        pass