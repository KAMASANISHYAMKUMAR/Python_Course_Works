def DEC_Greet(func):  #func is copy greet
    def wrapper(name):
        if name=="ramya":
            print("Hello ",name," Have a GOOD  Day")
        else:
            func(name)    
    return wrapper

@DEC_Greet  #greet=DEC_Greet(greet) 
def greet(name):    
    print("Hello ",name," Have a nice Day")

#calling
greet("ramya") 





