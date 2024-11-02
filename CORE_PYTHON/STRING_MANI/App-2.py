
''' Accept string from the user
findout no.of.cap , no.of.small
and no.of.digits in the given string
iff the given string alnum '''
import time

data=input("Enter Data ")

if data.isalnum():
    nc=ns=nd=0
    
    for i in data:
        time.sleep(.5)

        if i.isupper():
            nc+=1
        elif i.islower():
            ns+=1 #ns=ns+1
        elif i.isdigit():
            nd+=1

    print("No.of.Cap : ",nc)
    print("No.of.Small : ",ns)
    print("No.of.Digits : ",nd)
            
else:
    print("Not an alphanum")




