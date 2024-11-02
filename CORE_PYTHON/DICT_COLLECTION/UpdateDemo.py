
#D-Dict  | k-key | d-value

#D.keys() -> dict_keys | iterable
#D.values() -> dict_values | iterable
#D.items() -> dict_items | iterable

#D.update({k:d})
''' 1.Adding a new item to dict
    2.Updating an existed item in the dict
    3.Dict concatenation '''

stu={}

for i in range(1,4):
    k=input("Enter key :")
    d=input("Enter value : ")
    stu.update({k:d})

print("student : ",stu)




















