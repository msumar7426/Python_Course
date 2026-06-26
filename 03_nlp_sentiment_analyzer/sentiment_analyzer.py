"""
NLP Sentiment Analyzer — Scaffold File
=======================================
Your task: implement the body of each function marked with TODO.
Do NOT change function names, parameters, or the main() function.
Read each docstring carefully before writing your solution.

Concepts used: string methods (Lecture 1), custom functions (Lecture 1),
               if/elif/else and boolean logic (Lecture 2).

How scoring works:
  - Positive keywords add +1 to the positive score.
  - Negative keywords add +1 to the negative score.
  - The difference between scores determines sentiment and confidence.
"""


# ─── KEYWORD LISTS (already defined for you — do not change) ──────────────────

POSITIVE_WORDS = [
    "good", "great", "amazing", "excellent", "love",
    "wonderful", "fantastic", "best", "happy", "awesome"
]

NEGATIVE_WORDS = [
    "bad", "terrible", "awful", "hate", "worst",
    "horrible", "poor", "disappointing", "broken", "useless"
]


# ─── HELPER FUNCTIONS (you implement the body) ────────────────────────────────

def clean_text(text):
    """
    Remove leading/trailing spaces and convert the text to lowercase.

    Parameters:
        text (str): The raw input from the user.

    Returns:
        str: The cleaned, lowercased version of the text.

    Example:
        clean_text("  I LOVE this product!  ") → "i love this product!"

    Hint: chain .strip() and .lower()
    """
    # TODO: return the text after stripping whitespace and converting to lowercase
    pass


def get_word_count(text):
    """
    Count the number of words in the text.

    Parameters:
        text (str): The cleaned text.

    Returns:
        int: The number of words.

    Example:
        get_word_count("i love this product") → 4

    Hint: use .split() to break the text into words, then len()
    """
    # TODO: split the text into words and return the count
    pass


def get_char_count(text):
    """
    Count the total number of characters in the text (including spaces).

    Parameters:
        text (str): The cleaned text.

    Returns:
        int: The number of characters.

    Example:
        get_char_count("i love this") → 11

    Hint: use len()
    """
    # TODO: return the character count of the text
    pass


def count_positive_signals(text):
    """
    Count how many times any positive keyword appears in the text.
    Each keyword can appear more than once — count every occurrence.

    Parameters:
        text (str): The cleaned text.

    Returns:
        int: The total count of positive keyword occurrences.

    Example:
        count_positive_signals("great product, great quality") → 2

    Hint: use text.count("keyword") for each word in POSITIVE_WORDS.
          Add all the counts together.

    Note: Since you haven't learned loops yet, use individual
          .count() calls and add them together like this:
            score = text.count("good") + text.count("great") + ...
    """
    # TODO: count occurrences of each word in POSITIVE_WORDS and return the total
    pass


def count_negative_signals(text):
    """
    Count how many times any negative keyword appears in the text.
    Each keyword can appear more than once — count every occurrence.

    Parameters:
        text (str): The cleaned text.

    Returns:
        int: The total count of negative keyword occurrences.

    Example:
        count_negative_signals("terrible product, totally broken") → 2

    Hint: same approach as count_positive_signals but for NEGATIVE_WORDS.
    """
    # TODO: count occurrences of each word in NEGATIVE_WORDS and return the total
    pass


def classify_sentiment(pos_score, neg_score):
    """
    Determine the overall sentiment based on positive and negative scores.

    Rules:
        - If pos_score is greater than neg_score  → return "POSITIVE"
        - If neg_score is greater than pos_score  → return "NEGATIVE"
        - If both scores are equal                → return "NEUTRAL"

    Parameters:
        pos_score (int): Total positive keyword count.
        neg_score (int): Total negative keyword count.

    Returns:
        str: One of "POSITIVE", "NEGATIVE", or "NEUTRAL".

    Hint: use if / elif / else
    """
    # TODO: compare pos_score and neg_score and return the correct sentiment label
    pass


def get_confidence(pos_score, neg_score):
    """
    Determine the confidence level of the sentiment prediction
    based on how far apart the two scores are.

    Rules:
        - If the difference between scores is 3 or more → "HIGH"
        - If the difference is 1 or 2                   → "MODERATE"
        - If the difference is 0                         → "LOW"

    Parameters:
        pos_score (int): Total positive keyword count.
        neg_score (int): Total negative keyword count.

    Returns:
        str: One of "HIGH", "MODERATE", or "LOW".

    Hint: calculate the absolute difference.
          If pos_score is 5 and neg_score is 2, difference = 5 - 2 = 3.
          If neg_score is bigger, difference = neg_score - pos_score.
          Use an if/elif/else to return the right label.
    """
    # TODO: calculate the score difference and return the confidence level
    pass


# ─── MAIN FUNCTION (already written — do not change) ─────────────────────────

def main():
    print("=" * 50)
    print("   NLP Sentiment Analyzer — CS50P Project")
    print("=" * 50)
    print()

    raw_text = input("Enter a review or comment to analyze:\n> ")

    # Step 1: clean
    text = clean_text(raw_text)

    # Step 2: basic stats
    words = get_word_count(text)
    chars = get_char_count(text)

    # Step 3: keyword scoring
    pos_score = count_positive_signals(text)
    neg_score = count_negative_signals(text)

    # Step 4: classify
    sentiment = classify_sentiment(pos_score, neg_score)
    confidence = get_confidence(pos_score, neg_score)

    # Step 5: print report
    print()
    print("-" * 50)
    print("  📊 TEXT ANALYSIS REPORT")
    print("-" * 50)
    print(f"  Word Count      : {words}")
    print(f"  Character Count : {chars}")
    print("-" * 50)
    print(f"  ✅ Positive Signals : {pos_score}")
    print(f"  ❌ Negative Signals : {neg_score}")
    print("-" * 50)

    if sentiment == "POSITIVE":
        print(f"  🎯 SENTIMENT   : ✅ {sentiment}")
    elif sentiment == "NEGATIVE":
        print(f"  🎯 SENTIMENT   : ❌ {sentiment}")
    else:
        print(f"  🎯 SENTIMENT   : ⚖️  {sentiment}")

    print(f"  📈 Confidence  : {confidence}")
    print("-" * 50)


main()
