import sys
import time

def myFun():
    lst=[i for i in range(1,100000)]
    print( type(lst) )
    print("size : ", sys.getsizeof(lst) )
    print("===============")
    

def myFun2():
    t=(i for i in range(1,100000) )
    print( type(t) )
    print("size : ", sys.getsizeof(t) )
    print("==============")

myFun()
time.sleep(1)
myFun2()
