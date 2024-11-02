import time

f=open("data4.txt")
print("File closed ? : ",f.closed)
time.sleep(2)
f.close()
print("File closed ? : ",f.closed)
print("===================-====")

with open("data4.txt","r") as f:
    print("From inside of with ....")
    time.sleep(1)
    print("File closed ? : ",f.closed)

time.sleep(1)
print("From outside of with context ")
print("File closed ? : ",f.closed)




