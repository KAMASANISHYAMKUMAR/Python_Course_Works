import time

def myFun(**stu):
    time.sleep(.2)
    print("type is : ",type(stu))
    print("Data is : ",stu)
    for k,d in stu.items():
        time.sleep(.2)
        print(k,d,sep=' >>> ')
    print("=================")

#calling
myFun(sno=101,sname="Ramesh",scity="hyd")
myFun(sno=102,sname="Raj")
myFun(sno=103)
myFun()
