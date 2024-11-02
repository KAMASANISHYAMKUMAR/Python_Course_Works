
import csv

with open("stu2.csv","w") as f:
    wo=csv.writer(f)

    lst=['sno','sname','smarks']
    wo.writerow(lst)

    while True:
        n=int(input("Enter sno : "))
        na=input("Enter sname : ")
        ma=int(input("Enter marks: "))
        wo.writerow([n,na,ma])

        opt=input("do u want another rec y | n ")
        if opt in ['n','N']:
            break
        
print("Data is Saved ")

            
