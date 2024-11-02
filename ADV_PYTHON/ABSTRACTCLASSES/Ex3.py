
from abc import ABC,abstractmethod

class Test(ABC):
    def method1(self):
        print("mtd-1 of Test")

    @abstractmethod
    def method2(self):
        pass

class Testing(Test):
    pass

t=Testing()
