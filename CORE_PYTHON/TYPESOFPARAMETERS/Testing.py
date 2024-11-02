
import time

def myFun(*x,**y):
    time.sleep(.2)
    for i in x:
        time.sleep(.2)
        print(i)
    print("-----------------")

    for k,d in y.items():
        time.sleep(.2)
        print(k,d,sep=' <<<>>> ')

#calling
myFun(10,20,30,40,name="Sai",age=23,scity="Hyd")
