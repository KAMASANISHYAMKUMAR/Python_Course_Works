
def myFun():
    for i in range(1,11):
        print("MyFun .... ")

import threading
t1=threading.Thread(target=myFun)
#tname=t1.getName()
tname=t1.name
print("Thread Name is : ",tname)

#t1.setName("Child")
t1.name="Child"
tname=t1.name
print("Thread Name is : ",tname)


'''Note : whenever u define any thread
by default every thread is created with their defualt
names i.e Thread-1 | Thread-2 ....
Based On the App Req we can get or set name of
thread by using name property

Upto Python 3.9
setName(str)
getName( ) -> str

'''







