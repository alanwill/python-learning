name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()
listemails = []
listhours = []
hours = dict()

# Loop through the file and ignore any line that does NOT start with 'From '
for line in handle:
    if not line.startswith('From ') : continue
    line = line.rstrip()
    parsed = line.split()
    listemails.append(parsed[5])

for line in listemails:
    parsed = line.split(':')
    listhours.append(parsed[0])

for hour in listhours:
    hours[hour] = hours.get(hour,0) + 1

tmp = list()

for val, key in hours.items():
    tmp.append( (val, key) )

tmp.sort()

for val, key in tmp[:]:
    print val, key





