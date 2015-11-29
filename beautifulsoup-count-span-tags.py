import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

numlist = list()
runtotal = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    numlist.append(int(tag.contents[0]))

for val in numlist:
    runtotal = runtotal + val

print 'Count', len(numlist)
print 'Sum', runtotal


