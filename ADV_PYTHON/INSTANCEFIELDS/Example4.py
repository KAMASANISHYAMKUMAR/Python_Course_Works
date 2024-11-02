class Test:
    def m1(self):
        self.x=10

#calling
t1=Test()
t1.m1( )
t2=Test()
t2.m1()
print("t1 x : ",t1.x) #10
print("t2 x : ",t2.x) #10
t1.x=99
print("After Modification ")
print("t1 x : ",t1.x)
print("t2 x : ",t2.x)
