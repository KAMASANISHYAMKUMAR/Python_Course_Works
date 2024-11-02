import time

fname=input("Enter File name : ") #s.txt
f=None
try:
    f=open(fname,"r")
    
except FileNotFoundError as fnfe:
    print("sorry unable to continue....")
    print("Reason is : \n ",fnfe)

else: 
    data=f.read()
    for i in data:
        time.sleep(.1)
        print(i,end='')
        
finally:
    if f!=None:
        f.close()
        print("\n File is Closed ")






