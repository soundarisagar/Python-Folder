import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple':'red',

'orange':'orange',

'watermelon':'green',

'banana':'yellow'}
    def quiz(self):
        while True:
            fruit = random.choice(list(self.fruits.keys()))
            answer = input(f"What is the color of {fruit}? (or type 'exit' to quit): ")
            if answer.lower() == 'exit':
                break
            elif answer.lower() == self.fruits[fruit]:
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is {self.fruits[fruit]}.")

print("Welcome to the Fruit Color Quiz!")
fq = FruitQuiz()
fq.quiz()