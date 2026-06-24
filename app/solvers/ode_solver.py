from abc import ABC, abstractmethod
from typing import Dict, Any


class ODESolver(ABC):
    """Base ODE solver interface."""

    @abstractmethod
    def step(
        self,
        model: Any,
        t: float,
        state: Dict[str, float],
        dt: float
    ) -> Dict[str, float]:
        pass