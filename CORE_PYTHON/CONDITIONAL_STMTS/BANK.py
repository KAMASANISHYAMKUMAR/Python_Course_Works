obal=int(input("Enter oldbal  : "))
ttype=input("Enter Ttype : " )
tamt=int(input("Enter Tamt : "))

if ttype=="w" or ttype=="W":
    if tamt>obal:
        print("Ins Funds ")
    elif tamt==obal:
        print("M.M.Bal ")
    else:
        cbal=obal-tamt
        print("Current Bal : ",cbal)

elif ttype=="d" or ttype=="D":
    if tamt>=50000:
        print("REQ PAN CARD ")
    else:
        cbal=obal+tamt
        print("Current Bal : ",cbal)        

else:
    print("Invalid Operation")



    
