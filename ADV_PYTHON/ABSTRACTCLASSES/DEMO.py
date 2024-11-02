Abstract class and Abstract methods :
=================================
- Non abstract method
     def method1(self):
         print("Mtd-1 ")

- Null body method
     def method1(self):
         pass

- abstract method
    @abstractmethod
     def method1(self):
         pass

- what is a class ?
     - it the collection of non abstract methods

     class Sample:
         def method1(self):
             print("mtd-1")

        def method2(self):
            pass
    
- what is the abstract class ?
       - Is the collection of both abstract or non abstract
       methods
       
      from abc import ABC,abstractmethod 
      class Sample(ABC):   ABstract Class 
          def method1(self):   null body | non abstract mtd
              pass

          @abstractmethod  
          def method2(self):
              pass

- Defining the abstract class is nothing but creating
the sub class class ABC 






