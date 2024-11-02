
class Sample:
    def __init__(self):
        self.x=10
        self.y=20

    def __del__(self):
        print("Dest is invoked ")
        print("R.D.A.Logic")
        print("Object  is deleted ....")

    def getData(self):
        print("x val is : ",self.x)
        print("y val is : ",self.y)

#calling
s1=Sample()
s1.getData( )
print("==================")
s1=None
#s1.getData( ) AttributeError
print("==================")
s2=Sample()
s2.getData( )
