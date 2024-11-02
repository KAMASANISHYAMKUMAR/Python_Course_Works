import time
import threading

class Sample:
    def method1(self):
        ct=threading.current_thread()
        tname=ct.name
        print(tname," started its execution ....")
        time.sleep(5)
        print(tname," ends its execution .....")

#calling
s=Sample()
t1=threading.Thread(target=s.method1,name="Child-1")
t1.start()
print("Thread isalive ? : ",t1.is_alive())
time.sleep(10)
print("thread isalive ? : ",t1.is_alive())







