import random
import math
from typing import List

from app.models.base_model import BaseModel


class ANN(BaseModel):

    def __init__(self, params=None):
        super().__init__(params)

        self.learning_rate = self.params.get(
            "learning_rate",
            0.1
        )

        # 2 input neurons -> 2 hidden neurons and 4 weights
        # input1-w1->hidden1
        # input2-w2->hidden1
        # ...   ->hidden2
        self.input_hidden_weights = [
            [
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            ],
            [
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            ]
        ]

        # 2 hidden neurons -> 1 output neuron
        self.hidden_output_weights = [
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ]

        self.hidden_bias = [
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ]

        self.output_bias = random.uniform(-1, 1)

        # Store the loss after every training epoch
        # so it can be displayed as a training graph.
        self.loss_history = []

        # Store the final accuracy of the trained network.
        self.accuracy = 0.0


    def initialize(self):

        self.state = {
            "x": 1.0
        }

        return self.state


    def sigmoid(self, value: float) -> float:

        return 1 / (1 + math.exp(-value))


    def sigmoid_derivative(self, value: float) -> float:

        return value * (1 - value)


    def forward(self, inputs: List[float]) -> float:

        hidden_outputs = []

        for neuron in range(2):

            # w1*x1+w2*x2+bias
            total = (
                inputs[0] *
                self.input_hidden_weights[neuron][0]
                +
                inputs[1] *
                self.input_hidden_weights[neuron][1]
                +
                self.hidden_bias[neuron]
            )

            hidden_outputs.append(
                self.sigmoid(total)
            )


        output_total = (
            hidden_outputs[0] *
            self.hidden_output_weights[0]
            +
            hidden_outputs[1] *
            self.hidden_output_weights[1]
            +
            self.output_bias
        )


        return hidden_outputs, self.sigmoid(output_total)


    def predict(self, inputs: List[float]) -> int:

        _, output = self.forward(inputs)

        return 1 if output >= 0.5 else 0


    # data = input, target = [0,1],1
    def train(self, data, epochs: int = 1000):

        # Clear the previous training history
        # when starting a new training session.
        self.loss_history = []

        for _ in range(epochs):

            # Store the total error for the current epoch.
            total_loss = 0.0

            for inputs, target in data:

                # Forward part
                hidden_outputs, output = self.forward(inputs)

                # error
                error = target - output

                # Store the squared error so that
                # the average loss can be calculated
                # after processing all training examples.
                total_loss += error ** 2

                # output neuron change - output gradient
                output_delta = (
                    error *
                    self.sigmoid_derivative(output)
                )


                # hidden gradient
                hidden_deltas = []

                for i in range(2):

                    # backpropagation output->hidden
                    hidden_error = (
                        output_delta
                        *
                        self.hidden_output_weights[i]
                    )

                    hidden_delta = (
                        hidden_error
                        *
                        self.sigmoid_derivative(hidden_outputs[i])
                    )

                    hidden_deltas.append(
                        hidden_delta
                    )


                # update hidden-output weights

                for i in range(2):

                    self.hidden_output_weights[i] += (
                        self.learning_rate
                        *
                        output_delta
                        *
                        hidden_outputs[i]
                    )


                self.output_bias += (
                    self.learning_rate
                    *
                    output_delta
                )


                # update input-hidden weights

                for neuron in range(2):

                    self.input_hidden_weights[neuron][0] += (
                        self.learning_rate
                        *
                        hidden_deltas[neuron]
                        *
                        inputs[0]
                    )


                    self.input_hidden_weights[neuron][1] += (
                        self.learning_rate
                        *
                        hidden_deltas[neuron]
                        *
                        inputs[1]
                    )


                    self.hidden_bias[neuron] += (
                        self.learning_rate
                        *
                        hidden_deltas[neuron]
                    )


            # Calculate the average loss for the current epoch.
            # This value is later used by the frontend
            # to draw the training loss graph.
            if data:

                average_loss = (
                    total_loss / len(data)
                )

            else:

                average_loss = 0.0


            # Save the loss for this epoch.
            self.loss_history.append(
                average_loss
            )


        # Calculate the final accuracy of the network
        # using the training dataset.
        correct = 0

        for inputs, target in data:

            prediction = self.predict(inputs)

            if prediction == target:
                correct += 1


        # Accuracy is stored as a value between 0 and 1.
        if data:

            self.accuracy = (
                correct / len(data)
            )

        else:

            self.accuracy = 0.0


    # Used by SimulationEngine

    def step(self, x: List[float]):

        # new output
        hidden, output = self.forward(x)

        previous = self.state.get(
            "x",
            1.0
        )

        # 0.7 and 0.3 make a transition from previous and output
        new_x = (
            0.7 * previous
            +
            0.3 * output
        )


        self.state = {
            "x": new_x
        }

        return self.state


    # Required by BaseModel

    def derivatives(self, t, state):

        return {
            key: 0.0
            for key in state
        }