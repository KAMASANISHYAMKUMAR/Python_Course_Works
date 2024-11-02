
class Test:
    def __init__(self):
        self.__x=10
        self._y=20
        self.z=30

    def method1(self):
        print("From mtd-1 of Test ")
        print("private x : ",self.__x)
        print("protected y : ",self._y)
        print("public z : ",self.z)
        print("====================")

class Testing(Test):
    def method2(self):
        print("From mtd-2 of Testing ")
        #print("private x : ",self.__x)
        print("protected y : ",self._y)
        print("public z : ",self.z)
        print("========================")

#calling
t=Testing()
t.method1()
t.method2()
        
print("From outside of the class")
print("private x : ",t._Test__x) #obj._Clsname__private
print("protected y : ",t._y)
print("public z : ",t.z)












        







        
