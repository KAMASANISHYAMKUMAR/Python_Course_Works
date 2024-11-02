




import re
import time

data="an apple a day keeps the doctor away"
citr=re.finditer(r"\b[a-z]{3}\b",data)

for m in citr:
    time.sleep(.2)
    print(m.group( ))






