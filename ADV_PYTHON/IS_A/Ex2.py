
class SuperA:
    def method1(self):
        print("Int mtd-1 of SA")

class SubB(SuperA):
    def method2(self):
        self.method1()
        print("Ins mtd-2 of SB ")

#calling
sb=SubB()
#sb.method1()
sb.method2()
