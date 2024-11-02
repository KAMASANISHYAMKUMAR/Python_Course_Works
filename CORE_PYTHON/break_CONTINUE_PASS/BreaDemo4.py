import time

lst=[10,20,30,40,50,70,80,90,100]
print("List : ",lst)
found=0

sno=int(input("Enter sno : ")) #40

for i in lst:
    time.sleep(.2)
    if i==sno:
        found=1
        print("Found")
        break

if found==0:
    print("Sorry Not Found")


    
    

