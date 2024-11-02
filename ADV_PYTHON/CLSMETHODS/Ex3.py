class Test:
    x=10 #static variable
    def method1(self):
        self.y=20 #instance
        print("Ins mtd-1 of Test")
        print("instance y val is : ",self.y)
        print("static x val is : ",Test.x)
        print("=========================")

    @classmethod
    def method2(cls):
        print("cls mtd-2 of Test")
        #print("instance y val is : ",self.y)
        print("static x val is : ",Test.x)
        print("==========================")
        
#calling
Test.method2()
t=Test()
t.method1()

        
        

    
