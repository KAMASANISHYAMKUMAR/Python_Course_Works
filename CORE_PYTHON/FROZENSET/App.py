'''
set( ) 
set(iterable)

frozenset() -> empty frozenset
frozenset(iterable) -> frozenset   '''

l1=[1,2,3,4]
l2=[3,4,5,6]

print("l1 : ",l1)
print("l2 : ",l2)

'''
fs1=frozenset(l1)
fs2=frozenset(l2)
fs3=fs1.intersection(fs2)
l3=list(fs3)
print("Result is : ",l3)
'''

print("Result is : ",
      list(frozenset(l1).intersection(frozenset(l2))))






















