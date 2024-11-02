
class Person:
    def setPerson(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("no is : ",self.no)
        print("name is : ",self.name)
        print("------------------------------")

class Marks(Person):
    def setMarks(self):
        self.marks=[int(i) for i in input("Emter 3 sub marks").split()]

    def getTotal(self):
        self.tot=sum(self.marks)
        return self.tot

    def getMarks(self):
        import time
        print("Marks are : ")
        for i in self.marks:
            time.sleep(1)
            print(i)
        print("----------------------")
        s=self.getTotal()
        print("Total is : ",s)
        print("----------------------")

class Student(Marks):
    def setStudent(self):
        self.setPerson()
        self.setMarks()
        print("=================")

    def getStudent(self):
        self.getPerson()
        self.getMarks()

#calling
s=Student()
s.setStudent()
s.getStudent()
        







        






        
