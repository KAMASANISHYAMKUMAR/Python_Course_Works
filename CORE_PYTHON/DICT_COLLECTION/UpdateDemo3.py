
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
#D.values() -> dict_values | iterable
#D.items() -> dict_items | iterable

#D.update({k:d})
''' 1.Adding a new item to dict
    2.Updating an existed item in the dict
    3.Dict concatenation '''

stu1={"sno":101,"sname":"sai"}
print("stu : ",stu1)

stu2={"sage":32,"scity":"hyd","sname":"roja"}
print("stu2 : ",stu2)

#stu1+stu2 TupeError

stu1.update(stu2) # stu1=stu1+stu2
print("After Concatenation ")
print("stu1 : ",stu1)















