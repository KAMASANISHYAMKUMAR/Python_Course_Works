
import time

lst=[10,20,30,40,50,70,80,90,100]

for i in lst:
    time.sleep(.1)
    if i==70:
        break
    print(i)
