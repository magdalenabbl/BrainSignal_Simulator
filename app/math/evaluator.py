
from app.math.expression import Expression

class Evaluator:
    """
    Evaluates expression trees in a given context.
    """

    def evaluate(self, expression, context):
        return expression.evaluate(context)