# Python Terminal Calculator

A terminal-based calculator built from scratch in Python that evaluates arithmetic expressions using custom string parsing logic.

This project does **not** use `eval()` or external libraries for calculations.  
Instead, it manually scans operators, extracts numbers, performs operations, and rebuilds the expression step-by-step.

<img width="1149" height="1369" src="images\working explanation of Terminal Calculator.PNG" />


## Latest Update (v1.1)

### Changes
- Fixed operator precedence handling
- Corrected left-to-right evaluation logic
- Improved expression parsing behavior
- Added cleaner output examples

---

## Current features

✅ Supports:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Multi-digit numbers
- Decimal outputs
- Sequential expression solving

---

## Why I Built This

I wanted to improve my:

- Python logic building
- String manipulation skills
- Debugging mindset
- Understanding of expression evaluation

Instead of using shortcuts, I chose to build the calculator logic manually from scratch.

---

## How It Works

### Core Function: `Calculate_string()`

This function:

1. Finds the operator index
2. Detects left and right numbers around it
3. Performs the operation
4. Replaces that part of the expression with the result

Example:

12+8/4


becomes:

12+2.0


then later:

14.0


---

### Main Function: `bodmas()`

This function repeatedly scans the string and solves operators in this order:

- `/` or `*`
- `+` or `-`

Each solved operation shortens the string until only one result remains.

---

## Challenges Solved During Development

- Precedence handling for /,* and +,- operators
- String index out of range errors
- Loop issues while modifying string length
- Number slicing edge cases
- Rebuilding updated expressions dynamically

## Development Notes

One major challenge during development was correctly implementing operator precedence and left-to-right evaluation for operators with equal precedence.

---

## Example Run

Expression to be evaluated : 7882/57/9*393/7/8-8+8-20

<img width="1105" height="280" src="images\Correct Output - From TerminalCalc.png" />


##  Future Improvements
- Bracket support ()
- Better input validation
- Cleaner code structure

## Run the Project

```bash
python TerminalCalc.py
```
## Learning Note

This project taught me more through debugging and building than simply watching tutorials.

## Author

Built by Pranav Singh  
GitHub: @prankyio
