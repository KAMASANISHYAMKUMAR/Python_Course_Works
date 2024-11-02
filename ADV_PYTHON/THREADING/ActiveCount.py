
import threading
import time

def myFun1():
    ct=threading.current_thread()
    tname=ct.name
    print(tname," starteds  its Execution ....")
    time.sleep(10)
    print(tname," ends its Execution ....")

#calling
t1=threading.Thread(target=myFun1,name="Child-1")
t2=threading.Thread(target=myFun1,name="Child-2")
t1.start()
t2.start()

atc=threading.active_count()
print("Active Thread Count is : ",atc)

time.sleep(11)
atc=threading.active_count()
print("Active Thread Count is : ",atc)










