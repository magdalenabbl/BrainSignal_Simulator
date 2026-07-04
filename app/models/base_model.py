from abc import ABC, abstractmethod
from typing import Dict


class SimulationComponent(ABC):

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def set_state(self, state: Dict[str, float]):
        raise NotImplementedError

    @abstractmethod
    def get_state(self) -> Dict[str, float]:
        raise NotImplementedError