
class Sample:
    x=10  #static variable

#calling
print("From outside of the class")
#print("x val is : ",x)
print("x val is : ",Sample.x)

s=Sample()
print("x val is : ",s.x)
