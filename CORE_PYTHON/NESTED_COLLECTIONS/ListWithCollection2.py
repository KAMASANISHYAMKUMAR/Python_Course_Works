lst=[[10,20,30,40],
        (1.1,2.2,3.3,4.4),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"raj","scity":"hyd"} ]

import time

for i in lst:
    time.sleep(1)
    print("type is : ",type(i))
    print("Data is : ",i)

    if isinstance(i,dict):
        for k,d in i.items():
            time.sleep(.2)
            print(k,d,sep=' <<< >>> ')
    else:    
        for j in i:
            time.sleep(.2)
            print(j)
        print("==================")







