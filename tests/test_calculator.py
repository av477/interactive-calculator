import io

import pytest

from calculator.calculator import add, calculate, divide, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-2, 5, 3),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(20, 4) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize(
    ("a", "op", "b", "expected"),
    [
        (2, "+", 3, 5),
        (10, "-", 4, 6),
        (4, "*", 5, 20),
        (20, "/", 4, 5),
        (9, "add", 1, 10),
    ],
)
def test_calculate(a, op, b, expected):
    assert calculate(a, op, b) == expected


def test_run_interactive_handles_valid_and_invalid_operations(monkeypatch, capsys):
    responses = iter(["add", "5", "3", "divide", "10", "0", "quit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    calculate_and_print = False
    try:
        from calculator.calculator import run_interactive

        run_interactive()
        calculate_and_print = True
    except Exception:
        pass

    captured = capsys.readouterr()
    assert calculate_and_print is True
    assert "Interactive Calculator" in captured.out
    assert "Result: 8.0" in captured.out or "Result: 8" in captured.out
    assert "Cannot divide by zero" in captured.out


def test_run_interactive_invalid_operation_shows_available_choices(monkeypatch, capsys):
    responses = iter(["sqrt", "quit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    from calculator.calculator import run_interactive

    run_interactive()

    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out
    assert "add (+)" in captured.out
    assert "subtract (-)" in captured.out
    assert "multiply (*)" in captured.out
    assert "divide (/)." in captured.out


def test_run_interactive_invalid_number_prompts_user_again(monkeypatch, capsys):
    responses = iter(["add", "abc", "5", "quit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    from calculator.calculator import run_interactive

    run_interactive()

    captured = capsys.readouterr()
    assert "Invalid first number" in captured.out
    assert "Please enter a valid number" in captured.out
