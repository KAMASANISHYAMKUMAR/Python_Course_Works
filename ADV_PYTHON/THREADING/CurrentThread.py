



#threading.current_thread() -> Thread
import threading

ct=threading.current_thread() #mainThread
tname=ct.name
print("current Thread name is : ",tname)

ct.name="MyMain"
tname=ct.name
print("current Thread Name is : ",tname)
