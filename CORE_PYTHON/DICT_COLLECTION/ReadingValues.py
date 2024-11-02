
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
#D.values() -> dict_values | iterable
#D.items() -> dict_items | iterable

stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("stu : ",stu)

items=stu.items()
print("type is : ",type(items))

import time
for t in items:
    time.sleep(.5)
    print(t)
print("==============")

for t in items:
    time.sleep(.5)
    k,d=t
    print(k,d,sep=' ---> ')
print("==============")

for k,d in items:  #item=[(sno,101),(sname,ramesh),(scity,hyd)]
    time.sleep(.5)    
    print(k,d,sep=' ---> ')















