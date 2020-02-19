# analyser.py
#   natural language analysis script
# by: Noah Syrkis

# import statements and preliminary downloads
import nltk
from cleaner import legal
nltk.download('punkt')
import os

# global bvariables
lordjim = './data/joseph_conrad/lord_jim.txt'

# precursory analysis
def nostromo():
    data = legal(lordjim)
    print(data)

def main():
    print(nostromo())
    return

if __name__ == "__main__":
    main()