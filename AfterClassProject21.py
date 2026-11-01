class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# Take input from the user
word = input("Enter a word: ")

# Create an object
obj = Reverse(word)

# Display the reversed string
print("Reversed string:", obj.reverse_string())