
import time
import threading

def myFun():
    for i in range(1,11):
        time.sleep(.5)
        print("MyFun .... ",i)

def myFun2():
    for i in range(30,41):
        time.sleep(.2)
        print("MyFun2 >>> ",i)

#calling
t1=threading.Thread(target=myFun)
t2=threading.Thread(target=myFun2)
t1.start()
t2.start()

t1.join()
for i in range(20,31):
    time.sleep(.1)    
    print("Main >>>> ",i)
