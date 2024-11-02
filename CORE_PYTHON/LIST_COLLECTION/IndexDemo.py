
#L.append(item)
#L.insert(pos,item)
#L.copy( ) -> shallow copy of list

#L.pop(index=-1) -> int
#L.remove(item)   ValueError
#L.clear( )

#L.index(item[,start,end] ) -> int | ValueError

#        0   1    2   3   4    5
lst=[10,20,30,40,50,10]
print("List : ",lst)

pos=lst.index(10)
print("Found @ : ",pos)

pos=lst.index(100,2,6)
print("Found @ : ",pos)










