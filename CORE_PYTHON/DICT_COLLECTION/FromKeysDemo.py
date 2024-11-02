
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
#D.values() -> dict_values | iterable
#D.items() -> dict_items | iterable

#D.update({k:d})
''' 1.Adding a new item to dict
    2.Updating an existed item in the dict
    3.Dict concatenation '''




#D.setdefault(k,d=None)
#D.fromkeys(iterable,value=None) -> dict
lst=["Ram","Raj","Nani"]
stu={}

stu=stu.fromkeys(lst) #{"Ram":None,"Raj":None,"Nani":None}
print(stu)
print("======================")

stu2={}
stu2=stu2.fromkeys(lst,"Python")
print(stu2)
























