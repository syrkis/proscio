# analyser.py
#   natural language analysis script
# by: Noah Syrkis

#  imports
import os
import nltk; nltk.download('punkt')
import requests
from nltk.stem import *
from nltk.stem.porter import *
from nltk.tokenize import RegexpTokenizer
from cleaner import book_cleaner
from features import features

features_dict, authors_path = features()
titles = [title for title in features_dict.keys()]
path = os.getcwd(); data = 'data'

def constructor(title):
    author = features_dict[title][0]
    author.replace(' ', '_')
    directory = os.path.join(path, data, author, title)
    entry = [book_cleaner(directory), features_dict[title]]


# file analysis
def analysis(file):
    data = book_cleaner(file)
    data = [word for sentence in data for word in sentence]
    import requests
    stopwords = requests.get('https://stopwords.syrkis.com')
    stopwords = stopwords.text.split('\n')
    stopwords = [word for word in stopwords]
    essentials = [word for word in data if word not in stopwords]
    essentials = [word for word in essentials if word not in ['t', 'th', 's', 'o']]
    stemmed = stemmer(essentials)
    uniques = sorted(set(data))
    freq_dist = nltk.FreqDist(stemmed)
    bigrams = list(nltk.bigrams(data))
    return freq_dist.most_common(300)

# stem words
def stemmer(tokens):
    stem = PorterStemmer()
    singles = [stem.stem(token) for token in tokens]
    return singles


def main():
    print(features_dict['heart_of_darkness.txt'])
    print(authors_path)
    # return constructor('heart_of_darkness.txt')
    # file = './data/joseph_conrad/lord_jim.txt'
    # return analysis(file)

if __name__ == "__main__":
    print(main())