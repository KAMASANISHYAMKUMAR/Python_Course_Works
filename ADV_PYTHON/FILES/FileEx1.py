f=open("data1.txt","w+")
print("Type is : ",type(f))

print("File name : ",f.name)
print("File mode : ",f.mode)

print("Is Readable ? : ",f.readable())
print("Is Writable ? : ",f.writable())

print("Is File Closed ? : ",f.closed)

f.close()
print("Is File Closed ? : ",f.closed)

