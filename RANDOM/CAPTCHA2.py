
#2digits 3 UC 4,5 digit 6 LC
#1UC 2 digit 3 LC 4,5 digits 6 UC

import random
import time

for i in range(1,11):
    if i%2==0:
        time.sleep(.5)
        print( random.randint(11,99),
        chr( random.randint(65,90) ),
        random.randint(11,99),
        chr( random.randint(97,122) ),sep='' )
    else:
        print( chr( random.randint(65,90) ),
               random.randint(1,9),
               chr( random.randint(97,122) ),
               random.randint(11,99),
               chr(random.randint(65,90)),sep='' )








    
