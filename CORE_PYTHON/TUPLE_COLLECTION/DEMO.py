
#In the tuple there no support For
#append( ) | insert( ) | copy( )
#pop( ) | remove( ) | clear( )
#reverse( ) | sort( )

#It will support index( ) and count( )

t1=()
print("Data is : ",t1)
print("===============")

t2=(10,12.12,"Shashi",10,None)
print("Data is : ",t2)
print("===============")

#tuple( ) -> tuple object
t3=tuple()
print("Data is : ",t3)
print("===============")

#tuple(iterable) -> tuple
lst=[10,20,30,40]
print("List : ",lst)
t=tuple(lst)
print("Data is : ",t)
print("===============")

s="welcome"
print("string : ",s)
t=tuple(s)
print("Data is :",t)
print("===============")

t=(12.12,)
print("Type is : ",type(t))
print("Data : ",t)
print("===============")

#packing | internally works as tuple
t=10,20,30,40,"shashi"
print("type is : ",type(t))
print("Data is : ",t)

















































