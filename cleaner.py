# cleaner.py
#   cleans scraped data
# by: Noah Syrkis

# import statements
import os

# global viariables
start_line = "*** START OF THIS PROJECT GUTENBERG"
end_line = "End of the Project Gutenberg"

# switches out special characters with proper character
def legal(file_name):
    start = 0; end = -1
    prose = open(file_name, 'r').readlines()
    for i in range(len(prose)):
        if start_line in prose[i]:
            start = i+1
        if end_line in prose[i]:
            end = i
    prose = prose[start:end]
    return prose[:10]


# removes legal stuff
def essence():
    pass

# call stack
def main():
    pass

if __name__ == "__main__":
    main() 