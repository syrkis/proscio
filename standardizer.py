# cleaner.py
#   prepares file for nlp analysis
# by: Noah Syrkis

# import statements
import os
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import *
from nltk.stem.porter import *


# standardizer
def standardize(file):
    """returns list of stemmed and standardized list of sentences (also in list forms)"""
    data = opener(file)
    data = legal(data)
    data = [line[:-1] for line in data]
    # data = stemmer(data)
    data = " ".join(data)
    data = data.replace(r'â', '')
    sentences = data.split('.')
    tokenizer = RegexpTokenizer(r'\w+')
    data = [tokenizer.tokenize(sentence) for sentence in sentences]
    data = [sentence for sentence in data if len(sentence) > 0]
    # data = tokenizer.tokenize(data)
    # data = [word for word in data if word not in stopwords]
    return data


# stems work
def stemmer(tokens):
    stem = PorterStemmer()
    singles = [stem.stem(token) for token in tokens]
    return singles


# reads lines of file
def opener(file):
    filedata = open(file, 'r')
    data = filedata.readlines()
    data = [line.lower() for line in data]
    filedata.close()
    return data


# removes gutenberg legals
def legal(data):
    start_line = "*** START OF THIS PROJECT GUTENBERG".lower()
    end_line = "End of the Project Gutenberg".lower()
    start = 0; end = -1
    for i in range(len(data)):
        if start_line in data[i]:
            start = i+1
        if end_line in data[i]:
            end = i
    data = data[start:end]
    return data


# call stack
def main():
    return standardize('./data/joseph_conrad/lord_jim.txt')
    # author_paths = os.listdir('data')
    # author_books_structure = {}
    # for author in author_paths:
    #     if os.path.isdir(os.path.join(os.getcwd(), 'data', author)):
    #         author_books_structure[author] = author_books_data(author)
    # return author_books_structure
    # return cleaner('./data/joseph_conrad/lord_jim.txt')

if __name__ == "__main__":
    print(main())