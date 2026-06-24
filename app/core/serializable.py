from abc import ABC, abstractmethod


class Serializable(ABC):
    """
    Interface for JSON serialization of simulation state.
    """

    @abstractmethod
    def to_json(self) -> dict:
        pass

    @abstractmethod
    def from_json(self, data: dict):
        pass