


import re

m=re.match("m\w\w","mom mon dad gun jug map run")
print("Type is : ",type(m))
print("Match object : \n ",m)

if m!=None:
    print("Starting index : ",m.start() )
    print("Ending index+1 : ",m.end())
    print("Matched String : ",m.group())

