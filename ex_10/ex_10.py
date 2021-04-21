fileName = input("Enter a file name: ")

try:
    fhand = open(fileName)
except:
    print("ERROR: There is not a file with this name.")
    quit()

counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

for key, value in sorted(counts.items(), reverse=True):
    print(key, value)