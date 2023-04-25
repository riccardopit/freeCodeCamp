fname = input("Enter file name: ")
try:
    fopen = open(fname)
except:
    print("File doesn't exist.")
    quit()
dlist = list()  #list for the dictionary
for line in fopen:
    if line.startswith('From '):
        list1 = line.split()    #new list 1st split
        list2 = list1[5].split(":") #new list 2nd split
        dlist.append(list2[0])
counts = dict()
for num in dlist:
    counts[num] = counts.get(num,0) + 1
for k,v in sorted(counts.items()):
    print(k,v)