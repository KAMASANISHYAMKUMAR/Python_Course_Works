'''
Syn:
for variable in iterable:
    stmt(s)   '''

import time

stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("dict : ",stu)

for i in stu:
    time.sleep(.2)
    print(i)
    
