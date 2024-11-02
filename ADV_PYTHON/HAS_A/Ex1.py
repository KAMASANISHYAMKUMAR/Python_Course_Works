
class SuperA:
    def method1(self):
        print("Instance mtd-1 of SA ")

class SubB:
    def method2(self):
        sa=SuperA()
        sa.method1()
        print("Instance mtd-2 of SB")
        

#calling
sb=SubB()
sb.method2()
#sb.method1() AE
