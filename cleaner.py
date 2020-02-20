# cleaner.py
#   prepares file for nlp analysis
# by: Noah Syrkis

# import statements
import nltk
from nltk.tokenize import RegexpTokenizer

# cleaner
def cleaner(file):
    """returns list of normalized words"""
    data = opener(file)
    data = legal(data)
    data = [line[:-2] for line in data]
    data = " ".join(data)
    data = data.replace('â', '')
    sentences = data.split('.')
    tokenizer = RegexpTokenizer(r'\w+')
    data = [tokenizer.tokenize(sentence) for sentence in sentences]
    data = [sentence for sentence in data if len(sentence) > 0]
    # data = tokenizer.tokenize(data)
    # data = [word for word in data if word not in stopwords]
    return data

# reads lines of file
def opener(file):
    data = open(file, 'r').readlines()
    data = [line.lower() for line in data]
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
    return cleaner('./data/joseph_conrad/lord_jim.txt')

if __name__ == "__main__":
    print(main())