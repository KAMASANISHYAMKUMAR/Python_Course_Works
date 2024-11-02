
class Sample:
    def __init__(self):
        print("const is invoked ")

    def __del__(self):
        print("dest is invoked ")

#calling
s=[Sample(),Sample(),Sample()]
#del s[1] or
#s[1]=None
del s

