
class Sample:
    x=30  #static variable
    def method1(self):
        x=10 #local
        self.x=20  #instance
        print("x val is : ",x)
        print("static x : ",self.x)
        print("static x : ",Sample.x)

#calling
s=Sample()
s.method1( )


