from typing import Dict, Any

from app.models.base_model import BaseModel

from app.math.context import Context
from app.math.evaluator import Evaluator


class LIFNeuron(BaseModel):
    """
    Leaky Integrate-and-Fire neuron model.
    """

    def __init__(
        self,
        params: Dict[str, Any] = None
    ):
        super().__init__(params)

        """
        Cache symbolic equation.
        """
        self.expression = self.build_expression()

    def initialize(self):
        """
        Returns initial membrane potential.
        """

        self.state = {
            "V": self.params.get(
                "V_rest",
                -65.0
            )
        }

        return self.state

    def derivatives(
        self,
        t: float,
        state: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Calculate membrane potential derivative.
        """

        V = state["V"]

        context = Context({
            "V": V,
            "V_rest": self.params.get(
                "V_rest",
                -65.0
            ),
            "R": self.params.get(
                "R",
                1.0
            ),
            "I": self.params.get(
                "I",
                10.0
            ),
            "tau": self.params.get(
                "tau",
                10.0
            ),
        })

        value = Evaluator().evaluate(
            self.expression,
            context
        )

        return {
            "V": value
        }

    def build_expression(self):
        """
        Build LIF differential equation.

        dV/dt = (-(V - V_rest) + R * I) / tau
        """

        from app.math.variable import Variable
        from app.math.constant import Constant
        from app.math.binary_expression import (
            AddExpression,
            SubtractExpression,
            MultiplyExpression,
            DivideExpression
        )

        V = Variable("V")
        V_rest = Variable("V_rest")
        R = Variable("R")
        I = Variable("I")
        tau = Variable("tau")

        numerator = AddExpression(
            SubtractExpression(
                Constant(0),
                SubtractExpression(
                    V,
                    V_rest
                )
            ),
            MultiplyExpression(
                R,
                I
            )
        )

        return DivideExpression(
            numerator,
            tau
        )