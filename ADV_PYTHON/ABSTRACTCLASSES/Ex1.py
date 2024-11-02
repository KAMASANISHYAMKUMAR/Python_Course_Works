from abc import abstractmethod,ABC

class Test(ABC):
    def method1(self):
        print("Ins mtd-1 of Test")

    @abstractmethod
    def method2(self):
        pass

#calling
t=Test()
''' TypeError: Can't instantiate abstract class
Test with abstract method method2 '''

