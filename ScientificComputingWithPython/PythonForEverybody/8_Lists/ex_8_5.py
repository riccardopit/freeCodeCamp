fname = input("Enter file name: ")
try:
    fopen = open(fname)
except:
    print("File doesn't exist.")
    quit()
count = 0
for line in fopen:
    if line.startswith('From:'):
        nlist = line.split()    #new list
        print(nlist[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")