
def OuterFun():
    def InnerFun():
        x=10+20*3
        return x

    a=InnerFun()
    print("Result is : ",a)

#calling
OuterFun()

'''Note-1: If u want use the result of inner function
inside of outerfunction then inner function need
to return the result of inner function.

Note-2:
'''




