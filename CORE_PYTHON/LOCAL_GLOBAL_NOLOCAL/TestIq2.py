
x=20

def myFun():    
    x=10
    print("local x : ",x)
    d=globals()
    print("global x : ",d['x'])
    print("global x : ",globals()['x'])
    print("global x : ",d.get('x'))
    print("global x : ",globals().get('x'))
    

#calling
myFun( )
