y=20 #global variable

def myFun1():
    x=10 #localvariable
    print("Inside of myFun1")
    print("x val is : ",x)
    print("y val is : ",y)
    print("================")

def myFun2():
    print("Inside of myFun2")
    #print("x val is : ",x) NE
    print("y val is : ",y)
    print("================")

#calling
myFun1( )
myFun2( )
print("From outside of all function")
print("y val is : ",y)





