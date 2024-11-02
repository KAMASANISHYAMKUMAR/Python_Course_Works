import time

class Test:
    def __init__(self,x=None,y=None,z=None):
        time.sleep(1)
        if x!=None and y!=None and z!=None:
            print("3-para constructor ",x,y,z)
        elif x!=None and y!=None:
            print("2-Para constructor ",x,y)
        elif x!=None:
            print("1-Para constructor ",x)
        else:
            print("0-para constructor ")
            

#calling
t1=Test(10,20,30)
t2=Test(40,50)
t3=Test(60)
t4=Test()



        
