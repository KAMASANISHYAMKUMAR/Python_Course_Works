
import threading

def myFun():
    ct=threading.current_thread()
    tname=ct.name
    print(tname," Started its execution....")

#calling
t1=threading.Thread(target=myFun)
t1.name="Child-1"
t1.start()

t2=threading.Thread(target=myFun,name="Child-2")
t2.start()
