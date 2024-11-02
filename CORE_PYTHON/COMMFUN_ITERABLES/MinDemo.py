import time

#len(iterable) -> value
#sum(iterable) -> value
#min(iterable) -> value

lst=[10,2,30,40,50,60,1,70]

small=lst[0] #2

for i in lst[1: ]:
    if i<small:
        small=i

print("Smallest : ",small)
print("===================")

s=min(lst)
print("Smallest : ",s)







