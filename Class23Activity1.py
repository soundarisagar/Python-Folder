numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

nums = [1, 2, 3, 4, 5]
def square(n):
    return n * n
square = list(map(square, nums))
print("Squared numbers in list")
print(square)