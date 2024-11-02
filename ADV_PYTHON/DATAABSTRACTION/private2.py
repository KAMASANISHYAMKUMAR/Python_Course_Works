
class Sample:
    def __init__(self):
        self.__x=10 #private

    def getData(self):
        print("From Sample cls ")
        print("private x : ",self.__x)

#calling
s=Sample()
s.getData( )
print("From outside of Sample cls")
print("private x : ",s.__x)
