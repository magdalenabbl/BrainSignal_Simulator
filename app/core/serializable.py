# core/serializable.py

import json
from abc import ABC, abstractmethod


class Serializable(ABC):
    """
    Enables JSON serialization of simulation objects.
    """

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def from_dict(self, data: dict):
        pass

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def from_json(self, json_str: str):
        self.from_dict(json.loads(json_str))