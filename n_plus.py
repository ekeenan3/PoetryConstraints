
# Takes the input and replaces each word with the word n entries after it in
# the Merriam Webster dictionary. May later include options to maintain the part
# of speech, different dictionaries, etc. Based on the Oulipo constraint n+7

# Import re to use regex for maintaining punctuation
import re

# Get input
text_input = input()
maintain_capital = True
maintain_punctuation = True

# Preprocess input
def preprocess(text):
    # Split text into word list
    words = text.split(' ')

    # Find which words are capitalized and save them if maintaining capital
    is_capital = []
    if maintain_capital:
        is_capital = [word[0].isupper() for word in words]

    # Then remove capital letters
    words = [word.lower() for word in words]

    # Find which words have punctuation and save the punctuation if maintaining it
    punctuation = {}
    if maintain_punctuation:
        for i in range(len(words)):
            if re.search("[^a-z]", words[i]) is not None:
                punctuation[i] = re.search("[^a-z]", words[i]).group(0)

    # Then remove punctuation
    words = [re.search("[a-z]+", words[i]).group() for i in range(len(words))]

    return words, is_capital, punctuation

def n_plus(n, words):
    print(words)
    # Open and read wordlist
    f = open("data\wordlist.txt", "r")
    word_list = f.read().splitlines()

    # Add n to the index of each word in words
    for i in range(len(words)):
        words[i] = word_list[word_list.index(words[i])+n]

    return words

# Postprocess words with capitalization punctuation and spaces
def postprocess(words, is_capital=[], punctuation={}):
    # Uppercase the words that were capitalized before n_plus
    if maintain_capital:
        for i in range(len(words)):
            if is_capital[i]:
                words[i] = words[i].capitalize()

    # Append punctuation that was in text before n_plus
    if maintain_punctuation:
        for i in punctuation:
            words[i] = words[i] + punctuation[i]

    # Join words with spaces between
    text = " ".join(words)

    return text

# Run functions
words, is_capital, punctuation = preprocess(text_input)
words = n_plus(7, words)
text_output = postprocess(words, is_capital, punctuation)

# Return (print) the text output
print(text_output)
