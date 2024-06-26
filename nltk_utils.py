import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Define question words
question_words = [
    "color", "car", "model", "discuss", "fuel", "type", "price", "manufactured",
    "year", "engine", "size", "horsepower", "acceleration", "time", "automatic",
    "manual", "mileage", "safety", "features", "entertainment", "internal",
    "external", "customer", "rating", "units", "sold", "last"
]

def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    stemming = find the root form of the word
    """
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

# Example usage
sentence = "What is the color of the car?"
tokenized_sentence = tokenize(sentence)
print(bag_of_words(tokenized_sentence, question_words))
