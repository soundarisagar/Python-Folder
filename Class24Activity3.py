class Parrot:
    species = "Bird"
    def __init__(self,name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
foo = Parrot("Foo", 15)

print("The name of the first parrot is", blu.name)
print("The age of the first parrot is", blu.age)
print("Blu is also a", blu.species)

print("The name of the second parrot is", foo.name)
print("The age of the second parrot is", foo.age)
print("Foo is also a", foo.species)