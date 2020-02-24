# ngram.py
#   returns {1,2,3,4,5}-grams
# by: Noah Syrkis

# import statements
from corpus import constructor


def ngrams(n, sentences):
    grams = []
    for sentence in sentences:
        if len(sentence) >= n:
            for i in range((len(sentence)-n)+1):
                grams.append(sentence[i:i+n])
    return grams


# calls stack
def main():
    data = constructor()
    victory = data['joseph_conrad']['titles']['victory']['sentences']
    return ngrams(3, victory)

if __name__ == "__main__":
    print(main())  