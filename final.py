def returning():
    if entry == 1:
        print ("Returning Customer.")

def guest():
    if entry == 3:
        print ("Welcome! We hope to see you often!")

def new():
    if entry == 2:
        print ("New Customer")

entry = 0
while entry >=0:
    print (">*< >*< >*< >*< >*< >*< >*<")
    print (" Please choose an option:\n")
    print ("1. Returning Customer")
    print ("2. New Customer")
    print ("3. Guest")
    print (">*< >*< >*< >*< >*< >*< >*<")
    entry = int(raw_input("Enter option:     "))
    if entry < 1 or entry > 3:
        entry = int(raw_input("Please enter Customer option 1, 2 or 3:     "))
    elif entry == 1:
        returning()
        entry = -1
    elif entry == 2:
        new()
        entry = -1
    elif entry == 3:
        guest()
        entry = -1

