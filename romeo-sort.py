fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
print line.rstrip()