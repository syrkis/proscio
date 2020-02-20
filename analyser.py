# analyser.py
#   natural language analysis script
# by: Noah Syrkis

# import statements and preliminary downloads
import nltk
from nltk.stem.porter import *
nltk.download('punkt')
from cleaner import cleaner
import os

# global bvariables
lordjim = './data/joseph_conrad/lord_jim.txt'

# precursory analysis
def nostromo():
    data = cleaner(lordjim)
    tokens = nltk.word_tokenize(data)
    return tokens[:100]

def main():
    return nostromo()

if __name__ == "__main__":
    print(main())