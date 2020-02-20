# analyser.py
#   natural language analysis script
# by: Noah Syrkis

# costum imports
from cleaner import cleaner
from cleaner import stopwords

# local imports
import os
import nltk

# nltk imports
# nltk.download('punkt')
from nltk.stem import *
from nltk.stem.porter import *
from nltk.tokenize import RegexpTokenizer



# file analysis
def analysis(file):
    data = cleaner(file)
    stopwords = open('stopwords.txt', 'r').read().split('\n')
    essentials = [word for word in data if word not in stopwords]
    essentials = [word for word in essentials if word not in ['t', 'th', 's', 'o']]
    stemmed = stemmer(essentials)
    uniques = sorted(set(data))
    freq_dist = nltk.FreqDist(stemmed)
    bigrams = list(nltk.bigrams(data))
    return freq_dist.most_common(100)


# stem words
def stemmer(tokens):
    stem = PorterStemmer()
    singles = [stem.stem(token) for token in tokens]
    return singles


def main():
    file = './data/joseph_conrad/lord_jim.txt'
    return analysis(file)

if __name__ == "__main__":
    print(main())