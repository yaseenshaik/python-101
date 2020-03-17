# comprehension is easier way to understand list processing.

# easy to write and read

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# "n-for-n"

my_list = []

for n in nums:
    my_list.append(n)
print(my_list)


# comprehension way:

my_c_list = [n for n in nums]

print(my_c_list)

# Ex: 2
# squaring:

squares = [n * n for n in nums]
print(squares)

# squaring with lambdas

sq_lambda = map(lambda n: n * n, nums)

print(sq_lambda)

# 99% of lambda cam be replaced by comprehensions

# even numbers

even_nums = [n for n in nums if n % 2 == 0]
print(even_nums)

# n * m tuple list

tuple_list = [(letter, num) for letter in 'abcd' for num in range(3)]
print(tuple_list)

# creating dictionaries with comprehensions:

names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']

# Using for loop and zip

heros_1 = {}
for name, hero in zip(names, heros):
    heros_1[name] = hero

print(heros_1)

# Using comprehensions:
heros_2 = {name: hero for name, hero in zip(names, heros)}

print(heros_2)

# adding a conditional

heros_3 = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}

print(heros_3)

# set comprehension:

nums_2 = [1, 1, 2, 3, 4, 2, 2, 4, 5, 6, 8, 5]

# using for loop:
set_1 = set()
for n in nums_2:
    set_1.add(n)
print(set_1)

# using comprehension
# use braces but no colon
set_2 = {n for n in nums_2}
print(set_2)

# Generators Expressions


def gen_fun(nums):
    for n in nums:
        yield n * n


my_gen = gen_fun(nums)

for i in my_gen:
    print(i)

# using comprehension use ()

gen_2 = (n * n for n in nums)

for i in gen_2:
    print(i)
