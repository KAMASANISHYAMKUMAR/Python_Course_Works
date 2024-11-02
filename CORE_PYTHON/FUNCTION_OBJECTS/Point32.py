import time
def myFun():
    def stars():
        for i in range(1,11):
            time.sleep(.2)
            print("*",end=' ')

    stars()
    print("\n welcome ")
    stars()
    print("\n to ")
    stars()
    print("\n My Word ")
    stars()

#calling
#stars() NE
myFun()
