
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
#D.values() -> dict_values | iterable
#D.items() -> dict_items | iterable

stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("stu : ",stu)

import time
for k,d in stu.items():
    time.sleep(.2)
    print(k,d,sep=' << >> ')













