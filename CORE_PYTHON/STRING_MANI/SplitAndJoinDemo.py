
#S.split([chars]) -> list
s="welcome to sssit kphb hyd"
print("Data is : ",s)

lst=s.split()
print("Result is : ",lst)

import time
for i in lst:
    time.sleep(.2)
    print(i)
print("===================")

s2="have,a.nice,day"
print("Data is : ",s2)
lst=s2.split(".")
print("Result is : ",lst)







