class Test:
    def __init__(self):
        self.__x=10

    def getData(self):
        print("From Test : ")
        print("Private x is : ",self.__x)

class Testing(Test):
    def getData2(self):
        print("From Testing : ")
        print("Private x is : ",self.__x)

#calling
t=Testing()
t.getData()
t.getData2()


