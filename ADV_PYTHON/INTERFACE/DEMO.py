
What is the diff b|w class | abstract | interface

Class : is the collection of non abstract methods

class Sample:
    def method(self):
        pass

Abstract class : is the collection of both
           abstract or non abstract methods

from abc import ABC,abstractmethod 
class Sample(ABC):
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass
           
Interface : is the collection of abstract methods only

from abc import ABC,abstractmethod 
class Sample(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass





