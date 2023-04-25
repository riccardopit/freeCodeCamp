# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File doesn't exist")
    quit()    
count = 0
num = 0.0
avg = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    space = line.find(' ')
    num = num + float(line[space:].lstrip())
avg = num / count
print("Average spam confidence:",avg)