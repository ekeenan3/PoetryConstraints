# Takes some input text and creates a new sentence/paragraph by removing words
# from the original text. It takes the words of the input text, splits them
# into words, and tags their part of speech. Then it generates some random
# sentence pattern(s) based on some parameters and the text and goes through
# the words of the text in order building the sentence pattern to get some text
# that could be built just by removing words from the original text.

import nltk
import pickle
import random

# How many times to try sentence patterns before giving up
tries = 100

# Load sentence patterns
f = open("models\sentence_patterns.pickle", "rb")
model = pickle.load(f)


# Parameters
backwards = False

# Split text into words and tag the parts of speech
def process(text):
    word_list = nltk.word_tokenize(text)
    words_with_tags = nltk.pos_tag(word_list)
    return words_with_tags

# Generates an order of parts of speech to use as a sentence pattern
# Then it takes the pattern and applies it to the list of words with tags
# Changing backwards applies the pattern from the end of the words to the start
def apply_pattern(words_with_tags):
    # Try matching patterns tries times and find the best match
    best_sentence = ""
    best_success = 0
    for t in range(tries):
        # Choose a random pattern. Frequency may be used in a future version
        pattern = random.choice(list(model)).split(" ")

        sentence = ""
        # The index of how far the program has found matches
        word_id = 0
        # The index of the tag it's searching for
        tag_id = 0
        # How many matches it's found
        success = 0
        # Reverse the input if backwards
        if backwards:
            words_with_tags.reverse()
        # Go until all tags have matches or run out of words or no matches
        while tag_id < len(pattern):
            # Which words are left
            words_left = words_with_tags[word_id:]
            # Only continue if the search found something
            last_tag = tag_id
            # Check each availible word's part of speech against pattern
            for i in range(len(words_left)):
                if words_left[i][1] == pattern[tag_id]:
                    # Add matched word to sentence and increase values
                    sentence += " " + words_left[i][0]
                    success += 1
                    tag_id +=1
                    word_id += 1 + i
                # If matched all tags stop searching
                if tag_id >= len(pattern):
                    break
                # If no words left stop searching
                if word_id >= len(words_with_tags):
                    break
            # If search found nothing stop searching
            if tag_id == last_tag:
                break
        # Find percent success
        success /= len(pattern)
        # Update best sentence
        print(success)
        if success > best_success:
            best_sentence = sentence[1:]
            best_success = success
    return best_sentence

text = input()
words_with_tags = process(text)
print(apply_pattern(words_with_tags))
