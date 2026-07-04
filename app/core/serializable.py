from abc import ABC, abstractmethod


class Serializable(ABC):
    
    @abstractmethod
    def to_json(self) -> dict:
         raise NotImplementedError

    @abstractmethod
    def from_json(self, data: dict):
         raise NotImplementedError