import random


class ANN:

    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        self.weights = [
            [random.random() for _ in range(input_size)]
            for _ in range(output_size)
        ]

    def forward(self, x):
        return [
            sum(w * xi for w, xi in zip(neuron, x))
            for neuron in self.weights
        ]