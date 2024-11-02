



stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("Student : ",stu)

k=input("Enter Key : ") #sname
try:
    d=stu[k]
except KeyError:
    print("Sorry Invalid Key ")
else:
    print("Value is : ",d)
