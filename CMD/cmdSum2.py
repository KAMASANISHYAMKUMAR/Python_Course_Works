#cmdsum2.py

import sys
import time

s=0
for i in sys.argv[1:]:
    time.sleep(.2)
    s=s+int(i)
    print(i)

print("============")
print("Sum is : ",s)
