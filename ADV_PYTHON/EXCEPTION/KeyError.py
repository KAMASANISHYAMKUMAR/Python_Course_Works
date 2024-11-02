




stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print("Student : ",stu)

k=input("Enter Key : ") #sname

if k in stu.keys():    
    d=stu[k]
    print("Value is : ",d)
else:
    print("Sorry Invalid Key ")
