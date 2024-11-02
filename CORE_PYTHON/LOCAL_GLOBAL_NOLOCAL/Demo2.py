
def OuterFun():
    y=20
    
    def InnerFun():
        nonlocal y         
        y=y+20
        print("InnerFun ")
        print("y val is : ",y)

    InnerFun()
    print("From Inside of Outerfun")
    print("y val is : ",y)

#calling
OuterFun()


    
