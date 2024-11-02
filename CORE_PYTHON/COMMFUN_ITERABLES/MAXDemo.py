import time

#len(iterable) -> value
#sum(iterable) -> value
#min(iterable) -> value
#max(iterable) -> value

lst=[10,20,30,5,49,50,60,70,1]
big=lst[0] #30

for i in lst[1:]:
    if i>big:
        big=i

print("Biggest is : ",big)
print("===================")

b=max(lst)
print("Biggest is : ",b)










