fileName = input("Enter a file name:")

try:
    fhand = open(fileName)
except:
    print("There is not a file with this name.")
    quit()

for file in fhand:
    print(file.rstrip().upper())