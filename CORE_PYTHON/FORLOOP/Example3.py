'''
Syn:
for variable in iterable:
    stmt(s)   '''

import time

s={10,12.12,"Ramesh",None,"Python"}
print("set collection",s)

for i in s:
    time.sleep(.2)
    print(i)
