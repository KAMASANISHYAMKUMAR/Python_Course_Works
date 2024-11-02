
import time

n=int(input("Enter a number "))
i=1
s=0

while i<=n:
    time.sleep(.2)
    s=s+i
    i=i+1

print("Sum is : ",s)
