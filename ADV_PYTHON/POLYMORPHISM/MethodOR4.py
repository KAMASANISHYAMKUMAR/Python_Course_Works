
class Test:
    def method1(self):
        print("Mtd-1 of Test")

class Testing(Test):
    def method1(self):        
        print("Mtd-1 of Testing")

#calling
t=Testing()
t.method1()
