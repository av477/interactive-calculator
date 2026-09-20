import pytest

from calculator.calculator import add, calculate, divide, multiply, subtract

# This module focuses on the calculator's core arithmetic behavior from a unit-test perspective.
# It verifies that each operation returns the correct result for valid inputs and raises the
# expected error when invalid operations or division-by-zero cases are encountered.

@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (9, 6, 15),
        (-5, 11, 6),
        (0, 4, 4),
        (12.5, 3.5, 16.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (17, 9, 8),
        (-4, 6, -10),
        (0, 5, -5),
        (18.75, 2.25, 16.5),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (7, 8, 56),
        (-3, 9, -27),
        (0, 13, 0),
        (3.5, 4, 14.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (45, 5, 9),
        (24, 3, 8),
        (-16, 4, -4),
        (10.5, 2.5, 4.2),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (22, 0),
        (0, 0),
        (-8, 0),
    ],
)
def test_divide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(a, b)


@pytest.mark.parametrize(
    ("a", "operation", "b", "expected"),
    [
        (11, "+", 5, 16),
        (30, "-", 9, 21),
        (6, "*", 8, 48),
        (72, "/", 8, 9),
        (17, "add", 4, 21),
        (17, "sum", 4, 21),
        (17, "subtract", 4, 13),
        (17, "minus", 4, 13),
        (9, "multiply", 5, 45),
        (9, "times", 5, 45),
        (18, "divide", 3, 6),
        (18, "div", 3, 6),
    ],
)
def test_calculate(a, operation, b, expected):
    assert calculate(a, operation, b) == expected


@pytest.mark.parametrize(
    ("a", "operation", "b"),
    [
        (13, "mod", 5),
        (13, "power", 5),
        (13, "", 5),
        (13, "sqrt", 5),
    ],
)
def test_calculate_invalid_operation(a, operation, b):
    with pytest.raises(ValueError, match="Invalid operation"):
        calculate(a, operation, b)
