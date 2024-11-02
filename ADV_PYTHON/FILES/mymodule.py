#mymodule.py

class Employee:
    def setEmployee(self):
        self.eno=int(input("Enter eno : "))
        self.ename=input("Enter ename : ")
        self.ecity=input("Enter ecity : ")

    def getEmployee(self):
        print("Eno is : ",self.eno)
        print("Ename is : ",self.ename)
        print("Ecity is : ",self.ecity)
        print("======================")

        
