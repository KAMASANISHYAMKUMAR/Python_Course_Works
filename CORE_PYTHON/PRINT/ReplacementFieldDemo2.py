
sno=101
sname="Ramesh"
sage=23

print("sno is : {} and sname is : {}".format(sno,sname))
#print("sno is : {} and sname is : {}".format(sno))
#IndexError

print("sno is : {}, sname is : {} and sage is : {}".
      format(sno,sname,sage))

print("sno is : {}, sname is : {} and sage is : {}".
      format(sname,sage,sno))
print("==================================")

print("sno is : {2}, sname is : {0} and sage is : {1}".
      format(sname,sage,sno))

print("--------------------------------------------------------")
print("sno is : {}, sname is : {} and sage is : {} {} is manager".
      format(sno,sname,sage,sname))

print("--------------------------------------------------------")
print("sno is : {n}, sname is : {na} and sage is : {a} {na} is manager".
      format(n=sno,na=sname,a=sage))















