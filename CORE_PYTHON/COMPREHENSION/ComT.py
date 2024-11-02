




#[<exp> for var in iterable for var in iterable if test ]
l1=["sai","raj"]
l2=["pens","books","box"]

l3=[(i,j) for i in l1 for j in l2 ]

import time
for t in l3:
    time.sleep(.2)
    print(t)
