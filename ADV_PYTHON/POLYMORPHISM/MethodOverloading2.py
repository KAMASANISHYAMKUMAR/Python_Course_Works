import time

class Test:
    def method1(self,x=None,y=None,z=None):
        time.sleep(1)
        if x!=None and y!=None and z!=None:
            s=x+y+z
            print("Sum of 3 is : ",s)
            
        elif  x!=None and y!=None:
            s=x+y
            print("Sum of 2 is : ",s)

        elif x!=None:
            print("Sum is : ",x)

        else:
            print("Sum is : 0")

#calling
t=Test()
t.method1(10,20,30)
t.method1(10,20)
t.method1(10)
t.method1()


