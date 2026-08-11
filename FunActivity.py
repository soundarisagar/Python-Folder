import random

secret_number = random.randint(1, 10)

guess = int(input("Guess the number between 1 and 10: "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the number between 1 and 10: "))

print("Congratulations! You guessed the correct number:", secret_number)