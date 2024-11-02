
''' Accept Gender and age from the user
findout status of the condidate.

If gender is M | m
  then check the age, if age>=21 then major else minor

if gender is F | f
   then check the age, if age>=18 then major else minor

else third-gender '''

gender=input("Enter gender : ")
age=int( input("Enter age : ") )
lstm=['M','m']
lstf=['F','f']
#        0   1    2    3
lst=['m','M','F','f']

#if gender=='m' or gender=='M':
#if gender in lstm:
if gender in lst[0:2:1]:
    if age>=21:
        print("Major")
    else:
        print("Minor")

#elif gender=='f' or gender=='F':
#elif gender in lstf:
elif gender in lst[2::]:
    if age>=18:
        print("Major")
    else:
        print("Minor")

else:
    print("Third-Gender")






    













  
