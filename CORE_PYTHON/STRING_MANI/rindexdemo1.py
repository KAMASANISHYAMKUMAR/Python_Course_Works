
#s.index(sub[,start,end] ) -> int | ValueError
#s.rindex(sub[,start,end] ) -> int

#s.find(sub[,start,end]) -> int
#s.rfind(sub[,start,end]) -> int

s="welcome"
print("Data is : ",s)

pos=s.rindex("e")
print("Found @ : ",pos) 

pos=s.rindex("e",3,7)
print("Found @ : ",pos)

