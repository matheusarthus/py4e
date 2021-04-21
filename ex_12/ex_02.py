import socket

url = input('Enter the URL of the web site: ')

try:
    host = url.split('/')[2]
except:
    print("URL format is incorrect.")
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
mysock.send(cmd.encode())

count = 0

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    words = data.decode().split()
    for word in words:
        for character in word:
            count = count + 1
            if count < 3000: print(character)
mysock.close()

print("Total number of characters: ", count)
