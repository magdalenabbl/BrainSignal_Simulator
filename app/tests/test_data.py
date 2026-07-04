import pytest
from app.data.dataset import Dataset
from app.data.simulation_result import SimulationResult
from app.data.time_series import TimeSeries
from app.data.spike_train import SpikeTrain


def sample_data():
    time = [0.0, 0.1, 0.2]
    states = [
        {"x": 0.1, "y": 0.2},
        {"x": 0.4, "y": 0.6},
        {"x": 0.9, "y": 1.2},
    ]
    return time, states


def test_dataset_basic():
    time, states = sample_data()

    ds = Dataset(time, states)

    assert ds.size() == 3
    assert not ds.is_empty()

    assert ds.get(0) == states[0]
    assert ds.get_time(1) == 0.1


def test_dataset_sequences():
    time, states = sample_data()

    ds = Dataset(time, states)

    seq = ds.to_sequences(window_size=2)

    assert len(seq) == 1
    assert isinstance(seq[0], tuple)


def test_dataset_spikes():
    states = [
        {"x": 0.1, "y": 0.9},
        {"x": 0.6, "y": 0.2},
    ]

    ds = Dataset([0, 1], states)

    spikes = ds.to_spike_train(threshold=0.5)

    assert spikes[0]["x"] == 0
    assert spikes[0]["y"] == 1


def test_dataset_vectors():
    states = [{"x": 1, "y": 2}]
    ds = Dataset([0], states)

    vec = ds.to_vectors()

    assert vec == [[1, 2]]

def test_simulation_result():
    time, states = sample_data()

    sr = SimulationResult(time, states, "lorenz", "rk4")

    assert sr.get_final_state() == states[-1]

    d = sr.to_dict()

    assert d["model"] == "lorenz"
    assert d["solver"] == "rk4"

def test_time_series():
    time, states = sample_data()

    ts = TimeSeries(time, states)

    assert ts.get_time() == time
    assert ts.get_states() == states

def test_spike_train():
    ds = SpikeTrain([0], [{"x": 1}])

    # even if implementation is partial, just check it exists
    assert ds.size() == 1