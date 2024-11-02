
''' Accept Present Reading , Previous
Reading Calculate no.of.unit and bill '''

prr=int( input("Enter Present Reading : ") )
pvr=int(input("Enter previous reading : ") )

nu=prr-pvr
bill=nu*2

print("========================")
print(" Present Reading : ",prr)
print(" Previous Reading : ",pvr)
print("---------------------------------------")
print(" No.of.units : ",nu)
print(" Bill amount is : ",bill)
print("========================")


