import urllib.request

url = input('Enter the URL of the web site: ')

try:
    fhand = urllib.request.urlopen(url)
except:
    print("URL does not exist.")
    quit()

count = 0

for line in fhand:
    words = line.decode().strip().split()
    for word in words:
        for character in word:
            count = count + 1
            if count < 3000: print(character)

print("Total number of characters: ", count)
