# corpus.py
#   generates full nltk ready data corpus
# by: Noah Syrkis and edited by Johan Laursen

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
    data = [row.split(',') for row in data [1:-1]]
    authors = [row[1] for row in data]
    corpus = {}
    for idx, author in enumerate(authors):
        print(author)
        if ' ' in author:
            author = author.replace(' ', '_')
        author = author.lower()
        path = os.path.join(os.getcwd(), 'data', author)
        corpus[author] = {'titles' : { }, 'labels': {'birth' : data[idx][2], 'gender' : data[idx][-1], 'nationality' : data[idx][-2]}}
        for book in os.scandir(path):
            if book != '.DS_Store':
                # print(book)
                # print(author)
                # print(cleaner(book))
                corpus[author]['titles'][book] = {'sentences' : cleaner(book)}
    return corpus


def main():
    return constructor()

if __name__ == "__main__":
    print(main())

