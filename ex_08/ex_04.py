fileName = input("Enter file name: ")

try:
    fhand = open(fileName)
except:
    print("There is not a file with this name.")
    quit()

uniqueWordList = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in uniqueWordList:
            uniqueWordList.append(word)

uniqueWordList.sort()

print(uniqueWordList)