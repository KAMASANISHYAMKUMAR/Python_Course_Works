#len(iterable)  -> int 

#       0    1                 2   3     4
lst=[10,"Ramesh",23,40,50]
print("List : ",lst)

import time

index=0
while index<len(lst):
    time.sleep(.2)
    print( lst[index] )
    index+=1
print("===================")

for i in lst:
    time.sleep(.2)
    print(i)
print("=======================")


for i in range(len(lst)-1,-1,-1):
    time.sleep(.2)
    print(lst[i])










    
    


