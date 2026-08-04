a = True
b = True
c = False

if a and b and c:
    print("All the values are True.")
else:
    print("At least one value is False.")

a = True
b = False
c = False

if a or b:
    print("At least one value is True.")
else:
    print("Both values are False.")

if b or c:
    print("At least one value is True.")
else:
    print("Both values are False.")