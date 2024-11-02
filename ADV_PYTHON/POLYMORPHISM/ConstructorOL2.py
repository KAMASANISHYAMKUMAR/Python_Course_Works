
class Test:
    def __init__(self):
        print("0-parameter const ")

    def __init__(self,x):
        print("1-para const : ",x)

#calling
#t=Test() TypeError
t=Test(12)
