
import time

for o in range(3,0,-1):
    for i in range(1,o+1):
        time.sleep(.2)
        print("*",end=' ')
    print(" ")
