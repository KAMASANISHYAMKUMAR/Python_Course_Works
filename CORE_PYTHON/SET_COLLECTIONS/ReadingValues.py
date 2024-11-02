s={10,12.12,"Shashi",None,10,(10+20j)}
print("type is : ",type(s))
print("Data is : ",s)
print("========================")

#print("First : ",s[0]) TypeError
#print("First 3 Objects : ",s[0:3:1]) TypeError

import time

for i in s:
    time.sleep(.2)
    print(i)







