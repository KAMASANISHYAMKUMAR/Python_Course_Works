
import mymodule

e=mymodule.Employee()

print("ClassName is : ",e.__class__)
print("Module name is : ",e.__module__)
print("Doc_string is : ",e.__doc__)

e.getEmployee()

#Adding an instance field
#e.job='MANAGER'
e.__setattr__('ejob','Manager')
e.__setattr__('esal',50000)

import time

edict=e.__dict__
for k,d in edict.items():
    time.sleep(.2)
    print(k,d,sep=' >>> ')

print("=========================")

#Reading the value From an instance field
#name=e.ename

name=e.__getattribute__('ename')
print("Ename is : ",name)
job=e.__getattribute__('ejob')
print("Job title is : ",job)

#Deleting an instance field
#del e.ejob
e.__delattr__('ejob')
e.__delattr__('esal')

print("=================")
for k,d in e.__dict__.items():
    time.sleep(.2)
    print(k,d,sep=' >>> ')
    



































