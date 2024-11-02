
class Sample:
    def method1(self):
        for i in range(1,11):
            print("Mtd-1  >>> ",i)

    def method2(self):
        for i in range(30,41):
            print("Mtd-2  ::: ",i)

#calling
import threading
s=Sample()
t1=threading.Thread(target=s.method1)
t2=threading.Thread(target=s.method2)
t1.start()
t2.start()











