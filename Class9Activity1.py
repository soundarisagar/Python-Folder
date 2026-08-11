# 1) Ask the user to enter the number of terms and store it in `n`.
n = int(input("Enter a number: "))
# 2) Initialize `sum` to 0.
sum = 0
# (This will store the running total.)

# 3) Initialize `i` to 1.
i = 1
# (This is the first number we will add.)

# 4) Repeat while `i` is less than or equal to `n`:
while i <= n:
    sum += i
    i += 1

# 5) After the loop ends, print the final value of `sum`.
print(sum)