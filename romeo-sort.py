fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   # print line.rstrip()
    words = line.split()
    count = 0
    for uniqueword in words:
        if uniqueword not in lst:
            lst.append(uniqueword)
        continue
lst.sort()
print lst
