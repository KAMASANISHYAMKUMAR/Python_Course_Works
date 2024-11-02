lst=list() #constructor
print("List : ",lst)

class Shashi:
    def __init__(self):
        self.name="Mr.Shashi "
        self.job=" Digitial IT Coach "

    def __str__(self):
        return self.name+" as "+self.job   

#calling
s=Shashi() #constructor
print("s:",s)

'''Note: While printing the ref variable internally
PVM will calls __str__(self) from object class.

__str__(self)
   always returns the hashcode of the object. If u want
   return other than hashcode, Then we have to Override
   __str__(self) from object class. '''













