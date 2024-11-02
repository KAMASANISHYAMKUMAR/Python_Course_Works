
x=10

def myFun():
    global x
    x=x+10
    print("x val is : ",x)

#calling
myFun( )
print("From outside of myfun")
print("x val is : ",x)
