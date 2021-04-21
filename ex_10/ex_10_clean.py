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

print( sorted( [ (value, key) for key,value in counts.items() ], reverse=True ) )