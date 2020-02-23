# corpus.py
#   generates full nltk ready data corpus, marging features and labels
# by: Noah Syrkis

# import import statements
import os
from bibliography import bibliography

# generate corpus
def constructor():
    """returns nltk ready data structure"""
    file = open('data/meta.csv', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    data = [row.split(',') for row in data[1:-1]]
    authors = [row[1] for row in data]
    datastructure = {}
    for author in authors:
        datastructure[author] = bibliography(author)
    return datastructure

# calls stack
def main():
    return constructor()

if __name__ == "__main__":
    print(main())  