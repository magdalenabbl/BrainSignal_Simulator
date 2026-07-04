import pytest
from app.neural.ann import ANN
from app.neural.snn import SNN
from app.data.dataset import Dataset



def test_ann_step():
    model = ANN()
    model.initialize()

    x = [0.1, 0.2, 0.3]
    out = model.step(x)

    assert "x" in out
    assert isinstance(out["x"], float)


def test_ann_deterministic_shape():
    model = ANN()
    model.initialize()

    x = [0.1, 0.2, 0.3]

    out1 = model.step(x)
    out2 = model.step(x)

    assert "x" in out1
    assert "x" in out2


def test_snn_forward():
    model = SNN(neuron_count=3)

    inputs = [0.5, 0.2, 0.8]

    spikes = model.forward(inputs, t=0.0, dt=0.1)

    assert len(spikes) == 3
    assert all(s in (0, 1) for s in spikes)


def test_snn_state_update():
    model = SNN(neuron_count=2)

    inputs = [1.0, 0.5]

    spikes = model.forward(inputs, t=0.0, dt=0.1)
    spikes2 = model.forward(inputs, t=0.1, dt=0.1)

    assert len(spikes) == 2
    assert len(spikes2) == 2


def test_dataset_to_ann_compatibility():
    ds = Dataset(
        time=[0, 1],
        states=[
            {"x": 0.1, "y": 0.2, "z": 0.3},
            {"x": 0.4, "y": 0.5, "z": 0.6},
        ]
    )

    vectors = ds.to_vectors()

    model = ANN()
    model.initialize()

    out = model.step(vectors[0])

    assert "x" in out