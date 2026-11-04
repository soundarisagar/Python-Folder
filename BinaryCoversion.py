# Take input from the user
num = int(input("Enter a decimal number: "))

# Convert decimal to binary
binary = bin(num)

# Display the result
print("Binary number:", binary[2:])