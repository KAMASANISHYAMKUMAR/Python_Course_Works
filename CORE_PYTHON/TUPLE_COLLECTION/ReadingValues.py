#    0      1                  2    3   4
t=(101,"Ramesh",40,50,60)
print("Name is : ",t[1])

tot=t[2]+t[3]+t[4]
print("Sum is : ",tot)

tm=t[2:5:1]
print("Marks : ",tm)

#unpacking
m1,m2,m3=t[2:5:1]
avg=(m1+m2+m3)/3
print("Avg is : ",avg)



