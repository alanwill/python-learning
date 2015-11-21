# Seed variables
largest = None
smallest = None

# Start loop
while True:
    try:
        # Prompt for input
        num = raw_input("Enter a number: ")

        # When input is 'done' quit the program
        if num == "done" : break

        # Set variables to integers
        if smallest is None:
            smallest = int(num)
            largest = int(num)

        # Evaluate smallest
        elif int(num) < smallest:
            smallest = int(num)

        # Evaluate largest
        elif int(num) > largest:
            largest = int(num)

    # If bad added inputed, print exception and restart loop
    except:
        print "Invalid input"
        continue

print "Maximum is ", largest
print "Minimum is ", smallest