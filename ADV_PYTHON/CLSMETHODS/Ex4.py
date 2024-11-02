
class Test:
    x=10
    def method1(self):
        print("Ins Mtd-1")
        print("self : \n ",self)
        print("static x : ",Test.x)
        print("============")

    @classmethod
    def method2(cls):
        print("cls Mtd-2 ")
        print("cls : \n ",cls)
        print("static x : ",Test.x)
        print("static x : ",cls.x)
        print("==========")

#calling
t=Test()
t.method1()
Test.method2()

