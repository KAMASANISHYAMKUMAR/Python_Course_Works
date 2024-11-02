
class Sample:
    x=10  #static variable
    def method1(self):
        #print("x val is : ",x)
        print("static x : ",self.x)
        print("static x : ",Sample.x)

#calling
s=Sample()
s.method1( )


