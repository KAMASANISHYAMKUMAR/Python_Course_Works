class Person:
    def setPerson(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("no is : ",self.no)
        print("name is : ",self.name)
        print("-------------------------------")

class Student(Person):
    def setStudent(self):
        self.setPerson()
        self.course=input("Enter course : ")
        print("--------------------------------")

    def getStudent(self):
        self.getPerson()
        print("course is : ",self.course)

class Employee(Person):
    def setEmployee(self):
        self.setPerson()
        self.job=input("Enter job : ")
        print("---------------------------------")

    def getEmployee(self):
        self.getPerson()
        print("job is : ",self.job)
        print("----------------------------------")

#calling
s=Student()
print("Enter Student Details ....")
s.setStudent()
s.getStudent( )

e=Employee()
print("Enter Employee Details ....")
e.setEmployee()
e.getEmployee()
















        








        
        






        
        











        

