

def Smart_division(func):
    def wrapper(x,y):
        if y==0:
            print("SOrry V R N D BY Zero....")
        else:
            func(x,y)
    return wrapper

@Smart_division #division=Smart_division(division)
def division(x,y):
    z=x/y
    print("Result is : ",z)
        
#calling
division(10,0)





