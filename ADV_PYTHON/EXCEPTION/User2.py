class MyLoginException(Exception):
    def __init__(self,msg):
        self.msg=msg

uname=input("Enter username : ")
pword=input("Enter password : ")

if uname=="sssit" and pword=="kphb":
    print("Valid user ")
else:
    try:
        raise MyLoginException('Invalid UN or PW ')
    
    except MyLoginException as me:
        print("Sorry Unable to continue...")
        print("Reason : ",me)


        
    
        
