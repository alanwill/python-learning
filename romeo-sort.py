fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

# look through file and split each line up into a list
for line in fh:
    words = line.split()
    count = 0
    # loop through each word to ensure it's not already in the list
    for uniqueword in words:
        if uniqueword not in lst:
            lst.append(uniqueword)
        continue

# sort the list
lst.sort()

# print the list
print lst
