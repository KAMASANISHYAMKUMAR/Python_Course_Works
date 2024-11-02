
class Test:
    def __init__(self):
        print("Super cls constructor ")

class Testing(Test):
    def __init__(self):
        super().__init__()
        print("Sub cls constructor ")

#calling
t=Testing()

