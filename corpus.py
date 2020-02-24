# bibliography.py
#   generates nltk ready bibliography data structure for single author
# by: Noah Syrkis

# import statements
import os
from cleaner import cleaner


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


# constructs bibliography 
def bibliography(author):
    """constructs a dictionary for an author"""
    if ' ' in author:
        author = author.replace(' ', '_')
    author = author.lower()
    path = os.path.join(os.getcwd(),'data', author)
    bibliography = {author: {'unigrams': [], 'labels' : labeling(author)}}
    for book in os.scandir(path):
        unigrams = cleaner(book)
        bibliography[author]['unigrams'] += unigrams
    return bibliography[author]


    # labeling data generation
def labeling(author):
    """takes in author name (lowercase) and with space, not underscore."""
    if '_' in author:
        author = author.replace('_', ' ')
    author = author.lower()
    data = metadata(author)
    return data


# generate meta data dictionary
def metadata(author):
    file = open('data/meta.csv', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    data = [row.split(',') for row in data]
    data = data[1:-1]
    dictionary = {row[1] : None for row in data}
    for i in range(len(data)):
        dictionary[data[i][1]] = {'birth' : data[i][2], 'gender' : data[i][-1], 'nationality' : data[i][-2]}
    return dictionary[author]

# calls stack
def main():
    return constructor()

if __name__ == "__main__":
    print(main()) 