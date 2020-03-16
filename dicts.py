# key value pairs, like JS objects
student = {'name': 'John', 'age': 24, 'courses': ['Maths', 'CompSci']}

print(student)

print(student['name'])
print(student['courses'])

# keys can be any immutable data types

# print(student['phone']) # will throw error if key doesn't exits

# check with get method

print(student.get('phone'))

# pass default value

print(student.get('phone', 123))

# assignment after creation

student['phone'] = 225365

print(student.get('phone'))

# can also overwrite any value

student['age'] = 25

print(student.get('age'))

# use update to mass update

student.update({'name': 'Jane', 'age': 22})

print(student)

# delete key

del student['age']

# pop to remove and return

phone = student.pop('phone')

print(phone)

# No of keys in dic
print(student)
print(len(student))

# list of keys
print(student.keys())

# list of values
print(student.values())

# list of key-value pairs
print(student.items())

# keys
for key in student:
    print(key)

# both key and value

for key, value in student.items():
    print(key, value)
