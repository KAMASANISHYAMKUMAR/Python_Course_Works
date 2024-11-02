
import time
import threading

def myFun1():
    for i in range(1,11):
        print("myFun1..... ",i)

def myFun2():
    time.sleep(10)
    for i in range(20,31):
        print("myFun2 >>>> ",i)

t1=threading.Thread(target=myFun1)
t2=threading.Thread(target=myFun2)
t1.start()
t2.start()
