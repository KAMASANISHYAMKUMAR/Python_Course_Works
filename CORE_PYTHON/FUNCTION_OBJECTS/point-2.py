
def greet():
    a="Hello "
    return a

def specialGreetings(func): #func is copy of greet
    b=func() # greet()
    c=b+" MyDear "
    return c

d=specialGreetings(greet)
print("Result is : ",d)




'''
r=greet()
print("Result is : ",r)
'''
