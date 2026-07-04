import pytest
from app.models.lorenz_system import LorenzSystem
from app.models.lif_neuron import LIFNeuron
from app.models.izhikevich import IzhikevichNeuron


# fake check helper

def check_derivatives_output(model, state):
    result = model.derivatives(0.0, state)

    assert isinstance(result, dict)
    assert len(result) == len(state)

    for k in state:
        assert k in result


def test_lorenz_initialize():
    model = LorenzSystem()
    state = model.initialize()

    assert "x" in state
    assert "y" in state
    assert "z" in state


def test_lorenz_derivatives():
    model = LorenzSystem()
    model.initialize()

    state = {"x": 1.0, "y": 1.0, "z": 1.0}

    check_derivatives_output(model, state)

def test_lif_initialize():
    model = LIFNeuron()
    state = model.initialize()

    assert "V" in state


def test_lif_derivatives():
    model = LIFNeuron()
    model.initialize()

    state = {"V": -65.0}

    result = model.derivatives(0.0, state)

    assert "V" in result
    assert isinstance(result["V"], float)


def test_izhikevich_initialize():
    model = IzhikevichNeuron()
    state = model.initialize()

    assert "V" in state
    assert "u" in state


def test_izhikevich_derivatives():
    model = IzhikevichNeuron()
    model.initialize()

    state = {"V": -65.0, "u": 0.0}

    result = model.derivatives(0.0, state)

    assert "V" in result
    assert "u" in result