# Python Terminal Calculator (Work in Progress)

A terminal-based calculator built from scratch in Python that evaluates arithmetic expressions using custom string parsing logic.

This project does **not** use `eval()` or external libraries for calculations.  
Instead, it manually scans operators, extracts numbers, performs operations, and rebuilds the expression step-by-step.

<img width="1121" height="1361" alt="IMG_2763" src="https://github.com/user-attachments/assets/7a5cceed-be86-4929-90d6-1a6f26e4d9ee" />



## Current Status

✅ Supports:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Multi-digit numbers
- Decimal outputs
- Sequential expression solving

⚠️ Known Issue:

Operator precedence handling is currently being improved.

At the moment, the program processes:

1. All division first  
2. Then multiplication  
3. Then addition  
4. Then subtraction

But mathematically, `*` and `/` should have equal precedence and be solved left-to-right.

Example:

Expression:

7882/57/9*393/7/8-8+8-20


Current Output:

71.82

<img width="1586" height="572" alt="Screenshot 2026-04-25 022340" src="https://github.com/user-attachments/assets/4bd3ffe7-052d-484e-a057-c610c200eed1" />


Expected Output:

87.82


This fix is currently in progress.

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

- `/`
- `*`
- `+`
- `-`

Each solved operation shortens the string until only one result remains.

---

## Challenges Solved During Development

- String index out of range errors
- Loop issues while modifying string length
- Number slicing edge cases
- Rebuilding updated expressions dynamically

---

## Example Run

```bash
Enter the operation here :- 10+5*2

Output:
20
```
##  Future Improvements
- Correct left-to-right precedence for * and /
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
