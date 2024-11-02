



stu={"c":"cnu","a":"anu","b":"balu","d":"dhanu" }
print(stu)

#D.sort() X
sk=sorted(stu.keys()) #['a','b','c','d']
print("sorted keys : ",sk)

sv=sorted(stu.values()) #["anu","balu","cnu","dhanu"]
print("sorted values : ",sv)

z=zip(sk,sv)
stu=dict(z)
print(stu)







