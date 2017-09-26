class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def printArg(self, x):
        print x

    def printArg2(x):
        print x


x = MyClass()
print x.f()
#x = MyClass()
xp = x.printArg
xp('d')
x.printArg2('s')