# PoetryConstraints
remove_to_meaning.py takes some text and finds a few sentences that can be made just by removing words from the original text.
lipogram_checker.py takes some text and some letters and checks to see if the text is a lipogram of (aka doesn't use) those letters and if it does use some of them, it reccomends synonyms of the same part of speech that don't use the forbidden letters.
n_plus.py takes some text and replaces each word that it can find in the dictionary with a word 7 (this can be changed) entries later in the dictionary. Wordlist used can be found here: http://www-personal.umich.edu/~jlawler/wordlist
process_sentences.py creates a dictionary of possible sentence structures and their frequency given a file that is a list of english sentences. The data file is not included because it's 67MB. The data can be found here: https://tatoeba.org/eng/downloads
