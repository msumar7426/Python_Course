
# KEYWORD LISTS 

POSITIVE_WORDS = [
    "good", "great", "amazing", "excellent", "love",
    "wonderful", "fantastic", "best", "happy", "awesome"
]

NEGATIVE_WORDS = [
    "bad", "terrible", "awful", "hate", "worst",
    "horrible", "poor", "disappointing", "broken", "useless"
]


# HELPER FUNCTIONS 

def clean_text(text):
    # Remove leading/trailing spaces and convert the text to lowercase.
    return text.strip().lower()


def get_word_count(text):
    #Count the number of words in the text.
    word_count=len(text.split())
    return word_count



def get_char_count(text):
    # Count the total number of characters in the text (including spaces).
    char_count=len(text)
    return char_count


def count_positive_signals(text):
    """
    Count how many times any positive keyword appears in the text.
    Each keyword can appear more than once , count every occurrence.

    Since you haven't learned loops yet, we can use individual
    .count() calls and add them together like this:
        score = text.count("good") + text.count("great") + ...
    """
    positive_score=0
    positive_score+=(text.count("good")+text.count("great")+text.count("amazing")+text.count("excellent")
    +text.count("love")+text.count("wonderful")+text.count("fantastic")+text.count("best")
    +text.count("happy")+text.count("awesome"))

    return positive_score


def count_negative_signals(text):
    """
    Count how many times any negative keyword appears in the text.
    Each keyword can appear more than once , count every occurrence.
    
    """
    negative_score=0
    negative_score+=(text.count("poor")+text.count("disappointing")+text.count("broken")+text.count("useless")
    +text.count("bad")+text.count("terrible")+text.count("awful")+text.count("hate")
    +text.count("worst")+text.count("horrible"))
    return negative_score
    


def classify_sentiment(pos_score, neg_score):
    """
    Determine the overall sentiment based on positive and negative scores.

    """
    if pos_score>neg_score:
        return "Sentiment is Positive"
    elif neg_score>pos_score:
        return "Sentiment is Negative"
    else:
        return "Mixed Emotions"


def get_confidence(pos_score, neg_score):
    """
    Determine the confidence level of the sentiment prediction
    based on how far apart the two scores are.

    """
    if abs(pos_score-neg_score)>=3:
        return "Confidence Score is high"
    elif abs(pos_score-neg_score)>=1:
        return "Confidence Score is Moderate"
    else:
        return "Confidence Score is Low"

    
def main():
    raw_text = input("Enter a review or comment to analyze: ")

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
    print(f"   Word Count       : {words}")
    print(f"   Character Count  : {chars}")
   
    print(f"   Positive Signals : {pos_score}")
    print(f"   Negative Signals : {neg_score}")

    print(f"   Sentiment        : {sentiment}")
    print(f"   Confidence       : {confidence}")
   


main()
