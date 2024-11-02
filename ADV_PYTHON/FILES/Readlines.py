
f=open("data4.txt")
lst=f.readlines()

import time
for i in lst:
    time.sleep(1)
    print(i,end='')

