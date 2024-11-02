class A:
    pass

class B:
    def method1(self):
        print("mtd-B")

class C(A,B):
    def method1(self):
        super().method1()
        print("mtd-C")

#calling
c=C()
c.method1()

