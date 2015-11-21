fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

# Loop through the file and ignore any line that does NOT start with 'From '
for line in fh:
    if not line.startswith('From ') : continue
    parsed = line.split()
    print parsed[1]
    count = count + 1

print "There were", count, "lines in the file with From as the first word"





