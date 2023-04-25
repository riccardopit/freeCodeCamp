fname = input("Enter file name: ")
try:
    fopen = open(fname)
except:
    print("File doesn't exist.")
    quit()
dlist = list()  #list for the dictionary
for line in fopen:
    if line.startswith('From:'):
        nlist = line.split()    #new list
        dlist.append(nlist[1])
counts = dict() #dictionary
for name in dlist:
    counts[name] = counts.get(name,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)