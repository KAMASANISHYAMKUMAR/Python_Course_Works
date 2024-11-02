
''' Accept 4 numbers from the user
findout biggest in 4 '''

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
d=int(input("Enter d : "))

if a>b and a>c and a>d:
    print("a is big")
elif b>c and b>d:
    print("b is big")
elif c>d:
    print("c is big")
else:
    print("d is big")

print("a is big") if a>b and a>c and a>d else
print("b is big") if b>c and b>d else
print("c is big") if b>d else print("d is big")











    


    
