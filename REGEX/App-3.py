


import re
import time

data="Have a nice daY"
#m=re.search("\w\wy$",data,re.IGNORECASE)

m=re.search("\w\wy$",data,re.I)
if m!=None:
    print("Target Ends with given Pattern")
else:
    print("Sorry Target is not ends with Given Pattern")






