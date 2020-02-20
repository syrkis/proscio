# ${file}, Thu Feb 20 2020
# 
# by: Noah Syrkis

# import staements
from analysis import analysis

# gender analysis
def gender():
    meta = open('data/meta.csv', 'r').read().split('\n')
    meta = [line.split(';') for line in meta[1:]]
    for line in meta:
        line[7] = line[7].strip()
        if line[7] == 'Female':
            line[7] = 1
        else:
            line[7] = 0
        print(line[7])

def main():
    return gender()

if __name__ == "__main__":
    print(main()) 