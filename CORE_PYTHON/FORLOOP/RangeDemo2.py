




#range(stop) -> range object | iterable
#range(start,stop[,step]) -> range object | iterable
#default step value is +1

r=range(1,6)
print("type is : ",type(r))
print("range object : ",r)

import time
for i in r:
    time.sleep(.2)
    print(i)








