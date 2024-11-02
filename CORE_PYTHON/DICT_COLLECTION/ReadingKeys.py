
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("stu : ",stu)

keys=stu.keys()
print("keys : ",keys)

import time
for k in keys:
    time.sleep(.2)
    print(k)
