
''' Accept 4 numbers from the user
findout biggest in 4 '''

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
d=int(input("Enter d : "))

if a>b and a>c and a>d:
    print("a is big")

elif b>a and b>c and b>d:
    print("b is big")

elif c>a and c>b and c>d:
    print("c is big")

else:
    print("d is big")


    
