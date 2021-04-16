fileName = input('Enter a file name: ')

try:
    fhandle = open(fileName)
except:
    print('There is not a file wiht this name.')
    quit()

counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)