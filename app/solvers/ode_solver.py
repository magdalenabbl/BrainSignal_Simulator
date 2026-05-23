# solvers/ode_solver.py

from abc import ABC, abstractmethod


class ODESolver(ABC):
    """
    Base class for all numerical ODE solvers.
    Works with dict-based state systems.
    """

    @abstractmethod
    def step(self, model, t: float, dt: float) -> dict:
        """
        Performs one integration step.
        """
        pass