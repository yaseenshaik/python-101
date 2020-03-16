int_ex = 2
float_ex = 3.14

print(type(float_ex))

# Float/normal division

print(3 / 2)  # 1.5

# Floor division

print(3 // 2)  # gives 1

# Exponent

print(3 ** 2)  # 9

# Modulus

print(3 % 2)  # 1

# priorities - order of operations

print(3 + 2 * 4)  # 11

# increment

int_ex += 1

print(int_ex)

# round (takes a integer for decimal)

print(round(3.75, 1))  # 3.8

# comparison

print(int_ex == float_ex)

# same for !=, >, <, >=, <=

# typecasting

hund = '100'
# print(hund + int_ex) # Will throw error
print(int(hund) + int_ex)
