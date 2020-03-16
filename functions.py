# empty function


def pass_func():
    pass


pass_func  # just function, can use for assignment
print(pass_func)
print(id(pass_func))

pass_func()  # call function
print(id(pass_func()))


def hello_func():
    print('Hello World!')


hello_func()

# Funcs help Keep DRY


def return_anything(thing):
    return thing


another_thing = return_anything(25)

print(another_thing)


# args are nameless and tuples inside fun
# kwargs are named and a part of dict
def another_fun(*args, **kwargs):
    print(args)
    print(kwargs)


another_fun('anohter', 'one', another=1)

# unpacking is destructuring stuff
# unpack list with *
# unpack dicts with **


def is_leap(year):
    """ Return True for leap years, False otherwise"""
    return year % 400 and (year % 100 != 0 or year % 400 == 0)
