#copy.py

from copy import *

a = [1,2,3]
b = a
c = a.copy()

a.append(4)

print(a)
print(b)
print(c)

