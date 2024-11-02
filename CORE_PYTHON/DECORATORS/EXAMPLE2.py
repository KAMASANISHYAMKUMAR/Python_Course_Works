def greet(name):    
    print("Hello ",name," Have a nice Day")

def DEC_Greet(func):  #func is copy greet
    def wrapper(name):
        if name=="ramya":
            print("Hello ",name," Have a GOOD  Day")
        else:
            func(name)    
    return wrapper

#calling
#greet("ramya")
greet=DEC_Greet(greet)   #inf is copy of wrapper
greet("ramya") #wrapper()





