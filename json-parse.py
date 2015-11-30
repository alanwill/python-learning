import json
import urllib

address = raw_input('Enter location: ')
if len(address) < 1 : quit()

url = urllib.urlopen(address)
data = url.read()
comments = json.loads(str(data))

#print json.dumps(comments, indent=4)
#print 'Commentor Count:', len(comments)
#counts = comments['comments'][1]['count']
#print counts

commentsum = 0
counter = 0

for item in comments['comments']:
    #print 'Count', item['count']
    commentsum = commentsum + int(item['count'])
    #counter = counter + 1


print 'Count:', len(comments['comments'])
print 'Sum:', commentsum
