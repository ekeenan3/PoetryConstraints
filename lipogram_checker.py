# Takes some input text and a list of letters that are not allowed. Finds any
# words with letters that are not allowed, tags their part of speech, and
# suggests synonyms that are of the same part of speech and do not contain the
# forbidden letters.

# Import nltk and specifically wordnets to find synonyms
import nltk
from nltk.corpus import wordnets as wn

# test = "He told the fish to fish"
# tokens = nltk.word_tokenize(test)
# words_pos = nltk.pos_tag(tokens)
# print(words_pos)

# Finds words in text with forbidden letters and tags their parts of speech
def process(text, letters):
    # Split text into words
    words = nltk.word_tokenize(test)

    # Find forbidden words and put them in a list
    forbidden_words = []
    for word in words:
        for letter in letters:
            if letter in word:
                forbidden_words.append(word)

    # Tag the parts of speech of the words
    forbidden_words = nltk.pos_tag(forbidden_words)

    # Simplifies parts of speech tags for wordnets into NOUN, ADJ, ADV, VERB
    # Also changes parts of speech that don't fit those four to OTHER
    # I could have used a dictionary.
    for word_tag in forbidden_words:
        if word_tag[1] == "CC":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "CD":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "DT":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "EX":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "FW":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "IN":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "JJ":
            word_tag[1] = "ADJ"
        else if word_tag[1] == "JJR":
            word_tag[1] = "ADJ"
        else if word_tag[1] == "JJS":
            word_tag[1] = "ADJ"
        else if word_tag[1] == "LS":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "MD":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "NN":
            word_tag[1] = "NOUN"
        else if word_tag[1] == "NNS":
            word_tag[1] = "NOUN"
        else if word_tag[1] == "NNP":
            word_tag[1] = "NOUN"
        else if word_tag[1] == "NNPS":
            word_tag[1] = "NOUN"
        else if word_tag[1] == "PDT":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "POS":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "PRP":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "PRP$":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "RB":
            word_tag[1] = "ADV"
        else if word_tag[1] == "RBR":
            word_tag[1] = "ADV"
        else if word_tag[1] == "RBS":
            word_tag[1] = "ADV"
        else if word_tag[1] == "RP":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "TO":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "UH":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "VB":
            word_tag[1] = "VERB"
        else if word_tag[1] == "VBD":
            word_tag[1] = "VERB"
        else if word_tag[1] == "VBG":
            word_tag[1] = "VERB"
        else if word_tag[1] == "VBN":
            word_tag[1] = "VERB"
        else if word_tag[1] == "VBP":
            word_tag[1] = "VERB"
        else if word_tag[1] == "VBZ":
            word_tag[1] = "VERB"
        else if word_tag[1] == "WDT":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "WP":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "WP$":
            word_tag[1] = "OTHER"
        else if word_tag[1] == "WRB":
            word_tag[1] = "ADV"

    # Returns forbidden_words
    return forbidden_words


text = input()
letters = input().split(" ")
words = process(text, letters)
