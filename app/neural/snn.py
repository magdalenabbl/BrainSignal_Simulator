from app.models.lif_neuron import LIFNeuron


class SNN:

    def __init__(self, neuron_count=3):

        self.neurons = [
            LIFNeuron({
                "V_rest": -65.0,
                "R": 1.0,
                "I": 10.0,
                "tau": 10.0
            })
            for _ in range(neuron_count)
        ]

    def forward(self, inputs, t, dt):

        spikes = []

        for i, neuron in enumerate(self.neurons):

            I = inputs[i % len(inputs)]

            # ensure state exists
            if neuron.state is None:
                neuron.initialize()

            V = neuron.state["V"]

            dV = neuron.derivatives(t, {"V": V})["V"]

            V_new = V + dt * dV

            neuron.state["V"] = V_new

            if V_new >= -50.0:
                spikes.append(1)
                neuron.state["V"] = -65.0
            else:
                spikes.append(0)

        return spikes