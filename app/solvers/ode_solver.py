from abc import ABC, abstractmethod
from typing import Dict, Any


class ODESolver(ABC):
    """
    Base interface for ODE solvers.
    """

    @abstractmethod
    def step(
        self,
        model: Any,
        t: float,
        state: Dict[str, float],
        dt: float
    ) -> Dict[str, float]:
        """
        Perform one integration step.
        """
        pass