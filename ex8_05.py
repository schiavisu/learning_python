fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[1])
    count=count+1
print(count)
