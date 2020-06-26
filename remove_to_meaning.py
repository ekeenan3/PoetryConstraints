# Takes some input text and creates a new sentence/paragraph by removing words
# from the original text. It takes the words of the input text, splits them
# into words, and tags their part of speech. Then it generates some random
# sentence pattern(s) based on some parameters and the text and goes through
# the words of the text in order building the sentence pattern to get some text
# that could be built just by removing words from the original text.

# Parameters
backwards = False

# Split text into words and tag the parts of speech
def process(text):
    pass

# Generates an order of parts of speech to use as a sentence pattern
def generate_pattern():
    pass

# Takes the pattern and applies it to the list of words with tags
# Changing backwards applies the pattern from the end of the words to the start
def apply_pattern(pattern, words_with_tags, backwards=False):
    pass
