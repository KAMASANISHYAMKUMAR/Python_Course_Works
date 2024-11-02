




#sorted(iterable,key=None,reverse=False) -> list
lst=[(101,"ramesh",23),
        (103,"nani",22),
        (102,"anu",18),
        (104,"srija",27) ]

print(lst)
print("-------------------------------------------")
lst2=sorted(lst, key=lambda x: x[0]) 
print(lst2)
print("-------------------------------------------")
lst3=sorted(lst, key=lambda x:x[1])
print(lst3)
print("-------------------------------------------")
lst4=sorted(lst,key=lambda x:x[2])
print(lst4)
print("============================")

lst=sorted(lst,key=lambda x:x[2],reverse=True)
print(lst[1])









