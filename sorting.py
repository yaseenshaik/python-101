# sorting ccan be run on lists, dictionaries, tuples

li = [9, 2, 4, 5, 1, 3, 8, 9]

s_li = sorted(li)

print(s_li)

# to sort in place use
# li.sort()

# reverse

print(sorted(li, reverse=True))

# the sort method also takes this variable

tup = (9, 2, 4, 5, 1, 3, 8, 9)

print(sorted(tup))  # return sorted list

di = {'name': 'Yaseen', 'job': 'Developer', 'age': 29}

print(sorted(di))  # return list of sorted keys

li_2 = [1, 2, -4, 4, -5, 3]

# sorted takes a key function
# can use builtins like abs
# or write your own for your classes

print(sorted(li_2, key=abs))

# You can also use lambdas
# you can also use attrgetter to get the key too
# from operator import attrgetter
