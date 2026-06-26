# 📝 Day 01 Notes: Functions & Variables

A concise guide focusing on core syntax, practical lessons, observations from this codebase, and preparation for future concepts.

---

## Important Concepts
1. **Implicit String Types:** `input()` always captures and returns a string (`str`). Numeric operations require explicit type casting.
2. **String Chaining:** You can chain string methods (e.g., `input().strip().lower()`) to perform multi-step cleaning in a single line. The methods execute from left to right.
3. **Function Arguments & Scope:**
   * Custom functions accept parameters and return values using the `return` statement.
   * Variables defined inside a function are local to that function (local scope) and cannot be accessed outside of it.
4. **Main Function Pattern:** A design convention where execution logic starts in `main()`, and other custom helper functions are defined to be called from it.

---

## Python Syntax Learned

| Syntax / Method | Description | Example |
| :--- | :--- | :--- |
| `input(prompt)` | Reads a string from standard input | `name = input("Name: ")` |
| `.strip()` | Removes leading and trailing whitespace | `" hello ".strip() -> "hello"` |
| `.lower()` | Converts string to lowercase | `"HELLO".lower() -> "hello"` |
| `.title()` | Converts string to title case (First letter of each word capitalized) | `"john doe".title() -> "John Doe"` |
| `.split(sep)` | Splits a string into a list of strings by separator (default is whitespace) | `"a b c".split() -> ['a', 'b', 'c']` |
| `float(x)` / `int(x)`| Casts a string or number to a float or integer | `val = float("3.14")` |
| `def name(args):` | Defines a custom function | `def greet(n): print(n)` |
| `f"{val:.Nf}"` | Formats a float variable `val` to `N` decimal places | `f"{1/3:.2f}" -> "0.33"` |

---

## Common Mistakes & Pitfalls
* **Type Errors (`TypeError`):** Forgetting to cast string inputs from `input()` before doing math (e.g., `"5" + "5"` yields `"55"` instead of `10`).
* **Value Errors (`ValueError`):** Casting an invalid string to a numeric type (e.g., `float("abc")` will raise a `ValueError` and crash the program).
* **Index Errors (`IndexError`):** Trying to access an index of a list that does not exist. (e.g., `text.split()[0]` on an empty string `""` will crash because `split()` returns an empty list `[]`).
* **Operator Precedence:** Forgetting brackets in math equations (e.g., `temp - 32 * 5/9` is evaluated as `temp - (32 * 5 / 9)` instead of `(temp - 32) * 5/9`).

---

## Best Practices (PEP 8 Highlights)
* **Spaces around Operators:** Use single spaces around assignment (`=`) and math operators (`+`, `-`, `*`, `/`) for readability.
  * *Bad:* `x=5+y`
  * *Good:* `x = 5 + y`
* **Spaces in Parameters:** Add a space after commas in function arguments and parameters.
  * *Bad:* `def add(a,b):`
  * *Good:* `def add(a, b):`
* **Blank Lines:** Maintain two blank lines before and after top-level function definitions.
* **Variable Naming:** Use descriptive, lowercase snake_case for variable and function names.

---

## Observations from Your Code
* **Docstring Discrepancies:** In `Problem_1_Clean_User_Name.py`, the docstring stated the code converted the name to lowercase, but the code originally called `.title()`. Keeping code and documentation synchronized is crucial.
* **Code Duplication & Copy-Paste Bugs:** In `Problem_5_FahrenheitToCelsius_Converter.py`, the print statement printed "Fahrenheit" instead of "Celsius" due to copy-pasting from `Problem_4`. Always review and test copy-pasted blocks.
* **Formatting Conventions:** Throughout the files, there was a frequent lack of PEP 8 spaces around `=` and `,`. Aligning with these styling rules immediately increases the professionalism of the codebase.
* **Typographical Errors:** Typos in variable names (like `sentnce`) and UI strings (like `Multliplication`) can make code harder to read and look less polished. Using editor spellcheckers can help avoid this.

---

## Interview-Style Questions
1. **Q: What is the difference between passing arguments to functions and returning values?**
   * *A:* Arguments are the input data passed *into* a function for it to work with. Returns are the outputs sent *out* of the function back to the caller.
2. **Q: How does `string.split()` behave differently when called with no arguments versus with an argument like `string.split(" ")`?**
   * *A:* With no arguments, `.split()` treats any run of consecutive whitespace as a single separator and discards empty strings from the result (e.g., `"  a   b ".split()` yields `['a', 'b']`). With `" "`, it splits on *every* single space, keeping empty strings if consecutive spaces occur (e.g., `"a  b".split(" ")` yields `['a', '', 'b']`).
3. **Q: What error occurs if you run `float(input("Number: "))` and press Enter without entering anything? Why?**
   * *A:* A `ValueError: could not convert string to float: ''` is raised, because an empty string cannot be cast into a floating-point number.

---

## Things to Revise Before Moving to the Next Lecture
- [ ] Understand local vs. global scope for variables.
- [ ] Practice returning values from one custom function and feeding them directly into another function.
- [ ] Ensure familiarity with float formatting syntax (`f"{val:.2f}"`).
- [ ] Review PEP 8 guidelines regarding spaces around assignment operators and blank lines between functions.
