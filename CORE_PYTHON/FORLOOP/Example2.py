'''
Syn:
for variable in iterable:
    stmt(s)   '''

import time

t=(10,12.12,"Ramesh",None,"Python")
print("tuple : ",t)

for i in t:
    time.sleep(.2)
    print(i)
