# corpus.py
#   generates full nltk ready data corpus
# by: Noah Syrkis and Johan Laursen

#imports
import os
from cleaner import cleaner

# generate corpus
# dictionary with author names as keys and values of: {dictionary with unigrams and labels as keys}
# unigrams is a list of all unigrams from the author's work
# labels is meta data of author

def constructor():

    with open(os.path.join("data","meta.csv"),'r') as file:
        data = file.read()
    data = data.split('\n')
    data = [row.split(',') for row in data [1:]]
    authors = [row[1] for row in data]
    corpus = {}
    for idx, author in enumerate(authors):
        # print('__________________________________', author)
        if ' ' in author:
            author = author.replace(' ', '_')
        author = author.lower()
        path = os.path.join(os.getcwd(), 'data', author)
        corpus[author] = {'titles' : { }, 'labels': {'birth' : data[idx][2], 'gender' : data[idx][-1], 'nationality' : data[idx][-2]}}
        for book in os.scandir(path):
            # print(book.name)
            if book.name != '.DS_Store':
                corpus[author]['titles'][book.name[:-4]] = {'sentences' : cleaner(book)}
    return corpus


def main():
    return constructor()

if __name__ == "__main__":
    print(main())

