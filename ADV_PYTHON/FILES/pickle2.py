
import mymodule
import pickle

with open("einfo2.txt","wb") as f:

    while True:
        e=mymodule.Employee()
        e.setEmployee()
        pickle.dump(e,f)

        opt=input("Do u want another Rec Y | N ")
        if opt in ['n','N']:
            break

print("Recs are Saved ")
