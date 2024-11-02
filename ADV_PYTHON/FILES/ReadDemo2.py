
f=open("data4.txt")
data=f.read()

import time
for i in data:
    time.sleep(.1)
    print(i,end='')

pos=f.tell()
print("\n Iam @ : ",pos)
print("==============")

f.seek(0)
pos=f.tell()
print("Iam @ : ",pos)

data=f.read(6)
print("Data : ",data)
pos=f.tell()
print("Iam @ : ",pos)










