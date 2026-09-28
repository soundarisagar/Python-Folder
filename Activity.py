names = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]
students = dict(zip(names, marks))
print(students)
marks = list(map(lambda x: x + 5, marks))
print(marks)
passed = [x for x in marks if x > 75]
print(passed)
scores = {names[i]: marks[i] for i in range(3)}
print(scores)