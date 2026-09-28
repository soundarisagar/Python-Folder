test_dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'Coding': 1}

print("Test Dictionary:", test_dictionary)

value = int(input("Enter the value whose frequency you want to check: "))

frequency = list(test_dictionary.values()).count(value)

print("Frequency of", value, "is:", frequency)