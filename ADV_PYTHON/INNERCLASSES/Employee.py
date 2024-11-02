class Employee:
    def setEmployee(self):
        self.eno=input("Enter eno : ")
        self.ename=input("Enter ename : ")        

    def getEmployee(self):
        print("Eno is : ",self.eno)
        print("Ename is : ",self.ename)

    class Doj:
        def setDoj(self):
            print("Enter Doj : ")
            self.dd=input("Enter DD : ")
            self.mm=input("Enter MM : ")
            self.yy=input("Enter YY : ")

        def getDoj(self):
            print("DOJ is : {}-{}-{}".
                  format(self.dd,self.mm,self.yy))

#calling
e=Employee()
e.setEmployee( )

d=e.Doj()
d.setDoj()

print("==============")
e.getEmployee()
d.getDoj( )
print("===============")


            






        
