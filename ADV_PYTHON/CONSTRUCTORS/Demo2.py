
''' Can i create an object for the class
without constructor
Ans: NO

Can i create an object For an empty class ?
Ans: Yes
'''

class A:
    pass

a=A( )
print("Members of A class ")
print(dir(A))
print("=====================")

class B:
    pass

print(dir(B))

''' Rules For Constructors
       - it should be defined by using __init__(self)
       - it can be parameterized
       - constrcutor never return any values except
         None

























