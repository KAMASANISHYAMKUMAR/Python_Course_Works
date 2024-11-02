




import re
import time

citr=re.finditer("\S","A1# bc2$% N48M")

for m in citr:
    time.sleep(1)
    print("Found @ : ",m.start()," Match : ",m.group() )


''' Predefined Patterns
\d         ---> only Digits
\D         ---> Except Digits

\w     ---> Only A|N
\W     ---> Except A|N

\s   --> Only Space
\S   --> Except Spaces

^ --> Pattern starts with
$  --> Patterns ends with ....   '''






















