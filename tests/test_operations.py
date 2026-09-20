import pytest

from calculator.calculator import add, calculate, divide, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-2, 5, 3),
        (0, 0, 0),
        (10.5, 2.5, 13.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 4, 6),
        (-2, 5, -7),
        (0, 0, 0),
        (12.5, 2.5, 10.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (4, 5, 20),
        (-3, 2, -6),
        (0, 99, 0),
        (2.5, 4, 10.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (20, 4, 5),
        (9, 3, 3),
        (-12, 3, -4),
        (7.5, 2.5, 3),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (10, 0),
        (0, 0),
        (-5, 0),
    ],
)
def test_divide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(a, b)


@pytest.mark.parametrize(
    ("a", "operation", "b", "expected"),
    [
        (2, "+", 3, 5),
        (10, "-", 4, 6),
        (4, "*", 5, 20),
        (20, "/", 4, 5),
        (9, "add", 1, 10),
        (9, "sum", 1, 10),
        (9, "subtract", 1, 8),
        (9, "minus", 1, 8),
        (9, "multiply", 3, 27),
        (9, "times", 3, 27),
        (9, "divide", 3, 3),
        (9, "div", 3, 3),
    ],
)
def test_calculate(a, operation, b, expected):
    assert calculate(a, operation, b) == expected


@pytest.mark.parametrize(
    ("a", "operation", "b"),
    [
        (2, "mod", 3),
        (2, "power", 3),
        (2, "", 3),
        (2, "sqrt", 3),
    ],
)
def test_calculate_invalid_operation(a, operation, b):
    with pytest.raises(ValueError, match="Invalid operation"):
        calculate(a, operation, b)
