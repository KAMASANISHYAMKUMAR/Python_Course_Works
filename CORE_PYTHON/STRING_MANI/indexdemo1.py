
#s.index(sub[,start,end] ) -> int
#s.rindex(sub[,start,end] ) -> int
#s.find(sub[,start,end]) -> int
#s.rfind(sub[,start,end]) -> int

s="welcome"
print("Data is : ",s)

pos=s.index("e")
print("Found @ : ",pos)

pos=s.index("E",3,7)
print("Found @ : ",pos)

