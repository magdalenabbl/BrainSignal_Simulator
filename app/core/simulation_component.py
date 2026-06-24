from abc import ABC, abstractmethod


class SimulationComponent(ABC):
    """
    Base interface for any component controlled by SimulationEngine.
    """

    @abstractmethod
    def initialize(self):
        """Initialize internal state."""
        pass

    @abstractmethod
    def update(self, dt: float):
        """Update component by timestep dt."""
        pass

    @abstractmethod
    def reset(self):
        """Reset component to initial state."""
        pass