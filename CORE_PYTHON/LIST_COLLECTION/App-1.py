
lst=[10,20,10,30,40,50,10,30,30,]
print("List : ",lst)

lst2=[] #10,20

for i in lst:
    if i not in lst2:
        lst2.append(i)

print("Result is : ",lst2)
