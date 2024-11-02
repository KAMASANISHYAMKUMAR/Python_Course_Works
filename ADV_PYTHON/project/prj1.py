

import csv
count1=0
count2=0
with open("Test_DataCore.csv","r") as f:
    data=csv.reader(f)
    for column in data:
        if column[10]=="expired" or column[10]=="expired (deceased)":
            count1+=1
    print("No of people died in Test_DataCore: ",count1)

with open("Test_DataCore_VitalStats.csv","r") as f:
    data=csv.reader(f)
    for column in data:
        if column[1]=="#########":
            pass
        else:
            count2+=1
    print("No of people died Test_DataCore_VitalStats: ",count2)

count=count1+count2
print("Total no of deaths are in both:",count)


