z=30
def OuterFun():
    y=20
    def InnerFun():
        x=10
        print("From InnerFun ")
        print("x val is : ",x)
        print("y val is : ",y)
        print("z val is : ",z)
        print("=============")

    print("From OuterFun ")
    #print("x val is : ",x) NE
    print("y val is : ",y)
    print("z val is : ",z)
    InnerFun()

#calling
OuterFun()
print("From outside outer Fun")
print("z val is : ",z)



    
