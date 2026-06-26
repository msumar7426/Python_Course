def lowercase(sentence):
    return sentence.lower()


def uppercase(sentence):
    return sentence.upper()


def titlecase(sentence):
    return sentence.title()


def first_word(sentence):
    return sentence.split()[0]


def character_count(sentence):
    return len(sentence)


def main():
    sentence = input("Enter a sentence: ")

    lowercase_result = lowercase(sentence)
    uppercase_result = uppercase(sentence)
    titlecase_result = titlecase(sentence)
    first_word_result = first_word(sentence)
    character_count_result = character_count(sentence)

    print(f"Lowercase : {lowercase_result}")
    print(f"Uppercase : {uppercase_result}")
    print(f"Title Case : {titlecase_result}")
    print(f"First Word : {first_word_result}")
    print(f"Character Count : {character_count_result}")


main()