#cmd3.py

import sys
import time

print("All Command line args ")

for i in sys.argv[1: ]:
    time.sleep(.2)
    print(i)
