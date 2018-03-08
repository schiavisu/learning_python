name = input("Enter file name: ")
fh = open(name)
counts=dict()
lst= list()
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        words = line.split()
        lst.append(words[1])
for word in lst:
    print(word)
    counts[word]=counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
