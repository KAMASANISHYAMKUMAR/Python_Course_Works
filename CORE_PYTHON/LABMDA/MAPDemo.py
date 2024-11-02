



#map(func,*iterables) -> map object | iterable

#lst=[1,2,3]

'''
def sq(x):
    s=x*x
    return s '''

''' app-1
lst2=[]
for i in lst:
    a=sq(i)
    lst2.append(a)
print("Result is : ",lst2)   '''

''' App-2
m=map(sq ,lst)
lst2=list(m)
print("Map Object : ",lst2)   '''

'''
m=map(  lambda x: x*x  ,lst)
lst2=list(m)
print("Map object : ",lst2)
'''


print("Map object : ",list(map( lambda x: x*x , [1,2,3])))


















