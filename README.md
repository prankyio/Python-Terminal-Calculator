# Python Terminal Calculator - v2.0

A terminal-based calculator built completely from scratch in Python that evaluates arithmetic expressions using custom parsing logic.

This project does **not** use `eval()` or external libraries for calculations.
Instead, it manually scans operators, extracts numbers, performs operations, solves brackets, and rebuilds expressions step-by-step.

<img width="1024" height="1536" src="images/Updated Terminal Calculator (v2.0) Flowchart.png" />

---

# Latest Update (v2.0)

## New Features Added

* Added full bracket support:

  * Parentheses `()`
  * Square brackets `[]`
  * Curly braces `{}`
* Fixed operator precedence handling
* Implemented proper left-to-right evaluation
* Improved expression parsing logic
* Added support for nested bracket solving
* Cleaner control flow and structure

---

# Current Features

✅ Supports:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Multi-digit numbers
* Decimal outputs
* Nested arithmetic expressions
* Bracket solving:

  * `()`
  * `[]`
  * `{}`
* Sequential expression evaluation
* Custom BODMAS implementation
* Terminal-based interaction

---

# Why I Built This

I built this project to improve my understanding of:

* Python logic building
* String manipulation
* Expression parsing
* Debugging and problem solving
* Operator precedence handling
* Control flow design

Instead of using shortcuts like `eval()`, I wanted to manually implement the complete calculation logic from scratch.

---

# Project Flow

## 1. `BracketSolver()`

This function:

* Detects brackets inside the expression
* Finds the closest solvable bracket pair
* Solves the inner expression first
* Replaces the bracketed part with the result
* Repeats until no brackets remain

Example:

```text
10+[8*(6-2)]
```

becomes:

```text
10+[8*4.0]
```

then:

```text
10+32.0
```

then:

```text
42.0
```

---

## 2. `bodmas()`

This function handles operator precedence.

It repeatedly scans the expression and solves operations in this order:

### First Pass

* `/`
* `*`

(left to right)

### Second Pass

* `+`
* `-`

(left to right)

The expression becomes shorter after every calculation until only one final result remains.

---

## 3. `Calculate_string()`

This function performs the actual operation.

It:

1. Finds the operator index
2. Extracts left and right numbers
3. Performs the calculation
4. Rebuilds the updated expression string

Example:

```text
12+8/4
```

becomes:

```text
12+2.0
```

then later:

```text
14.0
```

---

# Challenges Faced During Development

* String index out of range errors
* Modifying string while iterating
* Handling changing string lengths
* Number slicing edge cases
* Operator precedence implementation
* Left-to-right evaluation logic
* Nested bracket solving
* Rebuilding expressions dynamically

---

# Example Run

Expression:

```text
{47 - (59*2)/7*{5-3} + [76*3/{44-34}]}
```

Output:

```text
36.0857
```

<img width="1593" height="495" src="images/Correct Output - TerminalCalc v2.png" />

---

# Future Improvements

Possible features planned for future versions:

* Exponent support (`^`)
* Percentage calculations (`%`)
* Trigonometric functions:

  * `sin()`
  * `cos()`
  * `tan()`
* Variable support:

  * Example:

    ```text
    x = 10
    y = 5
    x+y*2
    ```
* Better input validation
* Cleaner code optimization
* Improved parser structure
* GUI version using Tkinter or PyQt

---

# Run The Project

```bash
python TerminalCalc.py
```

---

# Learning Note

This project taught me more through debugging, experimenting, and fixing logical mistakes than simply watching tutorials.

Building the calculator logic manually helped me understand how expression evaluation actually works internally.

---

# Author

Built by Pranav Singh

GitHub: @prankyio
