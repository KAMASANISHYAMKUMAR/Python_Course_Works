



#map(func,*iterables) -> map object | iterable
#filter(function or None, iterable) -> filter object | iterable

lst=["anu","aishu","srija","Ramesh","Suresh","Babu"]
print("List : ",lst)

f=filter( lambda x: len(x)==5 , lst)
print("type is : ",type(f))
print("Filter Object : ",f)
t=tuple(f)
print("Result is : ",t)
