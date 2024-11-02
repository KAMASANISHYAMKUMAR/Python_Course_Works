




#[<exp> for var in iterable for var in iterable if test ]
l1= ["A","B","C"]
l2=[1,2,3]

l3=[i*j for i in l1 for j in l2 if i in ['A','C'] ]

import time
for i in l3:
    time.sleep(.5)
    print(i)






