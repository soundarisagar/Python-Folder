num = int(input("Enter a number: "))
digits = str(num)

if len(digits) >= 4:
    middle1 = digits[(len(digits) // 2) - 1]
    middle2 = digits[len(digits) // 2]

    middle1 = int(middle1)
    middle2 = int(middle2)

    product = middle1 * middle2
    print("Middle digits are:", middle1, "and", middle2)
    print("Product of middle digits is:", product)

else:
    print("It's not a 4 or more digit number.")