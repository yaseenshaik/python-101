'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'Global X'

# x is global because it is in the main body of the file


def test():
    y = 'local y'
    print(y)  # local to test function
    print(x)  # global scope


def testLocal():
    y = 'local y'
    print(y)  # local to test function
    x = 'local X'
    print(x)  # local scoped


test()
testLocal()
print(x)  # global value is unchanged

# print(y) will throw an error

# It is also possible to define global variable
# inside a function using the keyword


def makeGlobal():
    global z
    z = 'global z'
    print(z)


makeGlobal()
print(z)  # calling makeGlobal is required before we can access z
# don't use this often. Will increase chances of
# bugs

# built-ins are accessible without importing

m = min([1, 2, 3, 4])

print(m)
# to get list of built-ins:
# import builtins
# print(dir(builtins))

# built-ins can be overridden without errors


def outer():  # enclosing function
    o = 'outer o'
    p = 'outer p'

    def inner():
        # commenting out next line will use the outer o
        o = 'inner o'
        print(o)
        nonlocal p  # changes enclosing function variable
        p = 'inner p'
        print(p)

    inner()
    print(o)
    print(p)


outer()
