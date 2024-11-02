



import re
import time

citr=re.finditer("[.]","have a. nic.e ! da@y 123")

for m in citr:
    time.sleep(.2)
    print(m.group())

