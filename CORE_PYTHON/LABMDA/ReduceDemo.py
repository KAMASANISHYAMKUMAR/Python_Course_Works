



#map(func,*iterables) -> map object | iterable
#filter(function or None, iterable) -> filter object | iterable
#reduce(function,seq) -> value from functools

import functools

v=functools.reduce(lambda x,y: x+y , [1,2,3,4,5] )
print("Result is : ",v)

f=functools.reduce( lambda x,y : x*y , (1,2,3,4) )
print("Fact is : ",f)











