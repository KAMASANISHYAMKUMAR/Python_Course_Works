
class Employee:
    def __init__(self):
        self.ename=input("Enter name : ")
        self.spd=int(input("Enter sal per day :"))

    def __mul__(self,other):
        return self.spd*other.daysw

class TimeSheet:
    def __init__(self):
        self.daysw=int(input("Enter Days worked "))

    def __mul__(self,other):
        return self.daysw*other.spd

#calling
e=Employee()
t=TimeSheet()
ns=t*e
print("NetSalary : ",ns)





