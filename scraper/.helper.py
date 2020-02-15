# helper.py
#   development helper script
# by: Noah Syrkis

# improt statements
import re

# file reader
def reader(file):
    data = open(file, 'r').read()
    return data

def regex(file):
    pattern = "Title: .*"
    title = re.findall(pattern, file)
    title = title[0][7:]
    return "_".join(title[:].lower().split(' '))

# call stack
def main():
    data = reader('heart_of_darkness.txt')
    print(regex(data))

if __name__ == "__main__":
    main() 