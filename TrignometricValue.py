import math

# Take input from the user
angle = float(input("Enter the angle in degrees: "))

# Convert degrees into radians
radian = math.radians(angle)

# Calculate sin, cos and tan
print("Sin value:", math.sin(radian))
print("Cos value:", math.cos(radian))
print("Tan value:", math.tan(radian))