
import pickle

with open("einfo.txt","rb") as f:
    o=pickle.load(f)
    #print("Type is : ",type(o))
    o.getEmployee()
