
#range(stop) -> range object | iterable
r=range(10)  #range(0,10)
print("Type is : ",type(r))
print("Range object : ",r)

import time

for i in r:
    time.sleep(.2)
    print(i)

