#used links for testing:-
#https://py4e-data.dr-chuck.net/comments_42.html
#https://py4e-data.dr-chuck.net/comments_2284801.html


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


all_num = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url - ")
file = urllib.request.urlopen(url, context=ctx).read()
parsed = BeautifulSoup(file, 'html.parser')

tag = parsed('span')
for x in tag:
    #print("\n\n")
    #print('span:', x)
    #print('number/content:', x.contents[0])
    num = x.contents[0]
    converted = int(num)
    all_num.append(converted)


print(sum(all_num))

