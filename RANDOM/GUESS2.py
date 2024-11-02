
import random
import time

for i in range(1,11):
    item=int(input("Guess a number [1,100] : "))
    no=random.randint(1,100)

    if item==no:
        print("U R Guess is correct ....")
        break
    elif item<no:
        print("Guess too less ")
    elif item>no:
        print("Guess is too large...")
