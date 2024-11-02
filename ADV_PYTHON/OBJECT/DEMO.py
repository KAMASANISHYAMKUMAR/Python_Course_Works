


class A:
    pass

class B(A):
    pass

print("A is subclass of object ? : ",issubclass(A,object))
print("B is subclass of A ? : ",issubclass(B,A))
print("B is subclass of object ? : ",issubclass(B,object))

class C(object):
    pass

print("C is subclass of object ? : ",issubclass(C,object))

'''
1.How many methods are there in class A ?
Ans: All the methods of object class.

*** The Super class for every class in Python is object

2.Can i create a class without inheritance ?
Ans: No

Note: If any class is not inherited by other classe(s)
then that class is direct sub class of object.

If any class is inhertied by other classes then
that class is indirect sub class of object.
'''















