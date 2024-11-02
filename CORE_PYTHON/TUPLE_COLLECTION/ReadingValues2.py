#    0      1                  2    3   4
t=(101,"Ramesh",40,50,60)
print("Name is : ",t[1])

import time

index=0
while index<len(t):
    time.sleep(1)
    print(t[index])
    index+=1
print("====================")

for i in t:
    time.sleep(.2)
    print(i)


