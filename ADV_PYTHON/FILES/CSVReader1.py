
import csv
import time

with open("stu3.csv","r") as f:
    ro=csv.reader(f)

    for lst in ro:
        time.sleep(1)
        for i in lst:
            time.sleep(.2)
            print(i,end='\t')
            
        print(" ")
                               
            
