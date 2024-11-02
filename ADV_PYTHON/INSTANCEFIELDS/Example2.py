
class Test:
    def method1(self):
        x=10 #local variable
        self.y=20 #instance field
        print("x val is : ",x) #10
        #print("y val is : ",y) NE
        print("y val is : ",self.y)

#calling
t=Test()
t.method1()
print("From outside of the class \n y val is ",t.y)
