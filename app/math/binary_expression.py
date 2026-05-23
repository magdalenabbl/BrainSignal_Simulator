from app.math.expression import Expression


class BinaryExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class AddExpression(BinaryExpression):
    def evaluate(self, context):
        return self.left.evaluate(context) + self.right.evaluate(context)


class SubtractExpression(BinaryExpression):
    def evaluate(self, context):
        return self.left.evaluate(context) - self.right.evaluate(context)


class MultiplyExpression(BinaryExpression):
    def evaluate(self, context):
        return self.left.evaluate(context) * self.right.evaluate(context)


class DivideExpression(BinaryExpression):
    def evaluate(self, context):
        return self.left.evaluate(context) / self.right.evaluate(context)