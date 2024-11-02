
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
#zip(iterable,iterable) -> zip object | iterable
#dict(iterable)

#How to convert string to dict collection
#Ans : By using fromkeys

#D.get(k[,d=None])
stu={"sno":101,"sname":"ramesh"}
print(stu)

#D.pop(k[,d]) -> d
#D.popitem() -> tuple
t=stu.popitem()
print("deleted item is : ",t)
print("dict : ",stu)


















































