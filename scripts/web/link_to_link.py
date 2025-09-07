#link used : https://py4e-data.dr-chuck.net/known_by_Rebekha.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
counting = int(input('Enter count: '))
pos = int(input('Enter position: '))
x = 0

# Retrieve all the anchor tags


while x < counting:
    html = urllib.request.urlopen(url, context=ctx).read() #opening web page
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') #it's a list

    link = tags[pos-1]
    print("person name",link.contents[0])
    url = link.get('href', None) #reading it from 'link'th position


    x += 1
