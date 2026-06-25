from abc import ABC, abstractmethod
from typing import Dict, Any

from app.core.simulation_component import SimulationComponent


class BaseModel(SimulationComponent, ABC):
    """
    Base class for all dynamical systems.
    Uses dictionary state representation.
    """

    def __init__(self, params: Dict[str, Any] = None):
        self.params = params or {}
        self.state = {}

    @abstractmethod
    def initialize(self) -> Dict[str, float]:
        """
        Returns initial system state.
        """
        pass

    @abstractmethod
    def derivatives(
        self,
        t: float,
        state: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Computes derivatives for solver.
        """
        pass

    def reset(self):
        """Reset model state."""
        self.state = self.initialize()

    def set_state(self, state: Dict[str, float]):
        """Update current state."""
        self.state = state

    def get_state(self) -> Dict[str, float]:
        """Return current state."""
        return self.state