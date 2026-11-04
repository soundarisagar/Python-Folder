try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age! Please enter a valid age.")
    else:
        print("Your age is correct.")

        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

except ValueError:
    print("Error! Please enter your age in numbers only.")