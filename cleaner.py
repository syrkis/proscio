# cleaner.py
#   cleans scraped data
# by: Noah Syrkis


# cleaner
def cleaner(file):
    data = opener(file)
    data = legal(data)
    data = "".join(data)
    data = lower(data)
    data = character(data)
    return data


# reads lines of file
def opener(file):
    data = open(file, 'r').readlines()
    return data


# removes gutenberg legals
def legal(data):
    start_line = "*** START OF THIS PROJECT GUTENBERG"
    end_line = "End of the Project Gutenberg"
    start = 0; end = -1
    for i in range(len(data)):
        if start_line in data[i]:
            start = i+1
        if end_line in data[i]:
            end = i
    data = data[start:end]
    return data


# converts to lower case
def lower(data):
    return data.lower()


# character corrections
def character(data):
    delete = ['â\x80\x99', 'â\x80\x98', '--', 'â\x80\x99', 'â\x80\x99']
    for string in delete:
        data = data.replace(string, ' ')
    return data


# call stack
def main():
    return cleaner('./data/joseph_conrad/lord_jim.txt')

if __name__ == "__main__":
    print(main())