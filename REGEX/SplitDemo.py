



import re

data="have a nice day my dear friend"
lst=re.split(r"\b\w+e\b",data)
print("Result is : ",lst)
