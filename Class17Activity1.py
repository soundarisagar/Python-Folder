import random
playing = True

number = str(random.randint(1, 10))

print("I will generate a random number between 1 and 10. You have to guess the number one digit at a time.")
print("The game ends when ou get 1 hero!")
while playing:
    guess = input("Enter your guess: ")
    if guess == number:
        print("You guessed it right! The number was", number)
        break


    else:
        print("Wrong guess. Try again. \n")