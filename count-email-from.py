name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()
listemails = []

# Loop through the file and ignore any line that does NOT start with 'From '
for line in handle:
    if not line.startswith('From ') : continue
    line = line.rstrip()
    parsed = line.split()
    listemails.append(parsed[1])

for email in listemails:
    emails[email] = emails.get(email,0) + 1

topcount = None
topemail = None
for email,count in emails.items():
    if topcount is None or count > topcount:
        topemail = email
        topcount = count

print topemail, topcount




