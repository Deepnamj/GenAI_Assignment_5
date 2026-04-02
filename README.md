# Assignment 5 – Python Modules and Packages

A hands-on Python project covering core module and package concepts: creating and importing custom modules, using aliases, and organising related code into a package with an `__init__.py` file.

---

## Prerequisites

- Python 3.x

No external libraries are required — all code uses Python built-ins only.

---

## Project Structure

```
Assignment_5/
│
├── main.py                  # Entry point — runs all three tasks
├── math_utils.py            # Task 1: custom math module
├── string_utils.py          # Task 2: custom string utility module
│
└── shop_package/            # Task 3: package folder
    ├── __init__.py          # Makes shop_package importable; re-exports all functions
    ├── discount.py          # Discount calculation functions
    └── billing.py           # Total and tax calculation functions
```

> **Note:** `billing.py`, `discount.py`, and `__init__.py` must be placed inside a folder named `shop_package` for the Task 3 imports in `main.py` to work correctly.

---

## How to Run

Place all files in the structure shown above, then run the entry point from the terminal:

```bash
python main.py
```

All three tasks execute in sequence and print their output to the console. Below is a task-by-task breakdown.

---

### Task 1 — Custom Math Module (`math_utils.py`, Section 1 of `main.py`)

**Files involved:** `math_utils.py`, `main.py`

**What it does:** Defines three arithmetic functions in `math_utils.py` and imports the module into `main.py` using an alias (`mu`). Calls `add()`, `subtract()`, and `square()` and prints the results.

**Key concepts:**
- **Custom modules** — any `.py` file is a module. Helps in organizing related functions (math operations in this case).
- **`import ... as` alias** — `import math_utils as mu` lets you refer to the module with a shorter name (`mu.add(...)` instead of `math_utils.add(...)`).Thus makes function calls cleaner and easier to read
- **Modular Programming** - Breaking code into smaller, reusable parts instead of writing everything in one file.Improves readability and maintainability.

**Functions in `math_utils.py`:**

```python
add(a, b)       # returns a + b
subtract(a, b)  # returns a - b
square(n)       # returns n * n
```

**Test cases to try:**

```python
mu.add(5, 3)        # → 8
mu.subtract(10, 5)  # → 5
mu.square(5)        # → 25
mu.add(-4, 4)       # → 0
mu.square(0)        # → 0
```

**Expected output:**

```
Task 1
Addition : 5 +3 = 8
Subtraction : 10-5 = 5
Square of 5: 25
```

---

### Task 2 — Custom String Utility Module (`string_utils.py`, Section 2 of `main.py`)

**Files involved:** `string_utils.py`, `main.py` 

**What it does:** Defines three string helper functions in `string_utils.py` and imports the module with alias `st`. Applies all three functions to the string `"hello world"` and prints the results.

**Key concepts:**
- **Module reuse** — string utilities are kept separate from math utilities, following the single-responsibility principle: each module does one category of work.
- **`import ... as` alias** — `import string_utils as st` shortens repeated references.
- **`text[::-1]`** — Python slice syntax for reversing a string (step of `-1` walks backwards).
- **`text.split()`** — splits on whitespace by default, making it easy to count words.

**Note on `capitalize_words()`:** The current implementation uses `text.capitalize()`, which only capitalises the **first letter of the entire string**. To capitalise every word (e.g. `"Hello World"`), `text.title()` should be used instead — this is a known limitation.

**Functions in `string_utils.py`:**

```python
capitalize_words(text)  # capitalises first letter of the string (see note above)
reverse_string(text)    # returns the string reversed character by character
word_count(text)        # returns the number of words separated by whitespace
```

**Test cases to try:**

```python
st.capitalize_words("hello world")  # → "Hello world"  (note: not "Hello World")
st.reverse_string("hello world")    # → "dlrow olleh"
st.word_count("hello world")        # → 2
st.word_count("one two three four") # → 4
st.reverse_string("python")         # → "nohtyp"
```

**Expected output:**

```
Task 2
Capitalized: Hello world
Reversed: dlrow olleh
Word Count: 2
```

---

### Task 3 — `shop_package` Package (`discount.py`, `billing.py`, `__init__.py`, Section 3 of `main.py`)

**Files involved:** `shop_package/__init__.py`, `shop_package/discount.py`, `shop_package/billing.py`, `main.py` (lines 16–22)

**What it does:** Groups discount and billing logic into a package called `shop_package`. `main.py` imports `discount` as a module alias and imports individual functions from `billing` directly. Demonstrates both import styles working side by side.

**Key concepts:**
- **Packages** — a folder containing an `__init__.py` file is a Python package. This lets you group related modules under one namespace (e.g. `shop_package.discount`).
- **`__init__.py`** — runs automatically when the package is imported. Here it re-exports all four functions so they can also be accessed directly as `shop_package.apply_discount(...)` without specifying the submodule.
- **Two import styles used together:**
  - `import shop_package.discount as disc` — imports the whole submodule; functions called as `disc.apply_discount(...)`.
  - `from shop_package.billing import calculate_total, apply_tax` — imports specific functions directly into the current namespace; called as `calculate_total(...)` without a prefix.

**Functions in `discount.py`:**

```python
apply_discount(price, percent)  # applies a percentage discount; returns discounted price
flat_discount(price)            # deducts a fixed 50 from the price
```

**Functions in `billing.py`:**

```python
calculate_total(prices)  # returns the sum of a list of prices
apply_tax(amount)        # adds 5% tax to amount; returns final price
```

**Test cases to try:**

```python
disc.apply_discount(200, 10)    # → 180.0   (10% off 200)
disc.apply_discount(500, 20)    # → 400.0   (20% off 500)
disc.flat_discount(200)         # → 150     (200 - 50)
disc.flat_discount(30)          # → -20     (flat discount exceeds price — edge case)
calculate_total([100, 200, 300])# → 600
calculate_total([])             # → 0       (empty list)
apply_tax(500)                  # → 525.0   (5% of 500 = 25)
apply_tax(0)                    # → 0.0
```

**Expected output:**

```
Task 3
Price after 10% disc on 200: 180.0
Price after flat disc on 200: 150
Total price: 600
Price after tax on 500: 525.0
```

---

## Key Concepts (Summary)

* **Modular Programming**
  Breaking code into smaller modules improves readability, reuse, and maintenance.

* **Custom Modules**
  Any `.py` file can be used to group related functions and avoid code duplication.

* **Importing & Aliases**
  Using `import` and `import ... as` helps organize code and make it more readable.

* **Separation of Concerns**
  Different modules handle different responsibilities (math, strings, billing, etc.).

* **Packages in Python**
  A package is a folder of related modules, helping structure larger projects.

* **Role of `__init__.py`**
  Makes a folder a package and can simplify access to functions.

* **Different Import Styles**

  * Full module import
  * Selective function import
    Used based on readability and need.

* **Code Reusability**
  Functions can be reused across files without rewriting logic.

* **Basic String Handling**
  Use of slicing, splitting, and built-in methods for efficient text processing.

* **Clean Project Structure**
  Organizing files properly makes code scalable and easier to manage.
