
#s.index(sub[,start,end] ) -> int | ValueError
#s.rindex(sub[,start,end] ) -> int

#s.find(sub[,start,end]) -> int
#s.rfind(sub[,start,end]) -> int

s="welcome"
print("Data is : ",s)

pos=s.find("e") #1
print("Found @ : ",pos) 

pos=s.find("E",3,7) #6
print("Found @ : ",pos)

