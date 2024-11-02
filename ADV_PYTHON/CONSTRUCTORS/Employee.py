
class Employee:
    def __init__(self,no,name,sal):
        self.no=no
        self.name=name
        self.sal=sal        
        print("================")

    def getEmployee(self):
        print("no is : ",self.no)
        print("name is : ",self.name)
        print("salary is : ",self.sal)
        print("=================")

#calling
e=Employee(101,"Ramesh",20000)
e.getEmployee()

        

    
