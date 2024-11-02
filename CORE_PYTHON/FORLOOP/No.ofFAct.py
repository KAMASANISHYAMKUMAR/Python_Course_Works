
import time

n=int(input("Enter a number : "))
nf=0

for i in range(1,n+1):    
    if n%i==0:
        print(i)
        nf+=1

print("No. of Fact : ",nf)

