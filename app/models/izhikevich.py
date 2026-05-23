
from app.models.base_model import BaseModel


class IzhikevichNeuron(BaseModel):
    """
    Spiking neuron model with rich dynamics.
    """

    def initialize(self):
        self.state = {
            "V": -65.0,
            "u": 0.0
        }
        return self.state

    def derivatives(self, t, state):

        V = state["V"]
        u = state["u"]

        a = self.params.get("a", 0.02)
        b = self.params.get("b", 0.2)
        I = self.params.get("I", 10.0)

        dV = 0.04 * V * V + 5 * V + 140 - u + I
        du = a * (b * V - u)

        return {
            "V": dV,
            "u": du
        }