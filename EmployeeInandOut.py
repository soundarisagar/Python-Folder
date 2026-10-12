class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called, Employee deleted.")
def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end, now deleting obj")
    return obj

print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End, now deleting obj")