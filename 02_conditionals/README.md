# 📂 Day 02: Conditionals

Welcome to **Day 02** of the Python Playlist! Today's focus is on control flow, comparison operators, boolean logic, and decision trees using Python's conditional statements (`if`, `elif`, `else`) and structural pattern matching (`match-case`).

## Learning Objectives
* Understand control flow and how programs make decisions.
* Use comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`) to evaluate conditions.
* Combine logic statements using boolean operators (`and`, `or`, `not`).
* Implement Python's modern structural pattern matching (`match-case`).
* Prevent program crashes by validating user inputs (e.g., negative ages, empty strings, division by zero).

## Concepts Covered
* **Control Flow:** `if`, `elif`, `else` execution hierarchies.
* **Boolean Logic:** Truth tables and combining checks using `and` and `or`.
* **Pattern Matching:** Using `match` and `case` with default wildcards (`case _`).
* **Input Validation:** Guarding calculations against zero denominators or out-of-bound variables.

---

## Folder Structure

```text
02_conditionals/
├── practice_problems/
│   ├── Problem_1_Age_Classifier.py       # Classifies age cohorts with boundary safety
│   ├── Problem_2_Number_Comparer.py      # Checks greater, smaller, and equality properties
│   └── Problem_3_Voting_Eligibility.py   # Boolean helper functions and voting checks
├── challenge_problems/
│   └── Problem_1_Login_System.py         # Credentials authenticator using string inputs
└── mini_project/
    ├── smart_assistant.py                # Interactive command center compiling all tools
    └── sentiment_analyzer.py             # 🧠 Rule-based NLP sentiment classifier (Bonus)
```

---

## Practice & Challenge Problems Summary

1. **Problem 1: Age Classifier**
   * **Goal:** Accept an age and categorize the user into `"CHILD"`, `"TEEN"`, `"YOUNG"`, or `"OLD"`, with safety guards for negative numbers.
2. **Problem 2: Number Comparer**
   * **Goal:** Compare two integers and declare the greater number or state if they are equal.
3. **Problem 3: Voting Eligibility**
   * **Goal:** Determine if a user can vote (18+) using a boolean return helper function (`is_eligible()`).
4. **Challenge Problem 1: Login System**
   * **Goal:** Verify a username and password match hardcoded credentials. Safe input methods prevent non-numeric entry crashes.

---

## Mini Project Explanation

### Smart Assistant
The **Smart Assistant** (`mini_project/smart_assistant.py`) compiles all Day 1 and Day 2 exercises into an interactive CLI application. It features:
* A main match-case menu routing to different functions.
* Clean submenus (e.g., temperature scale selections).
* Nested matching systems.
* Input validation structures (like preventing division-by-zero crashes on calculator tools).

### 🧠 NLP Sentiment Analyzer (Bonus Mini Project)
The **Sentiment Analyzer** (`mini_project/sentiment_analyzer.py`) is a rule-based Natural Language Processing project built using only the concepts from Days 1 and 2. It demonstrates how conditionals and string methods can power real-world NLP tasks. It features:
* **Text cleaning** — strips whitespace and lowercases input via `clean_text()`.
* **Keyword scoring** — counts positive and negative signal words using `.count()` calls (a no-loops technique).
* **Sentiment classification** — compares scores with `if/elif/else` to return `Positive`, `Negative`, or `Mixed Emotions`.
* **Confidence scoring** — measures the gap between scores to output `High`, `Moderate`, or `Low` confidence.
* A clean `main()` function that ties all steps into a single analysis pipeline.

---

## 🧠 Application to ML, NLP & Data Science
* **Decision Trees in Machine Learning:** Random Forests and Decision Trees are complex nested chains of conditionals (e.g., `if feature_x >= value: go to left node`). Understanding conditionals helps you comprehend how these predictive algorithms subset data.
* **Data Sanitization & Labeling:** Conditional statements are the basis of feature labeling pipelines (e.g., classifying text length features into categories or labeling ages for demographic segmentation in Data Science).

---

## Example Outputs

### Problem 1: Age Classifier
```text
Enter your age: 15
TEEN
```

### Problem 3: Voting Eligibility
```text
Enter your age: 20
You are eligible to vote.
```

### Challenge Problem 1: Login System
```text
Enter your Username: msumar
Enter your password: admin
Incorrect Credentials
```

### Mini Project: Smart Assistant
```text
Enter 1 for temperature Conversion
Enter 2 for Username Generator
Enter 3 for Grade Checker
Enter 4 for Calculator
Enter 5 for Age Classifier
Enter your choice: 4
Enter 1 for Addition
Enter 2 for Subtraction
Enter 3 for Multiplication
Enter 4 for Division
Enter your choice: 4
Enter 1st number: 10
Enter 2nd number: 0
Error: Denominator cannot be zero.
```

### 🧠 NLP Sentiment Analyzer
```text
Enter a review or comment to analyze: This product is amazing and I love the great quality!
   Word Count       : 10
   Character Count  : 56
   Positive Signals : 3
   Negative Signals : 0
   Sentiment        : Sentiment is Positive
   Confidence       : Confidence Score is high
```
