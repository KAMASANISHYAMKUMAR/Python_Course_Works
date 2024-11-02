

#dd-mm-yy \d{1,2}-\w{1,3}-\d{2,4}

import re
import time

data=''' Ramesh 12-Jan-99 Suresh 2-03-2018 nani
12-12-22 Pooja 2-12-2009 Priya 22-3-99'''

citr=re.finditer("\d{1,2}-\w{1,3}-\d{2,4}",data)

for m in citr:
    time.sleep(.2)
    print(m.group())
