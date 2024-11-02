
#S.add(item)
#S.copy() -> shallow copy

#S.remove(item) KeyError
#S.discard(item)
#S.clear( )

#s.union(iterable) -> set  vs
#s.update(iterable)

#s.intersection(iterable) -> set vs
#s.intersection_update(iterable)

#s.difference(iterable) -> set
#s.difference_update(iterable) 

#s.symmetric_difference(iterable) -> set vs
#s.symmetric_difference_update(iterable) 

s1={1,2,3,4}
s2={3,4,5,6}
print("s1 : ",s1)
print("s2 : ",s2)

s3=s1^s2
print("s1^s2 : ")
print("s3 : ",s3)
print("==================")

s4=s1.symmetric_difference(s2)
print("s1 difference s2 ")
print("s4 : ",s4)
print("==================")

s1.symmetric_difference_update(s2) # s1=s1^s2
print("s1 sym_difference_update s2 : ")
print("s1 : ",s1)
















