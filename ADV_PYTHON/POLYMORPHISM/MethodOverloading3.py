
import time

class Test:
    def method1(self,*x):
        time.sleep(1)
        print("Elements : ",x)
        s=0
        for i in x:
            s=s+i

        print("Sum is : ",s)
        print("=========")

#calling
t=Test()
t.method1(10,20,30,40,50)
t.method1(10,20,30)
t.method1(10,20)
t.method1(10)
t.method1()






