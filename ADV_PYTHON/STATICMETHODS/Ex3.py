
class Test:
    @staticmethod
    def method1(x,y):
        print("static method")
        s=x+y
        print("Sum is : ",s)
        print("====================")

#calling
Test.method1(10,20)
