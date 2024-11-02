




import re
import time

citr=re.finditer("[^a-zA-Z0-9 ]","A1# bc2$% N48M")

for m in citr:
    time.sleep(.2)
    print("Found @ : ",m.start()," Match : ",m.group() )



''' Userdefined Pattern

a    ---> Search For only a
abc  --> Search For abc word

[abc] --> Either a or b or c
[^abc]  --> Except a or b or c

[a-z]  --> Any lower case letter
[A-Z] --> Any Ucase letter

[A-Za-z] ---> Any Alpha
[^a-zA-Z] --> Except Alpha

[0-9] or \d  --> only digits
[A-Z0-9a-z] or \w --> Any A|N  ....

'''






























