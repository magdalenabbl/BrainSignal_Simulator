from app.models.lif_neuron_fast import LIFNeuronFast


class SNN:

    def __init__(self, neuron_count=3):

        self.neurons = [
            LIFNeuronFast({
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

            # FIX: safe initialization
            if not neuron.state or "V" not in neuron.state:
                neuron.initialize()

            V = neuron.state.get("V", -65.0)

            # inject current
            neuron.params["I"] = I

            dV = neuron.derivatives(t, {"V": V})["V"]

            V_new = V + dt * dV

            neuron.state["V"] = V_new

            if V_new >= -50.0:
                spikes.append(1)
                neuron.state["V"] = neuron.params.get("V_rest", -65.0)
            else:
                spikes.append(0)

        return spikes