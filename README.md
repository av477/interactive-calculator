# Interactive Calculator

A command-line calculator application with a read-evaluate-print loop (REPL) that supports basic arithmetic operations.

## Features

- Addition, subtraction, multiplication, and division
- Accepts both words and symbols:
  - add / sum / +
  - subtract / minus / -
  - multiply / times / *
  - divide / div / /
- Validates user input and handles invalid operations gracefully
- Prevents division by zero with a clear error message
- Includes unit tests and CI coverage enforcement

## Project structure

- `src/calculator/` – calculator package and CLI entry point
- `tests/` – pytest test suite
- `.github/workflows/` – GitHub Actions CI workflow
- `pyproject.toml` – project metadata and dev dependencies

## Quick start in VS Code

1. Open the project folder in VS Code.
2. Open the integrated terminal: Terminal > New Terminal.
3. Create and activate a virtual environment if needed.
4. Install the project with dev dependencies:
   ```powershell
   python -m pip install -e ".[dev]"
   ```
5. Run the calculator:
   ```powershell
   python -m calculator.cli
   ```

Example interactive session:

```text
Choose an operation: add
Enter the first number: 10
Enter the second number: 5
Result: 15.0
```

## Running tests in VS Code

Open the terminal in VS Code and run:

```powershell
python -m pytest
```

## Code coverage in VS Code

This project enforces 100% test coverage in CI.

Run coverage locally from the VS Code terminal with:

```powershell
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

This will fail if total coverage drops below 100%.

## GitHub Actions

The workflow in `.github/workflows/python-tests.yml` installs dependencies and runs the test suite with the coverage threshold enabled.

If the coverage falls below 100%, the build fails automatically.
