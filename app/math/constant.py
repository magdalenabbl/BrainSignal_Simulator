
from app.math.expression import Expression


class Constant(Expression):
    def __init__(self, value: float):
        self.value = value

    def evaluate(self, context):
        return self.value