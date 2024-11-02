
#raise <ExceptionClsName>([list of args])

''' Accept age from the user
print elig for vote if age>=18 else
print not eligible for vote by raising
ZeroDivisionError '''

age=int(input("Enter age : "))

if age>=18:
    print("Eligible for Vote ")
else:
    try:
        raise ZeroDivisionError()
    
    except ZeroDivisionError:
        print("ZDE : Sorry Not Elig For vote ")
















