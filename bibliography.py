# bibliography.py
#   generates nltk ready bibliography data structure for single author
# by: Noah Syrkis

# import statements
import os
from standardizer import standardize


# constructs
def bibliography(author):
    """constructs a dictionary for an author"""
    if ' ' in author:
        author = author.replace(' ', '_')
    author = author.lower()
    path = os.path.join(os.getcwd(),'data', author)
    bibliography = {author: {'unigrams': [], 'labels' : labeling(author)}}
    for book in os.scandir(path):
        unigrams = standardize(book)
        bibliography[author]['unigrams'] += unigrams
    return bibliography[author]


    # labeling data generation
def labeling(author):
    """takes in author name (lowercase) and with space, not underscore."""
    if '_' in author:
        author = author.replace('_', ' ')
    author = author.lower()
    data = metadata()
    data = data[author]
    return data


# generate meta data dictionary
def metadata():
    file = open('data/meta.csv', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    data = [row.split(',') for row in data]
    data = data[1:-1]
    dictionary = {row[1] : None for row in data}
    for i in range(len(data)):
        # key = print(data[i][1])
        dictionary[data[i][1]] = {'birth' : data[i][2], 'gender' : data[i][-1], 'nationality' : data[i][-2]}
    return dictionary

# calls stack
def main():
    return labeling('george_eliot')

if __name__ == "__main__":
    print(main()) 