import pytest
from app.core.simulation_engine import SimulationEngine
from app.models.lorenz_system import LorenzSystem
from app.models.lif_neuron import LIFNeuron
from app.solvers.euler_solver import EulerSolver
from app.neural.ann import ANN


def test_engine_ann_mode():
    model = ANN()

    engine = SimulationEngine(model=model, solver=None, dt=0.01)
    engine.attach_model(model)

    result = engine.step()

    assert engine.state is not None
    assert isinstance(result, dict)



def test_engine_ode_step():
    model = LorenzSystem()
    solver = EulerSolver()

    engine = SimulationEngine(dt=0.01)
    engine.attach_model(model)
    engine.attach_solver(solver)

    state = engine.step()

    assert isinstance(state, dict)
    assert "x" in state
    assert "y" in state
    assert "z" in state


#full simulation test

def test_engine_run():
    model = LorenzSystem()
    solver = EulerSolver()

    engine = SimulationEngine(dt=0.01)
    engine.attach_model(model)
    engine.attach_solver(solver)

    result = engine.run(10)

    assert result is not None
    assert len(result.time_points) == 11  # initial + 10 steps
    assert len(result.states) == 11