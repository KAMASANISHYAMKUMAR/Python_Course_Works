
#[<exp> for variable in iterable] -> list

'''
lst=[]
for i in range(1,11):
    lst.append(i)    
print("list : ",lst)
'''

lst2=[i for i in range(1,11)]
print("type is : ",type(lst2))
print("List : ",lst2)

lst3=[i*i for i in range(1,11)]
print("SQ : ",lst3)









