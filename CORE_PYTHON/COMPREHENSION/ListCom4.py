




#[<exp> for variable in iterable if test ] -> list
lst1=["anu","cnu","srija","roja","madhu","manas"]
print("List : ",lst1)

'''
lst2=[]
for i in lst1:
    if len(i)==5:
        lst2.append(i)
print("List 2 : ",lst2)
'''

lst2=[i for i in lst1 if len(i)==5 ]
print("List 2 : ",lst2)
















