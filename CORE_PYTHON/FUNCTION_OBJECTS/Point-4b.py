def OuterFun():
    def InnerFun():
        x=10+20*3
        return x

    a=InnerFun()
    return a

#calling
b=OuterFun()
print("Result is : ",b)

'''Note-1: If u want use the result of inner function
inside of outerfunction then inner function need
to return the result of inner function.

Note-2:
If u want use the result of the inner function outside
of the outerfunction then outerfunction need to
return result of the innerfunction.
'''




