# 🧠 Bonus Project: Rule-Based NLP Sentiment Analyzer

> **This project is not part of the CS50P curriculum.** It is a standalone applied NLP project built using only the concepts from **Lecture 1 (Functions & Variables)** and **Lecture 2 (Conditionals)**.

---

## 🎯 What Is Sentiment Analysis?

Sentiment Analysis is one of the most widely used tasks in **Natural Language Processing (NLP)**. It answers the question:

> *"Does this piece of text express a positive, negative, or neutral opinion?"*

It is used in:
* ⭐ **Product review systems** (Amazon, Google, App Stores)
* 📊 **Social media monitoring** (Twitter/X brand tracking)
* 📰 **News bias detection**
* 🤖 **Chatbot emotion understanding**

---

## 🔬 The NLP Concept Behind This Project: Bag of Words

This project implements a simplified version of the **Bag of Words (BoW)** model — one of the oldest and most foundational NLP techniques.

**How it works:**
1. Strip all formatting from the text (lowercase, remove spaces).
2. Look at which words appear and how often.
3. Map those words to a score based on a predefined vocabulary (positive/negative).

```text
"The product is great and amazing!" 
→ count("great") = 1, count("amazing") = 1
→ positive_score = 2, negative_score = 0
→ SENTIMENT: POSITIVE (HIGH confidence)
```

This is the exact same logic used by `sklearn`'s `CountVectorizer` before training a classification model — only here you are implementing it yourself from scratch using pure Python string methods.

---

## 📋 Your Task

Open [`sentiment_analyzer.py`](./sentiment_analyzer.py) and **implement the body of each function** marked with `# TODO`.

The function signatures, docstrings, hints, and `main()` are already written for you. **Do NOT modify them.**

### Functions to implement:

| Function | What It Does | Concepts Used |
| :--- | :--- | :--- |
| `clean_text(text)` | Strip spaces and lowercase | `.strip()`, `.lower()` |
| `get_word_count(text)` | Count words in text | `.split()`, `len()` |
| `get_char_count(text)` | Count total characters | `len()` |
| `count_positive_signals(text)` | Sum occurrences of positive keywords | `.count()`, addition |
| `count_negative_signals(text)` | Sum occurrences of negative keywords | `.count()`, addition |
| `classify_sentiment(pos, neg)` | Return POSITIVE / NEGATIVE / NEUTRAL | `if / elif / else` |
| `get_confidence(pos, neg)` | Return HIGH / MODERATE / LOW | `if / elif / else` |

---

## 📤 Expected Output

```text
==================================================
   NLP Sentiment Analyzer — CS50P Project
==================================================

Enter a review or comment to analyze:
> The product is absolutely amazing. I love it! Great quality, best purchase ever.

--------------------------------------------------
  📊 TEXT ANALYSIS REPORT
--------------------------------------------------
  Word Count      : 14
  Character Count : 72
--------------------------------------------------
  ✅ Positive Signals : 4
  ❌ Negative Signals : 0
--------------------------------------------------
  🎯 SENTIMENT   : ✅ POSITIVE
  📈 Confidence  : HIGH
--------------------------------------------------
```

---

## 💡 Keyword Reference

**Positive Keywords (10):**
`good`, `great`, `amazing`, `excellent`, `love`, `wonderful`, `fantastic`, `best`, `happy`, `awesome`

**Negative Keywords (10):**
`bad`, `terrible`, `awful`, `hate`, `worst`, `horrible`, `poor`, `disappointing`, `broken`, `useless`

---

## 🔗 Connection to Future Lectures
Once you learn **Loops (Lecture 3)**, you will be able to replace the repetitive `.count()` calls with a clean loop over the keyword list — making your code dramatically shorter and more professional.
