
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
#D.values() -> dict_values | iterable
#D.items() -> dict_items | iterable

#D.update({k:d})
''' 1.Adding a new item to dict
    2.Updating an existed item in the dict
    3.Dict concatenation '''

#D.setdefault(k,d=None)
stu={}
stu.setdefault("sno") #{"sno":None}
stu.setdefault("sname","Ramesh") #{"sname":"Ramesh"}
stu.setdefault("sname","Roja")
print(stu)












