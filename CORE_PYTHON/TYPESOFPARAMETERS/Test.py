
def myFun(a,b,/,c,d,*,e,f):
    print("a : ",a)
    print("b : ",b)
    print("c : ",c)
    print("d : ",d)
    print("e : ",e)
    print("f : ",f)
    print("=============")
    
#calling
myFun(10,20,30,40,e=50,f=60)
myFun(10,20,c=30,d=40,e=50,f=60)
myFun(10,20,30,40,f=60,e=50)

'''
   a,b positional only argument
   c,d positional or keyword
   e,f keyword only argument
'''