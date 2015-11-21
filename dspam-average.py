# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

# Preset counters
count = 0
runtotal = 0

# Start loop to go through the file
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue

    # Find and extract confidence number
    startpos = line.find(':')
    dataextract = line[startpos+1:]
    datatrimmed = dataextract.lstrip()

    # Calculate sum of all values plus the count of numbers/lines
    runtotal = runtotal + float(datatrimmed)
    count = count + 1

# Compute average
average = runtotal / count

# Print average
print "Average spam confidence:",average





