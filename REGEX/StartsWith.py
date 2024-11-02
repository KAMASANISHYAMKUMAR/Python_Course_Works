


import re
import time

data="Have a nice daY"
#m=re.search("\w\wy$",data,re.IGNORECASE)

m=re.search("^h[a-zA-Z]{3}",data,re.I)
if m!=None:
    print("Target starts with given Pattern")
else:
    print("Sorry Target is not starts with Given Pattern")






