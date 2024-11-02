import time

def myFun(*x):
    time.sleep(1)
    print("Type is : ",type(x))
    print("Data is : ",x)
    for i in x:
        time.sleep(.2)
        print(i)
    print("===============")
    print("Sum is : ",sum(x))
    print("================")

#calling
myFun(10,20,30,40,50,60)
myFun(10,20,30)
myFun(10,20)
myFun(10)
myFun()
    
