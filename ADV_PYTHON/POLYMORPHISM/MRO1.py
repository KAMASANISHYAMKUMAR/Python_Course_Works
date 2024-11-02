
class A:
    pass

class B(A):
    pass

#calling
b=B()
lst=B.mro()

import time
for i in lst:
    time.sleep(.1)
    print(i)
