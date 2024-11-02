'''
Syn:
for variable in iterable:
    stmt(s)   '''

import time

lst=[10,12.12,"Ramesh",None,"Python"]
print("List : ",lst)

for i in lst:
    time.sleep(.2)
    print(i)


