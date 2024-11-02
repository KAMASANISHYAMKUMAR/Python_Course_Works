
#L.append(item)
#L.insert(pos,item)
#L.copy( ) -> shallow copy of list

#L.pop(index=-1) -> int

lst=[10,20,30,40,50,10]
print("List : ",lst)
item=lst.pop()
print("Deleted item is : ",item)
print("After pop : ",lst)

item=lst.pop(2)
print("Deleted item is : ",item)
print("List : ",lst)



