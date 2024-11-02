
def findAreaTriangle(base,height):
    area=0.5*base*height
    return area

#calling
b=int(input("Enter Base of Triangle : "))
h=int(input("Enter height of Triangle : "))

at=findAreaTriangle(b,h)
print("Area of Triangle : ",at)
