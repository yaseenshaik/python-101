language = 'Java'

if language == 'Python':
    print('Python')
elif language == 'Java':
    print('Ayy')
else:
    print('Not Python')

# Multiple conditions

user = 'sucker'

if language == 'Java' and user == 'sucker':
    print('Ayy lmao')

# or key
if language == 'Python' or user == 'sucker':
    print('Haha')

# object comparison
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# == is reverse JS :D

print(a == b)  # true
print(a is b)  # false
print(c is a and c == a)  # true

# Falsy values include:

# False, None, Zero of any type
# empty sequence Eg: '', (), []
# empty mapping e.g: {}


# double comparison
# if x < y < z
# if not x < y < z

def what_is_a(a):
    if 1 < a < 3:
        print('a lies between 1 and 3')
    else:
        print('We don\'t know about a')
    pass


print(what_is_a(2))
print(what_is_a(4))
