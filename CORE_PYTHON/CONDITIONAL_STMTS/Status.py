
''' Accept gender and age from the user
print major if gender is f or F and age should be >21
else minor
'''

gender=input("Enter any char ")
age=int(input("Enter age : "))

#if gender=='f' or gender=='F' and age>=21:
if gender in 'fF' and age>=21:
    print("Major")
else:
    print("Minor")
