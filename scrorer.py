score = raw_input("Enter a score between 0.0 and 1.0: ")
enteredscore = float(score)
try:
    if enteredscore >1:
        print "I'm sorry but that's not a valid number"
    elif enteredscore >= 0.9:
        print "A"
    elif enteredscore >= 0.8:
        print "B"
    elif enteredscore >= 0.7:
        print "C"
    elif enteredscore >= 0.6:
        print "D"
    elif enteredscore < 0.6:
        print "F"

except:
    print "I'm sorry but that's not a valid number"
    quit()
