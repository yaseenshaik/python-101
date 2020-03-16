nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break and continue

for num in nums:
    if num < 3:
        continue
    elif num == 3:
        print('Ayy')
        break
    print(num)

# range from 0 to x use range(x+1)

for i in range(10):
    print(i)

# range from x to y use range x, y+1
for i in range(5, 11):
    print(i)

# while loop

x = 11

while x < 20:
    print(x)
    x += 1

# infinite looping with conditional exit

while True:
    if x == 30:
        break
    print(x)
    x += 1
