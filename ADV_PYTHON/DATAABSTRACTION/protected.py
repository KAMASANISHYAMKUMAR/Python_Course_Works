
class Sample:
    def __init__(self):
        self._x=10 #protected

    def getData(self):
        print("from Sample ")
        print("protected x is : ",self._x)

#calling
s=Sample()
s.getData( )
