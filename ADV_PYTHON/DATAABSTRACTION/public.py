
class Test:
    def __init__(self):
        self.x=10

    def method1(self):
        print("from test ")
        print("x val is : ",self.x)

class Testing(Test):
    def method2(self):
        print("frm Testing ")
        print("x val is : ",self.x)

#calling
t=Testing()
t.method1()
t.method2()
print("From outside of the class")
print("public member x : ",t.x)



