
#S.add(item)
#S.copy() -> shallow copy

#S.remove(item) KeyError
#S.discard(item)
#S.clear( )

#s.union(iterable) -> set  vs
#s.update(iterable)

s1={1,2,3,4}
s2={3,4,5,6}
print("s1 : ",s1)
print("s2 : ",s2)

s3=s1|s2
print("s1 | s2 : ",s3)
print("==================")

s4=s1.union(s2)
print("s1 union s2 : ",s4)
print("s1 : ",s1)
print("==================")

s1.update(s2) #s1=s1.union(s2) meaning s1=s1+s2
print("s1 update s2 : ")
print("s1 : ",s1)



















