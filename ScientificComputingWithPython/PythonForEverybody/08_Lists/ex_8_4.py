fname = input("Enter file name: ")
try:
    fopen = open(fname)
except:
    print("File doesn't exist.")
    quit()
ftext = fopen.read()    #file text (a string)
flist = ftext.split()   #file list (list of strings from file text)
nlist = list()  #new list (empty)
for word in flist:
    if word in nlist:
        continue
    nlist.append(word)
nlist.sort()    #new list (sorted)
print(nlist)