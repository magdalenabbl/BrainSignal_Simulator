
from app.math.expression import Expression


class Variable(Expression):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self, context):
        return context.get(self.name)