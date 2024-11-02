
def myRange(start,end,step=1):
    while start<=end:
        yield start
        start=start+step

s=myRange(1,10)
print("type is : ",type(s))

import time
for i in s:
    time.sleep(.2)
    print(i)
