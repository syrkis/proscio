# scraper.py
#   downloads relevant books from crawled, nested arrays
# by: Noah Syrkis


# import statements
import re
import requests


# book crawler
def crawler(authors):
    """generates list of top 25 book txt gutenberg download urls based on the input author id list"""

    books = {author['name']: None for author in authors}                        # dictionary to hold links for authors books                 
    pattern = 'ebooks/[0-9]*'                                                   # regex expression for finding books links on author pages
    base = 'http://www.gutenberg.org/files'                                     # base url for gutenberg files
    format = '-0.txt'                                                           # format for download (could be switched to epub or html)

    for author in authors:                                                      # looping through authors
        url = "http://www.gutenberg.org/ebooks/author/" + author['id']          # generating author url based on author id
        page = requests.get(url)                                                # downloads content from gutenberg servers
        content = page.text                                                     # prepare content for regex matching
        urls = re.findall(pattern, content)                                     # regex matches contet
        urls = [url for url in urls if url != 'ebooks/']                        # removing empty links
        books[author['name']] = [base + url[6:] * 2 + format for url in urls]   # adding full links to books dict for scrape

    return books                                                                # returns dictionary with urls for scrape


# book scraper
def scraper(books):
    for author in books.keys():
        directory = "_".join(author.lower().split(' '))
        for book in books[author]:
            print(book)

# call stack
def main():
    data = [
        {'id': '9', 'name': "Herman Melville"},
        {'id': '125', 'name': "Joseph Conrad"}
        ]

    urls = crawler(data)

    names = scraper(urls)
    print(names)

if __name__ == "__main__":
    main() 