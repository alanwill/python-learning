hours = raw_input('How many hours did you work? ')
rate = raw_input('What is your rate? ')

def computepay(hours, rate):
    if hours <= 40:
        pay = float(hours) * float(rate)
    elif hours > 40:
        overtime = float(hours) - 40
        pay = (40 * float(rate)) + (overtime * (float(rate) * 1.5))
    return pay

print "You'll be paid $",computepay(hours, rate)