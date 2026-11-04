class Roman:
    def __init__(self, num):
        self.num = num

    def convert(self):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        for i in range(len(values)):
            while self.num >= values[i]:
                roman += symbols[i]
                self.num -= values[i]

        return roman


# Take input from the user
number = int(input("Enter an integer: "))

# Create an object
obj = Roman(number)

# Display the Roman numeral
print("Roman equivalent:", obj.convert())