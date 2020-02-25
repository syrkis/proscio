
def read_title(filetitle): 
    with open(filetitle) as file:
        names = [lines.replace("\n", "") for lines in file]
        return set(names)

female_names = read_title("female.txt") 
male_names = read_title("male.txt")


def read_book(filename):  
    a_test = []

    with open(filename) as file:
        names = [lines.replace(" ,", "") for lines in file]
        for lines in names: 
            names = lines.split("\n")            
            for i in names: 
                m = i.split(" ")
                some = [lines.replace(" ", '') for lines in m]
                for i in some:                    
                    a_test.append(i)
                 
    return set(a_test)


book = read_book("Firstyearprojekt/demographics_and_sociolinguistics/data/charles_dickens/a_christmas_carol.txt") 
#male_names = read_file("male.txt")

def find_unisex_names(): 
    return set(male_names).intersection(set(book)) 
    return set(female_names).intersection(set(book))
    


def main():
    filename = "Firstyearprojekt/demographics_and_sociolinguistics/data/charles_dickens/a_christmas_carol.txt"
    
    #print(read_book(filename))
    filetitle = "male.txt"
    #print(read_title(filetitle))
    filetitle = "female.txt"
    #print(read_title(filename))
    book = read_book("Firstyearprojekt/demographics_and_sociolinguistics/data/charles_dickens/a_christmas_carol.txt")  
    male_names = read_title("male.txt") 
    female_names = read_title("female.txt")  
    print(find_unisex_names())
    
    

if __name__ == '__main__':
    main()
    
   
