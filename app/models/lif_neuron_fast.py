from typing import Dict, Any
from app.models.base_model import BaseModel


class LIFNeuronFast(BaseModel):

    def initialize(self):
        self.state = {
            "V": self.params.get("V_rest", -65.0)
        }
        return self.state

    def derivatives(self, t: float, state: Dict[str, float]) -> Dict[str, float]:

        V = state.get("V", -65.0)

        V_rest = self.params.get("V_rest", -65.0)
        R = self.params.get("R", 1.0)
        I = self.params.get("I", 10.0)
        tau = self.params.get("tau", 10.0)

        dV = (-(V - V_rest) + R * I) / tau

        return {"V": dV}