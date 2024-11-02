
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

#s.issuperset(iterable) -> bool

s1={1,2,7}
s2={1,2,3,4,5,6}
print("s1 : ",s1)
print("s2 : ",s2)

print("s1 issuperset s2 ? : ",s2.issuperset(s1) )


