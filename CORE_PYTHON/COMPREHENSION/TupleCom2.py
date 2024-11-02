




#(<exp> for variable in iterable if test ) -> generator

import time

for i in (i*i for i in range(1,21)):
    time.sleep(.2)
    print(i)
print("=================")

g=(i*i for i in range(1,21) if i%2==0)

for i in g:
    time.sleep(.2)
    print(i)



















