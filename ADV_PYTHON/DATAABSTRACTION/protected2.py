
class Test:
    def __init__(self):
        self._x=10

    def method1(self):
        print("From Test ")
        print("Protected x : ",self._x)

class Testing(Test):
    def method2(self):
        print("From Testing ")
        print("protected x : ",self._x)

#calling
t=Testing()
t.method1()
t.method2()
