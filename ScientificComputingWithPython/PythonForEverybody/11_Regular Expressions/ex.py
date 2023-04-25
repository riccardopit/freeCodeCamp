import re
fname = input("Enter file name: ")
try:
    fopen = open(fname)
except:
    print("File doesn't exist.")
    quit()
slist = list()  #strings list
nlist = list()  #numbers list
for line in fopen:
    tlist = re.findall('[0-9]+', line)  #temporary list
    if len(tlist) < 1 : continue
    slist = slist + tlist
for num in slist:
    nlist.append(int(num))
print(sum(nlist))