# Learning Log

A running journal documenting my progression through CS50P, tracking learning hours, completed exercises, and architectural insights.

---

## 📈 Learning Summary

* **Total Completed Modules:** 2 / 9
* **Current Status:** Completed Lecture 2 (Conditionals)
* **Last Updated:** June 26, 2026

---

## 📓 Daily/Lecture Logs

### [Lecture 2] Conditionals
* **Date Completed:** June 26, 2026
* **Duration:** ~3 hours (including study, exercise, and mini-project)
* **Completed Exercises:**
  * 3 Practice Problems (Age Classifier, Number Comparer, Voting Eligibility)
  * 1 Challenge Problem (Login System)
  * 1 Mini-Project ([smart_assistant.py](../02_conditionals/mini_project/smart_assistant.py))
* **Key Learning Insights:**
  * Boolean operators (`and`, `or`) combine comparisons cleanly into a single readable condition.
  * `match-case` simplifies code that needs to route between many exact choices — much cleaner than stacked `if-elif` chains.
  * **Guard clauses** (early `if` checks for invalid input at the top of logic blocks) prevent crashes and produce helpful error messages.
  * Passwords and credential data must NEVER be cast to `int` — they should always remain strings.
* **Next Steps:** Proceed to Lecture 3 (Loops) to learn how to repeat actions without copy-pasting code.

### [Lecture 1] Functions & Variables
* **Date Completed:** June 26, 2026
* **Duration:** ~4 hours (including study, exercise, and documentation setup)
* **Completed Exercises:**
  * 6 Practice Problems (Casing, Email splitting, sentence calculations, temperature conversions, calculator)
  * 1 Challenge Problem (Username Generator)
  * 1 Mini-Project ([Text_Analyzer.py](../01_functions_variables/mini_project/Text_Analyzer.py))
* **Key Learning Insights:**
  * Importance of input cleaning (`.strip()`, `.lower()`) before database entry or processing.
  * Formatted output using Python f-strings with custom float rounding (`{val:.4f}`).
  * Breaking down complex programs into custom helper functions called from `main()` to improve testability.
* **Next Steps:** Proceeded to Lecture 2 (Conditionals).
