import array as arr
numbers = arr.array('i', [10, 20, 30, 40, 50])

print(numbers[2])
numbers.insert(1, 15)

numbers.append(50)

print(numbers)
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: ", array_num)

print("Number of occurencesof the number 3 in the said array: ", array_num.count(3))

array_num.reverse()
print("Array after reverse: ", array_num)
print(str(array_num))