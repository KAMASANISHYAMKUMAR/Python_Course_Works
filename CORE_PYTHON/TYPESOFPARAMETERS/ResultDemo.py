import time

def findResult(name,*marks):
    print("name is : ",name)
    print("marks ")
    for i in marks:
        time.sleep(.2)
        print(i)
    print("============")
    print("Total is : ",sum(marks))
    print("---------------------")

#calling
findResult("Ramya",40,50,60)
findResult("Roja",40,50)
findResult("Radha",30)
findResult("Sudha")

