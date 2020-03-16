# can just use `import find_index` where find_index is the .py
# then use find_index.greeting to access

# do `from find_index import *` to import everything
# and use just greeting. Not recommended since
# it can cause collision when importing a lot

# 3rd way:
from find_index import find_index as fi, greeting
import sys
import random
import math
import datetime
import calendar
import os

print(greeting)

courses = ['History', 'Physics', 'Chemistry', 'Maths']

index = fi(courses, 'Chemistry')

print(index)

print(sys.path)  # python path for imports

# sys.path is a list and can be appended

sys.path.append('H:\\Trading')

print(sys.path)
print(sys.executable)
print(sys.version)

# better way is to change the environment variable PYTHONPATH

# editors also have their own PYTHONPATH.

# random value from list
print(random.choice(courses))

# degree to radinaa
print(math.radians(90))
print(math.sin(90))

# datetime
print(datetime.date.today())

# calendar
print(calendar.isleap(2018))

# os
print(os.getcwd())

# other functions for scanning, creating and deleting files

# to get location

print(os.__file__)
