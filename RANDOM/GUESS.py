



import random
import time

lst=["android","java","python","django","dm"]
print("List : ",lst)

for i in range(1,11):
    item=random.choice(lst)
    gitem=input("   Enter u r guess ... ")
    if item==gitem:
        print("Congrats....")
        print(gitem," Is Free For u...")
        break
    else:
        print("Sorry Wrong Guess Try Again ... \n\n")






        
