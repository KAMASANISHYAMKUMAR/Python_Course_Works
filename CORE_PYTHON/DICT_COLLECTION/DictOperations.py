
stu={}
print("stu : ",stu)

#For adding new item to the dict
stu['sno']=10
stu['sname']='James'
print("stu : ",stu)

#For updating an existed item
stu['sname']='Ramesh'
print("stu : ",stu)
stu['sno']=222
print("stu : ",stu)

#For reading value
name=stu['sname']
print("sname is : ",name)
#city=stu['scity'] KeyError

#For deleting dict item
del stu['sname']
print("stu : ",stu)








