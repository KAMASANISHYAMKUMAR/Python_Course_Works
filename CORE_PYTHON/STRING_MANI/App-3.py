
''' Accept a string from the user
findout no.of.cap,no.of.small,
no.of.digits,no.of.spaces,total no.of.let
no.of.sym
'''
import time

data=input("Enter u r data : ")
ns=nc=nsp=nsy=nd=0

for i in data:
    if i.isupper():
        nc=nc+1
    elif i.islower():
        ns=ns+1
    elif i.isdigit():
        nd=nd+1
    elif i.isspace():
        nsp=nsp+1
    else:
        nsy=nsy+1

time.sleep(.2)
print("No.of.Cap : ",nc)
print("No.of.Small : ",ns)
print("No.of.Digits : ",nd)
print("No.of.Spa : ",nsp)
print("No.of.Sym : ",nsy)

tnl=nc+ns+nsp+nd+nsy
print("No.of.Tnl : ",tnl)








 









