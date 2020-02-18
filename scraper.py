# scraper.py
#   downloads relevant books from crawled, nested arrays
# by: Noah Syrkis

# import statements
import re                                                                               # import regex expression library
import requests                                                                         # import internet browser
import time                                                                             # import timer for loop pause
import os                                                                               # import os so as to create directories


# author-url constructor
def constructor(file):
    """generate a dictionary of authors and id's for scraping"""

    sheet = open(file, 'r').readlines()                                                 # open data sheet and read lines
    sheet = sheet[1:]
    sheet = [line.split(';') for line in sheet]                                         # split line into elements
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
        time.sleep(1)                                                                   # sleep so as to not dos gutenberg

    return books                                                                        # returns dictionary with urls for scrape


# book scraper
def scraper(books):
    """scrapes data from given urls, and saves them as .txt files in directories corresponding to author names"""
    
    pattern = "Title: .*"                                                               # regex expression for finding titles in text
    skips = 0                                                                           # error counter
    
    for author in books.keys():                                                         # outer author loop   
                                                      
        print('Starting scrape of', author)                                             # print new of author
        directory = "_".join(author.lower().split(' '))                                 # create directory name from author name
        if not os.path.exists(directory):                                               # ensuring directories do not already exists
            os.makedirs(directory)                                                      # makes author directory

        for book in books[author]:                                                      # looping through books in bibliography
            
            try:                                                                        # prevents programming from stopping in case of broken link
                page = requests.get(book)                                               # gets specific books .txt data from scraped url
                content = page.text                                                     # reads book data
                title = re.findall(pattern, content[:1000])                             # finds book title
                title = title[0][7:]                                                    # removes 'Title: ' from title-string
                nogos = ['[', ']', '/', '.', ',', '(', ')', '-', '_', '*', '—']
                title = [letter for lette in title if letter not in nogos]
                file_name = "_".join(title[:-1].lower().split(' ')) + '.txt'            # removes spaces and convers to lower case for title
                outfile = open(directory + '/' + file_name, 'w')                        # generating file to be written in, in author directory
                outfile.write(content)                                                  # writing content to file
                outfile.close()                                                         # closes file
                print('Scraped', title)                                                 # informs stdout of successfull scrape
                time.sleep(1)                                                           # waits for a second so as to not accedentally dos-attack gutenberg
                continue                                                                # continue   
            
            except:                                                                     # handler for if anything above goes wrong
                skips += 1                                                              # increment error counter
                print("Skip: ", skips)                                                  # print error notification to stdout
                time.sleep(1)                                                           # waits for a second so as to not accedentally dos-attack gutenberg
                pass                                                                    # continue


# call stack
def main():
    print("Procss initiated")                                                   # status update
    authors = constructor('../data/authors.csv')                                        # generate author dictionary
    print("Author dictionary generated")                                        # status update
    books = crawler(authors)                                                    # generate books urls
    print("Books links lists constructed")                                      # status update
    scraper(books)                                                              # perform scrape
    print("Prcess completed")                                                   # status update

if __name__ == "__main__":
    main() 