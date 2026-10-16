# Simple Calculator

A command-line calculator written in Python. It adds, subtracts, multiplies and divides two numbers through a text menu.

Built for *Programming with Python*, Term 1, MSc Computer Science & Digital Innovation at IE University.

## Requirements

- Python 3.9 or newer
- No third-party packages are needed to run the calculator

## Running it

From the project folder:

```bash
python calculator.py
```

Or, with [uv](https://docs.astral.sh/uv/):

```bash
uv run calculator.py
```

## Usage

The program prints a title banner, shows a menu and waits for a command. Type the operation's **name**, not its number. Commands are not case-sensitive, and extra spaces around them are ignored:

| Command | Operation      |
|---------|----------------|
| `sum`   | a + b          |
| `sub`   | a − b          |
| `mul`   | a × b          |
| `div`   | a ÷ b          |
| `exit`  | Quit           |

Example session:

```
1.Sum
2.Sub
3.Mul
4.Div
5.Exit

Type the name of the operation you wish to do. > mul
Enter first number > 4
Enter second number > 2.5
Result: 10.0
```

Results are printed as floats. After each operation the menu is shown again.

### Errors

The calculator handles bad input without crashing and goes back to the menu:

| Situation                          | Message                           |
|------------------------------------|-----------------------------------|
| A number entry is not a number     | `Please enter a number.`          |
| Dividing by `0`                    | `Cannot divide by zero.`          |
| An unrecognized command            | `Please enter a valid selection.` |

Both numbers are entered before they are checked, so a bad first number is reported after the second one is entered.

## How it works

- `add`, `sub`, `mul` and `div` are small functions that take two floats and return a float.
- `div` raises `ZeroDivisionError` when the second number is `0`. It does not print anything itself; the menu catches the error and shows the message.
- A few `assert` checks run at startup to confirm each function returns the expected result.
- A `while True` loop shows the menu, reads the user's choice and calls the matching function until the user types `exit`.
- In each operation's sub-menu, one `try` block wraps both inputs and the calculation. `except ValueError` catches input that isn't a number, and in the division sub-menu a second `except ZeroDivisionError` catches division by zero.

## Project structure

```
Calculator/
├── calculator.py   # Calculator functions, startup tests and menu loop
├── pyproject.toml  # Project metadata
├── README.md       # This file
└── uv.lock         # Locked dependencies (uv)
```
