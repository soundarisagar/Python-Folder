num = int(input("Enter a number: "))

odd_numbers = []

for i in range(1, num):
    if i % 2 != 0:
        odd_numbers.append(i)

print("List of odd numbers:", odd_numbers)

fruits = ["apple", "banana", "mango", "orange", "grapes"]

new_fruits = []

for fruit in fruits:
    new_fruits.append(fruit.capitalize())

print("Original list:", fruits)
print("Updated list:", new_fruits)