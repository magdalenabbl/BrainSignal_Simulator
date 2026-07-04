from typing import Dict, Tuple, Any
from app.models.base_model import BaseModel
from app.math.context import Context
from app.math.evaluator import Evaluator
from app.math.variable import Variable
from app.math.binary_expression import (
            SubtractExpression,
            MultiplyExpression
        )

class LorenzSystem(BaseModel):
    """
    Lorenz dynamical system.
    """

    def __init__(self, params: Dict[str, Any] = None):
        super().__init__(params)

        """
        Cache symbolic expressions.
        """
        self.expressions = self.build_expressions()

    def initialize(self):
        """
        Returns initial system state.
        """

        self.state = {
            "x": self.params.get("x0", 1.0),
            "y": self.params.get("y0", 1.0),
            "z": self.params.get("z0", 1.0),
        }

        return self.state

    def derivatives(
        self,
        t: float,
        state: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Calculate Lorenz derivatives.
        """

        context = Context({
            "x": state["x"],
            "y": state["y"],
            "z": state["z"],
            "sigma": self.params.get(
                "sigma",
                10.0
            ),
            "rho": self.params.get(
                "rho",
                28.0
            ),
            "beta": self.params.get(
                "beta",
                8 / 3
            ),
        })

        dx_expr, dy_expr, dz_expr = self.expressions

        evaluator = Evaluator()

        return {
            "x": evaluator.evaluate(
                dx_expr,
                context
            ),
            "y": evaluator.evaluate(
                dy_expr,
                context
            ),
            "z": evaluator.evaluate(
                dz_expr,
                context
            ),
        }

    def build_expressions(
        self
    ) -> Tuple[Any, Any, Any]:
        """
        Build symbolic Lorenz equations.
        """

        

        x = Variable("x")
        y = Variable("y")
        z = Variable("z")

        sigma = Variable("sigma")
        rho = Variable("rho")
        beta = Variable("beta")

        dx = MultiplyExpression(
            sigma,
            SubtractExpression(
                y,
                x
            )
        )

        dy = SubtractExpression(
            MultiplyExpression(
                x,
                SubtractExpression(
                    rho,
                    z
                )
            ),
            y
        )

        dz = SubtractExpression(
            MultiplyExpression(
                x,
                y
            ),
            MultiplyExpression(
                beta,
                z
            )
        )

        return dx, dy, dz