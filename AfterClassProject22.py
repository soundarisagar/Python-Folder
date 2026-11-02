import random
import string

# Create character groups
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits

# Generate a password
password = random.choice(lowercase)
password += random.choice(uppercase)
password += random.choice(numbers)

# Add more random characters
all_characters = lowercase + uppercase + numbers

for i in range(5):
    password += random.choice(all_characters)

# Shuffle the password
password = list(password)
random.shuffle(password)

# Display the password
password = ''.join(password)

print("Your random password is:", password)