import time

n=int( input("Enter a number ") )

i=f=1
while i<=n:
    time.sleep(.2)
    f=f*i
    i=i+1

print("Fact is : ",f)
