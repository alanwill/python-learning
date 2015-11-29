import re

enterfile = raw_input("Enter file name: ")
handle = open(enterfile)

numlist = list()
runtotal = 0

for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    for val in stuff:
        numlist.append(int(val))

for val in numlist:
    runtotal = runtotal + val

print runtotal






