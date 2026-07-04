import pytest

from app.math.constant import Constant
from app.math.variable import Variable
from app.math.context import Context
from app.math.evaluator import Evaluator

from app.math.binary_expression import (
    AddExpression,
    SubtractExpression,
    MultiplyExpression,
    DivideExpression,
)

from app.math.unary_expression import Negate


def test_constant():
    expr = Constant(5.0)
    result = expr.evaluate(None)

    assert result == 5.0


def test_variable():
    ctx = Context({"x": 10.0})
    expr = Variable("x")

    result = expr.evaluate(ctx)

    assert result == 10.0


def test_add():
    expr = AddExpression(Constant(2.0), Constant(3.0))
    result = expr.evaluate(None)

    assert result == 5.0


def test_subtract():
    expr = SubtractExpression(Constant(5.0), Constant(3.0))
    result = expr.evaluate(None)

    assert result == 2.0


def test_multiply():
    expr = MultiplyExpression(Constant(2.0), Constant(3.0))
    result = expr.evaluate(None)

    assert result == 6.0


def test_divide():
    expr = DivideExpression(Constant(6.0), Constant(2.0))
    result = expr.evaluate(None)

    assert result == 3.0


def test_negate():
    expr = Negate(Constant(5.0))
    result = expr.evaluate(None)

    assert result == -5.0


def test_evaluator():
    ctx = Context({"x": 7.0})
    expr = Variable("x")

    evaluator = Evaluator()
    result = evaluator.evaluate(expr, ctx)

    assert result == 7.0