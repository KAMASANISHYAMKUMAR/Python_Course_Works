
def myFun(*,name,age):
    print("name is : ",name)
    print("age is : ",age)
    print("===============")

#calling
#myFun("james",23) TypeError
myFun(name="James",age=22)
myFun(age=22,name="Srija")

