import pytest

from app.solvers.euler_solver import EulerSolver
from app.solvers.improved_euler_solver import ImprovedEulerSolver
from app.solvers.rk4_solver import RK4Solver
from app.solvers.leapfrog_solver import LeapfrogSolver
from app.solvers.verlet_solver import VerletSolver


class FakeModel:
    def __init__(self):
        self.state = {"x": 1.0, "y": 2.0}

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def derivatives(self, t, state):
        return {k: 1.0 for k in state}


def base_test(solver):
    model = FakeModel()
    state = {"x": 1.0, "y": 2.0}

    new_state = solver.step(model, 0.0, state, 0.1)

    assert isinstance(new_state, dict)
    assert "x" in new_state
    assert "y" in new_state


def test_euler():
    solver = EulerSolver()
    base_test(solver)


def test_improved_euler():
    solver = ImprovedEulerSolver()
    base_test(solver)


def test_rk4():
    solver = RK4Solver()
    base_test(solver)


def test_leapfrog():
    solver = LeapfrogSolver()
    base_test(solver)


def test_verlet():
    solver = VerletSolver()
    base_test(solver)