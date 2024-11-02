
class MyNumberException(Exception):
    def __init__(self,msg):
        self.msg=msg

import re

class ValidateNumber:
    def __init__(self):
        self.data=input("Enter u r mobile number : ")

    def validate(self):
        m=re.fullmatch("[6-9]\d{9}",self.data)
        if m!=None:
            print("Valid M Number ")
        else:
            try:
                raise MyNumberException("Invalid MNumber")
            except MyNumberException as mne:
                print("Sorry Unable to continue....")
                print("Reason is : ",mne)

#calling
v=ValidateNumber()
v.validate()




        
        
    
    
