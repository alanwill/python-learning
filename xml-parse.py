import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
if len(address) < 1 : quit()

url = urllib.urlopen(address)
data = url.read()
print data
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print 'Number of commentors:', len(results)
commentsum = 0
for comment in results:
    commentsum = commentsum + int(comment.find('count').text)

print 'Sum of comments:', commentsum