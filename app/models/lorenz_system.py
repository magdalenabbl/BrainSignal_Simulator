from app.models.base_model import BaseModel

from app.math.context import Context
from app.math.evaluator import Evaluator


class LorenzSystem(BaseModel):
    """
    Lorenz system using symbolic math layer.
    """

    def initialize(self):
        self.state = {
            "x": self.params.get("x0", 1.0),
            "y": self.params.get("y0", 1.0),
            "z": self.params.get("z0", 1.0),
        }
        return self.state

    def derivatives(self, t, state):

        context = Context({
            "x": state["x"],
            "y": state["y"],
            "z": state["z"],
            "sigma": self.params.get("sigma", 10.0),
            "rho": self.params.get("rho", 28.0),
            "beta": self.params.get("beta", 8/3),
        })

        dx_expr, dy_expr, dz_expr = self.build_expressions()

        evaluator = Evaluator()

        return {
            "x": evaluator.evaluate(dx_expr, context),
            "y": evaluator.evaluate(dy_expr, context),
            "z": evaluator.evaluate(dz_expr, context),
        }
    
    def build_expressions(self):
        """
        Builds symbolic Lorenz equations.
        """

        from app.math.variable import Variable
        from app.math.constant import Constant
        from app.math.binary_expression import (
            AddExpression,
            SubtractExpression,
            MultiplyExpression
        )

        x = Variable("x")
        y = Variable("y")
        z = Variable("z")

        sigma = Variable("sigma")
        rho = Variable("rho")
        beta = Variable("beta")

        # dx = σ(y - x)
        dx = MultiplyExpression(
            sigma,
            SubtractExpression(y, x)
        )

        # dy = x(ρ - z) - y
        dy = SubtractExpression(
            MultiplyExpression(x, SubtractExpression(rho, z)),
            y
        )

        # dz = xy - βz
        dz = SubtractExpression(
            MultiplyExpression(x, y),
            MultiplyExpression(beta, z)
        )

        return dx, dy, dz