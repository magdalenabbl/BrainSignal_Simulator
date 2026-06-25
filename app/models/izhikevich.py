from typing import Dict, Any

from app.models.base_model import BaseModel


class IzhikevichNeuron(BaseModel):
    """
    Izhikevich spiking neuron model.
    """

    def initialize(self) -> Dict[str, float]:
        """
        Returns initial neuron state.
        """

        self.state = {
            "V": -65.0,
            "u": 0.0
        }

        return self.state

    def derivatives(
        self,
        t: float,
        state: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Calculate neuron state derivatives.
        """

        V = state["V"]
        u = state["u"]

        a = self.params.get(
            "a",
            0.02
        )

        b = self.params.get(
            "b",
            0.2
        )

        I = self.params.get(
            "I",
            10.0
        )

        dV = (
            0.04 * V * V
            + 5 * V
            + 140
            - u
            + I
        )

        du = a * (b * V - u)

        return {
            "V": dV,
            "u": du
        }