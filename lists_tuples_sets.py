# lists are arrays

courses = ['History', 'Physics', 'Chemistry']

print(courses[0])  # start from first

print(courses[-1])  # start from last

print(courses[0:2])  # same as strings

print(courses[:2])

print(courses[2:])

# push an item with location

courses.insert(0, 'Art')

print(courses)


# concat is extend (mutate)

courses.extend(['Tamil', 'Mathematics'])

print(courses)

# pop to pop (Mutation)

last_subject = courses.pop()

print(last_subject)
print(courses)

# reverse

courses.reverse()

print(courses)

# sort

courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

# without mutation

print(sorted(courses))
print(courses)


# min, max

nums = [1, 6, 2, 65, 8]

print(min(nums))
print(max(nums))
print(sum(nums))

# index (will throw errow when not fund)

print(nums.index(65))

# check if it is present

print(25 in nums)

# for loop

for subject in courses:
    print(subject)

# to get index

for index, subject in enumerate(courses):
    print(index, subject)

# enumerate takes a second arg for stating number
# e.g. to start form 1
for index, subject in enumerate(courses, 1):
    print(index, subject)

# joining lists

courses_str = ' "" '.join(courses)
print(courses_str)

# splitting (undo join)

new_courses = courses_str.split(' "" ')
print(new_courses)

# Tuples are similar to lists but immatable
# Use () to create tuples

nums_tuple = (2, 3, 4, 5)

print(nums_tuple)

# Sets are unordered and don't have duplicates
# Use {} to create non-empty Sets.
# Use set() to create empty sets
# Note: order is not guaranteed but you can be sure
# that no item is duplicated

nums_set = {2, 3, 4, 5}

# use to find common items

another_nums_set = {2, 1, 5, 8}

print(nums_set.intersection(another_nums_set))  # {2, 5}

# or different items

print(nums_set.difference(another_nums_set))  # {3, 4}

# to combine, use union

print(nums_set.union(another_nums_set)) # {1, 2, 3, 4, 5, 8}

