
class SuperA:
    @classmethod
    def method1(cls):
        print("Cls mtd-1 of SuperA")

class SubB:
    def method2(self):
        sa=SuperA()
        sa.method1()
        SuperA.method1()    
        print("Ins mtd-2 of SubB")

#calling
sb=SubB()
sb.method2()
