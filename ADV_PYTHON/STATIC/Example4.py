class Student:
    course="Python" #static
    
    def setStudent(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")      
        print("======================")

    def getStudent(self):
        print("sno is : ",self.no)
        print("sname is : ",self.name)
        print("course is : ",Student.course)
        print("=========================")
        
#calling
s1=Student()
s1.setStudent( )

s2=Student()
s2.setStudent( )

s1.getStudent()
s2.getStudent()





        
