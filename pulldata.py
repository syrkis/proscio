import os

import difflib as db
# WORK IN PROGRESS PLEASE DO NOT EDIT
# By Johan Laursen



# Folder data should be in the directory from which you're running this script

#list of authors from directory names, excludes any files in directory

data="data"  # folder path component containing the data
authors=os.listdir(data)
authors=[author for author in authors if os.path.isdir(os.path.join("data",author))]


cwd = os.getcwd()
path=cwd


# keys are titles of document and values contain the meta information for those titles
documents = {}
meta=[]
with open(os.path.join(path,data,"meta2.csv"), "r", encoding='utf-8', newline='') as file:
        lines = file.readlines()
        for line in lines:
            line=line.split(",")
            for i in range(len(line)):
                line[i]=line[i].strip()
            meta.append(line)


authors=[author[0] for author in meta[1:]]


authors2=os.listdir(data)
authors2=[author for author in authors2 if os.path.isdir(os.path.join(data,author))]
compare=[]
for idx, author in enumerate(authors):
    tmp = db.get_close_matches(author,authors2, n=1, cutoff=0.3)
    compare.append((author,tmp))



for idx, author in enumerate(authors2):


    titles=os.listdir(os.path.join(path,data,authors2[idx]))
    for idx2, title in enumerate(titles):
        #authors doesn't include meta line zero thus add 1
        meta_index = authors.index(db.get_close_matches(author,authors, n=1,cutoff=0.3)[0])+1  
        documents[str(title)]=meta[meta_index]
print(documents)
