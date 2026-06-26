# 📝 Day 02 Notes: Conditionals

Quick, practical revision notes for conditional statements, boolean logic, and pattern matching in Python.

---

## Important Concepts

### 1. `if / elif / else` — The Core Decision Ladder
Python runs blocks one at a time **from top to bottom** and stops as soon as a condition is `True`.
```python
if condition_1:      # Checked first
    ...
elif condition_2:    # Only checked if condition_1 is False
    ...
else:               # Runs if ALL conditions above are False
    ...
```
> **Key Rule:** Only ONE block ever runs. Python does not check the rest once a match is found.

---

### 2. Comparison Operators

| Operator | Meaning | Example |
| :---: | :--- | :--- |
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `name != "admin"` |
| `>` | Greater than | `score > 90` |
| `<` | Less than | `score < 60` |
| `>=` | Greater than or equal | `age >= 18` |
| `<=` | Less than or equal | `temp <= 0` |

---

### 3. Boolean Operators

| Operator | Meaning | Example |
| :---: | :--- | :--- |
| `and` | Both must be `True` | `age >= 18 and has_id == True` |
| `or` | At least one must be `True` | `user == "admin" or user == "root"` |
| `not` | Flips a `True` to `False` | `not is_banned` |

---

### 4. `match-case` — Structural Pattern Matching
Introduced in **Python 3.10**. A cleaner alternative to long `if-elif` chains when checking a single variable against specific values.
```python
match choice:
    case 1:
        print("Option 1")
    case 2:
        print("Option 2")
    case _:             # Default fallback (like 'else')
        print("Invalid Choice")
```
> Use `case _:` as the **default** (wildcard) to catch unexpected inputs — always include it.

---

## Common Mistakes & Pitfalls
1. **Using `=` instead of `==` in comparisons.** A single `=` assigns a value; `==` checks equality.
   ```python
   # Wrong (syntax error in conditions):
   if age = 18:

   # Correct:
   if age == 18:
   ```
2. **Converting passwords to `int()`:** Passwords can contain letters or leading zeros (e.g., `"007"`). Casting them to `int` will either crash or strip leading zeros. Always treat passwords as **strings**.
   ```python
   # Bug: Crashes if password has letters, strips leading zeros
   password = int(input("Password: "))

   # Correct:
   password = input("Password: ")
   ```
3. **Missing the wildcard `case _:`:** Without a default case in `match-case`, unexpected inputs are silently ignored with no feedback to the user.

4. **Off-by-one errors in ranges:** An age of exactly `25` should not fall between "YOUNG" and "OLD" ambiguously. Define boundaries precisely:
   ```python
   # Ambiguous: what happens at exactly 25?
   if age > 25:
       print("YOUNG")

   # Clear:
   elif age >= 18:
       print("ADULT")
   ```

---

## Best Practices
* **Validate early:** Check for invalid inputs (negative ages, zero denominators) at the top before your main logic runs. This is called a **guard clause**.
  ```python
  if age < 0:
      print("Invalid Age")
  elif age >= 18:
      print("Eligible to vote")
  else:
      print("Not eligible to vote")
  ```
* **One space around comparison operators:** `if age > 18:` not `if age>18:`.
* **Use boolean return functions:** Wrap a condition in a helper function so your intent is clear and reusable.
  ```python
  def is_eligible(age):
      return age >= 18    # Returns True or False

  if is_eligible(age):
      print("Can vote")
  ```

---

## Personal Observations from Your Code

| File | Observation |
| :--- | :--- |
| `Problem_1_Age_Classifier.py` | The original logic had no `CHILD` category and no guard against negative ages. An age of `-5` would have printed "TEEN". |
| `Problem_2_Number_Comparer.py` | Output said `"Both X and Y are Equal"` with capital E. In Python string output, only proper nouns are capitalised. |
| `Problem_1_Login_System.py` | Used `int("123456")` to set the password, then `int(input(...))` to get it — this would crash immediately if a user types any letter. Passwords must always be strings. |
| `smart_assistant.py` | The `year` variable for username generation was cast to `int`, which made it impossible to concatenate (join) with the username string. Since `username_generator` expects strings, `year` must remain a `str`. |
| `smart_assistant.py` | The print statement in temperature case 2 said `"Fahrenheit"` again instead of `"Celsius"` — same copy-paste pattern from Day 1! Always re-read your output strings after copying a block. |
| `smart_assistant.py` | Division-by-zero case asked for input again using a bare second `input()` call, but still did NOT check if the new value was also zero. |

---

## Interview-Style Questions

1. **Q: What is the difference between `=` and `==` in Python?**
   * `=` is the **assignment operator** (stores a value). `==` is the **comparison operator** (checks equality and returns `True` or `False`).

2. **Q: Why should passwords be stored and compared as strings and not integers?**
   * Passwords may contain non-numeric characters, and leading zeros in numeric strings (like `"007"`) are lost when converted to `int`. Strings compare safely character by character.

3. **Q: What does `case _:` do in a `match` statement?**
   * It acts as the **default wildcard** — it matches any value not caught by previous cases, equivalent to `else` in an `if-elif` chain.

4. **Q: What is a guard clause?**
   * A guard clause is an early `if` check at the top of a block that catches invalid input and exits (or prints an error) before running the main logic, keeping nested conditions shallow.

---

## Things to Revise Before Moving to the Next Lecture
- [ ] Practice writing `if-elif-else` chains that test at least 4 boundary conditions.
- [ ] Write at least one function that returns a boolean (`True`/`False`) and use it in an `if` statement.
- [ ] Build a `match-case` block with a nested inner `match-case` and a `case _:` fallback in both.
- [ ] Understand why `"5" == 5` is `False` in Python (type mismatch between `str` and `int`).
