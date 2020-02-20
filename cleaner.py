# cleaner.py
#   prepares file for nlp analysis
# by: Noah Syrkis

# import statements
import nltk
# nltk.download('punkt')
from nltk.tokenize import RegexpTokenizer

# cleaner
def cleaner(file):
    """returns list of normalized words"""
    stopwords = open('stopwords.txt', 'r').read().split('\n')
    data = opener(file)
    data = legal(data)
    data = [line[:-2] for line in data]
    data = " ".join(data)
    data = data.replace('â', '')
    tokenizer = RegexpTokenizer(r'\w+')
    data = tokenizer.tokenize(data)
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


# character corrections
def character(data):
    delete = [r'â\x80\x99', r'â\x80\x98', '--', r'â\x80\x99', r'â\x80\x99', '_', r'â\\x80\\x9']
    data = [entry for entry in data if entry not in delete]
    return data

# remove stop words
def stopwords(data):
    words = open('stopwords.txt', 'r').read().split('\n')
    data = [word for word in data if word not in words]
    return data

# call stack
def main():
    return cleaner('./data/joseph_conrad/lord_jim.txt')

if __name__ == "__main__":
    print(main())