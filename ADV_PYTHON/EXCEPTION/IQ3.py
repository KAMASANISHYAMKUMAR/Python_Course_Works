
'''Can i handle any Exception
in a single except
Ans: Yes. possible uy writing
except with Exception or except without
Exception '''

import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
except :
    print("Sorry Unable to continue....")
else:
    print("Result is : ",z)






    
