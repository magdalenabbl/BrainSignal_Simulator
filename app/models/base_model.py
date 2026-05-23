
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModel(ABC):
    """
    Base class for all dynamical systems.
    Uses dict-based state representation.
    """

    def __init__(self, params: Dict[str, Any] = None):
        self.params = params or {}
        self.state = {}

    @abstractmethod
    def initialize(self) -> Dict[str, float]:
        """
        Returns initial state of the system.
        """
        pass

    @abstractmethod
    def derivatives(self, t: float, state: Dict[str, float]) -> Dict[str, float]:
        """
        Computes dX/dt for solver.
        """
        pass

    def set_state(self, state: Dict[str, float]):
        self.state = state

    def get_state(self) -> Dict[str, float]:
        return self.state