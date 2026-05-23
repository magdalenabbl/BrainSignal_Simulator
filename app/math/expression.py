
from abc import ABC, abstractmethod


class Expression(ABC):
    """
    Base class for all symbolic math nodes.
    """

    @abstractmethod
    def evaluate(self, context):
        pass