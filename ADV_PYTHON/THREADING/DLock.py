
import threading
import time

def myFun():
    ct=threading.current_thread()
    tname=ct.name
    print(tname," started Its Execution .....")
    mt.join()
    print(tname," Ends its Execution.....")    

#calling
mt=threading.current_thread()  #MainThread
print("Main is started Its Execution .....")

t1=threading.Thread(target=myFun,name="Child")
t1.start()
t1.join( )
print("Main Ends its Execution ....")




