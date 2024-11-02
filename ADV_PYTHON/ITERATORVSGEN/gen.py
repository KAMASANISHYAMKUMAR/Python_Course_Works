'''
Generator  | iterable 
  - defining the generator is nothingbut
  creating a function with yield keyword

  - If any Function which is having yield keyword
  then that function returns generator object.
'''
import time

def myFun():
    yield "Shashi"
    yield "Chinni"
    yield "khanna"
    yield "munny"

s=myFun()
print("Type is : ", type(s) )
for i in s:
    time.sleep(1)
    print(i)





    

