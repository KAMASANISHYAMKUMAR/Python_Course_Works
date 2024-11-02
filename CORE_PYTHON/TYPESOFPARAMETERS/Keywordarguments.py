#keyword arguments

def myFun(name,age):
    print("name is : ",name)
    print("age is : ",age)
    print("===============")

#calling
myFun(name="Chinni",age=22)
myFun(age=23,name="Khanna")

# myFun(name="James") TypeError
myFun("Kumar",age=28)
#myFun(age=19,"Roja") SyntaxError
