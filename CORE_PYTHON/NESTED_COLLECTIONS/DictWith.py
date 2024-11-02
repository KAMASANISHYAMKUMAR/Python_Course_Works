
stu={
    "no":101,
    "name":"Ramesh",
    "address":{"hno":"1-2-3",
                          "city":"hyd",
                          "pin":500090
                         },
     "qualifications":("Msc","BEd","LLB"),
     "properties ":["House","Car","Bike"],
     "values":[5000000,800000,200000]
    }

import time
for k,d in stu.items():
    if isinstance(d,dict):
        print(k)
        for k1,d1 in d.items():
            time.sleep(.2)
            print("    ",k1,"->",d1)
            
    elif isinstance(d,tuple):
        print(k)
        for i in d:
            time.sleep(.2)
            print("    ",i)

    elif isinstance(d,list):
        print(k)
        for i in d:
            time.sleep(.2)
            print("    ",i)

    else:
        time.sleep(.2)
        print(k,"--->",d)
            
    

'''Output :
no -> 101
name -> Ramesh
address
    hno -> 1-2-3
    city -> hyd
    pin  -> 500090
qualifications:
   Msc
   BEd
   LLB
Properties:
   House
   Car
   Bike
Values:
   50L
   8L
   2L
======
 xxxxx
=======
'''
