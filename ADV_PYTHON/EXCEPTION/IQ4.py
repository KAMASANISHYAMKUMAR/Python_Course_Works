
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
    
except Exception as e:
    print("Sorry Unable to continue....")
    print("Reason : ",e)
    
else:
    print("Result is : ",z)






    
