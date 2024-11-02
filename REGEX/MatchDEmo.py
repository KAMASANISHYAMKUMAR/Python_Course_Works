



import re

p=re.compile("m\w\w")
m=p.match("mom mam dad gun map mad jug")
print("Type is : ",type(m))
print("Data is : \n ",m)

