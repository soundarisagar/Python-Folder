from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I can walk and run")

class Snake(animal):
    def move(self):
        print("I can crawl")

R = Human()
R.move()

K = Snake()
K.move()