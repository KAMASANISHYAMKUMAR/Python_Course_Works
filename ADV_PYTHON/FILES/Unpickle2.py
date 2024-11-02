import mymodule
import pickle
import time

with open("einfo2.txt","rb") as f:
    while True:    
        time.sleep(1)
        try:
            o=pickle.load(f)        
        except EOFError:
            break
        else:
            if isinstance(o,mymodule.Employee):
                o.getEmployee()
            elif isinstance(o,mymodule.Student):
                pass
