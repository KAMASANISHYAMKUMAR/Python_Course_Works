class Test:
    def m1(self):
        x=10
        self.y=20
        print("m1 x : ",x)
        print("m1 y : ",self.y)
        print("=============")

    def m2(self):
        #print("m2 x : ",x) NE
        print("m2 y : ",self.y)

#calling
t=Test( )
t.m1()
t.m2()
#print("x val is : ",x) NE   x is not defined 
#print("y val is : ",self.y) NE  self is not defined
print("y val is : ",t.y)








