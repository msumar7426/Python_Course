# 📂 Day 01: Functions and Variables

Welcome to **Day 01** of the Python Playlist! Today is all about the building blocks: defining variables to store data, interacting with the user, cleaning up text inputs, and writing your first custom Python functions.

## Learning Objectives
* Understand how variables store data in memory.
* Interact with users using input and output functions (`input()`, `print()`).
* Perform string cleaning and manipulation using built-in methods.
* Implement basic mathematical calculations using integer and float representations.
* Define custom functions with parameters and return values to design modular programs.
* Organize code using a standard execution entry point (`main()`).

## Concepts Covered
* **Basic I/O:** `print()`, `input()`, string concatenation, and f-strings.
* **String Methods:** `.strip()`, `.lower()`, `.title()`, `.split()`.
* **Data Types:** `str`, `int`, `float`.
* **Custom Functions:** `def`, arguments/parameters, return values, scope.
* **Floating-Point Formatting:** Rounding values using f-string precision (e.g., `{value:.4f}`).
* **Code Structure:** Structuring code with `main()` functions.

---

## Folder Structure

```text
01_functions_variables/
├── practice_problems/
│   ├── Problem_1_Clean_User_Name.py              # Removes spaces & downcases user name
│   ├── Problem_2_Email_Extractor.py              # Splits email to extract the name prefix
│   ├── Problem_3_Sentence_Analyzer.py            # Counts words and total characters
│   ├── Problem_4_CelciusToFahrenheit_Converter.py # Converts °C to °F using floats
│   ├── Problem_5_FahrenheitToCelsius_Converter.py # Converts °F to °C using floats
│   └── Problem_6_Simple_Calculator.py            # Basic arithmetic calculator (+, -, *, /)
├── challenge_problems/
│   └── Problem_1_Generate_Username.py            # Custom username generator (name + birth year)
├── mini_project/
│   └── Text_Analyzer.py                          # Comprehensive string operations engine
```

---

## Practice Problems Summary

1. **Problem 1: Clean User Name**
   * **Goal:** Accept a user's name, strip extra spaces, convert it to lowercase, and print the output.
   * **Skills:** Input handling, string methods (`.strip()`, `.lower()`).

2. **Problem 2: Email Extractor**
   * **Goal:** Extract and display the username portion of an email address (everything before the `@` symbol).
   * **Skills:** String splitting (`.split()`), list indexing.

3. **Problem 3: Sentence Analyzer**
   * **Goal:** Take a sentence as input, clean it, count the number of words, and find the total characters.
   * **Skills:** Length check (`len()`), whitespace splitting.

4. **Problem 4: Celsius to Fahrenheit Converter**
   * **Goal:** Define a helper function to convert a Celsius input float to Fahrenheit.
   * **Skills:** Function arguments, float parsing, f-string float precision styling.

5. **Problem 5: Fahrenheit to Celsius Converter**
   * **Goal:** Define a helper function to convert Fahrenheit float inputs to Celsius.
   * **Skills:** Arithmetic conversion logic, function return values, output formatting.

6. **Problem 6: Simple Calculator**
   * **Goal:** Build four arithmetic helper functions (`add`, `subtract`, `multiply`, `division`) and display results for two numbers.
   * **Skills:** Modular arithmetic function design, multiple return values.

---

## Challenge Problems Summary

1. **Problem 1: Generate Username**
   * **Goal:** Create a username generator that extracts the first name (lowercased/stripped) and appends their birth year.
   * **Skills:** Compound string methods, function invocation, string concatenation.

---

## Mini Project Explanation

### Text Analyzer
The **Text Analyzer** (`mini_project/Text_Analyzer.py`) is a unified tool designed to process a string and print five statistics:
1. The text in lowercase.
2. The text in uppercase.
3. The text in title case.
4. The first word of the text.
5. The total length of the text.

It demonstrates a structured architecture by implementing specialized helper functions (`lowercase()`, `uppercase()`, `titlecase()`, `first_word()`, `character_count()`) called from a central `main()` loop.

---

## Skills Learned
* **Input Cleaning:** Removing leading/trailing whitespaces to avoid data contamination.
* **Basic Type Casting:** Using `float()` to convert raw string inputs for math calculations.
* **f-Strings:** Constructing formatted output strings with inline variable evaluations and custom decimal precision.
* **Custom Function Scoping:** Declaring local variables inside custom functions and using `return` to pass results to `main()`.

---

## 🧠 Application to ML, NLP & Data Science
* **Text Preprocessing in NLP:** Cleaning text inputs using `.strip()` and `.lower()`, and segmenting sentences using `.split()`, are the exact foundational steps of tokenization and preprocessing required for NLP training pipelines (e.g., preparing text for bag-of-words or TF-IDF representations).
* **Feature Engineering & Transformation:** Defining isolated, deterministic mathematical functions (like temperature scaling and basic calculations) mimics the custom transformers needed to engineer features and normalize inputs before feeding datasets into machine learning algorithms.

---

## Example Outputs

### Problem 4: Celsius to Fahrenheit Converter
```text
Enter the temp in Celsius: 25.5
The temperature in Fahrenheit will be 77.9000
```

### Problem 5: Fahrenheit to Celsius Converter
```text
Enter temp in F: 77.9
The temperature in Celsius will be 25.5000
```

### Problem 6: Simple Calculator
```text
Enter first number: 10
Enter second number: 3
The result of Addition will be 13.0
The result of Subtraction will be 7.0
The result of Multliplication will be 30.0
The result of Division will be 3.3333333333333335
```

### Challenge Problem 1: Generate Username
```text
Enter your name: Alice Smith
Enter your birth year: 2004
Username will be alice2004
```

### Mini Project: Text Analyzer
```text
Enter a sentence: CS50 is awesome!
Lowercase      : cs50 is awesome!
Uppercase      : CS50 IS AWESOME!
Title Case     : Cs50 Is Awesome!
First Word     : CS50
Character Count: 16
```

---

## Future Improvements (Post-Lecture 0/1 Concepts)
1. **Validation & Exception Handling:** Using `try-except` blocks to handle non-numeric input for calculations (Lecture 3).
2. **Conditional Validation:** Guarding division calculations against dividing by zero (Lecture 1).
3. **Looping:** Allowing users to perform multiple calculations or analyze multiple strings without restarting the script (Lecture 2).
4. **Edge Case Safety:** Adding sanity checks for empty sentences or invalid email addresses.

## Key Takeaways
* In Python, all inputs returned from `input()` are of type `str` by default.
* Functions help compartmentalize complex logic, making code more readable, maintainable, and testable.
* Consistent variable naming and standard formatting improve collaborative development.
