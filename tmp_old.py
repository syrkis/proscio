# tmp
#   temporary work space
# by: Noah Syrkis

# import statements
from corpus import constructor
import nltk
import sys

# prelimnary nltk analysis
def analysis(data):
    return data['joseph conrad']['labels']['gender']


# calls stack
def main():
    data = constructor()
    return analysis(data)

if __name__ == "__main__":
    print(main())  