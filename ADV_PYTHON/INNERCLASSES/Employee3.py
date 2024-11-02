
class Employee:
    def setEmployee(self):
        self.eno=input("Enter eno : ")
        self.ename=input("Enter ename : ")
        self.d=self.Doj()
        self.d.setDoj()
        print("=========================")

    def getEmployee(self):
        print("Eno is : ",self.eno)
        print("Ename is : ",self.ename)
        self.d.getDoj()        

    class Doj:
        def setDoj(self):
            print("Enter Doj : ")
            self.dd=input("Enter DD : ")
            self.mm=input("Enter MM : ")
            self.yy=input("Enter YY : ")

        def getDoj(self):
            print("Doj is :{}-{}-{}".
                  format(self.dd,self.mm,self.yy))
            print(f"Doj is : {self.dd}-{self.mm}-{self.yy}")

#calling
e=Employee()
e.setEmployee()
e.getEmployee()





        
