



#map(func,*iterables) -> map object | iterable
#filter(function or None, iterable) -> filter object | iterable

lst=["anu","aishu","srija","Ramesh","SuresH","Babu"]
print("List : ",lst)

print("Result is : ",set( filter( lambda x: len(x)==5 , lst)))
print("Result is : ",
      tuple(filter(lambda x: x[-1]=='h' or x[-1]=='H', lst)))

print("Result is : ",
      list( filter( lambda x : x[-1] in ['h','H'] ,lst) ))











