# analyser.py
#   natural language analysis script
# by: Noah Syrkis

# costum imports
from cleaner import cleaner
from cleaner import stopwords

# local imports
import os

# nltk imports
import nltk
nltk.download('punkt')
from nltk.stem import *
from nltk.stem.porter import *



# file analysis
def analysis(file):
    data = cleaner(file)
    tokens = nltk.word_tokenize(data)
    essentials = stopwords(tokens)
    # stemmed = stemmer(tokens)
    uniques = sorted(set(tokens))
    freq_dist = nltk.FreqDist(essentials)
    bigrams = list(nltk.bigrams(tokens))
    collocations = nltk.collocations(data)
    return freq_dist.most_common(10), bigrams[:10], collocations


# precursory analysis
def tokenize(file):
    data = cleaner(file)
    tokens = nltk.word_tokenize(data)
    return data[:100]


# stem words
def stemmer(tokens):
    stem = PorterStemmer()
    singles = [stem.stem(token) for token in tokens]
    return singles

# tokenize words

def main():
    file = './data/joseph_conrad/lord_jim.txt'
    return analysis(file)

if __name__ == "__main__":
    print(main())