import os


#untested script

#potential points of failure:
#"data" might need to be renamed to \data or /data or something equivalent
# if umlaut[0] in str(author) should work
#script needs to be run in the directory where the data folder is located



authors=os.listdir("data")

#removes non folders from list of authors i.e meta.csv
authors=[author for author in authors if os.path.isdir(os.path.join("data",author))]


# please include all the (umlaut, replace) pairs in this list
umlauts=[]

cwd = os.getcwd()
path=cwd

for idx, author in enumerate(authors):
    for umlaut in umlauts:

        if umlaut[0] in str(author):
            tmp = authors[idx]
            authors[idx].replace(umlaut[0],umlaut[1])
            os.rename(os.path.join(path,"data",tmp),os.path.join(path,"data",authors[idx]))

    titles=os.listdir(os.path.join(path,"data",author[idx]))
    for idx2, title in enumerate(titles):
        for umlaut in umlauts:
            if umlaut[0] in str(title):
                tmp= titles[idx2]
                titles[idx2].replace(umlaut[0],umlaut[1])
                os.rename(os.path.join(path,"data",authors[idx],tmp), os.path.join(path,"data",authors[idx],titles[idx2]))



