import io
import runpy
import sys

import pytest

from calculator.calculator import (
    add,
    calculate,
    divide,
    evaluate_expression,
    multiply,
    subtract,
)

# This module takes a higher-level integration perspective by testing the interactive CLI flow,
# expression evaluation, and the script entry points. It checks how the calculator behaves from
# the user's point of view rather than only validating raw arithmetic outputs.

@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (12, 7, 19),
        (-8, 4, -4),
        (0, 9, 9),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(18, 9) == 9


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(36, 6) == 6


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(15, 0)


@pytest.mark.parametrize(
    ("a", "op", "b", "expected"),
    [
        (12, "+", 8, 20),
        (18, "-", 7, 11),
        (9, "*", 6, 54),
        (48, "/", 6, 8),
        (14, "add", 3, 17),
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


def test_evaluate_expression_handles_valid_and_invalid_inputs():
    assert evaluate_expression("2 + 3 * 4") == 14.0

    with pytest.raises(ValueError, match="Invalid expression: bad_name"):
        evaluate_expression("bad_name + 2")

    with pytest.raises(ValueError, match="Expression did not produce a number"):
        evaluate_expression("'hello'")


def test_cli_module_runs_main(monkeypatch):
    called = {"run": False}

    def fake_run_interactive():
        called["run"] = True

    import calculator.calculator as calculator_module

    monkeypatch.setattr(calculator_module, "run_interactive", fake_run_interactive)
    sys.modules.pop("calculator.cli", None)
    runpy.run_module("calculator.cli", run_name="__main__")

    assert called["run"] is True


def test_calculator_module_runs_main(monkeypatch, capsys):
    responses = iter(["quit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    sys.modules.pop("calculator.calculator", None)
    runpy.run_module("calculator.calculator", run_name="__main__")

    captured = capsys.readouterr()
    assert "Interactive Calculator" in captured.out
    assert "Goodbye!" in captured.out
