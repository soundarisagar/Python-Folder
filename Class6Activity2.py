is_raining = False
print(not is_raining)

is_sunny = True
print(not is_sunny)

has_homework = False

if not has_homework:
    print("You can play!")

number = int(input("Enter a number: "))

if not (number % 2 == 0):
    print("The number is odd.")
else:
    print("The number is even.")