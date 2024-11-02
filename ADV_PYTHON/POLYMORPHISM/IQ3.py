class Student:
    def __init__(self):
        self.sno=input("Enter sno : ")
        self.sname=input("Enter sname : ")
        self.stot=int(input("Enter stot : "))

    def getStudent(self):
        print("sno is : ",self.sno)
        print("sname is : ",self.sname)
        print("stot is : ",self.stot)

    def __gt__(self,other):
        if self.stot > other.stot:
            return True
        else:
            return False            

#calling
s1=Student()
s2=Student()
if s1>s2:
    s1.getStudent()
else:
    s2.getStudent()
