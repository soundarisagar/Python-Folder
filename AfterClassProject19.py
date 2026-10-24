class Dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def display(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)


# Create two objects
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Brown")

# Display details
print("Details of the first dog:")
dog1.display()

print("\nDetails of the second dog:")
dog2.display()