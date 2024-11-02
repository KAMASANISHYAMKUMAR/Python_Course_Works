import time

#len(iterable) -> int
lst=[10,20,30,40,50]
print("List : ",lst)

count=0
for i in lst:
    time.sleep(.2)
    print(i)
    count+=1
print("===========")
print("No.of.Objects are : ",count)

s="welcome"
print("String data : ",s)
count=0
for i in s:
    time.sleep(.2)
    print(i)
    count=count+1
print("=================")
print("No.of.char : ",count)


    

#sum(iterable) -> int
#min(iterable) -> int
#max(iterable) -> int
#all(iterable) -> int
#any(iterable) -> int


