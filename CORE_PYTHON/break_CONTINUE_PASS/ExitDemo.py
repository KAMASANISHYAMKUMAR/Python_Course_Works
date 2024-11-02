
import time
import sys

lst=[10,20,30,40,50,70,80,90,100]

for i in lst:
    time.sleep(.1)
    if i==70:
        sys.exit()
    print(i)

print("Outside of the loop")
print("Have a nice day ")

