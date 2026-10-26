class myClass:
    __privateVar = 27;
    def privMeth(self):
        print("I'm inside class Myclass.")
    def hello(self):
        print("Private Variable:", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.privMeth()