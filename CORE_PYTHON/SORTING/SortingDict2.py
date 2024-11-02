



stu={"c":"cnu","a":"anu","b":"balu","d":"dhanu" }
print(stu)

lst=sorted(stu.items())
print(lst)

stu2={}
for t in lst:
    k,d=t
    stu2.update({k:d})

print("sorted dict : \n ",stu2)





    



