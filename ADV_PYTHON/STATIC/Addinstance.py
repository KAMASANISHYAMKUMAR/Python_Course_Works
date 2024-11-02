
class Sample:
    pass

#calling
s=Sample( )
#Adding an instance field to the object from outside of class
s.x=10

print("x val is : ",s.x)
s.x=20
print("x val is : ",s.x)

#deleting an instance field
del s.x
print("x val is : ",s.x)
