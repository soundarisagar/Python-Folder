valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            print("Bye")
            valid= True
        else:
            print("Please enter an even number.")
    except ValueError:
        print("Invalid input.")