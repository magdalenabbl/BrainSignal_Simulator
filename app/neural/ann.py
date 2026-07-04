import random
from typing import List, Dict, Any
from app.models.base_model import BaseModel


class ANN(BaseModel):

    def initialize(self):
        self.input_size = self.params.get("input_size", 3)

        self.weights = [
            random.random() for _ in range(self.input_size)
        ]

        self.state = {"x": 1.0}
        return self.state

    def forward(self, x: List[float]):
        return [
            sum(w * xi for w, xi in zip(self.weights, x))
        ]

    def step(self, x: List[float]):
        output = self.forward(x)

        prev = self.state.get("x", 1.0)

        new_x = 0.7 * prev + 0.3 * output[0]

        self.state = {"x": new_x}

        return self.state

    def derivatives(self, t, state):
        return {k: 0.0 for k in state} if isinstance(state, dict) else {}