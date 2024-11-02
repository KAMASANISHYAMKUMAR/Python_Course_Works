

import time

class Sample:
    def __init__(self):
        time.sleep(1)
        print("Constr wout args is invoked ....")

#calling
s1=Sample()
print(s1)

s2=Sample()
print(s2)

s3=Sample()
print(s3)
