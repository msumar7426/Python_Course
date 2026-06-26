"""Count the number of words in a sentence and the number 
of characters in the sentence."""

sentnce=input("Enter a sentence: ").strip()
word_count=len(sentnce.split())
char_count=len(sentnce)
print("Number of words in the sentence:", word_count)
print("Number of characters in the sentence:", char_count)
