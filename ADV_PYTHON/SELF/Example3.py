
class Test:
    def method1(self):
        print("mtd-1 of Test")
        print("self : \n ",self)
        print("===================")

    def method2(self):
        print("mtd-2 of Test")
        print("self : \n ",self)
        print("===================")

#calling
t=Test()
print("From Outside of class")
print("T : ",t)
print("===================")

t.method1()
t.method2()


