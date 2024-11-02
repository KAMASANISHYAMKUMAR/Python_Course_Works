


'''
Nested Collection
   - collection(s) with in the collection  '''

lst=[10,12.12,"Shashi",
        [11,22,33],
        (1.1,2.2,3.3),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"sai"}
      ]

print("Inner List : ",lst[3])
print("2nd Item from Inner List : ",lst[3][1])
lst[3][1]=222
print("Inner List : ",lst[3])
print("===============================")

print("Inner Dict : ",lst[6])
print("Inner Dict : ",lst[-1])

print("Sname is : ",lst[6]['sname'])
print("Sname is : ",lst[-1]['sname'])
print("Sname is : ",lst[-1].get('sname'))















