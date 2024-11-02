import time

data=input("Enter Data ")
nc=ns=nd=nsp=nsy=0

for i in data:
    time.sleep(.2)
    x=ord(i)

    if x>=65 and x<=90:
        nc+=1
    elif x>=97 and x<=122:
        ns+=1
    elif x>=48 and x<=57:
        nd+=1
    elif x==32:
        nsp+=1
    else:
        nsy+=1

time.sleep(1)
print("No.of.Cap : ",nc)
print("No.of.Small : ",ns)
print("No.of.Digits : ",nd)
print("No.of.Sp : ",nsp)
print("No.of.nsy : ",nsy)
print("Length is : ",len(data))







    
