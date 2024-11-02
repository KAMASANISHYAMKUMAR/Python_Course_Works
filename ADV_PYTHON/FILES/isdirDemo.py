
#os.path.exists(path) -> bool
#os.path.isfile(path) -> bool
#os.path.isdir(path) -> bool

import os.path

path="e:\\adv_super\\html\\intex"

if os.path.exists(path):
    print("Path is Existed ")
    
    if os.path.isdir(path):
        print("Yes it is directory")
        
else:
    print("Path is Not Existed ")
