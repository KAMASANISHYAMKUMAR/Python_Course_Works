
t=(  [10,20,30,40],
        (1.1,2.2,3.3,4.4),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"raj","scity":"hyd"}
     )

import time

for i in t:
    time.sleep(.2)    
    if isinstance(i,tuple):
        s=0
        for j in i:
            print(j)
            time.sleep(.2)
            s=s+j
        print("============")
        print("Sum is : ",s)
        
    elif isinstance(i,list):
        print("List : ",i)
        m=max(i)
        print("Max is : ",m)
        print("============")








    
    

