
import time
import random


for i in range(1,11):
    time.sleep(.5)
    s=""
    f=str(random.randint(6,9))
    for i in range(1,10):
        s=s+str( random.randint(0,9) )
    m=f+s
    print(m)
    
