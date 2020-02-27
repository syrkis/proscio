

def read_file(filename):  
   
    with open(filename) as file:
        names = [lines.replace("\n", "") for lines in file]
        return set(names)

female_names = read_file("female.txt") 
male_names = read_file("male.txt")



def find_unisex_names(): 
    return set(male_names).intersection(set(female_names)) 
    


def main():
    #filename = "female.txt"
    #print(read_file(filename))
    #filename = "male.txt"
    #print(read_file(filename))
   
    male_names = read_file("male.txt") 
    female_names = read_file("female.txt")  
    print(find_unisex_names())
    
    

if __name__ == '__main__':
    main()
    
   
