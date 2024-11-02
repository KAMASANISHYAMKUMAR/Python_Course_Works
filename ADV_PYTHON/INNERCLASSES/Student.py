import time

class Student:
    def setStudent(self):
        self.sno=input("Enter sno : ")
        self.sname=input("Enter sname : ")

        self.d=self.Dob()
        self.d.setDob()
        
        self.m=self.Marks()
        self.m.setMarks()

    def getStudent(self):
        print("Sno is : ",self.sno)
        print("Sname is : ",self.sname)
        self.d.getDob()
        self.m.getMarks()

    class Dob:
        def setDob(self):
            print("Enter Dob : ")
            self.dd=input("Enter DD : ")
            self.mm=input("Enter MM : ")
            self.yy=input("Enter YY : ")

        def getDob(self):
            print("==================")
            print(f"Dob is : {self.dd}-{self.mm}-{self.yy}")

    class Marks:
        def setMarks(self):
            print("Enter Marks : ")
            self.marks=[int(i) for i in input().split()]

        def getMarks(self):
            print("===================")
            print("Marks are ")
            for i in self.marks:
                time.sleep(.2)
                print(i)
            print("=============")
            print("Total is : ",sum(self.marks))

#calling
s=Student()
s.setStudent()
s.getStudent()






        
