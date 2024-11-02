

''' Accept 3 sub marks calculate
             total, avg, result and grade.

    Pass marks>34 in all subjects else Fail

    if Result is Pass
       then check the avg marks
           if avg>=70 print Grade-A
           if avg>=60 print Grade-B
           if avg>=50 print Grade-C else Grade-D '''

m1=int(input("Enter m1 : "))
m2=int(input("Enter m2 : "))
m3=int(input("Enter m3 : "))

tot=m1+m2+m3
avg=tot/3

print("Total is : ",tot)
print("Avg is : ",avg)

if m1>34 and m2>34 and m3>34:
    if avg>=70:
        print("Grade-A")
    elif avg>=60:
        print("Grade-B")
    elif avg>=50:
        print("Grade-C")
    else:
        print("Grade-D")
else:
    print("Result is : Fail ")
          





















           
    
