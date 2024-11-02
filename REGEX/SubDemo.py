



import re

data="have a nice day my dear friend"
t=re.subn(r"\b[a-zA-Z]{4}\b","####",data)
print("Result is : ",t[0])
print("No.of.Replements : ",t[1])
