# core/simulation_component.py

from abc import ABC, abstractmethod


class SimulationComponent(ABC):
    """
    Base abstraction for all dynamic simulation objects.
    Uses dict-based state for maximum flexibility.
    """

    @abstractmethod
    def initialize(self) -> dict:
        """
        Returns initial state of the system.
        """
        pass

    @abstractmethod
    def derivatives(self, t: float, state: dict) -> dict:
        """
        Computes time derivatives for the system.
        """
        pass

    @abstractmethod
    def set_state(self, state: dict):
        """
        Updates internal model state.
        """
        pass

    @abstractmethod
    def get_state(self) -> dict:
        """
        Returns current internal state.
        """
        pass