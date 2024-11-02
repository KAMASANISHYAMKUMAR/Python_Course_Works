




import re
import time

citr=re.finditer("m\w\w","mom man dad jug map run")
print("Type is : ",type(citr))

for m in citr:
    time.sleep(1)
    print("Found @ : ",m.start()," Match : ",m.group() )






