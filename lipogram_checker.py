# Takes some input text and a list of letters that are not allowed. Finds any
# words with letters that are not allowed, tags their part of speech, and
# suggests synonyms that are of the same part of speech and do not contain the
# forbidden letters.

# Import nltk and specifically wordnets to find synonyms
import nltk
from nltk.corpus import wordnet as wn

# test = "He told the fish to fish"
# tokens = nltk.word_tokenize(test)
# words_pos = nltk.pos_tag(tokens)
# print(words_pos)

# Finds words in text with forbidden letters and tags their parts of speech
def process(text, letters):
    # Split text into words
    words = nltk.word_tokenize(text)

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
    for i in range(len(forbidden_words)):
        word_tag = list(forbidden_words[i])
        if word_tag[1] == "CC":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "CD":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "DT":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "EX":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "FW":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "IN":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "JJ":
            word_tag[1] = wn.ADJ
        elif word_tag[1] == "JJR":
            word_tag[1] = wn.ADJ
        elif word_tag[1] == "JJS":
            word_tag[1] = wn.ADJ
        elif word_tag[1] == "LS":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "MD":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "NN":
            word_tag[1] = wn.NOUN
        elif word_tag[1] == "NNS":
            word_tag[1] = wn.NOUN
        elif word_tag[1] == "NNP":
            word_tag[1] = wn.NOUN
        elif word_tag[1] == "NNPS":
            word_tag[1] = wn.NOUN
        elif word_tag[1] == "PDT":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "POS":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "PRP":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "PRP$":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "RB":
            word_tag[1] = wn.ADV
        elif word_tag[1] == "RBR":
            word_tag[1] = wn.ADV
        elif word_tag[1] == "RBS":
            word_tag[1] = wn.ADV
        elif word_tag[1] == "RP":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "TO":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "UH":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "VB":
            word_tag[1] = wn.VERB
        elif word_tag[1] == "VBD":
            word_tag[1] = wn.VERB
        elif word_tag[1] == "VBG":
            word_tag[1] = wn.VERB
        elif word_tag[1] == "VBN":
            word_tag[1] = wn.VERB
        elif word_tag[1] == "VBP":
            word_tag[1] = wn.VERB
        elif word_tag[1] == "VBZ":
            word_tag[1] = wn.VERB
        elif word_tag[1] == "WDT":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "WP":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "WP$":
            word_tag[1] = "OTHER"
        elif word_tag[1] == "WRB":
            word_tag[1] = wn.ADV
        else:
            print("This program forgot about: " + word_tag[1])
            word_tag[1] = "OTHER"
        forbidden_words[i] = tuple(word_tag)
    # Returns forbidden_words
    return forbidden_words

# Finds synonyms that follow the letter rules for each forbidden word
def give_synonyms(words, letters):
    synonym_list = []
    # Loop through forbidden words
    for word in words:
        synonyms = []
        # If part of speech is noun, adjective, adverb, or noun, find synonyms
        if word[1] != "OTHER":
            # Get list of synonyms of the same part of speech
            synset = wn.synsets(word[0],pos=word[1])
            for lemma in synset[0].lemmas():
                # Check word against each forbidden letter
                allowed = True
                for letter in letters:
                    if letter in lemma.name():
                        allowed = False
                # Add synonym to list if it is allowed
                if allowed:
                    synonyms.append(lemma.name())
        # Add list of synonyms to the list of lists of synonyms
        synonym_list.append(synonyms)

    # Return forbidden words and synonyms
    return synonym_list

# Get input text and forbidden letter list
text = input()
letters = input().split(" ")

# Get list of tuples with forbidden words and their part of speech
words_with_tags = process(text, letters)

# Get list of lists of synonyms, one list for each forbidden word
synonyms = give_synonyms(words_with_tags, letters)
for i in range(len(words_with_tags)):
    print(words_with_tags[i][0] + " uses a forbidden letter. Some possible synonyms that are allowed are: " + ", ".join(synonyms[i]))
