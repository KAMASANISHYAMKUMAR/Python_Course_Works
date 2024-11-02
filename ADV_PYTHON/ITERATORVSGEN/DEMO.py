import time

#Internally list is nothing but an object class list
lst=[10,20,30,40]
print("List : ",lst)
for i in lst:
    time.sleep(1)
    print(i)
print("======================")

class Shashi:
    def __init__(self):   #0             1           2
        self.courses=["Java","Python","Android"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index=self.index+1
        if self.index<len(self.courses):
            return self.courses[self.index]
        else:
            raise StopIteration()
        

s=Shashi()
for i in s:
    time.sleep(1)
    print(i)

''' If u want define any class as an iterable class then
that class must be overridden with __iter__(self)
and __next__(self) from object class

__iter__(self) should return current class object

Note: Whenever we use any iterable class object
in the for loop then PVM internally calls __next__(self)

'''












        
