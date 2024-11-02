
#S.add(item)
#S.copy() -> shallow copy

#S.remove(item) KeyError
#S.discard(item)

s1={101,"ramesh","roja"}
print("set s1 : ",s1)

s1.discard("roja")
print("After remove : ",s1)

s1.discard("khanna")

