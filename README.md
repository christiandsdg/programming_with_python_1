# Programming with Python — Coursework

My work for *Programming with Python*, Term 1, MSc Computer Science & Digital Innovation at IE University.

| Work | Type | Location |
|------|------|----------|
| [Simple Calculator](#simple-calculator) | Command-line program | `src/calculator.py` |
| [Session 03: Advanced Data Structures](#session-03-advanced-data-structures) | Jupyter notebook | `notebooks/S03_Advanced_Data_Structures_ChristianDSDG.ipynb` |

## Setup

- Python 3.9 or newer
- [uv](https://docs.astral.sh/uv/), to install dependencies

From the project folder:

```bash
uv sync
```

This creates `.venv` and installs `ipykernel`, which the notebooks need. The calculator needs only the standard library.

## Project structure

```
Calculator/
├── src/
│   └── calculator.py      # Simple Calculator
├── notebooks/
│   └── S03_Advanced_Data_Structures_ChristianDSDG.ipynb
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Locked dependencies (uv)
└── README.md              # This file
```

`.venv/` is created by `uv sync` and is not tracked by git.

---

## Simple Calculator

A command-line calculator that adds, subtracts, multiplies and divides two numbers through a text menu.

### Running it

```bash
uv run src/calculator.py
```

Or, without uv:

```bash
python src/calculator.py
```

### Usage

The program prints a title banner, shows a menu and waits for a command. Type the operation's **name**, not its number. Commands are not case-sensitive, and extra spaces around them are ignored:

| Command | Operation |
|---------|-----------|
| `sum`   | a + b     |
| `sub`   | a − b     |
| `mul`   | a × b     |
| `div`   | a ÷ b     |
| `exit`  | Quit      |

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

| Situation                      | Message                           |
|--------------------------------|-----------------------------------|
| A number entry is not a number | `Please enter a number.`          |
| Dividing by `0`                | `Cannot divide by zero.`          |
| An unrecognized command        | `Please enter a valid selection.` |

Both numbers are entered before they are checked, so a bad first number is reported after the second one is entered.

### How it works

- `add`, `sub`, `mul` and `div` are small functions that take two floats and return a float.
- `div` raises `ZeroDivisionError` when the second number is `0`. It does not print anything itself; the menu catches the error and shows the message.
- A few `assert` checks run at startup to confirm each function returns the expected result.
- `main()` runs a `while True` loop that shows the menu, reads the user's choice and calls the matching function until the user types `exit`.
- In each operation's sub-menu, one `try` block wraps both inputs and the calculation. `except ValueError` catches input that isn't a number, and in the division sub-menu a second `except ZeroDivisionError` catches division by zero.

---

## Session 03: Advanced Data Structures

A guided notebook on Python's built-in collections. Each section has a worked example, which I modified and re-ran, and a guided exercise I completed:

1. **Lists:** appending, removing, slicing, and count/total/average of a list of expenses.
2. **Tuples:** unpacking fixed records and starred unpacking (`first, *middle, last`).
3. **Sets:** finding missing, unexpected and shared categories with `-`, `&` and `|`.
4. **Dictionaries:** `get()`, `update()`, `setdefault()` and `pop()` on a product record.
5. **Nested collections:** a list of dictionaries indexed by ID with a dict comprehension, then filtered with a list comprehension.

The final challenge is a grade tracker: a dictionary of students with grade lists and subject sets, an `average()` function that returns `None` for students with no grades, and a ranking that leaves those students out.

### Opening it

Open the notebook in PyCharm or VS Code and select the project's `.venv` as the kernel. Or, from the terminal:

```bash
uv run --with jupyter jupyter lab notebooks/
```
