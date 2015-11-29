# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import ssl
from BeautifulSoup import *

url = raw_input('Enter URL : ')
position = raw_input('Enter position : ')
count = raw_input('Enter count : ')

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()
soup = BeautifulSoup(data)

# Retrieve all of the anchor tags
tags = soup('a')

links = list()

for tag in tags:
    links.append(tag.get('href', None))

print 'Retrieving: ', links[0]
print 'Retrieving: ', links[int(position)-1]

link = links[int(position)-1]
counter = 1
while counter < int(count):
    uh = urllib.urlopen(link, context=scontext)
    data = uh.read()
    soup = BeautifulSoup(data)

    # Retrieve all of the anchor tags
    tags = soup('a')

    links = list()

    for tag in tags:
        links.append(tag.get('href', None))
    print 'Retrieving: ', links[int(position)-1]
    link = links[int(position)-1]
    counter = counter + 1

