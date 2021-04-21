import urllib.request
from bs4 import BeautifulSoup

url = input('Enter the URL of the web site: ')

try:
    html = urllib.request.urlopen(url).read()
except:
    print("URL does not exist.")
    quit()

try:
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('p')
except:
    print('HTML parsing has been failed.')

print('The total of tag is:', len(tags))
