import mymodule
import pickle

f=open("einfo.txt","wb")

e=mymodule.Employee()
e.setEmployee()
pickle.dump(e,f)

f.close()
print("Object is Saved ")
