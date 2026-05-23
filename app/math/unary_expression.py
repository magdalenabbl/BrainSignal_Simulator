
from app.math.expression import Expression


class UnaryOp(Expression):
    
    def __init__(self, operand):
        self.operand = operand


class Negate(UnaryOp):
    def evaluate(self, context):
        return -self.operand.evaluate(context)