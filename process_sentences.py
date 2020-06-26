# This file was used to create bigram and trigram conditional frequency
# distributions for the parts of speech of English sentences. It loads a list
# of English sentences, tags their parts of speech, then finds the each
# possible sentence pattern and its frequency into a dictionary then saves it

import nltk
import pickle

# Amount of sentence data to use. Takes more time if larger
size = 1000000

# Load the sentences
f = open("data\sentences.txt", "r", encoding="utf-8")
sentences = f.readlines(size)
f.close()

# Turn each sentence into a list of words
words_list = [nltk.word_tokenize(s) for s in sentences]

# Turn list of lists of words into a list of lists of tagged words
pos_sentence = []
for i in range(len(words_list)):
    pos_sentence.append(nltk.pos_tag(words_list[i]))

# Turn list of lists of tagged words into list of lists of tags
parts_of_speech = []
for i in range(len(pos_sentence)):
    parts_of_speech.append([])
    for j in range(len(pos_sentence[i])):
        parts_of_speech[i].append(pos_sentence[i][j][1])

# Create dictionary of all possible sentence patterns with frequency
sentence_patterns = {}
for sentence in parts_of_speech:
    pattern = " ".join(sentence)
    if pattern in sentence_patterns:
        sentence_patterns[pattern] += 1
    else:
        sentence_patterns[pattern] = 1

# Check the dictionary
print(sentence_patterns)

# Save both cfds
f = open("models\sentence_patterns.pickle", "wb")
pickle.dump(sentence_patterns, f)
f.close()
