import urllib.request, urllib.parse, urllib.error
file = urllib.request.urlopen("https://data.pr4e.org/romeo.txt") #reads the webpage as file with just one line of code

for line in file:
    print(line.decode().strip())
print("\n\n")
fhand = urllib.request.urlopen("https://www.dr-chuck.com/page1.htm") #can also read html file
for l in fhand:
    print(l.decode().strip())