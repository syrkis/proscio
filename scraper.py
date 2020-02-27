# scraper.py
#   downloads relevant books from crawled, nested arrays
# by: Noah Syrkis

# import statements
import re                                                                               # import regex expression library
import requests                                                                         # import internet browser
import time                                                                             # import timer for loop pause
import os                                                                               # import os so as to create directories
import datetime
import string


# global variables
nogo = r'\'".,:;%?_-/\()[]â¨Ã³ëäöüË'

# author-url constructor
def constructor(file):
    """generate a dictionary of authors and id's for scraping"""

    sheet = open(file, 'r').readlines()                                                 # open data sheet and read lines
    sheet = sheet[1:]
    sheet = [line.split(',') for line in sheet]                                         # split line into elements
    authors = [{'id' : line[0], 'name' : line[1]} for line in sheet if line[2] != '1']  # construct list of dictionaries of ids and names
    return authors                                                                      # return constructed dictionary for book url crawling


# book crawler
def crawler(authors):
    """generates list of top 25 book txt gutenberg download urls based on the input author id list"""

    books = {author['name']: [] for author in authors}                                  # dictionary to hold links for authors books                 
    pattern = 'ebooks/[0-9]*'                                                           # regex expression for finding books links on author pages
    base = 'http://www.gutenberg.org/files'                                             # base url for gutenberg files
    format = '-0.txt'                                                                   # format for download (could be switched to epub or html)

    for author in authors:                                                              # looping through authors
        url = "http://www.gutenberg.org/ebooks/author/" + author['id']                  # generating author url based on author id
        page = requests.get(url)                                                        # downloads content from gutenberg servers
        content = page.text                                                             # prepare content for regex matching
        urls = re.findall(pattern, content)                                             # regex matches contet
        urls = [url for url in urls if url != 'ebooks/']                                # removing empty links
        books[author['name']] = [base + url[6:] * 2 + format for url in urls]           # adding full links to books dict for scrape
        print(author, ' done')                                                          # status update
        time.sleep(0.3)                                                                   # sleep so as to not dos gutenberg

    return books                                                                        # returns dictionary with urls for scrape


# book scraper
def scraper(books):
    """scrapes data from given urls, and saves them as .txt files in directories corresponding to author names"""
    
    date = datetime.datetime.now()
    date = [date.year, date.month, date.day, date.hour, date.minute, date.second]
    date = [str(entry) for entry in date]
    date = "".join(date)    

    pattern = "Title: .*"                                                               # regex expression for finding titles in text
    skips = 0                                                                           # error counter
    scrapes = 0
    
    for author in books.keys():                                                         # outer author loop   
                                                      
        print('Starting scrape of', author)   
        directory = "".join([letter for letter in author if letter not in nogo])           # print new of author
        directory = "_".join(directory.lower().split(' '))                                 # create directory name from author name
        directory = 'dumps/' + date + '/' + directory
        if not os.path.exists(directory):                                               # ensuring directories do not already exists
            os.makedirs(directory)                                                      # makes author directory

        for book in books[author]:                                                      # looping through books in bibliography
            
            try:                                                                        # prevents programming from stopping in case of broken link
                page = requests.get(book)                                               # gets specific books .txt data from scraped url
                content = page.text                                                     # reads book data
                title = re.findall(pattern, content[:1000])                             # finds book title
                title = title[0][7:]                                                    # removes 'Title: ' from title-string
                title = "".join([letter for letter in title if letter not in nogo])
                file_name = "_".join(title[:-1].lower().split(' ')) + '.txt'            # removes spaces and convers to lower case for title
                outfile = open(directory + '/' + file_name, 'w')                        # generating file to be written in, in author directory
                outfile.write(content)                                                  # writing content to file
                outfile.close()                                                         # closes file
                print('Scraped', title)                                                 # informs stdout of successfull scrape
                scrapes += 1
                time.sleep(0.3)                                                           # waits for a second so as to not accedentally dos-attack gutenberg
                continue                                                                # continue   
            
            except:                                                                     # handler for if anything above goes wrong
                skips += 1                                                              # increment error counter
                print("Skip: ", skips)                                                  # print error notification to stdout
                time.sleep(0.3)                                                           # waits for a second so as to not accedentally dos-attack gutenberg
                pass                                                                    # continue

    print(scrapes, "scraped works in total")


# call stack
def main():
    authors = constructor('./data/meta.csv'); print("Procss initiated")         # generate author dictionary
    books = crawler(authors); print("Author dictionary generated")              # generate books urls
    scraper(books); print("Books links lists constructed")                      # perform scrape
    return 0

if __name__ == "__main__":
    main() 