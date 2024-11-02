
f=open("data3.txt","w")
print("Enter u r data press * For Exit ")

'''
data=input() #chinni
while data!='*':
    f.write(data+"\n")
    data=input() #*
'''

while data:=input()!='*': 
    f.write(data+"\n")

f.close()
print("Data is Saved ")




