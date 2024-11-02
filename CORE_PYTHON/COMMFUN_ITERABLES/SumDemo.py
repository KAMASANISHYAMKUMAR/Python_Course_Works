import time

#sum(iterable) -> value
lst=[10,20,30,12.12,(10+20j)]

s=0
for i in lst:
    time.sleep(.2)
    print(i)
    s=s+i
    
print("===========")
print("Sum is : ",s)

s2=sum(lst)
print("Sum is : ",s2)







