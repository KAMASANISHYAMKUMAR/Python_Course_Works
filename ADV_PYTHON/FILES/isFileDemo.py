#os.path.exists(path) -> bool
#os.path.isfile(path) -> bool
#os.path.isdir(path) -> bool

import os.path
import time

path="e:\\adv_super\\html\\first.html"

if os.path.exists(path):
    time.sleep(1)
    print("Path is Existed ")

    if os.path.isfile(path):
        time.sleep(1)
        print("Yes it is a File ")

        #with open(path,"r") as f:
        with open(path) as f:
            data=f.read()
            for i in data:
                time.sleep(.1)
                print(i,end='')

    elif os.path.isdir(path):
        time.sleep(1)
        print("Yes it is a directory")

else:
    print("Path is not existed ")






