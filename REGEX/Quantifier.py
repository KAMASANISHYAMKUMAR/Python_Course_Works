import re
import time

citr=re.finditer("a*","ab aac aaad aaaae")

for m in citr:
    time.sleep(.3)
    print("Found @ : ",m.start()," Match : ",m.group())

''' Quantifiers
      "a"  --> Search For only a
      "a+"  --> Atleast one a
      "a?"   ---> Atmost one a 0-a's or 1-a's
      "a*"   --> 0 a's or any No.of.a's  ... '''

