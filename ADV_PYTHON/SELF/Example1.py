def myFun():
    print("MyFun ...")
    
class Sample:
    def myMethod(self):
        print("myMethod  of Sample ")

#calling
myFun()
# myFun2() NameError
#myMethod() NameError

s=Sample()
s.myMethod()
#s.myMethod2()  AttributeError
