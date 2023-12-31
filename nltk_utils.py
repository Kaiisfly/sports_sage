import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


# Function to tokenize a sentence
def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word: str):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag


# Example
'''
sentence = ['what', 'makes', 'topflight', 'special', '?']
words = ['how', 'what', 'who', 'why', 'makes', 'topflight', 'is', 'special', '?']
bag = bag_of_words(sentence, words)
print(bag)
output = [0. 1. 0. 0. 0. 1. 0. 1. 1.]
'''
# Split each word using tokenization (Test)
'''
a = "How long are the classes?"
print(a)
a = tokenize(a)
print(a)
'''

# Using stem function to generalize the word
'''

words = ["Organize", "organizes", "organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)
'''
