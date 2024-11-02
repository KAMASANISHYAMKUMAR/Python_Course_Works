

def myCalc(x,y):
    a=x+y
    s=x-y
    m=x*y
    return a,s,m      #    t=12,8,20  #packing \ tuple 

#calling
t=myCalc(10,2)
print("Mul is : ",t[0])
print("sub is : ",t[1])
print("Add is : ",t[2])
