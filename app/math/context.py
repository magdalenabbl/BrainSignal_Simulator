
from app.math.expression import Expression

class Context:
    """
    Holds variable values for expression evaluation.
    """

    def __init__(self, variables=None):
        self.variables = variables or {}

    def get(self, name: str):
        return self.variables.get(name, 0.0)

    def set(self, name: str, value: float):
        self.variables[name] = value