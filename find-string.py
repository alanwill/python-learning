text = "X-DSPAM-Confidence:    0.8475";

startpos = text.find(':')

dataextract = text[startpos+1:]
datatrimmed = dataextract.lstrip()

print "Data Extracted:",dataextract
print "Data trimmed:",datatrimmed
print "Number:", float(datatrimmed)
