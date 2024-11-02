from abc import abstractmethod,ABC

class Test(ABC):
    def method1(self):
        print("Ins mtd-1 of Test")    

#calling
t=Test()
''' TypeError: Can't instantiate abstract class
Test with abstract method method2 '''

