


lst=[10,20,10,30,40,50,10,30,30,]
print("List : ",lst)
lst2=[]

item=int(input("Enter an item : ")) #10

if item in lst:
    for i in lst:
        if i!=item:
            lst2.append(i)

    print("After Deleting the Item ")
    lst=lst2
    print("List : ",lst)
            
else:
    print("Sorry Specified item is not existed ")

