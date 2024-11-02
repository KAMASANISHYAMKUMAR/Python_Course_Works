'''
s={  [10,20,30,40],
        (1.1,2.2,3.3,4.4),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"raj","scity":"hyd"}
     }
TypeError : Unhashable type list

s={  
        (1.1,2.2,3.3,4.4),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"raj","scity":"hyd"}
     }
TypeError: unhashable type: 'set'

s={  
        (1.1,2.2,3.3,4.4),
        {"sno":101,"sname":"raj","scity":"hyd"}
     }
TypeError: unhashable type: 'dict'
'''
s={
       
        (1.1,2.2,3.3,4.4),
        ( 10,20,30,40),
        ("aaa","bbb","ccc"),       
    }



import time

for i in s:
    time.sleep(.2)
    print(i)


























