
'''Can i write more than one Exception
in a single except
Ans: Yes. '''

import sys

try:
    x=int(sys.argv[1])

except (IndexError,ValueError) as e:
    print("IE | VE : Please enter an int input.....")
    print("Reason : ",e)

else:
    print("Given number is : ",x)

