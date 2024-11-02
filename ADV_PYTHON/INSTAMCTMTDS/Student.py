
class Student:
    def  setStudent(self):
        self.m1=int(input("Enter m1 : "))
        self.m2=int(input("Enter m2 : "))
        self.m3=int(input("Enter m3 : "))

    def findResult(self):
        if self.m1>34 and self.m2>34 and self.m3>34:
            print("Result is : PASS ")
        else:
            print("Result is : Fail ")

#calling
s=Student( )
s.setStudent()
s.findResult( )

