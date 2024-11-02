



import re

p=re.compile("m\w\w")
m=p.search("dad mam man map run gun mad")
print("type is : ",type(m))
print("Match object : \n ",m)
