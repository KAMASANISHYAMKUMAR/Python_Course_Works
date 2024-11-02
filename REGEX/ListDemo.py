


import re

p=re.compile("m\w\w")
lst=p.findall("dad    run gun ")
print("Result is : ",lst)
