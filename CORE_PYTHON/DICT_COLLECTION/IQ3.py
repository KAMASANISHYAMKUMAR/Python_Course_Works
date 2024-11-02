
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



s="Ramesh=32, suresh=22, chinni=26"
print("string : ",s)

#S.split() -> list
#D.update({k:d})

lst=s.split(",")  #["ramesh=32','suresh=22','chinni=26']

stu={}
for i in lst:
    k,d=i.split("=") # ['Ramesh','32']
    stu.update({k:int(d)})

print("Result ")
print(stu)
    




















































