# cleaner.py
#   prepares file for nlp analysis
# by: Noah Syrkis

# import statements
import os
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import *
from nltk.stem.porter import *
import random


# standardizer
def cleaner(file):
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
    filedata = open(file, 'r', encoding='utf-8')
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

#Takes in author_corpus, shuffles it and then splits it into n new features
def title_features(author_corpus, n=30, log=False):  # note used to be called author_features thus author_corpus input
    """Input:
        author_corpus is a list of sentences (list) or a list of words (strings)
        n is the number of desired chunks to split the input
        log=False if True it returns n*log(len(input)) chunks
        
        Return:
            returns a list of features each of which is a dictionary"""
   
    # including the if check because I'm not sure if it works properly with lists of strings instead of lists of lists
    if not all(isinstance(x, str) for x in author_corpus):
        words=[]
        for sentence in author_corpus:
            words += sentence
    else:
        words = author_corpus

    if log == True:
        n=int(n*math.log(len(words),2))
    
    random.shuffle(words)
    def chunks(lst, n):  # taken from stackoverflow
        """Yield successive n-sized chunks from lst."""
        n = len(lst)//n
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    features = list(chunks(words, n))
    document_words_list = []

    for feature in features:
        document_words_list.append(set(feature))
    #document_words = set(words)
    features_list = []
    for document_words in document_words_list:

        features = {}
        for word in word_features:
            features[f'contains({word})'] = (word in document_words)
        features_list.append(features)
    return features_list






# call stack
def main():
    return cleaner('./data/joseph_conrad/lord_jim.txt')
    # author_paths = os.listdir('data')
    # author_books_structure = {}
    # for author in author_paths:
    #     if os.path.isdir(os.path.join(os.getcwd(), 'data', author)):
    #         author_books_structure[author] = author_books_data(author)
    # return author_books_structure
    # return cleaner('./data/joseph_conrad/lord_jim.txt')

if __name__ == "__main__":
    print(main())
