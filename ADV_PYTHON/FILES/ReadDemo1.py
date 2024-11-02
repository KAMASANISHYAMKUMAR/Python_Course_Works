
f=open("data4.txt","r")
data=f.read()
print(data)
print("===================")

import time

for i in data:
    time.sleep(.1)
    print(i,end='')


f.close()


       
