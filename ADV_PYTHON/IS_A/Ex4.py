
class SuperA:
    @staticmethod
    def method1():
        print("Static mtd-1 of SA")

class SubB(SuperA):
    def method2(self):
        self.method1()
        SubB.method1()
        SuperA.method1()
        print("Ins mtd-2 of SubB")

#calling
sb=SubB()
#sb.method1()
sb.method2()
